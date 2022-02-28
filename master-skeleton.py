from http import server
import string
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import sys


workers = {
    'worker-1': ServerProxy("http://localhost:23001/"),
    'worker-2': ServerProxy("http://localhost:23002/")
}
      
def getbylocation(location):
    # TODO
    with ServerProxy(f"http://localhost:23001/") as proxy:
        result1 = proxy.getbylocation(location)
    with ServerProxy(f"http://localhost:23002/") as proxy:
        result2 = proxy.getbylocation(location)
    result = result1+result2
    if(len(result)>0):
        return result  
    return {
            'error': False,
            'result': ['no data found']
        }
def getbyname(name):
    # TODO
    print(name[0])
    initial_char_range1 = list(map(chr, range(97, 109)))
    initial_char_range2 = list(map(chr, range(110, 123)))
    if(name[0] in initial_char_range1):
        with ServerProxy(f"http://localhost:23001/") as proxy:
            result = proxy.getbyname(name)
            return result
    elif(name[0] in initial_char_range2):
        print('here in master')
        with ServerProxy(f"http://localhost:23002/") as proxy:
            result = proxy.getbyname(name)
            return result
    else:
        return {
            'error': False,
            'result': []
        }

def getbyyear(location, year):
    with ServerProxy(f"http://localhost:23001/") as proxy:
        result1 = proxy.getbyyear(location,year)
    with ServerProxy(f"http://localhost:23002/") as proxy:
        result2 = proxy.getbyyear(location,year)
    result = result1+result2
    return result

def main():
    port = int(sys.argv[1])
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # TODO: register RPC functions
    server.register_function(getbyname)
    server.register_function(getbylocation)
    server.register_function(getbyyear)
    server.serve_forever()


if __name__ == '__main__':
    main()