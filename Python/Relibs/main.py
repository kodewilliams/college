import os
import mysql.connector

# Database connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="relibs"
)

cursor = db.cursor()

def clear():
  os.system('clear')

def pause():
  programPause = input("\n\nPress the <enter> key to continue...")

def menu():
  while(True):
    clear()
    print ("RELIBS :: Main Menu\n\n")
    print("1 :: Authors")
    print("2 :: Publishers")
    print("3 :: Books")
    print("4 :: Reviews")
    print("5 :: Readers")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      print("Thank you for using RELIBS.")
      exit(0)
    process_choice(choice)

def process_choice(choice):
  clear()
  if choice == 1:
    author_menu()
  elif choice == 2:
    publisher_menu()
  elif choice == 3:
    book_menu()
  elif choice == 4:
    review_menu()
  elif choice == 5:
    reader_menu()

def author_menu():
  while(True):
    clear()
    print ("RELIBS :: Author Menu\n\n")
    print("1 :: Create author(s)")
    print("2 :: View author(s)")
    print("3 :: Edit author(s)")
    print("4 :: Delete author(s)")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      return
    elif choice == 1:
      create_author()
    elif choice == 2:
      view_author()
    elif choice == 3:
      edit_author()
    elif choice == 4:
      delete_author()

def create_author():
  global cursor, db
  clear()
  sql = "INSERT INTO Author (FirstName, LastName, Country, YearOfBirth) VALUES (%s, %s, %s, %s)"
  print ("RELIBS :: Create Author\n\n")
  first_name = input("First Name :: ")
  last_name = input("Last Name :: ")
  country = input("Country :: ")
  year = input("Year of Birth :: ")
  data = (first_name, last_name, country, year)
  cursor.execute(sql, data)
  db.commit()
  print("\nAuthor created.")
  pause()

