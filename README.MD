
# Document Search and Upload using Google Drive API and NLP

This Python module provides functionality to upload documents to Google Drive and perform natural language queries on the uploaded documents. It utilizes the Google Drive API for file upload and retrieval, SQLAlchemy for database management, NLTK for natural language processing, and dotenv for loading environment variables.


## Prerequisites

Before running the code, make sure you have the following:

* Python 3.x installed on your system.
* Google Cloud project and credentials with access to the Google  Drive API.
* PostgreSQL or a compatible database management system installed and configured.
* NLTK library installed. You can install it using pip install nltk.
## Getting Started

1. Clone the repository or create a new Python file.
    ```
    https://github.com/kingdragon46/Document-Search-and-Upload-using-Google-Drive-API-and-NLP.git
    ```
2. Install the required dependencies by running the following command:
    ```
    pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 sqlalchemy psycopg2-binary dotenv nltk
    ```
3. Set up the Google Drive API:
    * Enable the Google Drive API for your project by visiting the Google Cloud Console, navigating to your project, and enabling the Drive API.
    * Create a service account and download the JSON key file. This file will be used as the SERVICE_ACCOUNT_FILE in the code.
    * Grant the necessary permissions to the service account to access and manage Google Drive files.
4. Set up the database:
    * Create a PostgreSQL database or use an existing one.
    * Set the database connection URL in the .env file as DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>.
    * Make sure the necessary database tables are created using the provided code or by running the appropriate database migration commands.
5. Update the .env file with the required environment variables:
    ```
    SERVICE_ACCOUNT_FILE=/path/to/service_account.json
    UPLOAD_FILE_PATH=/path/to/upload/file.pdf
    ```
6. Modify the provided code according to your requirements.
7. Run the Python module to execute the desired functionality.
## Functionality

The code provides the following functionality:

* Uploading a document to Google Drive:
    * Use the upload_document function by passing the file path and desired file name as arguments.
    * The document will be uploaded to Google Drive and its details will be stored in the database.
* Querying documents using natural language queries:
    * Use the query_documents function by passing the query string as an argument.
    * The function will perform a natural language query on the document names stored in the database and return the matched documents.
    * The matching is performed using NLTK's word tokenization and matching algorithm.
    * The matched documents' names are printed as an example, but you can modify the code to suit your needs.

Note: The NLTK resources for tokenization (punkt) need to be downloaded once. Uncomment the line nltk.download('punkt') before running the code for the first time. After the resources are downloaded, you can comment out that line.
## Logging

The code is configured to log messages using the Python logging module. By default, the log level is set to INFO, but you can modify it according to your preference. The logs can be redirected to a file or any other desired output using the Python logging configuration.
## Error Handling

The code includes basic exception handling for handling errors during document upload and query execution. Any exceptions that occur during these operations will be logged with appropriate error messages.
## License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT