class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        if self.name == '':
            self.AskName()

        if self.age == 0:
            self.AskAge()

            if self.age <= 0:
                print("Age invalid")
                self.AskAge()

    def AskName(self):
        self.name = input("What is your name : ")

    def AskAge(self):
        result = input("What is your age : ")
        self.age = int(result)

    def Presentation(self):
        print(f"Hi, my name is {self.name}, i have {self.age} years old.")

        if self.Adults():
            print("I'm adults")
        else:
            print("I need more time before became adults :( ")

    def Adults(self):
        majority = int(18)

        if self.age >= majority:
            return True
        else:
            return False
