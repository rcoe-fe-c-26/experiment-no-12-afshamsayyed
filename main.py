# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Afsha Sayyed
# Date:10/02/2026

print("--- Extracting Words from Text File ---\n")
n = int(input())

file = open("story.txt", "r")
data = file.read().lower()
file.close()

words = data.split()

result = set()

for word in words:
    if len(word) == n:
        result.add(word)

result = sorted(result)

print(result)
