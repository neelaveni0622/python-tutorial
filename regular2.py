import re

#match() : to check the given pattern at the beginning of the target string
#if then returns match object otherwise none

s=input('Enter the string:')
m=re.match(s,'hello')
if m!=None:
    print("match is available at the beginning of the string")
    print('start index:{} and end index:{}'.format(m.start(),m.end()))
else:
    print("match is not available at the beginning of the string")     



#sub():substitutation or replacement

s1=re.sub('\d','@','abc123')
print(s1)

