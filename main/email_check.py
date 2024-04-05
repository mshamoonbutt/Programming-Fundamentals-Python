at_the_rate=False
start_end=False
dot=False
length=False
repeat=False
email=input("Enter your email: ")

if '@' in email:
    at_the_rate=True
    
if email[0]!='@' and email[-1]!='@':
    start_end=True
    
if '.' in email[email.index('@'):-1]:
    dot=True 

if len(email[email.index('.'):-1])>=2:
    length=True       

                   
if at_the_rate and start_end and dot and length:
    print("Valid")                   
else:
    print("Invalid")           