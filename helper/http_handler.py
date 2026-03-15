from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        Handle GET requests

        Args:
            None

        Returns:
            Any: Function result.
        """
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "GET request received"}
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        """
        Handle POST requests

        Args:
            None

        Returns:
            Any: Function result.
        """
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {"status": "success", "message": "POST request received"}
        self.wfile.write(json.dumps(response).encode())
    
    def log_message(self, format, *args):
        """
        Suppress default logging

        Args:
            format (Any): Input parameter.
            *args (Any): Variable positional arguments.

        Returns:
            Any: Function result.
        """
        pass

def start_server(host='localhost', port=5000):
    """
    Start the HTTP server

    Args:
        host (Any, optional): Input parameter. Defaults to 'localhost'.
        port (Any, optional): Input parameter. Defaults to 5000.

    Returns:
        Any: Function result.
    """
    server_address = (host, port)
    httpd = HTTPServer(server_address, HTTPHandler)
    print(f"Server running on http://{host}:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()