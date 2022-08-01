n=int(input("Enter amount :"))
dict={2000:0,500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
lst=list(dict.keys())
while(n!=0):
    for i in lst:
        if(n>=i):
            a=0
            a=n//i
            dict[i]+=a
            n-=i*a
for key,value in dict.items():
    if(value!=0):
        print(key,"\t",value)
