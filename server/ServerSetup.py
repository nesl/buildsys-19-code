import socketserver

class ServerHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print('\nData Received: ' + self.data.decode('utf-8'))
        # just send back the same data, but upper-cased
        self.request.sendall(('I received your message. RL.').encode('utf-8'))

if __name__ == '__main__':
    HOST, PORT = '172.17.52.6', 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), ServerHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
