import os
import settings
import subprocess
import tempfile
import time


class Meow():
    """The MEOW HTTP proxy."""
    def __init__(self, sslocal):
        self.__sslocal = sslocal
        self.__meow = None

    def __del__(self):
        if self.__meow:
            self.__meow.terminate()

            try:
                self.__meow.wait(3)
            except subprocess.TimeoutExpired:
                self.__meow.kill()

    def start(self):
        s = settings.Settings('Q', 'pysslink')
        configFile = tempfile.NamedTemporaryFile('w+', prefix = 'sslink-', suffix = '.conf',
            encoding = 'UTF-8', delete = False)
        configFile.write('listen = http://0.0.0.0:' + str(s.get('MEOW', 'port', 8123)) + '\n')
        configFile.write('proxy = socks5://127.0.0.1:' + str(self.__sslocal.local_port()) + '\n')
        configFile.close()

        program = s.get('MEOW', 'program', 'MEOW')
        self.__meow = subprocess.Popen([program, '-rc=' + configFile.name])
        time.sleep(3)
        os.unlink(configFile.name)
