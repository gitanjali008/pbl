
num = 131
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"Yes, {num} is a palindrome")
else:
    print(f"No, {num} is not a palindrome")
