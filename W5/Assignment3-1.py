#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


Hrs = input("Enter Hours:")
Pay = input("Enter Pay: ")

h = float(Hrs)
p = float(Pay)

def computepay(hrs,pay):
       if hrs <= 40 :
           p=hrs*pay
       else:
           p=((40 * pay) + ((hrs - 40) * (pay * 1.5)))
       return p

o = computepay(h,p)
print(o)