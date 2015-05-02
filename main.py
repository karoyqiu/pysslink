import ping
import settings
import sslocal
import spider

print('Fetching the server list...')
servers = spider.get_servers()
print('Got', len(servers), 'servers.')

print('Finding the fastest server...')
fastest = {}
minTtl = 100

for ss in servers:
    print('Pinging', ss['name'], ss['ip'])
    p = ping.ping(ss['ip'])
    print('  - ', p)

    if p < minTtl:
        minTtl = p
        fastest = ss

print('Fastest server:', fastest['name'], fastest['ip'], minTtl)
ss = sslocal.SSLocal(fastest)
ss.start()
