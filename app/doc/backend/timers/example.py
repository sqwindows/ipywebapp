import os
import time

from ipyweb.logger import logger


class example():
    ipywebAutoConfig = {
        'name': __name__,
        'enable': False,  # 是否关闭运行
        'daemon': True,  # 是否守护执行
        'block': False,  # 是否阻塞执行
        'max': 1,  # 进程池或线程池数量
        'useProcess': True,  # 是否使用独立进程 默认独立线程
        'usePool': True,  # 是否线程池或进程池
        'setting': {
            'interval': 1,  # 间隔时间
            'sleep': 0,  # 延时执行
        }

    }

    def run(self, timer):
        logger.console.debug(f'im timer:example:{time.time()} [pid:{os.getpid()},{timer}]')
