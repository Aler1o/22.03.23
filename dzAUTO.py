class Auto():
    def __init__(self, model, year, manufacturer, engine, colour, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.colour = colour
        self.price = price

    def setmodel(self):
        self.model = input("enter model - ")
    def setyear(self):
        self.year = input("enter year - ")
    def setmanufacturer(self):
        self.manufacturer = input("enter manufacturer - ")
    def setengine(self):
        self.engine = input("enter engine - ")
    def setcolour(self):
        self.colour = input("enter colour - ")
    def setprice(self):
        self.price = input("enter price - ")

    def setAll(self):
        self.model = input("enter model - ")
        self.year = input("enter year - ")
        self.manufacturer = input("enter manufacturer - ")
        self.engine = input("enter engine - ")
        self.colour = input("enter colour - ")
        self.price = input("enter price - ")

    def getmodel(self):
        print(self.model)
    def getyear(self):
        print(self.year)     
    def getmanufacturer(self):
        print(self.manufacturer)       
    def getengine(self):
        print(self.engine)    
    def getcolour(self):
        print(self.colour)
    def getAddres(self):
        print(self.price)

    def out(self):
        print("model = ", self.model)
        print("year = ", self.year)
        print("manufacturer = ", self.manufacturer)
        print("engine = ", self.engine)
        print("colour = ", self.colour)
        print("price = ", self.price)

Leo = Auto("Lamborghini","215", "Italy", "5.2", "yellow","200k$")
Leo.out()
Leo.getmodel()
Leo.out       

anonim = Auto(" ", " ", " ", " ", " ", " ")
anonim.out()
anonim.setAll()
anonim.out