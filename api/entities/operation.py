class Operation():
    def __init__(self, name, resume, cost, type, account):
        self.__name= name
        self.__resume = resume
        self.__cost = cost
        self.__type = type
        self.__account = account


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
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        self.__type = type

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account):
        self.__account= account    