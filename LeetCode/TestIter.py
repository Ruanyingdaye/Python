import sys
def feb(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=feb(10)
while True: #True一定要是大写
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()