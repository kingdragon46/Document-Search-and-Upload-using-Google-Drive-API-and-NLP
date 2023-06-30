import os
import logging
import asyncio
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import nltk
from nltk.tokenize import word_tokenize

# Load environment variables from .env file
load_dotenv()

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure database
DATABASE_URL = os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define document model
class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    file_id = Column(String)

# Initialize Google Drive API client
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

# Function to upload a document to Google Drive
async def upload_document(file_path, file_name):
    media_body = MediaFileUpload(file_path, mimetype='application/pdf')

    file_metadata = {
        'name': file_name,
        'mimeType': 'application/pdf'
    }

    try:
        response = await asyncio.get_event_loop().run_in_executor(
            None, lambda: drive_service.files().create(
                body=file_metadata, media_body=media_body).execute())
        file_id = response['id']

        # Store document details in the database
        session = Session()
        document = Document(name=file_name, file_id=file_id)
        session.add(document)
        session.commit()
        session.close()

        logger.info(f"Document '{file_name}' uploaded successfully.")
    except Exception as e:
        logger.error(f"Error uploading document: {str(e)}")

# Function to query documents using natural language queries
async def query_documents(query):
    try:
        # Perform the query using the database or any other search algorithm
        session = Session()
        documents = session.query(Document).all()

        # Perform NLP query matching
        tokenized_query = word_tokenize(query.lower())
        matched_documents = []
        for document in documents:
            tokenized_name = word_tokenize(document.name.lower())
            if all(token in tokenized_name for token in tokenized_query):
                matched_documents.append(document)

        session.close()

        logger.info(f"Query '{query}' executed successfully.")
        return matched_documents
    except Exception as e:
        logger.error(f"Error executing query: {str(e)}")

# Example usage
async def main():
    # Upload a document
    await upload_document(os.getenv('UPLOAD_FILE_PATH'), 'My Document')

    # Query documents using natural language queries
    matched_documents = await query_documents('document')
    for document in matched_documents:
        print(document.name)

if __name__ == '__main__':
    # nltk.download('punkt')  # Download the required NLTK resources
    asyncio.run(main())
