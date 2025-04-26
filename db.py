import psycopg2  # Import the PostgreSQL adapter for Python

def get_db_connection():
    """
    Establish a connection to the PostgreSQL database using psycopg2.

    Returns:
        A connection object to interact with the PostgreSQL database.
    """
    # Connect to the database with the specified credentials and connection parameters
    return psycopg2.connect(
        dbname='dav6100s25',          # Name of the database
        user='postgres',              # Username for authentication
        password='postgres',          # Password for authentication
        host='localhost',             # Host address where the database is running (change if necessary)
        port='5432'                   # Port number (default PostgreSQL port is 5432)
    )
