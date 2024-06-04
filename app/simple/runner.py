from ipyweb.utils import utils


class runner():
    def run(self, windows):
        print(f'simple running:{windows}')

    def onStart(self):
        print('simple onStart')

    def onBased(self):
        print('simple onBased')

    def onPreloaded(self):
        print('simple onPreloaded')

    def onOpened(self):
        print('simple onOpened')

    def onClosed(self):
        print('simple onClosed')
