class functions():
    def __init__(self, values, anwser):
        self.anwser, self.done, function, leftint, rightint = anwser, False, [], [], []
        for i in range(len(values)):
            if values[i] == "x" or values[i] == "÷" or values[i] == "+" or values[i] == "-":
                f1Pose = i
                for i in range(f1Pose):
                    leftint.append(values[i])
                break
        function.append(values[f1Pose])
        for i in range(len(values)):
            if values[i] == "x" or values[i] == "÷" or values[i] == "+" or values[i] == "-":
                f1Pose = i
                for i in range(f1Pose, len(values)):
                    rightint.append(values[i])
                break
        rightint.pop(0)
        try:
            a, b = [str(i) for i in leftint], [str(i) for i in rightint]
            a, b  = "".join(a), "".join(b)
            a, b  = float(a), float(b)
            self.done = True
            self.anwser = self.method(a, b, function)
        except:
            newright = []
            newValues = rightint
            for i in rightint:
                if i == "x" or i == "÷" or i == "+" or i == "-":
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
        elif func == ["÷"]:
            self.anwser = a / b
        elif func == ["+"]:
            self.anwser += a + b
        elif func == ["-"]:
            self.anwser += a - b
        if self.anwser % 1 == 0:
            self.anwser = int(self.anwser)
            return self.anwser
        else:
            return self.anwser
    

