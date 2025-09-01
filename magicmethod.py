class book:
    def __init__(self,name,author,nopages):
        self.name=name
        self.author=author
        self.nopages=nopages

    def __str__(self):#return strinng
        return f"{self.name} is written by {self.author} in {self.nopages} pages" 
    def __eq__(self,other):#equal to
        return self.name==other.name and self.author==other.author 
    def __lt__(self,other): #lessthan
        return self.nopages<other.nopages  
    def __gt__(self,other): #greaterthan
        return self.nopages>other.nopages 
    def __add__(self,other):
        return self.nopages+other.nopages 
    def __sub__(self,other):
        return self.nopages-other.nopages
    def __contains__(self,keyword):
        return keyword in self.name
    def __getitem__(self,key):
        if key=="name":
            return self.name
        
book1=book("my wish","tillu",210)
book2=book("rowdy","abhi",320)
book3=book("return of dargon","babu",430)
print(book1)  
print(book2)  
print(book1==book2)    
print(book2<book1)
print(book3>book1)
print(book1+book2)
print(book1-book2)
print("of" in book3 )
print(book3['name'])