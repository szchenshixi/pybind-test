from xmlrpc.server import SimpleXMLRPCServer
import os

server = SimpleXMLRPCServer(("localhost", 3000), logRequests=True)

def listDirectory(dir):
    return os.listdir(dir)

server.register_function(listDirectory)

if __name__ == "__main__":
    try:
        print("Serving...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting")
