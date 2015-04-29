import configparser
import os


class Settings():
    """A settings class."""
    def __init__(self, org, app):
        filePath = ''
        if os.name == 'nt':
            filePath = os.environ['APPDATA']
        elif os.name == 'posix':
            filePath = os.environ['HOME'] + '/.config'

        self.__filePath = os.path.join(filePath, org, app + '.conf')
        self.__config = configparser.ConfigParser()
        self.__config.read(self.__filePath, encoding = 'UTF-8')

    def file_path(self):
        return self.__filePath

    def get(self, section, option, fallback = None):
        return self.__config.get(section, option, fallback = fallback)

    #def set(self, section, option, value):
    #    if not self.__config.has_section(section):
    #        self.__config.add_section(section)

    #    self.__config.set(section, option, value)
