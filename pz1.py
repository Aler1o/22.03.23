class City():   
    def __init__(self, name, region, country, human ,index , phone):
        self.name = name
        self.region = region
        self.country = country
        self.human = human
        self.index = index
        self.phone = phone

    def setname(self):
        self.name = input("enter name - ")
    def setregion(self):
        self.region = input("enter region - ")
    def setcountry(self):
        self.country = input("enter country - ")
    def sethuman(self):
        self.human = input("enter human - ")
    def setindex(self):
        self.index = input("enter index - ")
    def setphone(self):
        self.phone = input("enter phone - ")

    def setAll(self):
        self.name = input("enter name - ")
        self.region = input("enter region - ")
        self.country = input("enter country - ")
        self.human = input("enter human - ")
        self.index = input("enter index - ")
        self.phone = input("enter phone - ")

    def getname(self):
        print(self.name)
    def getregion(self):
        print(self.region)     
    def getcountry(self):
        print(self.country)       
    def gethuman(self):
        print(self.human)    
    def getindex(self):
        print(self.index)
    def getAddres(self):
        print(self.phone)

    def out(self):
        print("name = ", self.name)
        print("region = ", self.region)
        print("country = ", self.country)
        print("human = ", self.human)
        print("index = ", self.index)
        print("phone = ", self.phone)
       
anonim = City(" ", " ", " ", " ", " ", " ")
anonim.out()
anonim.setAll()
anonim.out