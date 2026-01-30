def name_operation(fname, lname):
  fname = fname.capitalize()
  lname = lname.capitalize()

  return fname + lname

first_name = input("Enter the first name of a person(all in small): ")
last_name = input("Enter the last name of a person(all in small): ")
print("The capitalized name is : ", name_operation(first_name, last_name))