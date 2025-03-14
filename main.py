from datetime import datetime, timedelta
from database import Member, Admin, load_admin_data

def main():
    admins = load_admin_data()
    role = input("Enter your role (1 for Admin, 2 for Member): ")
    
    if role == "1":  # Admin role
        admin_id = input("Enter your admin_id: ")
        admin_data = None

        for admin in admins:
            if admin["admin_id"] == admin_id:
                admin_data = admin
                break
        
        if admin_data:
            admin = Admin(admin_data["admin_id"], admin_data["name"]) 
            print(f"{admin_id} successfully logged in") 

            # Admin options
            print("1: Add Books")
            print("2: Add Members")
            print("3: View Members")
            print("4: View Available Books")

            while True:
                choice = input("Enter your choice: ")
                if choice == "1":
                    title = input("Enter book title: ")
                    author_name = input("Enter author name: ")
                    stock = int(input("Enter number of books available: "))
                    admin.add_books(title, author_name, stock)  # Add book method
                elif choice == "2":
                    member_id = input("Enter member ID: ")
                    name = input("Enter name: ")
                    role = input("Enter role (e.g.Student, Faculty): ")
                    admin.add_member(member_id, name, role)  # Add member method
                elif choice == "3":
                    admin.view_member()  
                elif choice == "4":
                    admin.view_avilable_books()  
                elif choice.lower() == "exit":
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid admin_id. Something went wrong.")
    # Member role
    elif role == "2":  
        member_id = input("Enter your member_id: ")
        name = input("Enter your name: ")
        member = Member(member_id, name,role)  

        print(f"Welcome, {name}! Member features:")
        print("1: Borrow a book")
        print("2: Return a book")
      

        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                book_name = input("Enter the book you want to borrow: ")
                borrow_date = datetime.now()
                expiry_date = (borrow_date + timedelta(days=15)).strftime("%Y-%m-%d")
                member.borrow_book(book_name, borrow_date, expiry_date)  # Borrow book method
                print(f"Book '{book_name}' borrowed by {name} (ID: {member_id})")
            elif choice == "2":
                book_name = input("Enter the book name: ")
                return_date = datetime.now()
                member.return_books(book_name, return_date) 
                print(f"Book '{book_name}' returned by {name} (ID: {member_id})")
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Invalid role. Please enter 1 for Admin or 2 for Member.")

if __name__ == "__main__":
    main()
