title = '[ipyweb]个低代码多组件功能型快启快开python业务框架'  # 窗口标题
debug = True  # 调试开关
resizable = True  # 是否可以重设窗体尺寸
text_select = False  # 文本是否可以选择
confirm_close = False  # 退出是否弹出确认
frameless = False  # 是否无边框
easy_drag = False  # 无边框点窗体任意位置可拖动
on_top = False  # 是否最上层
width = 1200  # 窗体宽度
height = 800  # 窗体高度
x = None  # 窗口打开后X坐标
y = None  # 窗口打开后Y坐标
min_size = (200, 100)  # 最小尺寸
minimized = False  # 是否最小化
background_color = '#FFFFFF'  # 背景颜色
transparent = False  # 是否透明
hidden = False  # 窗体打开后是否隐藏
fullscreen = False  # 是否全屏
private_mode = False  # 是否开启隐私模式 开启后缓存随着窗体关闭后销毁
storage_path = 'cache'  # 浏览器引擎缓存目录 相对runtime目录下
user_agent = None  # 浏览器请求头
# 语言包
localization = {
    'global': {
        'quitConfirmation': '确定关闭吗？'
    }
}

# gui设置为cef有效
cef_settings = {
    'settings': {
        'locale': "zh-CN",
        'persist_session_cookies': True,
    },
    'browser_settings': {
        'ignore_certificate_errors': True,
    }
}
webview_settings = {
    'ALLOW_DOWNLOADS': False,
    'ALLOW_FILE_URLS': True,
    'OPEN_EXTERNAL_LINKS_IN_BROWSER': True,
    'OPEN_DEVTOOLS_IN_DEBUG': False
}

guiDriverEnable = True  # 关闭后为无窗应用
gui = ''  # GUI浏览器引擎
guiDriver = 'ipyweb'  # guiDriver类型  local：本地静态html remote:远程url flask：flask框架 bottle：bottle框架(纯静态支持) ipyweb自定义bottle框架(静态+控制器支持)
guiDriverConfig = {
    'ipyweb': {
        'index_html': 'index.html',  # 首页文件 相对于resource目录
        'http_port': 8090,  # 端口
        'ssl': False,
    },
    'flask': {
        'index_html': 'index.html',  # 首页文件 相对于resource目录
        'static_folder': 'assets',  # 静态资源文件 相对于resource目录
        'http_port': 8090,  # 端口
        'ssl': False,  # 是否开启https
        'controllerBlueprint': False  # 控制器蓝图路由支持
    },
    'bottle': {
        'index_html': 'index.html',  # 首页文件 相对于resource目录
        'http_port': 8090,  # 端口
        'ssl': False,
    },
    'remote': {
        'loading': True,
        'url': 'http://localhost:8090/#/',
        'http_server': False,  # 是否同时开启本地服务器
        'http_port': 8090,
        'ssl': False
    },
    'local': {
        'html': 'index.html',  # 本地静态页面 相对于resource目录
        'http_server': False,  # 是否同时开启本地服务器
        'http_port': 8090,
        'ssl': False
    }

}
