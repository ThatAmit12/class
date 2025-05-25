class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"\nThe {self.restaurant_name} is now open! Come on in!")

restaurant = Restaurant('The Gourmet Garden', 'Italian')

print(f"Restaurant Name: {restaurant.restaurant_name}")
print(f"Cuisine Type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe {self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"\nThe {self.restaurant_name} is now open! Come on in!")

restaurant1 = Restaurant('The Gourmet Garden', 'Italian')
restaurant2 = Restaurant('Sushi World', 'Japanese')
restaurant3 = Restaurant('Taco Haven', 'Mexican')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

class User:

    def __init__(self, first_name, last_name, age, gender, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.occupation = occupation

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}! Welcome back!")

user1 = User("Ruhi", "uddin", 20, "Male", "Software Engineer")
user2 = User("Hannah", "annah", 19, "Female", "Graphic Designer")
user3 = User("Prima", "prema", 21, "Female", "Data Analyst")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
