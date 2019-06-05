#Write a Python program to check if a string is numeric.

st = input("Enter the string\n")
if st.isalpha() is False:
	print("True")
else:
	print("False")