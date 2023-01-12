def gugudan():

	for i in list(range(2,10)):
		for j in list(range(1,10)):
			print(i,' * ',j,' = ',i*j)



def multiply(c):
	for j in list(range(1,10)):
			print(c,' * ',j,' = ',c*j)

def gugudan2():
	for i in list(range(2,10)):
		multiply(i)

gugudan2()