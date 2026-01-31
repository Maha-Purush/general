############      ARGS      #################
#def add(*args):
  #sum = 0
  #for arg in args:
    #sum = sum + arg

  #return sum
  
#n = int(input("How many numbers do you want to add?: "))
#user_list = []
#for i in range(n):
  #num = int(input(f"Enter number {i+1}: "))
  #user_list.append(num)

#print("The addition of all terms is :", add(*user_list))

###############          KWARGS          ###################
def example(**kwargs):
  for key,value in kwargs.items():
    print(f"Key: {key} \
          Value: {value}")

example(street = "123 Fake Street", 
        city = "Detroit", 
        state = "MI", 
        zip = "54321")

 #ARGS AND KWARGS can be used together in a function, but the order has to be reflected in the arguments AND the parameters.