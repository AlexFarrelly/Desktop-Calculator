class fractions():
    def __init__(self):
        action = int(input("""Here is a list of the actions you can do;
1| add
2| subtract
3| multiply
4| divide
5| rationilse a decimal
Please pick the number of what action you would like to do: """))
        if action == 5:
            self.rationalAprox()
        else:
            self.functions(action)
        
            

    class functions():
        def __init__(self, action):
            f1 = list(input("Please input first fraction in the form a/b: "))
            f2 = list(input("Please input second fraction in the form a/b: "))
            count, topf1, bottomf1, topf2, bottomf2 = 0, [], [], [], []
            while True:
                try:
                    f1Pose, f2Pose = f1.index("/"), f2.index("/")
                    for i in range(f1Pose):
                        topf1.append(f1[i])
                    for i in range(f1Pose, (len(f1))):
                        bottomf1.append(f1[i])
                    for i in range(f2Pose):
                        topf2.append(f2[i])
                    for i in range(f2Pose, (len(f2))):
                        bottomf2.append(f2[i])
                    bottomf1.remove("/"), bottomf2.remove("/")
                    a, b, c, d = [str(i) for i in topf1], [str(i) for i in bottomf1], [str(i) for i in topf2], [str(i) for i in bottomf2]
                    a, b, c, d  = "".join(a), "".join(b), "".join(c), "".join(d)
                    a, b, c, d  = int(a), int(b), int(c), int(d)
                    if action == 1:
                        return self.add(a, b, c, d)
                    elif action == 2:
                        return self.subtract(a, b, c, d)
                    elif action == 3:
                        return self.multiply(a, b, c, d)
                    else:
                        return self.divide(a, b, c, d)
                except:
                    print("syntax error")
                    break
                
        def add(self, a, b, c, d):
            try:
                if (a+c) % d == 0 and (a+c) % b == 0:
                    return print(1)
                else:
                    if b == d:
                        return self.simplify((a+c), d, False)
                    else:
                        a *= d
                        d *= b
                        c *= b
                        self.add(a, d, c, d)
            except:
                print("syntax error")

        def subtract(self, a, b, c, d):
            try:
                if b == d:
                    if (a/b) - (c/d) < 0:
                        num = ((a-c)*(-1))
                        return self.simplify(int(num), d, True)
                    else:
                        return self.simplify(int(a-c), d, False)
                else:
                    a *= d
                    d *= b
                    c *= b
                    self.subtract(a, d, c, d)
            except:
                print("syntax error")
        
        def divide(self, a, b, c, d):
            self.multiply(a, b, d, c)
        
        def multiply(self, a, b, c, d):
            try:
                num = a*c
                denum = b*d
                return self.simplify(num, denum, False)
            except:
                pass


        def simplify(self, a, b, negitive):
            try:
                for i in range(2, (b+2)):
                    if a % i == 0 and b % i == 0:
                        a /= i
                        b /= i
                        self.simplify(a, b, negitive)
                if b % a == 0:
                    if negitive == False:
                        return print(1, "/", int(b / a))
                    else:
                        return print("-", 1, "/", int(b / a))
                else:
                    if negitive == False:
                        return print(int(a), "/", int(b))
                    else:
                        return print("-", int(a), "/", int(b))
            except:
                pass

            
    class rationalAprox():
        def __init__(self):
            try:
                n = (input("Please enter a number you would like the fraction of: "))
                self.decimal(n)
            except:
                print("Syntax Error")

        def decimal(self, n):
            wholeN, count = [], 0
            try:
                listN = list(n)
                for i in listN:
                    if i == ".":
                        for i in range(count):
                            wholeN.append(listN[0])
                            listN.pop(0)
                        listN, wholeN = [str(i) for i in listN], [str(a) for a in wholeN]
                        listN, wholeN = "".join(listN), "".join(wholeN)
                        listN, wholeN = float(listN), int(wholeN)
                        return self.mediant(listN, wholeN, 0, 1, 1, 1)
                    else:
                        count += 1
                print(n)
            except:
                return self.mediant(float(n), 0, 0, 1, 1, 1)

        def mediant(self, n, wn, a, b, c, d):
            try:
                mediantTop = a+c
                mediantBottom = b + d
                if n > (mediantTop/mediantBottom):
                    self.mediant(n, wn, mediantTop, mediantBottom, c, d)
                elif n < (mediantTop/mediantBottom):
                    self.mediant(n, wn ,a, b, mediantTop, mediantBottom) 
                else:
                    return print((mediantTop + (wn * mediantBottom)), "/", mediantBottom)
            except:
                return print(n)

while True:
    fractions() 
