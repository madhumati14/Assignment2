#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
#for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
#parameters as number and perform the operation. Write on python program which call all the
#functions from Arithmetic module by accepting the parameters from user.

import Arithmatic

def main():
	no1=int(input("Enter the no1="))
	no2=int(input("Enter the no2="))

	ans=ass2q1.Add(no1,no2)
	print("Addition is =",ans)

	ans=ass2q1.Sub(no1,no2)
	print("Substraction is=",ans)

	ans=ass2q1.Mult(no1,no2)
	print("Multiplication is=",ans)

	ans=ass2q1.Div(no1,no2)
	print("Division is=",ans)

if __name__=="__main__":
	main();
