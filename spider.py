import requests
from htmlparser import SSLinkHTMLParser

__all__ = ['getServerList']

def __fetchHtml(email, password):
    payload = {
        'email': email,
        'password': password,
        'redirect': '/my/free'
    }

    r = requests.post('http://my.ss-link.com/login', data = payload)
    return r.text

def __parseHtml(html):
    parser = SSLinkHTMLParser()
    parser.feed(html)
    return parser.servers

def getServerList():
    html = __fetchHtml('karoyqiu@qq.com', '66e2ad00f406bbb56411305279d9866f')
    return __parseHtml(html)
