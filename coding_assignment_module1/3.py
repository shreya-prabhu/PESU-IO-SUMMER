#Write a python program for binary search to search a number 
#in the list of given numbers. 
#If the number isn't present, give the appropriate message
#Both the list and the number to be searched is given by the user.

nums = input("Enter the numbers that constitute the list\n").split(",")
nums = [int(n) for n in nums]
nums.sort()
value = int(input("Enter the value to be searched\n"))

low=0 ;  high = len(nums) - 1
def binary_search(nums,low,high,value):
	

	flag = 0
	pos = -1

	while(low<=high and flag == 0):
		mid = int((low+high)/2)

		if nums[mid] == value:
			pos = mid
			flag = 1

		elif value<nums[mid]:
			high = mid-1

		elif value>nums[mid]:
			low = mid+1

	if pos == -1:
		print( "The value is not present in given list")
	else:
		print("The value is present in the list!")


	

print(binary_search(nums,low,high,value))


	

