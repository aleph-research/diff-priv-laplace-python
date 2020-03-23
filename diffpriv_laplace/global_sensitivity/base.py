class GlobalSensitivity(object):
    def __init__(self, value):
        super().__init__()
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value
