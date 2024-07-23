print("Enter two strings and I'll tell you if they are anagrams:")
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")

def isAnagram(first_string, second_string):
    return sorted(first_string) == sorted(second_string)

if isAnagram(first_string, second_string):
    print(f"{first_string} and {second_string} are anagrams.")
else:
    print(f"{first_string} and {second_string} are NOT anagrams.")