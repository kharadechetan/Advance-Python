# class Mobile:
#     def __init__(self):
#         print('Realme X')

# realme=Mobile()


#  Constructor Without Parameter **************************************************
# class Mobile:
#     def __init__(self):
#         self.model='Real Me X'
    
#     def show_model(self):
#         print("model : ",self.model)

# realme=Mobile()
# realme.show_model()



# Constructor With Parameter ***********************************************************

class Mobile:
    def __init__(self,m,v=80):
        self.model=m
        self.volumn=v
    def show_model(self,p):
        price=p
        print("model : ",self.model,'price : ',price)
        print("volumn : ",self.volumn)
        
realme=Mobile('Real Me X')
realme.show_model(1000)

print()

redmi=Mobile('Redmi',50)
redmi.show_model(2000)
