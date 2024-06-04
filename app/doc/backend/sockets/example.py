from ipyweb.logger import logger
from ipyweb.services.socketServer import socketServer


class example():
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭运行
        'daemon': True,  # 是否守护执行
        'block': False,  # 是否阻塞执行
        'max': 1,  # 进程池或线程池数量
        'useProcess': False,  # 是否使用独立进程 默认独立线程
        'usePool': False,  # 是否启动线程池或进程池
        'setting': {
            'host': 'localhost',  # 服务地址
            'port': 8765,  # 服务端口
            'ssl': False,  # 是否开启wss
            'autoKill': True,  # 端口被占用时自动杀死进程 建议开启 进程不能有效关闭时该功能有效果
            # webSockets服务启动参数
            'serveConfig': {}
        }

    }
    socketServer = None

    async def onStart(self, socketServer):
        self.socketServer = socketServer
        logger.console.debug(f'onStart:{socketServer}')

    async def onServe(self, websocketsServe):
        logger.console.debug(f'onServe:{websocketsServe}')

    async def onConnect(self, path, header, client_id):
        logger.console.debug((f'exampleSocket服务已连接', path, header, client_id))

    async def onMessage(self, message, client_id):
        await  socketServer.sendToClient(client_id, 'I have received')
        # await self.socketServer.sendToClient(client_id, 'hello!') #等同于上一句
        logger.console.debug(f'onMessage:[{client_id}] {message}')

    async def onClosed(self, client_id):
        logger.console.debug(f'onClosed: {client_id}')

    async def onError(self, error):
        logger.console.debug(f'onError: {error}')

    async def onStop(self, socketServer):
        logger.console.debug(f'onStop: {socketServer}')
