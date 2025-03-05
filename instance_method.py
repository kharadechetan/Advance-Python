# class Mobile:
#     def show_model(self):
#         print("Real Me x")
        
# realme=Mobile()
# realme.show_model()

# instance method without parameter  ********************************************************
# class Mobile:
#     def __init__(self):
#         self.model='Real Me x'
        
#     def show_model(self):
#         print("model : ",self.model)
        
# realme=Mobile()
# realme.show_model()


class Mobile:
    def __init__(self):
        self.model='Real Me x'
        
    def show_model(self,p):
        self.price=p
        print("model : ",self.model,self.price)
        
realme=Mobile()
realme.show_model(1000)