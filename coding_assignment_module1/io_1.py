#WAP that accepts a sequence of comma separated numbers from user 
#and generates a list and tuple with those numbers


nums = input("Enter the numbers\n").split(",")
nums = [int(n) for n in nums]
print(nums)

print(tuple(nums))