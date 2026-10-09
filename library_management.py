import colorama
import ast
from colorama import Fore , Style , init
def menu():


 print( Fore.MAGENTA+ """
┌────────────────────────────────────────────────┐
│  [ SYSTEM INITIALIZED ]                        │
│                                                │
│       📚  LIBRARY MANAGEMENT SYSTEM            │
│                                                │
│  ────────────────────────────────────────────  │
│       DIGITAL LIBRARY MANAGEMENT PLATFORM       │
│  ────────────────────────────────────────────  │
│                                                │
│  STATUS : ● ONLINE                             │
└────────────────────────────────────────────────┘
""")
 print(Fore.GREEN+""" 1.Add Book
 2.View Book 
 3.Search Book 
 4.Register User 
 5.Issue Book 
 6.Return Book
 7.View Issued Books
 8.Exit """)



def read_book():
    with open("book_data.txt", "r") as f:
        book_data = f.readlines()

    books = []

    for line in book_data:
        if line.strip():  # Skip empty lines
            book = ast.literal_eval(line)
            books.append(book)

    return books

def add_book():
    book_data=read_book()

    print(Fore.GREEN+"---ADD BOOK---")
    
    if len(book_data) == 0:
      book_Id = 101
    else:
      book_Id = book_data[-1]["Book_Id"] + 1
    
    
    while True:
       book_name = input("Enter the Book name: ").strip()

       exists = False

       for i in book_data:
          if book_name.lower() == i["Book_Name"].lower():
             print(Fore.RED + "The Book Already Exists!")
             exists = True
             break

       if not exists:
          break

    author_name = input("Enter Author's name: ").strip()

    if author_name.replace(" ", "").isalpha():
        author_name = author_name.title()
    else:
         print(Fore.RED + "Invalid author name. Use letters only.")
    
    genre=input("Enter genre of the book : ")
    
    genre=genre.strip().title()
    section=input("Enter book section (e.g.A1) :").upper()
    
    while True:
       copies = input("Enter number of copies: ").strip()

       if copies.isdigit() and int(copies) > 0:
          copies = int(copies)
          break

       print(Fore.RED + "Enter a valid number greater than 0!")

    print(Fore.CYAN + "\n--- BOOK SUMMARY ---")
    print(f"Book ID      : {book_Id}")
    print(f"Book Name    : {book_name}")
    print(f"Author       : {author_name}")
    print(f"Genre        : {genre}")
    print(f"Section      : {section}")

    print(Fore.GREEN + "\n✓ BOOK DETAILS VALIDATED ")
    book = {
    "Book_Id": book_Id,
    "Book_Name": book_name,
    "Author": author_name,
    "Genre": genre,
    "Section": section,
    "No_of_Copies":copies
     }

    book_data.append(book)
    
    with open("book_data.txt", "w") as f:
          for i in book_data:
            f.write(str(i) + "\n")

def view_book():
    book_data = read_book()
    print("---BOOKS AVAILABLE---".center(85))

    print("\nBook_Id | Book_Name | Author | Genre | No_of_Copies | Section")
    print("-" * 85)

    for book in book_data:
        print(f"{book['Book_Id']} | {book['Book_Name']} | {book['Author']} | {book['Genre']} | {book['No_of_Copies']} | {book['Section']}")
    print("-" * 85)


def search_book():
    book_data = read_book()
    book_name = input("Search book name: ").strip()

    for i in book_data:
        if book_name.lower() == i["Book_Name"].lower():
            print(Fore.GREEN + "Book Available!")
            print("\nBook_Id | Book_Name | Author | Genre | No_of_Copies | Section")
            print("-" * 85)
            print(
                f"{i['Book_Id']} | {i['Book_Name']} | "
                f"{i['Author']} | {i['Genre']} | "
                f"{i['No_of_Copies']} | {i['Section']}"
            )
            print("-" * 85)
            break
    else:
        print(Fore.RED + "Book is not available!")

def read_user():
    with open("user_data.txt", "r") as f:
        user_data = f.readlines()

    users = []

    for line in user_data:
        user = ast.literal_eval(line) #converts string back into dictionary 
        users.append(user)

    return users
def register_user():
    user_data=read_user()
    

    user_name=input("Enter you name : ").strip().title()
    if len(user_data) == 0:
          user_Id = 1001
    else:
          user_Id = user_data[-1]["User ID"] + 1
    user={ "User Name": user_name,
          "User ID" : user_Id }
    user_data.append(user)

    with open("user_data.txt", "w") as f:
     for i in user_data:
        f.write(str(i) + "\n")
