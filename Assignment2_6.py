#6. Write a program which accept one number and display below pattern.
#Input :5
#Output :
#	*	*	*	*	*
#	*	*	*	*
#	*	*	*	
#	*	*	
#	*		

def displaypattern(no):
	for i in range(no,0,-1):
		for j in range(1,no+1):
			if i>=j:
				print("*",end=" ")
			else:
				print(" ",end=" ")
		print(" ")
def main():
	print("enter the no")
	no=int(input());
	displaypattern(no);

if __name__=="__main__":
	main()
