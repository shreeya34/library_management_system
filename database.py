from datetime import datetime, timedelta
import json 

#file to store library data 
FILE_NAME="library_data.json"


data = {"Book":[],"Member":[],"Admin":[],"Borrow_Books":[]}
    

def load_data():
    try:
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"Book":[],"Member":[],"Admin":[],"Borrow_Books":[]}
        
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
    def __init__(self, member_id, name, role):
        self.member_id = member_id
        self.name = name
        self.role = role
    
    def borrow_book(self, book_name,borrow_date,expiry_date):
        data = load_data()
        
        if "Borrow_Books" not in data:
            data["Borrow_Books"] = []
        
        for book in data["Book"]:
            if book['title'] == book_name:
                if int(book['stock']) > 0:
                    book['stock'] = int(book['stock']) - 1
                    borrow_date = datetime.now().strftime("%Y-%m-%d")  # Current date
                    expiry_date = (datetime.now() + timedelta(days=15)).strftime("%Y-%m-%d")  # 15-day return period
                    borrow_details = {
                        "member_id": self.member_id,
                        "book_name": book_name,
                        "borrow_date": borrow_date,
                        "expiry_date": expiry_date
                    }
                    data["Borrow_Books"].append(borrow_details)
                    print(f"Borrow Date: {borrow_date}")
                    print(f"Return By: {expiry_date}")
                    save_data(data)
                    return
                else:
                    print(f"Book '{book_name}' is out of stock")
                    return
        print(f"Book '{book_name}' not found")
 
    def return_books(self,book_name,return_date):
        data = load_data()
        for book in data["Book"]:
            if book['title'] == book_name:
                if int(book['stock']) > 0:
                    book['stock'] = int(book['stock']) + 1
                    print(f"Return Date: {return_date}")
                    save_data(data)
 
def load_admin_data():
    data = load_data()  
    return data.get("Admin", [])
             
class Admin(Member):
    def __init__(self, admin_id, name):
        super().__init__(admin_id, name, "Admin") 
    
    def auth(self,admin_name):
        data = load_data()
       
        
    def add_books(self, title, author_name, stock):
        data = load_data()
        book_id = len(data["Book"]) + 1  
        book = Book(book_id, title, author_name, stock)
        data["Book"].append(book.__dict__)        
        save_data(data)
        print(f'Book "{title}" added successfully')
        
    def add_member(self,member_id,name, role):
        data = load_data()
        member = Member(member_id, name, role)
        
        data["Member"].append(member.__dict__)  
        save_data(data)
        print(f"Member '{name}' added successfully")
        
    def view_member(self):
        data = load_data()
        print("List of member:")
        for member in data["Member"]:
            print(member['name'])
    
    def view_avilable_books(self):
        data = load_data()
        print("List of books avilable:")
        for book in data["Book"]:
            stock = int(book.get("stock", 0)) 
            if stock > 0:
                 print(f"{book['title']} by {book['author_name']} (Stock: {stock})")
            else:
                 print(f"{book['title']} by {book['author_name']} Out of stock")
            



        
        
# data = load_data()

# admin = Admin(1, "shreeya")
# admin.add_books("1984", "George Orwell", "8")
#renew books
# when user renew the book it should automatically update


