num = int(input("Enter the number\n"))

def addDigits(num):
	s = 0; l = []
	for ch in str(num):
		l.append(int(ch))

	s = [s + k for k in l]
	sum_of_digits = sum(s)
	return sum_of_digits

print(addDigits(num))


            
            
        	
