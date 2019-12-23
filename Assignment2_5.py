#Write a program which accept one number for user and check whether number is prime or not.
#Input :5
#Output : It is Prime Number


def cheakprime(no):
	for i in range(2,no+1):
		if((no%i)==0):
			break
	return i;
		

def main():
	print("enter the number")
	no=int(input());
	bret=cheakprime(no);
	if bret==no:
		print("no is prime")
	else:
		print("no is not prime")
	
if __name__=="__main__":
	main();
