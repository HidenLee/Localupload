def read(text):
	ridename, limit = map(str.strip, text.split(':'))
	cmin = cmax = None
	if '~' in limit:
		cmin, cmax = map(lambda x: int(x.replace('cm','')),limit.split('~'))
	elif '이상' in limit:
		cmin = int(limit.replace('cm 이상',''))
	return ridename, cmin, cmax


if __name__ == "__main__":
    ridename, cmin, cmax = read(input())
    print("이름:", ridename)
    print("하한:", cmin)
    print("상한:", cmax)