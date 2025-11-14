class User:
    def __init__(self):
        self.__name = None
        self.__email = None
        self.__password = None
    def get_name(self):
        return self.__name
    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password
user = User()
user.set_name("Коваленко")
user.set_email("kovalenko@gmail.com")
user.set_password("qwerty123")

print(user.get_name())
print(user.get_email())
print(user.get_password())
