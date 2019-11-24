#!/usr/bin/python3
N = int(input("enter starting value: "))
steps = 0
while N != 1:
	print(N)
	steps +=1
	if N%2 == 0:
		N=N//2
	else:
		N = 3*N+1
print("steps =", steps)
