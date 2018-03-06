fibo=[0,1]
for i in range(50):
    fibo.append(fibo[-1]+fibo[-2])
for i in fibo:
    print(i)
    if i >= 89:
        break
