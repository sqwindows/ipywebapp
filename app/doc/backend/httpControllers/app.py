from ipyweb.contracts.ipywebHttpController import ipywebHttpController


class app(ipywebHttpController):

    def fullscreen(self):
        windows = self.windows('main')
        windows.toggle_fullscreen()

        return self.success('ok')

    # def registerRoute(self):
    #     @self.blueprint.route('/register', methods=['POST'])
    #     def register():
    #         return self.success('ok')
