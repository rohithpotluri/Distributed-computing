from pkgutil import get_data
from xmlrpc.server import SimpleXMLRPCServer
import sys
import json
import time


# Storage of data
data_table_nz = {}

with open('data-nz.json') as json_file:
    data_table_nz= json.load(json_file)

def load_data(group):
    # TODO load data based which portion it handles (am or nz)
    with open('data-nz.json') as json_file:
        data_table_nz= json.load(json_file)


def getbyname(name):
    # TODO
    if (len(name) > 0):
        return data_table_nz[name]
    else:
        return {
            'error': False,
            'result': ['No data']
        }

def getbylocation(location):
    # TODO
    list1 = []
    No_data_list=['Sorry no data from worker-2']
    for i in range(0,len(data_table_nz)):
        if(list(data_table_nz.items())[i][1]['location'] == location):
            list1.append(list(data_table_nz.items())[i][1])
    print(f"Total size of data : {len(list1)}")
    if(len(list1)>0):
        return list1
    return No_data_list

def getbyyear(location, year):
    # TODO
    list1 = []
    for i in range(0,len(data_table_nz)):
        if(list(data_table_nz.items())[i][1]['location'] == location
        and list(data_table_nz.items())[i][1]['year'] == year):
            list1.append(list(data_table_nz.items())[i][1])
    #delay for 10 secs
    time.sleep(10)
    print(f"Total size of data : {len(list1)}")
    return list1

def main():
    if len(sys.argv) < 3:
        print('Usage: worker.py <port> <group: am or nz>')
        sys.exit(0)

    port = int(sys.argv[1])
    group = sys.argv[2]
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")
    print(f"total records are: {len(data_table_nz)}")
    # TODO register RPC functions
    server.register_function(getbyname)
    server.register_function(getbylocation)
    server.register_function(getbyyear)
    server.register_function(get_data)
    server.serve_forever()

if __name__ == '__main__':
    main()