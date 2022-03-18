n = input("Enter the word and see if it is palindrome: ") 
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")
     