from ipyweb.singleton import singleton
from ipyweb.contracts.ipywebController import ipywebController
from ipyweb.app import app as application


class app(ipywebController, metaclass=singleton):

    def version(self, window):
        try:
            return self.success('获取版本信息成功', {
                'ver': application.ver,
                'version': application.version
            })
        except Exception as e:
            return self.error(f'获取版本信息失败:{e}')