def edit_author():
  global cursor, db
  clear()
  sql = "SELECT * FROM Author WHERE AuthorID = %s"
  print ("RELIBS :: Edit Author\n\n")
  author_id = input("Author ID :: ")
  data = (author_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  sql = "UPDATE Author SET "
  clear()
  print("Available Attributes :: ")
  print("\nFirstName (String)")
  print("LastName (String)")
  print("Country (String)")
  print("YearOfBirth (Year)\n")
  while(True):
    attr = input("Attribute :: ")
    val = input("New Value :: ")
    sql += attr + " = '" + val + "'"
    again = input("Finished? (;) :: ")
    if again == ';': break
  sql += " WHERE AuthorID = " + author_id
  cursor.execute(sql)
  db.commit()
  print("\nAuthor edited.")
  pause()

def view_author():
  while(True):
    clear()
    print ("RELIBS :: View Author\n\n")
    print("1 :: View author by ID")
    print("2 :: View all authors")
    print("3 :: View author by name")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      return
    elif choice == 1:
      view_author_by_id()
    elif choice == 2:
      view_all_authors()
    elif choice == 3:
      view_author_by_name()

def view_author_by_id():
  global cursor, db
  clear()
  sql = "SELECT * FROM Author WHERE AuthorID = %s"
  print ("RELIBS :: View Author by ID\n\n")
  author_id = input("Author ID :: ")
  data = (author_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def view_all_authors():
  global cursor, db
  clear()
  sql = "SELECT * FROM Author"
  print ("RELIBS :: View All Authors\n\n")
  cursor.execute(sql)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def view_author_by_name():
  global cursor, db
  clear()
  sql = "SELECT * FROM Author WHERE FirstName = %s AND LastName = %s"
  print ("RELIBS :: View Author by Name\n\n")
  author_fn = input("Author First Name :: ")
  author_ln = input("Author Last Name :: ")
  data = (author_fn, author_ln, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def delete_author():
  global cursor, db
  clear()
  sql = "DELETE FROM Author WHERE AuthorID = %s"
  print ("RELIBS :: Delete Author\n\n")
  author_id = input("Author ID :: ")
  data = (author_id, )
  cursor.execute(sql, data)
  print("\nAuthor deleted.")
  pause()

def publisher_menu():
  while(True):
    clear()
    print ("RELIBS :: Publisher Menu\n\n")
    print("1 :: Create publisher(s)")
    print("2 :: View publisher(s)")
    print("3 :: Edit publisher(s)")
    print("4 :: Delete publisher(s)")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      return
    elif choice == 1:
      create_publisher()
    elif choice == 2:
      view_publisher()
    elif choice == 3:
      edit_publisher()
    elif choice == 4:
      delete_publisher()

def create_publisher():
  global cursor, db
  clear()
  sql = "INSERT INTO Publisher (Name, Country, State, YearStarted) VALUES (%s, %s, %s, %s)"
  print ("RELIBS :: Create Publisher\n\n")
  name = input("Publisher Name :: ")
  country = input("Country :: ")
  state = input("State :: ")
  year = input("Year Started :: ")
  data = (name, country, state, year, )
  cursor.execute(sql, data)
  db.commit()
  print("\nPublisher created.")
  pause()

def edit_publisher():
  global cursor, db
  clear()
  sql = "SELECT * FROM Publisher WHERE PublisherID = %s"
  print ("RELIBS :: Edit Publisher\n\n")
  pub_id = input("Publisher ID :: ")
  data = (pub_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  sql = "UPDATE Publisher SET "
  clear()
  print("Available Attributes :: ")
  print("\nName (String)")
  print("Country (String)")
  print("State (String)")
  print("YearStarted (Year)\n")
  while(True):
    attr = input("Attribute :: ")
    val = input("New Value :: ")
    sql += attr + " = '" + val + "'"
    again = input("Finished? (;) :: ")
    if again == ';': break
  sql += " WHERE PublisherID = " + pub_id
  cursor.execute(sql)
  db.commit()
  print("\nPublisher edited.")
  pause()

def view_publisher():
  global cursor, db
  clear()
  sql = "SELECT * FROM Publisher"
  print ("RELIBS :: View Publishers\n\n")
  cursor.execute(sql)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def delete_publisher():
  global cursor, db
  clear()
  sql = "DELETE FROM Publisher WHERE PublisherID = %s"
  print ("RELIBS :: Delete Publisher\n\n")
  pub_id = input("Publisher ID :: ")
  data = (pub_id, )
  cursor.execute(sql, data)
  print("\nPublisher deleted.")
  pause()

def book_menu():
  while(True):
    clear()
    print ("RELIBS :: Book Menu\n\n")
    print("1 :: Create book(s)")
    print("2 :: View books")
    print("3 :: View books by genre")
    print("4 :: View books by author")
    print("5 :: View book rating")
    print("6 :: Edit book(s)")
    print("7 :: Delete book(s)")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      return
    elif choice == 1:
      create_book()
    elif choice == 2:
      view_book()
    elif choice == 3:
      view_book_by_genre()
    elif choice == 4:
      view_book_by_author()
    elif choice == 5:
      view_book_rating()
    elif choice == 6:
      edit_book()
    elif choice == 7:
      delete_book()

def create_book():
  global cursor, db
  clear()
  sql = "INSERT INTO Book (Title, Genre, PublisherID, Description, UnitPrice, YearOfRelease) VALUES (%s, %s, %s, %s, %s, %s)"
  print ("RELIBS :: Create Book\n\n")
  title = input("Title :: ")
  genre = input("Genre :: ")
  pub_id = input("Publisher ID :: ")
  desc = input("Description :: ")
  price = input("Price :: ")
  yor = input("Year of Release :: ")
  data = (title, genre, pub_id, desc, price, yor, )
  cursor.execute(sql, data)
  db.commit()
  print("\nBook created.")
  pause()

def edit_book():
  global cursor, db
  clear()
  sql = "SELECT * FROM Book WHERE BookID = %s"
  print ("RELIBS :: Edit Book\n\n")
  book_id = input("Book ID :: ")
  data = (book_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  sql = "UPDATE Book SET "
  clear()
  print("Available Attributes :: ")
  print("\nTitle (String)")
  print("Gender (String)")
  print("PublisherID (Int)")
  print("Description (String)")
  print("UnitPrice (Float)")
  print("YearOfRelease (Year)\n")
  while(True):
    attr = input("Attribute :: ")
    val = input("New Value :: ")
    sql += attr + " = '" + val + "'"
    again = input("Finished? (;) :: ")
    if again == ';': break
  sql += " WHERE BookID = " + book_id
  cursor.execute(sql)
  db.commit()
  print("\nBook edited.")
  pause()

def view_book():
  global cursor, db
  clear()
  sql = "SELECT * FROM Book"
  print ("RELIBS :: View Books\n\n")
  cursor.execute(sql)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def view_book_by_genre():
  global cursor, db
  clear()
  sql = "SELECT * FROM Book WHERE Genre = %s"
  print ("RELIBS :: View Book Rating\n\n")
  genre = input("Genre :: ")
  data = (genre, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def view_book_by_author():
  global cursor, db
  clear()
  sql = "SELECT Title, FirstName, LastName FROM Book join BookAuthor ON Book.BookID = BookAuthor.BookID join Author ON BookAuthor.AuthorID = Author.AuthorID WHERE Author.FirstName = %s;"
  print ("RELIBS :: View Books by Author\n\n")
  fn = input("First Name :: ")
  data = (fn, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def view_book_rating():
  global cursor, db
  clear()
  sql = "SELECT Title, AVG(Rating) AS 'Average Rating' FROM Book join ReaderBookReview using (BookID) join Review using (ReviewID) where Title = %s"
  print ("RELIBS :: View Book Rating\n\n")
  title = input("Book Title :: ")
  data = (title, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def delete_book():
  global cursor, db
  clear()
  sql = "DELETE FROM Book WHERE BookID = %s"
  print ("RELIBS :: Delete Book\n\n")
  book_id = input("Book ID :: ")
  data = (book_id, )
  cursor.execute(sql, data)
  print("\nBook deleted.")
  pause()

def review_menu():
  while(True):
    clear()
    print ("RELIBS :: Review Menu\n\n")
    print("1 :: Create review(s)")
    print("2 :: View review(s)")
    print("3 :: Edit review(s)")
    print("4 :: Delete review(s)")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      return
    elif choice == 1:
      create_review()
    elif choice == 2:
      view_review()
    elif choice == 3:
      edit_review()
    elif choice == 4:
      delete_review()

def create_review():
  global cursor, db
  clear()
  sql = "INSERT INTO Review (Comment, Rating) VALUES (%s, %s)"
  print ("RELIBS :: Create Review\n\n")
  comment = input("Comment :: ")
  rating = input("Rating :: ")
  data = (comment, rating, )
  cursor.execute(sql, data)
  db.commit()
  print("\nReview created.")
  pause()

def edit_review():
  global cursor, db
  clear()
  sql = "SELECT * FROM Review WHERE ReviewID = %s"
  print ("RELIBS :: Edit Review\n\n")
  rev_id = input("Review ID :: ")
  data = (rev_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  sql = "UPDATE Review SET "
  clear()
  print("Available Attributes :: ")
  print("\nComment (String)")
  print("Rating (Int)")
  print("YearOfReview (Year)\n")
  while(True):
    attr = input("Attribute :: ")
    val = input("New Value :: ")
    sql += attr + " = '" + val + "'"
    again = input("Finished? (;) :: ")
    if again == ';': break
  sql += " WHERE ReviewID = " + rev_id
  cursor.execute(sql)
  db.commit()
  print("\nReview edited.")
  pause()

def view_review():
  global cursor, db
  clear()
  sql = "SELECT * FROM Review"
  print ("RELIBS :: View Reviews\n\n")
  cursor.execute(sql)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  pause()

def delete_review():
  global cursor, db
  clear()
  sql = "DELETE FROM Review WHERE ReviewID = %s"
  print ("RELIBS :: Delete Review\n\n")
  rev_id = input("Review ID :: ")
  data = (rev_id, )
  cursor.execute(sql, data)
  print("\nReview deleted.")
  pause()

def reader_menu():
  while(True):
    clear()
    print ("RELIBS :: Reader Menu\n\n")
    print("1 :: Create reader(s)")
    print("2 :: View reader(s)")
    print("3 :: Edit reader(s)")
    print("4 :: Delete reader(s)")
    print("\n0 :: Exit")
    choice = int(input("\nSelection :: "))
    if choice == 0:
      clear()
      return
    elif choice == 1:
      create_reader()
    elif choice == 2:
      view_reader()
    elif choice == 3:
      edit_reader()
    elif choice == 4:
      delete_reader()

def create_reader():
  global cursor, db
  clear()
  sql = "INSERT INTO Reader (FirstName, LastName, Country) VALUES (%s, %s, %s)"
  print ("RELIBS :: Create Reader\n\n")
  fn = input("First Name :: ")
  ln = input("Last Name :: ")
  country = input("Country :: ")
  data = (fn, ln, country, )
  cursor.execute(sql, data)
  db.commit()
  print("\nReader created.")
  pause()

def edit_reader():
  global cursor, db
  clear()
  sql = "SELECT * FROM Reader WHERE ReaderID = %s"
  print ("RELIBS :: Edit Reader\n\n")
  reader_id = input("Reader ID :: ")
  data = (reader_id, )
  cursor.execute(sql, data)
  results = cursor.fetchall()
  if (results):
    print("Results\n\n")
    for row in results:
      print(row)
  else:
      print("\nNo results.")
  sql = "UPDATE Reader SET "
  clear()
  print("Available Attributes :: ")
  print("\nFirstName(String)")
  print("LastName (String)")
  print("Country (String)")
  while(True):
    attr = input("Attribute :: ")
    val = input("New Value :: ")
    sql += attr + " = '" + val + "'"
    again = input("Finished? (;) :: ")
    if again == ';': break
  sql += " WHERE ReaderID = " + reader_id
  cursor.execute(sql)
  db.commit()
  print("\nReader edited.")
  pause()

def view_reader():
  global cursor, db
  clear()
  sql = "SELECT * FROM Reader"
  print ("RELIBS :: View Readers\n\n")
  cursor.execute(sql)
  results = cursor.fetchall()
  if (results):
    clear()
    print("Results\n\n")
    for row in results:
      print(row)
  else:
    print("\nNo results.")
  pause()

def delete_reader():
  global cursor, db
  clear()
  sql = "DELETE FROM Reader WHERE ReaderID = %s"
  print ("RELIBS :: Delete Reader\n\n")
  reader_id = input("Reader ID :: ")
  data = (reader_id, )
  cursor.execute(sql, data)
  print("\nReader deleted.")
  pause()

def main():
  # Define variables needed
  global cursor
  # Display menu on launch
  menu()
    
# Start program
main()