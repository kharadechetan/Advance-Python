

class Mobile:
    fp="Yes"        # class variable
    
    @classmethod
    def is_fp(cls):
        print(cls.fp)    # Accessing class variable
        
realme=Mobile()

Mobile.is_fp()
# print(Mobile.fp)