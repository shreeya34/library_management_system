from database import Book, Member, Admin


def main():
    role = input("Enter your role: ")
    admin = None

    if role == "1":
        admin_id = input("Enter your admin_id: ")
        admin = Admin(admin_id, "Admin Name")  
    if not admin:
        print("Invalid admin_id")
    else:
        print(f"{admin_id} successfully logged in")
        while True:
            choice = input("Enter your choice: ")
            if choice == "1":
                title = input("Enter book title: ")
                author_name = input("Enter author name: ")
                stock = input("Enter number of books available: ")
                admin.add_books(title, author_name, stock)  
            elif choice == "2":
                name = input("Enter a name: ")
                roles = input("Enter your role: ")
                admin.add_member(name, roles, None)  
            elif choice == "exit":
                print("Exiting...")
                break
            else:
                print("Invalid Choice. Please try again")


if __name__ == "__main__":
    main()

               
                
                

            
                
                
            
        
        
        
        

  
        

        
    
    




        
        
    
        
        
        
        
        