text = "Engineers are Awesome"
words = text.split()
print("words :", words)

#OR

print("Engineers are great".split())


#If you want to remove extra spaces between words too:
text = "  Hello   there are   spaces you can see  "
print(" ".join(text.split()))