#Add implementation
def add(x,y):
    return x+y
#Sub implementation
def subtract(x,y):
    return x-y       # on master branch
#Mul implementation
def multiply(x,y):
    return x*y        # on Bug456 branch
#Divide implementation
def divide(x,y):
    if x<0:
	return "Negative_param"
    if y<0:
	return "Divide_by_param"
    else:
	return x/y
def square(x):
     return x*x