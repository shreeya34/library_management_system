import json 
from datetime import datetime, timedelta

#file to store library data 
FILE_NAME="library_data.json"


data={"Book":[],"Member":[],"Admin":[]}
    

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Book":[],"Member":[],"Admin":[]}
        
def save_data(data):
    with open("library_data.json","w") as file:
        # Fix the mode here
        json.dump(data,file, indent=4)
    

class Book:
    def __init__(self,book_id,title,author_name):
        self.book_id=book_id
        self.title=title
        self.author_name=author_name
        self.avilable=True
        
    def __str__(self):
        return f"{self.book_id}.{self.title}.{self.author_name}"
        

class Member:
    def __init__(self,member_id,name,role,expiry_date):
        self.member_id=member_id
        self.name=name
        self.role=role
        self.expiry_date=expiry_date
    
    def __str__(self):
        return f"{self.member_id}.{self.name}.{self.role}.{self.expiry_date}"
        

class Admin(Member):
    def __init__(self,admin_id,name):
        super().__init__(admin_id,name,"Admin",None)
        
    def add_books(self,title,author_name):
        data=load_data()
        book_id = len(data["Book"]) + 1  
        book = Book(book_id,title,author_name)
        data["Book"].append(book.__dict__)        
        save_data(data)
        print(f'Book {title} added succesfully')
        
    def add_member(self,member_id,name,role):
        data=load_data()
        member_id = len(data["Member"]) + 1
        expiry_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        member = Member(member_id,name,role,expiry_date)
        data["Member"].append(member.__dict__)
        save_data(data)
        print(f"Member {name} has successfully added")
    
    def view_member(self):
        data = load_data()
        print("/n List of member:")
        for member in data["Member"]:
            print(f"{member['id']},{member['name']},{member['role' ]}")
        
        
data = load_data()

admin = Admin(1, "shreeya")
admin.add_books("1984", "George Orwell")
admin.add_member("1","shreeya","member")




        
        
    
        
        
        
        
        