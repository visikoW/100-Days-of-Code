class User:
    def __init__(self, user_id = None, name = None, username = None, password = None):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('0001', 'Vinycius Florêncio', 'visiko', 'goku')
user_2 = User('0002', 'Anderson Florêncio', 'anf', 'saitama')
print(user_1.follow(user_2))

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)