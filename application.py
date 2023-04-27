
from wsgiref.simple_server import make_server
import sqlite3

def handler_index():
    return [b'Hello world Index']


def handler_greetings():
    conn=sqlite3.connect('test_db.db')
    cursor=conn.cursor()
    cursor.execute(
        '''
        
        
        '''
    )
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

 

    try:
        ret=url_patterns[path]()
    except:
        ret=[b'Error 404']

    
    print(path)

    start_response(status, headers)
   

    print(type(ret))
    return ret

with make_server('', 8000, application) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()
    conn=sqlite3.connect('test_db.db')
    cursor=conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT

    )
    
    ''')

