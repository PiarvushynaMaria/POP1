s = input("Введите первое слово: ")
p = input("Введите второе слово: ")
dict1={}
dict2={}
for i in range(len(s)):
    dict1[i+1]=s[i]
print(dict1)
for i in range(len(p)):
    dict2[i+1]=p[i]
print(dict2)
count=0
if len(dict1)==len(dict2):
    for i in range(len(s)):
        if dict1[i+1] in dict2.values():
            count+=1
    if count==len(dict1):
        print('True')
    else:
        print('False')
else:
    print('False')
        
                       
    
