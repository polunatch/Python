class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
class UserManager:
    def create_user(self, name, email):
        return User(name, email)
    def update_user(self, user, name=None, email=None):
        if name:
            user.name = name
        if email:
            user.email = email

    def delete_user(self, user):
        del user
        manager = UserManager()
        user = manager.create_user("Коваленко", "kovalenko@gmail.com")
        manager.update_user(user, email="kovalenkonew@gmail.com.com")
        manager.delete_user(user)