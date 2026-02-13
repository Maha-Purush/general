class Person:

  def __init__(self, name, id):
    self.name = name
    self.id = id
    self.book = set()

  def borrow_book(self, book_title):
    print(f"{self.name} is borrowing {book_title}")  
    self.book.add(book_title)

  def return_book(self, book_title):
    print(f"{self.name} is returning {self.book.pop()}")

  def details(self):
    print(f"The details of {self.name} are: ")
    print(f"Name\tID\tBooks Borrowed")
    print(f"{self.name}\t{self.id}\t{self.book}")

    
print("////////Mini Library System////////")
name = input(("Enter the name of the library member: "))
id = input(("Enter the id of the library member: "))
member = Person (name, id)
while True:
  option = int(input("Enter the operation to perform: \n 1. View details\n 2. Borrow book\n 3. Return book"))

  match(option):
    case 1:
      member.details()

    case 2:
      book_title = input("Enter the title of the book to borrow: ")
      member.borrow_book(book_title)

    case 3:
      book_title = input("Enter the title of the book to return: ")
      member.return_book(book_title)

    case _:
      print("Invalid option selected.")