class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Book details: Title - {self.title}, Author - {self.author}, Year - {self.year}"


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"{self.name}'s grade has now been updated to Grade {self.grade}"


class Car:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year
        self.mileage = mileage

    def show_car_info(self):
        return f"Car details: Model - {self.model}, Year - {self.year}, Mileage - {self.mileage}k miles"

    def drive(self, distance):
        self.mileage += distance
        return (
            f"After driving {distance}k miles, the new mileage is {self.mileage}k miles"
        )


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if isinstance(car, Car):  # Ensure only Car objects are added
            self.cars.append(car)
            return f"{car.model} has been added to the garage."
        else:
            return "Only Car objects can be added to the garage."

    def show_garage_cars(self):
        if not self.cars:
            return "The garage is empty."
        return "Cars in the garage:\n" + "\n".join(
            [f"{i+1}. {car.model} ({car.year}) - {car.mileage}k miles" for i, car in enumerate(self.cars)]
        )

# Creating instances of the classes
book1 = Book("Atomic Habits", "James Clear", 2018)
student1 = Student("Athul", "B", 24)
car1 = Car("Supra", 1998, 27)
car2 = Car("Tesla Model 3", 2021, 15)

# Creating a Garage instance
garage = Garage()

# Output
print(book1.get_info())
print(f"Student: {student1.name}, Grade: {student1.grade}, Age: {student1.age}")
print(student1.update_grade("A"))

print(car1.show_car_info())
print(car1.drive(5))
print(car1.show_car_info())

# Adding cars to the garage
print(garage.add_car(car1))
print(garage.add_car(car2))

# Showing cars in the garage
print(garage.show_garage_cars())