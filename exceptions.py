#python exceptions let you deal with unexpected results

try:
	print(a)						#this will throw an exception since a is not defined
except:
	print("a is not defined!")
	
#there are specific errors to help with cases
try:
	print(a)
except NameError:
	print("a is not defined!")
except:
	print("Something else went wrong.")
	
#This will break our program since a is not defined
print(a)