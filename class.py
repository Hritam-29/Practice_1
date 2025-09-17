class Cat:

    species="Persian"
    def __init__(self,name,age):
        self.name=name
        self.age=age

cat1=Cat("Berry",5)
cat2=Cat("Liza",4)
print(cat1.species,cat1.name,cat1.age)
print(cat2.species,cat2.name,cat2.age)
print(Cat.species)
cat1.name="Sonu"
Cat.species="Furry"
print(cat1.name)
print(cat1.species,cat2.species)