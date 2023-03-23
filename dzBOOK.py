class Book():
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def settitle(self):
        self.title = input("enter title - ")
    def setyear(self):
        self.year = input("enter year - ")
    def setpublisher(self):
        self.publisher = input("enter publisher - ")
    def setgenre(self):
        self.genre = input("enter genre - ")
    def setauthor(self):
        self.author = input("enter author - ")
    def setprice(self):
        self.price = input("enter price - ")

    def setAll(self):
        self.title = input("enter title - ")
        self.year = input("enter year - ")
        self.publisher = input("enter publisher - ")
        self.genre = input("enter genre - ")
        self.author = input("enter author - ")
        self.price = input("enter price - ")

    def gettitle(self):
        print(self.title)
    def getyear(self):
        print(self.year)     
    def getpublisher(self):
        print(self.publisher)       
    def getgenre(self):
        print(self.genre)    
    def getauthor(self):
        print(self.author)
    def getAddres(self):
        print(self.price)

    def out(self):
        print("title = ", self.title)
        print("year = ", self.year)
        print("publisher = ", self.publisher)
        print("genre = ", self.genre)
        print("author = ", self.author)
        print("price = ", self.price)

Leo = Book("Гарри Поттер","1997", "Издательская группа «Азбука-Аттикус в РФ", "Фэнтези", "Джоа́н Ро́улинг","50$")
Leo.out()
Leo.gettitle()
Leo.out       

anonim = Book(" ", " ", " ", " ", " ", " ")
anonim.out()
anonim.setAll()
anonim.out