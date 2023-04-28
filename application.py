
from wsgiref.simple_server import make_server
import sqlite3

# def check_table_exists(conn,table_name):
#     cursor=conn.execute(
#         f'''
#         SELECT name FROM sqlite_master WHERE type='table' AND name={table_name}
        
#         '''
#     )
#     return cursor.fetchone() is not None
conn=None

def handler_index(conn):
    print("INDEX")
    cursor=conn.execute('''
    SELECT * FROM users
    
    ''')
    print("EXECUTED")
    for row in cursor:
        print('In CURSOR')
        id=row[0]
        name=row[1]
        email=row[2]

    res=f'DB data name{name} '    
    return [bytes(res,'utf-8')]


def handler_greetings(conn):


    return [b'Greetings Index']

url_patterns={
    '/':handler_index,
    '/greetings':handler_greetings
}





def application(environ, start_response):

    print("INSIDE")
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    ret = [b'Hiii']
    path=environ.get('PATH_INFO')
    print(f'path {path}')

 


    ret=url_patterns[path](conn)


    
 

    start_response(status, headers)
   

    print(type(ret))
    return ret

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    conn=sqlite3.connect('test_database.db')
    # table_exists=check_table_exists(conn=conn,table_name='test_database')
    # print(table_exists)
    # if(not table_exists):
    conn.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT

    )
    ''')




    httpd.serve_forever()


