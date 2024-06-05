
import os
from ipyweb.ipyweb import ipyweb
if __name__ == '__main__':
    appName = os.environ.get('appName', 'doc')
    ipyweb.boot(appName)  # appName为应用名称


