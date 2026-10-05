class familyMember:
    def __init__(self, eye_color, hair_color):
        self.eye_color = eye_color
        self.hair_color = hair_color
    def show_traits(self):
        print("Eye Color:", self.eye_color)
        print("Hair Color:", self.hair_color)
class kid(familyMember):
    def __init__(self,name,age, eye_color, hair_color):
        self.name = name
        self.age = age
        super().__init__(eye_color, hair_color)
    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()
    def favorite_hobby(self,hobby):
        print(self.name,"s favorite hobby is", hobby)
child=kid("John", 10, "blue", "brown")
child.show_traits()
child.favorite_hobby("soccer")
print("is kid a subclass of familyMember?", issubclass(kid, familyMember))
