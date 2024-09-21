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


# Creating instances of the classes
book1 = Book("Atomic Habits", "James Clear", 2018)
student1 = Student("Athul", "B", 24)
car1 = Car("Supra", 1998, 27)

# Output
print(book1.get_info())
print(f"Student: {student1.name}, Grade: {student1.grade}, Age: {student1.age}")
print(student1.update_grade("A"))
print(car1.show_car_info())
