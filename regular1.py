import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for match in matcher:
    count+=1
    ##print('match is available at start index:',match.start())
    print('start:{},end:{},group:{}'.format(match.start(),match.end(),match.group()))
print('total number of occurances:',count)    

