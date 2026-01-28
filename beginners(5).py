class Avenger:

    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
        print()

    def is_leader(self):
        if self.name == "Captain America":
            print(self.name, "is the leader")
        else:
            print(self.name, "is not the leader")


# Creating Avengers objects
captain = Avenger("Captain America", 100, "Male", "Super Strength", "Shield")
ironman = Avenger("Iron Man", 45, "Male", "Technology", "Armor")
widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")
hulk = Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon")
thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir")
hawkeye = Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")


# Display information
captain.get_info()
ironman.get_info()
widow.get_info()
hulk.get_info()
thor.get_info()
hawkeye.get_info()

# Check leader
captain.is_leader()
ironman.is_leader()
