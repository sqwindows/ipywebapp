import os
import time
import traceback
from ipyweb.logger import logger
from ipyweb.contracts.ipywebRunner import ipywebRunner


class runner(ipywebRunner):
    windows = None
    flask = None

    def run(self, windows=None):
        self.windows = windows
        try:
            logger.console.info(f'doc 主进程已经启动 PID：{os.getpid()}')
            self.loadJs()

            # input('按任意键退出')
        except Exception as e:
            tb = traceback.extract_tb(e.__traceback__)
            print(tb)
            logger.file.error(f'软件启动异常: {e}')
        return self

    def loadJs(self):
        if self.windows is None:
            return self
        self.windows.evaluate_js(
            r"""

            """
        )
        return self
