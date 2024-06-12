import re

s="Learning python is Easy"
res=re.search("easy$",s,re.IGNORECASE)
if res!=None:
    print("match found")
else:
    print("match not found")



     