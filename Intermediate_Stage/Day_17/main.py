class User:
    def __init__(self, user_id, username, seats):
        self.id = user_id
        self.username = username
        self.seats = seats
        print(f"New object created with {self.seats}")
        self.follower = []
        self.following = []

    def enter_race_mode(self):
        self.seats = 2

    def follow(self, following, follower):
        self.following.append(following)
        self.follower.append(follower)
        print(f"Numbers of followers: {len(self.follower)} and it is {self.follower[0]}")


user_1 = User("001", "Victor", 500)
print(user_1.id)
print(user_1.username)
print(user_1.follower)
user_1.enter_race_mode()
print(user_1.seats)

user_1.follow("Ariande Grande", "Michecl Jackson")

