import re
str1='Hey'
str2='ewfewfwe[["gotMessage", "Hey"]]fewfe'
found=re.search('.*[["gotMessage", ".*"]].*', str1)
print found.group(1)
