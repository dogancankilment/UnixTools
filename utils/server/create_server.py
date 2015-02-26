import SimpleHTTPServer
import SocketServer
import webbrowser


def create_server():
    # give port number
    port = 6060

    handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), handler)

    # This will open the given address in default browser
    webbrowser.open("http://localhost:"+str(port))

    print port, "->in this PortNumber -- Hi, I'm Python Web Server."
    httpd.serve_forever()


if __name__ == '__main__':
    create_server()