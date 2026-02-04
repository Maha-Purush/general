#class Car:
  #def __init__(self, model , year,color, for_sale):
    #self.model = model
    #self.year = year
    #self.color = color
    #self.for_sale = for_sale

  #def drive(self):
    #print(f"You are driving a {self.model} of {self.color} color")

class Student:
  class_var = 2024
  def __init__(self, Name, Class):
    self.Name = Name
    self.Class = Class

  def describe(self):
    print(f"Name: {self.Name} \
          Class: {self.Class}\
            Year: {self.class_var}")