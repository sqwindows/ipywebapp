class example():
    ipywebAutoConfig = {
        'enable': True,  # 是否关闭事件注册器
    }

    def event1(self, eventName='', eventRegister=None):
        print(f'evnet1 register ok')

    def event2(self, eventName='', eventRegister=None):
        print(f'evnet2 register ok')
