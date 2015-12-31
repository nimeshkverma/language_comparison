import psycopg2
from psycopg2.extras import RealDictCursor
import datetime
from config import PSQL_PARAMS, QUERY_DICT, CRUD_KEYS

def psql_db_connect():
    """
        Aim: Connects to Postgres databases
        Input:
                db_name: database_name, type:string
        Output:
                conn: database connection, type psycopg2 connection object
    """
    conn_string = '''host='''+ PSQL_PARAMS['host']+''' dbname='''+ PSQL_PARAMS["dbname"] + ''' user=''' +PSQL_PARAMS["user"] + ''' password=''' + PSQL_PARAMS["password"]+''' port='''+ PSQL_PARAMS["port"]
    conn = psycopg2.connect(conn_string)
    return conn

def query_over_psql(query, return_bool):
    """
        Aim: Executes psql query
        Input:
                db_name: database_name, type:string
                query: psql query to be executed, type:string
        Output:
                rows: result of the query execution. type:list of dicts with
                key as colums selected and corresponding values
    """
    connection = psql_db_connect()
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query)
    connection.commit()

    if return_bool:
        rows = cursor.fetchall()
        return rows
    
def perform_crud():
    for key in CRUD_KEYS:
        if key == 'read':
            query_over_psql(QUERY_DICT[key], True)
        else:
            query_over_psql(QUERY_DICT[key], False)

