import time
from datetime import datetime


class clear:
    ipywebAutoConfig = {
        'name': __name__,  # 计划任务名称  不配置配置以模块名为准
        'enable': True,  # 是否关闭运行
        'daemon': True,  # 启动线程是否守护执行
        'block': False,  # 启动线程是否阻塞执行
        'usePool': False,  # 是否线程池启动
        'useProcess': True,  # 是否使用进程
        'max': 1,  # 启动线程数量
        # 调度器配置选项
        'setting': {
            'scheduler': 'background',  # 调度器类型 blocking:阻塞计划任务 background:非阻塞计划任务 也可以是一个scheduler的调度器实例
            'schedulerParams': {},  # 调度器参数
            'jobTrigger': 'interval',  # 任务触发类型  cron:定时任务  interval:间隔循环任务  date：在指定的时间点触发任务。
            'jobParams': {  # 任务触发参数
                'seconds': 3,  # 参数支持类型 与scheduler.add_job所有参数保持一致 其参数配合jobTrigger设置
            }
        },
        'taskSetting': {
            'enable': False,  # 是否开启内置任务 关闭后则自动执行run方法
            'default': 'invokeCall',  # 内置任务类型 openUrl:打开网址 exeCommand:执行命令 invokeCall:调用类方法
            'openUrl': {
                'type': 'get',  # 请求方式
                'url': 'https://www.baidu.com',  # 请求地址
                # ...支持requests.get()或.post()所有参数
            },
            'exeCommand': {
                'runCommand': ['python', 'cli.py', 'demotest', 'start'],  # 命令行命令
                'runParams': {}  # 与subprocess.run多变参数保持一致
            },
            'invokeCall': {
                'module': 'app.demo.backend.crontabs.clear',  # 模块路径
                'class': 'clear',  # 类名
                'method': 'test',  # 方法名
                'params': {}  # 参数
            }
        }
    }

    def run(self, **config):
        print('running::' + str(time.time()))

    def onStart(self, scheduler, job):
        pass
        # print('onStart::', scheduler, job)

    def onTasked(self, result):
        print('onTasked::', result)
