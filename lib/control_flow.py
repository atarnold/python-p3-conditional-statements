#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if password == "12345" and (username == 'admin' or username == "ADMIN") :
        print("Access granted")
    else:
        print("Access denied")   
    pass

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out here!"
    elif temperature > 85:
        return "Its too dang hot out here"
    else:
        return "Its perfect out here!"                
    pass

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz" 
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num        
    pass

def calculator(operation, num1, num2):
    # your code here
    try:
        quotient = f"{num1}{operation}{num2}"
        return eval(quotient)
    except:
        print ("Invalid oepraion!")   
        return None 
    pass