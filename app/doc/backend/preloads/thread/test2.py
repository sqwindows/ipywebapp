import asyncio
import os
from ipyweb.logger import logger
from ipyweb.contracts.ipywebPreload import ipywebPreload
from ipyweb.services.socketClient import socketClient
from ipyweb.services.timer import timer
from ipyweb.singleton import singleton


class test2(ipywebPreload, metaclass=singleton):
    ipywebAutoConfig = {
        'enable': False,  # 是否关闭运行
        'windowsOpen': True,  # 启动节点 True:窗口打开后 False:窗口打开前 默认 False
        'daemon': True,  # 是否守护执行 默认True
        'block': False,  # 是否阻塞执行 默认False
        'max': 1,  # 进程池或线程池数量 默认1
        'usePool': False,  # 是否线程池 默认False
        'reloadIpyweb': True,  # 该参数预载进程有效： 关闭后为纯进程，不共享ipwe配置、日志、事件等实例数据  与主进程完全隔离
    }
    queue = None

    def run(self, **config):
        wss = None

        async def onConnect(wss):
            self.wss = wss
            sendTimer(wss).run()
            # time.sleep(5)
            # await  self.wss.close()
            print('onConnect22222222222222222221', wss)

        async def onError(wss, e):
            print('onError', wss)

        async def onClosed():
            print('onClosedtest2222222')

        async def onMessage(msg):
            print('onMessage', msg)


        socketClient().connect(
            setting={
                'uri': 'ws://localhost:8765'
            },
            event={
                'onConnect': onConnect,
                'onError': onError,
                'onClosed': onClosed,
                'onMessage': onMessage
            }
        )
        print('test2::running...........', os.getpid())

    def onIpc(self, ipc):
        pass
        # ipc.send({
        #     'message': 'i am test2',
        # })

    def onShare(self, manager):
        return {'test2::share': 'hello'}

    def onMessage(self, message):
        print('test2:recive:', message, os.getpid())
        return 'ok'

    def onStart(self, thread):
        print(thread, os.getpid())

    def onError(self, msg, e):
        logger.console.debug((msg, e))
class sendTimer():
    wss = None

    def __init__(self, wss):
        self.wss = wss

    def run(self):
        timer().run(
            name=__name__+'124' ,
            run=self.sendCount,
            setting={
                'interval': 3,
                'sleep': 0
            }

        )

    def sendCount(self, timer):
        asyncio.run(
            self.wss.send('w我是test22222222')
        )

