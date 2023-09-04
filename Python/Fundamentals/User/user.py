class User:

    def __init__(self, firstName, lastName, email, age):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.age = age
        self.isRewardsMember = False
        self.goldCardPoints = 0

    def displayInfo(self):
        print("~~~~~~~~~~~~~~~~~~")
        print(self.firstName)
        print(self.lastName)
        print(self.email)
        print(self.age)
        print(self.isRewardsMember)
        print(self.goldCardPoints)
        print("~~~~~~~~~~~~~~~~~~")
        return self
    
    def enroll(self):
        if self.isRewardsMember == True:
            print("User already a member.")
        else:
            self.isRewardsMember = True
            self.goldCardPoints = 200
        return self

    def spendPoints(self, amount):
        if self.goldCardPoints >= amount:
            self.goldCardPoints -= amount
        else:
            print("User does not have enough points.")
        return self

user1 = User("Will", "Ours", "wo@email.com", 25)
user2 = User("Yeiri", "Desi", "yd@email.com", 25)
user3 = User("Evios", "Vicern", "ev@email.com", 25)

user1.displayInfo().enroll().spendPoints(50).enroll().displayInfo()


user2.enroll()
user2.spendPoints(80)
user2.displayInfo()

user3.spendPoints(40)
user3.displayInfo()
