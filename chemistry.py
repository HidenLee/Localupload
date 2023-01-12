a = input().split()
min = int(a[0])
max = int(a[1])
temp = int(input())

while temp != -999:
	if min <= temp <= max:
		print('ok')
		temp =int(input())
	else:
		print('no')
		break