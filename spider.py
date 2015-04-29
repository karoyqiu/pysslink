import requests
import settings
from htmlparser import SSLinkHTMLParser

__all__ = ['get_servers']

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

def get_servers():
    s = settings.Settings('Q', 'pysslink')
    email = s.get('Account', 'email')
    password = s.get('Account', 'password')
    html = __fetchHtml(email, password)
    return __parseHtml(html)
