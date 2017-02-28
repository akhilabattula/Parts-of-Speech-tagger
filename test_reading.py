'''
Created on Apr 11, 2016

@author: akhila
'''
lines = open("sample.txt",'r').read().splitlines()
all_tag=[]
for i in lines:
    a=i.split() 
    for j in a:
        #temp=j.split("/")
        t=j.rindex("/")+1
        if j[t:] not in all_tag:
            print j,"----",j.rindex('/'),"\n"
            
            all_tag.append(j[t:])
print all_tag
    