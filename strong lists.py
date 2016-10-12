word=input("please enter a word: \n")
word=str(word)
rvs=word[::-1]
print(rvs)
if rvs == word:
    print("this word is a pallindrom")
else:
    print("This word is not a palindrome")