def write_book(book_data):
    with open("book_data.txt", "w") as f:
        for book in book_data:
            f.write(str(book) + "\n")

def read_issued_books():
    try:
        with open("issued_books.txt", "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        return []

    issued_books = []

    for line in data:
        if line.strip():
            record = ast.literal_eval(line)
            issued_books.append(record)

    return issued_books


def issue_book():
    user_data = read_user()

    print("\n===== ISSUE BOOK =====")

    user_Id = int(input("Enter User ID: "))
    for i in user_data:
          if user_Id == i["User ID"]:
             print("User Found!")
             break
    else:
         print("User Not Registered!")
         return
    book_data = read_book()
    book_Id = int(input("Enter Book ID: "))
    
    for i in book_data:
        if book_Id == i["Book_Id"]:
            print("Book Found!")

            if i["No_of_Copies"] > 0:
                print("Copies Available!")

                i["No_of_Copies"] -= 1
                write_book(book_data)

                issue_record = {
                    "User ID": user_Id,
                    "Book ID": book_Id,
                    "Book Name": i["Book_Name"]
                }

                with open("issued_books.txt", "a") as f:
                    f.write(str(issue_record) + "\n")

                
                print(Fore.CYAN + "\n===== BOOK ISSUE RECEIPT =====")
                print("-" * 35)
                print(f"User ID       : {user_Id}")
                print(f"Book ID       : {book_Id}")
                print(f"Book Name     : {i['Book_Name']}")
                print(f"Copies Left   : {i['No_of_Copies']}")
                print(f"Status        : Issued Successfully!")
                print("-" * 35)


            else:
                print("No copies available!")

            break
    else:
        print("Book does not exist!")
        return


def return_book():
    issued_books = read_issued_books()

    print("\n===== RETURN BOOK =====")

    if len(issued_books) == 0:
        print("No books are currently issued!")
        return

    user_Id = int(input("Enter User ID: "))
    book_Id = int(input("Enter Book ID: "))
    
    for i in issued_books:
        if i["User ID"] == user_Id and i["Book ID"] == book_Id:
            print("Issue record found!")
            break
    else:
        print("No matching issue record found!")
        return
    
    book_data = read_book()

    for book in book_data:
        if book["Book_Id"] == book_Id:
            book["No_of_Copies"] += 1
            write_book(book_data)
            print("Book copies updated successfully!")
            break
    else:
        print("Book not found in library records!")
        return
    
    updated_issues = []

    for record in issued_books:
        if not (record["User ID"] == user_Id and record["Book ID"] == book_Id):
            updated_issues.append(record)

    with open("issued_books.txt", "w") as f:
        for record in updated_issues:
            f.write(str(record) + "\n")

    print(Fore.GREEN + "\n===== BOOK RETURNED SUCCESSFULLY! =====")
    print(f"User ID   : {user_Id}")
    print(f"Book ID   : {book_Id}")
    print("Status    : Returned Successfully!")


def view_issued_books():
    issued_books = read_issued_books()

    print(Fore.CYAN + "\n===== CURRENTLY ISSUED BOOKS =====")

    if len(issued_books) == 0:
        print(Fore.YELLOW + "No books are currently issued!")
        return

    print("-" * 75)
    print(f"{'User ID':<12} {'Book ID':<12} {'Book Name':<30}")
    print("-" * 75)

    for record in issued_books:
        print(
            f"{record['User ID']:<12} "
            f"{record['Book ID']:<12} "
            f"{record['Book Name']:<30}"
        )

    print("-" * 75)
    print(f"Total issued records: {len(issued_books)}")



while True:


    menu()
    choice=input("Enter your choice from 1 to 6 : ")

    if choice=="1":
        add_book()
    elif choice=="2":
        view_book()
    elif choice=="3":
        search_book()
    elif choice=="4":
        register_user()
    elif choice=="5":
        issue_book()
    elif choice=="6":
        return_book()
    elif choice=="7":
        view_issued_books()
    elif choice=="8":
        print(Fore.CYAN + "\n📚 Thank you for using LIBRARY OS!")
        print(Fore.GREEN + "Session terminated successfully. See you next time! 👋")
        break
    else:
        print(Fore.RED+"Invalid choice")


   


