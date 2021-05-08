class User:
    def __init__(self, user_id, username, follower):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.followers += 1


user_1 = User("0012", "Brandon")
user_2 = User("00132", "Jenna")


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
