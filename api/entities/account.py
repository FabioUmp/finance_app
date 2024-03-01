class Account():
    def __init__(self, name, resume, value):
        self.__name= name
        self.__resume = resume
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def resume(self):
        return self.__resume

    @resume.setter
    def resume(self, resume):
        self.__resume = resume

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value  