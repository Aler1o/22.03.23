class Stadium():
    def __init__(self, title, date, country, city, capacity,):
        self.title = title
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def settitle(self):
        self.title = input("enter title - ")
    def setdate(self):
        self.date = input("enter date - ")
    def setcountry(self):
        self.country = input("enter country - ")
    def setCity(self):
        self.city = input("enter city - ")
    def setcapacity(self):
        self.capacity = input("enter capacity - ")

    def setAll(self):
        self.title = input("enter title - ")
        self.date = input("enter date - ")
        self.country = input("enter country - ")
        self.city = input("enter city - ")
        self.capacity = input("enter capacity - ")

    def gettitle(self):
        print(self.title)
    def getdate(self):
        print(self.date)     
    def getcountry(self):
        print(self.country)       
    def getCity(self):
        print(self.city)    
    def getcapacity(self):
        print(self.capacity)

    def out(self):
        print("title = ", self.title)
        print("date = ", self.date)
        print("country = ", self.country)
        print("City = ", self.city)
        print("capacity = ", self.capacity)

Leo = Stadium("Tottenham Hotspur Stadium","April 3, 2019", "England", "London", "62k")
Leo.out()
Leo.gettitle()
Leo.out       

anonim = Stadium(" ", " ", " ", " ", " ", " ")
anonim.out()
anonim.setAll()
anonim.out