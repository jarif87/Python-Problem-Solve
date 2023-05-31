li=[1,2,3,4,5,6,7,8]
i=9
found=False
for m in li:
    if i==m:
        found=True
        break
    
if found:
    print(True)
else:
    print(False)

#%%

if i in li:
    print(True)
else:
    print(False)
    
    
    
    