x=[1,2]
print(x.append(3))
##in python append didn't return any value ,
#in python if function doesn't return any value so  it returns 'None'  by default. 
#In-place operation:  directly modifies an  existing list ( ). 
#It does not create a new list.x

y=[1,2]
z=y.append(3)
print(z)
#Python's append() method modifies lists in place and evaluates to None. 
#Therefore, z becomes None while the original list y is successfully 

x = [1, 2]
x.append(3)  
print(x) 
#in this case append modifies the list.
#and after that  the print statement displays  updated list 
