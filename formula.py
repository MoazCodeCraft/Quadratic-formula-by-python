from math import*
a=int(input("Enter a"))
b=int(input("Enter b"))      
c=int(input("Enter c"))
discriminant=(b*b-4*a*c)
def quadratic():
    if discriminant<0:
            print('ROOT OF NEGATIVE NOT POSSIBLE')
    else:      

            root=(-b+sqrt(discriminant))  
            equ=root/2*a
            print(f"Positive value of discriminant== {equ}")           
            root=(-b+sqrt(discriminant))  
            equ=root/2*a
            print(f"Negative value of discriminant== {equ}")  
