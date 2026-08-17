print("=" * 45)
print("     TEXT ANALYZER TOOL")
print("=" * 45)

paragraph = input("Enter a Paragraph: \n")

total_lenth = len(paragraph)

print("\n------Basic Info-----")
print("Total Characters (including Spaces): ",total_lenth)
print("First 10 Character (slicing)     :", paragraph[0:10])
print("Last 10 Character (slicing)     :", paragraph[-10:])
print("Reverse Paragraph (slicing)     :", paragraph[::-1])

vowel_count = 0
space_count = 0
consonant_count = 0
digit_count = 0
other_count = 0

vowels = "aeiouAEIOU"

for i in range(len(paragraph)):
    ch = paragraph[i]

    if ch == " ":
        space_count = space_count + 1
    elif ch.isalpha():
        if ch in vowels:
            vowel_count = vowel_count + 1
        else:
            consonant_count = consonant_count + 1
    elif ch.isdigit():
        digit_count = digit_count + 1
    else:
        other_count = other_count + 1

words = paragraph.split()
word_count = len(words)

print("\n -------Character Analysis-------")
print("Total Vowels     :",vowel_count)
print("Total Consonanta         :", consonant_count)
print("Total Spaces     :",space_count)
print("Total Digit      :",digit_count)
print("Other Characters     :",other_count,"(punctuation/symbols)")

print("\n ------- Word Analysis -------")
print("Total Words      :",word_count)
print("First Word       :", words[0])
print("Last Word       :", words[-1])

print("\n--------Word List (Traversal)-------")
for i in range(len(words)):
    print(f"word{i + 1}: {words[i]}")

print()