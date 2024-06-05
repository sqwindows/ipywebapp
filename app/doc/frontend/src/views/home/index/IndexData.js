export default {
    menus: {
        actives: 'install.intro',
        lists: [
            {
                name: 'install',
                title: '快速上手',
                child: [
                    {
                        name: 'intro',
                        title: '框架介绍'
                    },
                    {
                        name: 'use',
                        title: '安装使用'
                    },
                    {
                        name: 'path',
                        title: '目录结构'
                    },
                    {
                        name: 'life',
                        title: '生命周期'
                    },
                ],
            },
            {
                name: 'framework',
                title: '基本功能',
                child: [
                    {
                        name: 'run',
                        title: 'run 框架入口'
                    },
                    {
                        name: 'runner',
                        title: 'runner 应用入口'
                    },
                    {
                        name: 'app',
                        title: 'app 多应用'
                    },

                    {
                        name: 'config',
                        title: 'config 配置'
                    },
                    {
                        name: 'gui',
                        title: 'gui 窗口驱动'
                    },
                    {
                        name: 'windows',
                        title: 'windows 窗口操作'
                    },

                    {
                        name: 'controller',
                        title: 'controller 控制器'
                    },
{
                        name: 'httpController',
                        title: 'httpController http控制器'
                    },

                    {
                        name: 'preload',
                        title: 'preload 预载器'
                    },

                    {
                        name: 'command',
                        title: 'command 命令行'
                    },
                    {
                        name: 'event',
                        title: 'event 事件'
                    },


                    {
                        name: 'cache',
                        title: 'cache 缓存'
                    },
                    {
                        name: 'orm',
                        title: 'orm 数据库'
                    },

                    {
                        name: 'queue',
                        title: 'queue 队列'
                    },

                    {
                        name: 'socket',
                        title: 'socket 服务'
                    },
                    {
                        name: 'timer',
                        title: 'timer 定时器'
                    },
                    {
                        name: 'crontab',
                        title: 'crontab 计划任务'
                    },
                    {
                        name: 'thread',
                        title: 'thread 线程'
                    },
                    {
                        name: 'process',
                        title: 'process 进程'
                    },

                    {
                        name: 'logger',
                        title: 'logger 日志'
                    },
                    {
                        name: 'service',
                        title: 'service 服务层'
                    },
                ]
            },
            {
                name: 'builder',
                title: '编译打包',
                child: [
                    {
                        name: 'build',
                        title: '编译打包'
                    },
                    {
                        name: 'setup',
                        title: '制作安装包'
                    },
                ]
            },
            {
                name: 'help',
                title: '常见问题',
                child: [
                    {
                        name: 'framework',
                        title: '关于框架'
                    },
                    {
                        name: 'bulider',
                        title: '关于打包'
                    },
                ]
            },
            {
                name: 'other',
                title: '其他附录',
                child: [
                    {
                        name: 'donate',
                        title: '捐赠我们'
                    },
                    {
                        name: 'update',
                        title: '更新日志'
                    },
                ]
            },

        ],
    },

}