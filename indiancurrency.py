n=int(input("Enter amount :"))
dict={2000:0,500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
while(n!=0):
    if(n>=2000):
        dict[2000]+=1
        n-=2000
    elif(n>=500):
        dict[500]+=1
        n-=500
    elif(n>=200):
        dict[200]+=1
        n-=200
    elif(n>=100):
        dict[100]+=1
        n-=100
    elif(n>=50):
        dict[50]+=1
        n-=50
    elif(n>=20):
        dict[20]+=1
        n-=20
    elif(n>=10):
        dict[10]+=1
        n-=10
    elif(n>=5):
        dict[5]+=1
        n-=5
    elif(n>=2):
        dict[2]+=1
        n-=2
    else:
        dict[1]+=1
        n-=1
for key,value in dict.items():
    if(value!=0):
        print(key,"\t",value)