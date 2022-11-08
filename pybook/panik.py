phrase = "Don't panic!"
plist = list(phrase)
print(phrase) 
print(plist)
plist=plist[1:8]
# for i in range(4):
#     plist.pop()
plist.insert(5,plist.pop(6)) 

plist.remove("'")
# plist.pop(0) 
plist.insert(2,plist.pop(3))
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)


phrase = "Don't panic!" 
plist = list(phrase) 
print(phrase) 
print(plist) 
new_phrase = ''.join(plist[1:3]) 
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]]) 
print(plist) 
print(new_phrase)

paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android) 
for char in letters[:6]: 
 print('\t', char) 
print() 
for char in letters[-7:]: 
 print('\t'*2, char) 
print() 
for char in letters[12:20]: 
 print('\t'*3, char)