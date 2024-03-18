class Account():
    def __init__(self, name, resume, value, user):
        self.__name= name
        self.__resume = resume
        self.__value = value
        self.__user = user


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

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user     