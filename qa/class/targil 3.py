class Person:
    def __init__(self,name,age,kids):
        self.name=name
        self.age=age
        self.kids=kids

    def show(self):
        print(f"name:{self.name} age:{self.age} kids:{self.kids}")

    def haschildren (self):
        if self.kids>0:
            return True
        else:
            return False

    def agegroup (self):
        if 0<=self.age<=18:
            return ("child")
        if 19<=self.age<=60:
            return ("adult")
        if 61<=self.age<=120:
            return ("senior")

me_person=Person("shlomi",21,0)
me_person.show()
if me_person.haschildren():
    print("has kids")
else:
    print("dosen't has kids")
print(me_person.agegroup())