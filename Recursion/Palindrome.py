# if the string is word then

def palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


print(palindrome("rahul"))
print(palindrome("madam"))

# if the string have white space and symbols

# s = "A man, a plan, a canal: Panama";
# new_str = ""
# for ch in s:
#     if ch.isalnum():  # keep only letters and digits
#         new_str += ch.lower()

# arr =  list(new_str)
# arr.reverse()

# revse = "".join(arr)


# print(new_str == revse)


