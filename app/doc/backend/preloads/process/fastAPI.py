import os
from ipyweb.logger import logger
from ipyweb.contracts.ipywebPreload import ipywebPreload
from ipyweb.singleton import singleton


class fastAPI(ipywebPreload, metaclass=singleton):
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
        import uvicorn
        from fastapi import FastAPI
        app = FastAPI()

        @app.get("/")
        async def root():
            return {"message": "Hello fastAPI"}

        uvicorn.run(app, host="0.0.0.0", port=8000)
        print('FastAPI running as 8000', os.getpid())

    def onIpc(self, ipc):
        pass
        # ipc.send({
        #     'message': 'i am fastAPI',
        # })

    def onShare(self, manager):
        return {'config': 'hello'}

    def onMessage(self, message):
        print('onMessage:', message, os.getpid())
        return 'ok'

    def onStart(self, thread):
        pass
        # print(thread, os.getpid())

    def onError(self, msg, e):
        logger.console.debug((msg, e))
