c=str(raw_input())
k=('a','e','i','o','u')
if c.isalpha():
     if c in k:
         print("vowel")
     else:
         print("Consonant")
else:
     print("invalid")
