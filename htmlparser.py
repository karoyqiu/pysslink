from html.parser import HTMLParser

class SSLinkHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.servers = []
        self.__tbody = False
        self.__tr = False
        self.__td = False
        self.__td_index = 0
        self.__cur = {}

    def handle_starttag(self, tag, attribs):
        if tag == 'tbody':
            self.__tbody = True
        elif tag == 'tr' and self.__tbody:
            self.__tr = True
        elif tag == 'td' and self.__tbody and self.__tr:
            self.__td = True

    def handle_endtag(self, tag):
        if tag == 'tbody':
            self.__tbody = False
        elif tag == 'tr' and self.__tbody:
            self.__tr = False
            self.__td_index = 0
            self.servers.append(self.__cur)
            self.__cur = {}
        elif tag == 'td' and self.__tr:
            self.__td = False
            self.__td_index += 1

    def handle_data(self, data):
        if self.__td:
            if self.__td_index == 0:
                self.__cur['name'] = data
            elif self.__td_index == 1:
                self.__cur['ip'] = data
            elif self.__td_index == 2:
                self.__cur['port'] = int(data)
            elif self.__td_index == 3:
                self.__cur['password'] = data
            elif self.__td_index == 4:
                self.__cur['method'] = data
