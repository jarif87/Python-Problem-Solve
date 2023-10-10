for i in range(0, 10):
    print('*', end="")
print("\n")

#%%
for i in range(10):
    print(i,"*",end=" ")
print("\n")

#%%
import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')