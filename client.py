import xmlrpc.client
import sys

master_port = int(sys.argv[1])
with xmlrpc.client.ServerProxy(f"http://localhost:{master_port}/") as proxy:
    name = 'bob'
    print(f'Client => Asking for person with {name}')
    result = proxy.getbyname(name)
    print(result)
    print()

    location = 'Miami'
    print(f'Client => Asking for person lived at {location}')
    result = proxy.getbylocation(location)
    for items in result:
        print(items)
    print()

    location = 'Chicago'
    year = 2019
    print(f'Client => Asking for person lived in {location} in {year}')
    result = proxy.getbyyear(location, year)  
    for items in result:
        print(items)
    print(f"Total number of records are: {len(result)}")
    print()


""" 
Additional features are
1. Call workers from masters not like running them individually.
2. provide total data count at each worker
3. Add delay for 3rd task of 10 seconds at each worker.
"""