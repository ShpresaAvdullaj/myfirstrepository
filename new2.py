

# te shfaqen faktor te thjesht
def printfactors(x):
    print("the factors of", x , "are:")
    c = 1
    a = int(x)
    for k in range(2,x):
        for i in range(2,int(a)):


            if(a%i==0):
                if(i == 2):
                    a /= i
                    c *= i
                    print(i)
                    break
                else:
                    b = False
                    for j in range(2,i):
                        if(i%j == 0):
                            b = False
                            break
                        else:
                            b = True
                    if(b == True):
                        print(i)
                        a /= i
                        c *= i
                        break
    print(x/c)



num = 547320
printfactors(num)