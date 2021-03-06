'''
Starter code fetched from
https://github.com/udacity/course-ud303/raw/master/Lesson-2/1_EchoServer/EchoServer.py
on 7 June 2018 as part of the Udacity.com Full-Stack-Nanodegree coursework
'''

#!/usr/bin/env python3
#
# The *echo server* is an HTTP server that responds to a GET request by
# sending the query path back to the client.  For instance, if you go to
# the URI "http://localhost:8000/Balloon", the echo server will respond
# with the text "Balloon" in the HTTP response body.
#
# Instructions:
#
# The starter code for this exercise is the code from the hello server.
# Your assignment is to change this code into the echo server:
#
#   1. Change the name of the handler from HelloHandler to EchoHandler.
#   2. Change the response body from "Hello, HTTP!" to the query path.
#
# When you're done, run it in your terminal.  Try it out from your browser,
# then run the "test.py" script to check your work.

from http.server import HTTPServer, BaseHTTPRequestHandler


class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        path = self.path.encode()

        # Now, write the response body.
        self.wfile.write(path)

if __name__ == '__main__':
    server_address = ('', 80)  # Serve on all addresses, port 80.
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()
