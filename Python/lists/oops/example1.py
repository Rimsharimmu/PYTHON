#OOPS Concepts
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def work(self,lang):
        print(f"Hi my name is {self.name} and my age is {self.age} and my language is {lang}")

chari= Person("Chari",20)
rimm=Person("Rimsha",21)

chari.work("Malayalam")
rimm.work("Urdu")


