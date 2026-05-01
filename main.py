
# 8-m
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self):
        print(f"{self.username} tizimga kirdi")


class Admin(User):
    def __init__(self, username, password, email, role, permissions):
        super().__init__(username, password, email)
        self.role = role
        self.permissions = permissions

    def login(self):
        super().login()
        print(f"Role: {self.role}")

    def delete_user(self):
        print("Foydalanuvchi o‘chirildi")


a = Admin("admin1", "1234", "admin@mail.com", "SuperAdmin", "All")
a.login()
a.delete_user()
