#Write a program which accept one number and display below pattern.
#Input :
#5
#Output :	* * * * *
#		      * * * * *
#		      * * * * *
#		      * * * * *
#		      * * * * *

def pattern():

	print("enter the number")
	no=int(input())

	for i in range(no):
		for j in range(no):
			print("*",end=" ")
		print(" ")

def main():
	pattern();

if __name__=="__main__":
	main()
