#Write a program which accept one number form user and return addition of its factors.
#Input : 12
#Output : 16   (1+2+3+4+6)


def fun(no):
	imult=1
	for i in range(1,no+1):
		imult=imult*i
	print(imult)

def main():
	print("enter the number")
	no=int(input())
	fun(no)

	
if __name__=="__main__":
	main()
