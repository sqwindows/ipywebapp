import time
from ipyweb.logger import logger


class example():
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭事件监听
    }

    def example_event1(self, *args, **kwargs):
        print('example::event1 recive------------------', args)

    def example_event2(self, *args, **kwargs):
        print('example::event2 recive------------------')
