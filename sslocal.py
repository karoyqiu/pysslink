import json
import os
import settings
import subprocess
import tempfile
import time


class SSLocal():
    """The shadowsocks proxy."""
    def __init__(self, server):
        self.__server = server
        self.__sslocal = None

    def __del__(self):
        if self.__sslocal:
            #sself.__sslocal.terminate()

            try:
                self.__sslocal.wait(100)
            except subprocess.TimeoutExpired:
                self.__sslocal.kill()

    def local_port(self):
        s = settings.Settings('Q', 'pysslink')
        return s.getint('sslocal', 'localPort', 1080)

    def start(self):
        config = {
            'server': self.__server['ip'],
            'server_port': self.__server['port'],
            'local_port': self.local_port(),
            'password': self.__server['password'],
            'method': self.__server['method'],
            'timeout': 60
        }
        configFile = tempfile.NamedTemporaryFile('w+', prefix = 'sslink-', suffix = '.json',
            encoding = 'UTF-8', delete = False)
        json.dump(config, configFile)
        configFile.close()

        s = settings.Settings('Q', 'pysslink')
        program = s.get('sslocal', 'program', 'sslocal')
        self.__sslocal = subprocess.Popen([program, '-c', configFile.name])
        time.sleep(3)
        os.unlink(configFile.name)
