def print_list(a):
	for i in a:
		print(i)

a_list = [3, 56, 78, 123, 2452, 65656]

print_list(a_list)


def func(a,b):
	
	if a > b:
		print(a,'>',b)
	if b > a: 
		print(b,'>',a)
	else:
		print('same')

func(input(),input())
	