"""
This script runs the TwitterMapProj application using a development server.
"""

from os import environ, system
from TwitterMapProj import app

if __name__ == '__main__':
    # HOW DO YOU RUN THE THIS FILE???
    #system('elasticPutData.py')
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
