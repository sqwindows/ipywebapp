import time
from ipyweb.logger import logger


class user():
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭监听

    }

    def example_event1(self, *args, **kwargs):
        print('user::example_event1 recive------------------', args)
