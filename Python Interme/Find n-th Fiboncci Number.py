# a = (a-1) + (a-2)

# recurssion mehthod

def Fibonacci(n):
	if n<0:
		print("Wrong Input ! Please Check Again")
	elif n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))


'''so in Fibonacci Series (9th ) number is 21'''