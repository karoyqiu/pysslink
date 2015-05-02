import meow
import ping
import settings
import sslocal
import spider
import time
import signal

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
hp = meow.Meow(ss)
hp.start()

while True:
    time.sleep(10)
