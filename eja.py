def simple_interest(p,r,t):
	return p*r*t


def simple_interest_amount(p,r,t):
	a = (r*t + 1) * p
	return a

def cp_inter(p,r,t,n):
	b = p * (1+ r / n) ** (n * t)
	return b
	

print(cp_inter(1500000,0.043,6,0.5))
# print(simple_interest(100,50,3/2),"",simple_interest_amount(100,50,3/2))



	