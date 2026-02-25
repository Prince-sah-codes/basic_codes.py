import re #regular expression

with open("emails.txt","r") as fh:
    data = fh.read()

#print(data)    

pattern = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
mach = re.finditer(pattern, data)

for matches in mach:
    print(matches)

#only vald emails id displayed.
    
