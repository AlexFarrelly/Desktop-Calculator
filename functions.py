class basicFunctions():
    def __init__(self, values, anwser):
        self.pi = 3.14159265358979323846264338
        print(values)
        self.anwser, self.done, function, leftint, rightint = anwser, False, [], [], []
        for i in range(len(values)):
            if values[i] == "x" or values[i] == "÷" or values[i] == "+" or values[i] == "-" or values[i] == "sin" or values[i] == "cos" or values[i] == "tan":
                f1Pose = i
                for i in range(f1Pose):
                    leftint.append(values[i])
                    print(leftint)
                break
        function.append(values[f1Pose])
        for i in range(len(values)):
            if values[i] == "x" or values[i] == "÷" or values[i] == "+" or values[i] == "-" or values[i] == "sin" or values[i] == "cos" or values[i] == "tan":
                f1Pose = i
                for i in range(f1Pose, len(values)):
                    rightint.append(values[i])
                break
        rightint.pop(0)
        print(leftint, rightint)
        try:
            if function == ["sin"] or function == ["cos"] or function == ["tan"]:
                if len(leftint) == 0:
                    leftint.append(1)
            a, b = [str(i) for i in leftint], [str(i) for i in rightint]
            a, b  = "".join(a), "".join(b)
            a, b  = float(a), float(b)
            self.done = True
            self.anwser = self.method(a, b, function)
        except:
            newright = []
            newValues = rightint
            for i in rightint:
                if i == "x" or i == "÷" or i == "+" or i == "-" or i == "sin":
                    for num in range(0, rightint.index(i)):
                        rightint.pop(0)
                    break
                else:
                    newright.append(i)
            a, b = [str(num) for num in leftint], [str(num) for num in newright]
            a, b  = "".join(a), "".join(b)
            a, b  = float(a), float(b)
            anwser = self.method(a, b, function)
            rightint.insert(0, anwser)
            self.newvalues = rightint
        
                      
    def method(self, a, b, func):
        if func == ["x"]:
            self.anwser += a * b
        elif func == ["÷"] or func == ["/"]:
            self.anwser = a / b
        elif func == ["+"]:
            self.anwser += a + b
        elif func == ["-"]:
            self.anwser += a - b
        elif func == ["sin"]:
            self.anwser = a * (self.sinValue(a, b))
        elif func == ["cos"]:
            self.anwser = a * (self.cosValue(a, b))
        elif func == ["tan"]:
            self.anwser = a * (self.tanValue(a, b))
        if self.anwser % 1 == 0:
            self.anwser = int(self.anwser)
        else:
            try:
                self.anwser = (round(self.anwser, 6))
            except:
                pass
        return self.anwser

    def sinValue(self, a, b):
        radValue = self.findRadians(b)
        sinSeries = ((radValue) - (radValue**3) / ((self. factorial(3))) + ((radValue **5 ) /(self. factorial(5))) - (radValue**7/ (self. factorial(7))))
        return (sinSeries)
    
    def cosValue(self, a, b):
        radValue = self.findRadians(b)
        cosSeries = ((1 - (radValue**2) / ((self. factorial(2))) + ((radValue **4 ) /(self. factorial(4))) - (radValue**6/ (self. factorial(6)))))
        return (cosSeries)

    def tanValue(self, a, b):
        tanSeries = (self.sinValue(a, b)) / (self.cosValue(a, b))
        return (tanSeries)

    def findRadians(self, b):
        radValue = b * self.pi
        radValue /= 180
        return radValue

    def factorial(self, n):
        factorial = 1
        if int(n) >= 1:
            for i in range (1,int(n)+1):
               factorial = factorial * i
        return(factorial)
            
class priorityValues():
    def __init__(self, values):
        bracketsValues, removedValues, self.newEquation = [], [], []
        self.searchForIndices(values, removedValues)
        self.searchForBrackets(self.newEquation, removedValues, bracketsValues)
        for i in self.newEquation:
            if i == "^" or i == "(":
                print(self.newEquation)
                priorityValues(self.newEquation)

    def searchForBrackets(self, values, removedValues, bracketsValues):
        try:
            for i in range(len(values)):
                if values[i] == "(":
                    removedValues.append(i)
                    for var in range((i+1), len(values)):
                        if values[var] == ")":
                            removedValues.append(var)
                            break
                        else:
                            bracketsValues.append(values[var])
                            removedValues.append(var)
                    break
            if len(bracketsValues) > 0:
                for i in range(len(removedValues)):
                    values.pop(removedValues[0])
                bracketAnwser = basicFunctions(bracketsValues, 0)
                
                while bracketAnwser.done == False:
                    bracketAnwser = basicFunctions(bracketAnwser.newvalues, 0)
                bracketAnwser = bracketAnwser.anwser
                if len(removedValues) > 0:
                    self.newEquation.insert(removedValues[0], bracketAnwser)
            else:
                self.newEquation = values
        except:
            pass
            
    def searchForIndices(self, values, removedValues):
        try:
            newleft, self.newEquation, leftValue, rightValue = 1,[], [], []
            for i in range(len(values)):
                if values[i] == "^":
                    removedValues.append(i)
                    for var in range(i+1, len(values)):
                        if values[var] == "+" or values[var] =="x" or values[var] =="-" or values[var] =="÷" or values[var] == ")":
                            break
                        else:
                            rightValue.append(values[var])
                            removedValues.append(var)
            i = (removedValues[0]-1)
            while i >= 0:
                if values[i] == "+" or values[i] =="x" or values[i] =="-" or values[i] =="÷" or values[i] == "(":
                    break
                else:
                    if i == 0:
                        leftValue.append(values[i])
                        removedValues.append(i)
                        break
                    else:
                        leftValue.append(values[i])
                        removedValues.append(i)
                        i -= 1
            if len(removedValues) > 0:
                left, right = [str(num) for num in reversed(leftValue)], [str(num) for num in rightValue]
                left, right  = "".join(left), "".join(right)
                left, right  = float(left), int(right)
                for i in range(right):
                    newleft *= left
            try:
                if len(removedValues) != len(values):
                    for i in range(len(removedValues)):
                        values.pop(removedValues[(len(removedValues)-1)])
                    self.newEquation = values
                    pose = removedValues[len(removedValues)-1]
                    self.newEquation.insert(pose, newleft)
                    self.searchForBrackets(self.newEquation, [], [])
                    
                else:
                    self.newEquation.append((round(newleft, 12)))
            except:
                pass
        except:
            self.newEquation = values


class rationalAprox():
    def __init__(self, value):
        self.anwser = 0
        try:
            self.decimal(value)
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
                self.anwser = (mediantTop + (wn * mediantBottom), "/", mediantBottom)
        except:
            pass
