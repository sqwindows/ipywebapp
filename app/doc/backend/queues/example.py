import os
import random

from ipyweb.config import config
from ipyweb.logger import logger
from ipyweb.singleton import singleton


class example(metaclass=singleton):
    ipywebAutoConfig = {
        'enable': False,  # 是否关闭运行
        'daemon': True,  # 启动线程是否守护执行
        'block': False,  # 启动线程是否阻塞执行
        'usePool': False,  # 是否线程池启动
        'useProcess': False, # 是否使用进程
        'max': 1,  # 启动线程数量
        'name': 'example',  # 队列名称  请保持唯一 不配置配置以模块名为准
        'maxsize': 0,  # 队列的容量 设置为0 容量不受限制
        # Queue:先入先出  LifoQueue:后入先出 PriorityQueue:优先级队列 ProcessQueue:跨进程队列
        'queueType': 'Queue',
        # 请注意，使用 getBlock = False 时需要谨慎，因为如果没有适当的错误处理，它可能会导致你的程序在队列为空时意外地失败。此外，确保在使用
        # getBlock = False 之前检查队列是否为空（quque.empty()）通常是一个好习惯，尽管这个检查本身并不是线程安全的。
        'getBlock': True,  # 执行队列是否阻塞
        'getTimeout': None,  # 执行队列最大阻塞时间 如果设置了指定时间内队列中没有数据，将抛出queue.Empty异常 可以用onEmpty()监听
        'putBlock': True,  # 添加队列是否阻塞
        'putTimeout': None,  # 添加最大阻塞时间
        'excepTaskDone': True,  # 发生异常是否标记队列任务执行完毕

    }
    queue = None

    def getQ(self):
        return self.queue

    def run(self, task):
        # time.sleep(5)
        logger.console.debug((f'执行任务', os.getpid(), task, config.get('windows')))

    def onStart(self, queue):
        self.queue = queue
        print(f'example队列实例', queue, self)

        for i in range(2):
            r = random.randint(1, 9)
            self.queue.add(name=f'name' + str(i), value={'a': i})

    def onRecv(self, task):
        logger.console.debug((f'收到任务', task))

        # logger.console.debug(self.queue.size())

    def onError(self, error, excep):
        logger.console.debug((f'任务异常', error, excep))

    def onEmpty(self):
        # logger.console.debug(f'任务已空')
        pass

    def onFull(self):
        # logger.console.debug(f'队列已满')
        pass
