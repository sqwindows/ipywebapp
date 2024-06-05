import os
from ipyweb.logger import logger
from ipyweb.contracts.ipywebPreload import ipywebPreload
from ipyweb.singleton import singleton


class example(ipywebPreload, metaclass=singleton):
    ipywebAutoConfig = {
        'enable': False,  # 是否关闭运行
        'windowsOpen': False,  # 启动节点 True:窗口打开后 False:窗口打开前 默认 False
        'daemon': True,  # 是否守护执行 默认True
        'block': False,  # 是否阻塞执行 默认False
        'max': 1,  # 进程池或线程池数量 默认1
        'usePool': False,  # 是否线程池 默认False
        'reloadIpyweb': True,  # 该参数预载进程有效： 关闭后为纯进程，不共享ipwe配置、日志、事件等实例数据  与主进程完全隔离
    }
    queue = None

    def run(self, **config):
        print('test:threading...')
        pass

    def onIpc(self, ipc):
        pass
        # ipc.send({
        #     'message': 'i am test2',
        # })

    def onShare(self, manager):
        return {'test::share': 'hello'}

    def onMessage(self, message):
        print('test:recive:', message, os.getpid())
        return 'ok'

    def onStart(self, thread):
        print(thread, os.getpid())

    def onError(self, msg, e):
        logger.console.debug((msg, e))
