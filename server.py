"""
CHRONOS LUXE CLOCK - Local Web Server
Runs a local HTTP server to preview in the IDE's built-in emulator / Simple Browser.
"""

import http.server
import socketserver
import os
import sys

DEFAULT_PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

def find_available_port(start_port=3000):
    import socket
    for port in [start_port, 8080, 5000, 8000]:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return 3000

def run():
    port = find_available_port(DEFAULT_PORT)
    server_address = ('127.0.0.1', port)
    
    # Allow address reuse
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(server_address, Handler) as httpd:
        print("=" * 60)
        print(f"  CHRONOS LUXE CLOCK SERVER RUNNING")
        print(f"  Local URL: http://localhost:{port}")
        print("=" * 60)
        print("  Press Ctrl+C to stop the server.")
        sys.stdout.flush()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == '__main__':
    run()
