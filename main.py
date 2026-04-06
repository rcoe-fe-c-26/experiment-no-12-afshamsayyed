# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Afsha Sayyed
# Date:10/02/2026

print("--- Extracting Words from Text File ---\n")
n = int(input("Enter Length of Words: "))

file = open("story.txt", "r")
data = file.read()
file.close()

# convert to lowercase
data = data.lower()

# remove punctuation
for ch in ",.!?\"":
    data = data.replace(ch, "")

words = data.split()

result = set()

for word in words:
    if len(word) == n:
        result.add(word)

result = sorted(result)

print(f"Words with length {n} are: {result}")
