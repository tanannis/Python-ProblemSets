from cs50 import get_string  # cs50 library from Harvard University

letterCount = 0
wordCount = 1
sentenceCount = 0

text = get_string("Text: ")

for i in text:
    if i.isalpha():
        letterCount += 1
    elif i.isspace():
        wordCount += 1
    elif i in [".", "?", "!"]:
        sentenceCount += 1

L = float(letterCount / wordCount * 100)

S = float(sentenceCount / wordCount * 100)

index = float(0.0588 * L - 0.296 * S - 15.8)

grade = round(index)
if grade >= 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
