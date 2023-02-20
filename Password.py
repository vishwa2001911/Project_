# this program create to genarate random password 
#
#
#



import random

def password_genarater(length):
  
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_letters = lower_letters.upper()
    symbels = "!@#$%^&*?"
    numbers = "1234567890"
    
    all_list = lower_letters+ upper_letters + symbels +numbers
    random_list = random.choices(pas,weights=None, k=length)
    password = "".join(random_list)
    
    return f"Your password is :-{password}"
    

x = int(input("password length:-"))
print(Password_genarater(x))
