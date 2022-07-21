# 8.16.21

'''
Python Program to Create a Class in which One
Method Accepts a String from the User and Another Prints it
in another
'''

class Noolock:
    acceptor=input("Accept String: ")        
class Printer(Noolock):
    def __init__(self):
        super().__init__()
        print("Printed string: " + super().acceptor)
  


PP = Printer()
