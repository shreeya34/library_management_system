from datetime import datetime, timedelta
import json 

#file to store library data 
FILE_NAME="library_data.json"


data = {"Book":[],"Member":[],"Admin":[]}
    

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Book":[],"Member":[],"Admin":[]}
        
def save_data(data):
    with open("library_data.json","w") as file:
        json.dump(data,file, indent=4)

class Book:
    def __init__(self, book_id, title, author_name, stock):
        self.book_id = book_id
        self.title = title
        self.author_name = author_name
        self.stock = stock
        self.available = True
        
    def __str__(self):
        return f"{self.book_id}. {self.title} by {self.author_name}"

class Member:
    def __init__(self, member_id, name, role, expiry_date):
        self.member_id = member_id
        self.name = name
        self.role = role
        self.expiry_date = expiry_date
    
    def __str__(self):
        return f"{self.member_id}. {self.name} ({self.role}) - Expires on {self.expiry_date}"

class Admin(Member):
    def __init__(self, admin_id, name):
        super().__init__(admin_id, name, "Admin", None) 
        
    def add_books(self, title, author_name, stock):
        data = load_data()
        book_id = len(data["Book"]) + 1  
        book = Book(book_id, title, author_name, stock)
        data["Book"].append(book.__dict__)        
        save_data(data)
        print(f'Book "{title}" added successfully')
        
    def add_member(self, name, role, expiry_date):
        data = load_data()
        member_id = len(data["Member"]) + 1
        expiry_date = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        member = Member(member_id, name, role, expiry_date)
        
        data["Member"].append(member.__dict__)  
        save_data(data)
        print(f"Member '{name}' added successfully")
# Example usage:
# admin = Admin(1, "John Doe")
# admin.add_books("The Great Gatsby", "F. Scott Fitzgerald", 10)
# admin.add_member("Jane Doe", "Student", datetime.now() + timedelta(days=365))
 
        
        
# data = load_data()

# admin = Admin(1, "shreeya")
# admin.add_books("1984", "George Orwell", "8")
