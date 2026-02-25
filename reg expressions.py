'''
mes = "hey i am prince i am 20 yrs old"
print("prince " in mes)
print("20" in mes)#it checks wheather the mes is available or not
print("21" in mes)
print(mes.find("am"))
print(mes.find("20"))#it gives the index of given find("")
'''
#now using regex 
import re
'''
mes = "hey i am prince i am 20 yrs old"
opt = re.search("20", mes)
print(opt)
print(mes[21:28])
'''
'''
phones = "prince-9822788065, dev-1234567890, alok-0987654321"
pattern= r"\d{10}"
matchh = re.findall(pattern,phones)
print(matchh)'''


