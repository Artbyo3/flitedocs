"""
Run script for Flitedocs
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    import sys
    
    # Parse command line arguments
    host = '127.0.0.1'
    port = 5000
    debug = False
    
    if '--host' in sys.argv:
        host = sys.argv[sys.argv.index('--host') + 1]
    if '--port' in sys.argv:
        port = int(sys.argv[sys.argv.index('--port') + 1])
    if '--debug' in sys.argv:
        debug = True
    
    app.run(host=host, port=port, debug=debug)
