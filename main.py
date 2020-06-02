#+addition
#-subtraction
#*multiplication
#/division
#% remainder
#** exponent
#// is division without decimals
#> greater than
#<less than
#>= greater than equal to
#<= less than equal to
#x==y will check if equal
#x !=y is x is not equal to

#amountofnumbers=int(input("Enter how many number you want of the fibbonachi sequence"))
#Pascal's triangle ask for number and then tell if that number is a prime number or not ask for max count n should the first n prime number 


t=2
prime_number=int(input("Enter a number"))

if prime_number%0 !=0
  break
  
while True:
  Fizz_Buzz=int(input("Enter a number "))
  if Fizz_Buzz%3==0:
    if Fizz_Buzz%15==0:
      print("Fizz Buzz")
    else:
      print("Fizz")
  elif Fizz_Buzz%5==0:
    print("Buzz")
  else:
    print("Oops")

fan_status="unkown"
while True:
  command=input(f'Enter what you would like to do with the fan(on off or q)')
  command=command.lowercase
  if command=='on' :
    if fan_status=="on":
      print("fan already on")
    else:
      print("Fan turned on")
      fan_status="on"
  elif command=="off":
    if fan_status=="off":
      print("Fan already turned off")
    else:
      print("Fan turned off")
      fan_status="off"
  elif command=="q":
    break
  else:
    print("Invalid command")
    

number3=int(input("Enter a number"))
if number3%2==0:
  print(f'The number is even')
else:
  print(f' the number is odd')

number4=int(input("Enter a number"))
if number4%5==0:
  print(f'The number is divisble by 5')
else:
  print(f' the number is not divisible by 5')

number5=int(input("Enter a number"))
factorial=1
for x in range(2,number5+1):
  factorial*=x
print(f'The factorial of {number5} is {factorial}') 




































#simple interest calculation
str9=(float(input(''' What interest rate would you like to use?
Please enter a decimal ex. 0.035 ''')))
str17=int(input("Enter the amount of months that have passed since the loan was taken "))
str11=int(input("Enter how much money is loaned $"))
str10=(str17/12)
str13=(str10*str9)
str14=(str13*str11)
str15=(str10*str14)
str16=(str15+str11)
print(f'${str16}')


#first string program
number1 = (input("Enter a word or number "))
number2 = (input("Enter another word or number "))
str1=str(number1)
str2=str(number2)
print()
print(f'The first entry is a number: {str1.isnumeric()}')
print(f'The second entry is a number: {str2.isnumeric()}')


#second string program
print()
str3=(input("Enter a word a three or more letter word "))
str4=str(input("Enter a letter you would like to take out of your word "))
print()
print(f"If your word had {str4} taken out of it it would look like {str3.split(str4)}")


#3rd string program
print()
print(f'Your word is typed in all lowercase: {str3.islower()}')


#4th string program
print()
str5=str((input("Enter a letter that is found in your word ")))
print(f'Your letter has been found{str3.partition(str5)}')

#5th string program
print()
str6=int(str(input("Enter a dividened ")))
str7=int(str(input("Enter a divisor ")))
str8=str(str6/str7)
print(f'Quotient is decimal: {str8.isdecimal()}')

#using if function
str18=int(input("Enter a number "))
str19=int(input("Enter another number "))
if str18>str19:
  print(f'{str18} is greater than {str19} the result is {str18-str19}')
elif str18==str19:
  print("Your numbers are equal ")
else:
  print(f'{str18} is less than {str19} the result is {str18+str19}')
str20=int(input("Enter your child's age "))
if 13<=str10<=18:
  print(f' Your child is an adult')
elif 18<=str20:
  print("Your child is a teenager ")
elif 4<=str10<=12:
  print("Your child is a kid")
else:
  print("Your child is a kid")
str21=str(input("Enter your weight"))
str21=int or float(str21)
str22=str(input("Enter you weight unit"))
if str21 == ("kg"):
  print(f'{str21/2.2}lbs')
else:
  print(f'{str21*2}kg')
str22='hello worl'
print(str22())