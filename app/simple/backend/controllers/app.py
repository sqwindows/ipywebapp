from ipyweb.app import app as ipyweb
from ipyweb.singleton import singleton
from ipyweb.contracts.ipywebController import ipywebController


class app(ipywebController, metaclass=singleton):

    def version(self, *args, **kwargs):
        try:
            return self.success('获取版本信息成功', {
                'ver': ipyweb.ver,
                'version': ipyweb.version
            })
        except Exception as e:
            return self.error(f'获取版本信息失败:{e}')
