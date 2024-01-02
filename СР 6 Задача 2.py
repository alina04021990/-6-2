x=int(input(' введите число'))
c=0
for a in range(1,x+1):
   if x % a == 0:
        c+=1
print(c)
