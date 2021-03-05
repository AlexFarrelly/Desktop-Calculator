from tkinter import *
import tkinter as tk
import functions as func
import time

class window():
    def __init__(self):
        GUI = tk.Tk()
        GUI.title(""), GUI.config(bg = "#171717")
        self.DisplayWindow(GUI)
        self.SpecialButtons(GUI)
        self.MainButtonFrame(GUI)
        GUI.mainloop()
    
    class DisplayWindow():
        def __init__(self, GUI):
            self.inputlist= []
            topFrame = tk.Frame(GUI)
            self.inputLabel = tk.Label(topFrame, text = "", width = 40, height = 4, padx = 6, anchor = "w")
            self.inputLabel.grid(row = 0, column = 0)
            self.anwserLabel = tk.Label(topFrame, width = 40, height = 4, padx = 6, anchor = "e")
            self.anwserLabel.grid(row = 1, column = 0)
            topFrame.grid(row = 0, column = 0)

        def enteredValue(self, text):
            if text == None:
                self.inputLabel.configure(text = self.inputlist)
            else:
                self.inputlist.append(text)
                self.inputLabel.configure(text = self.inputlist)

        def deleteValue(self):
            try:
                self.inputlist.pop((len(self.inputlist)-1))
                self.enteredValue(None)
            except:
                pass

        def clearValues(self):
            self.inputlist.clear()
            self.anwserLabel.config(text = "")
            self.enteredValue(None)

        def exuecute(self):
            try:
                try:
                    a = func.functions(self.inputlist, 0)
                    while a.done == False:
                        a = func.functions(a.newvalues, 0)
                    anws = a.anwser
                    self.anwserLabel.config(text = anws)
                    self.lastanwser = anws
                    self.inputlist.clear()
                except:
                    print(self.inpLabel.cget("text"))
            except:
               print(2)

    class SpecialButtons(DisplayWindow):
        def __init__(self, GUI):
            super().__init__(GUI)
            self.inputList = []
            middleFrame = tk.Frame(GUI)
            optionButton, varsButton, menuButton, squareButton, powerButton, exitButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            varibleButton, logButton, naturalLogButton, sinButton, cosButton, tanButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            fractionButton, sdButton, outsideBracketButton, insideBracketButton, commaButton, arrowButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            buttonText, textValue = ["OPTN", "VARS", "MENU", "x^2", "^", "EXIT", "X,θ,T", "log", "ln", "sin", "cos", "tan", "[]/[]", "S<->D", "(", ")", ",", "->"], 0
            rowPose, columnPose = 0, 0
            for i in buttonText:
                if i == "x^2":
                    rowPose, columnPose = 1, 0
                elif i == "X,θ,T":
                    rowPose, columnPose = 2, 0
                elif i == "[]/[]":
                    rowPose, columnPose = 3, 0
                i = tk.Button(middleFrame, text = buttonText[textValue], width = 5, height = 1, padx = (33/10))
                i.grid(row = rowPose, column = columnPose)
                columnPose += 1
                textValue += 1
            middleFrame.grid(row = 1, column = 0)
            

    class MainButtonFrame(DisplayWindow):
        def __init__(self, GUI):
            super().__init__(GUI)
            bottomFrame = tk.Frame(GUI, bg = "white")
            #Number Buttons------------------------------------------------------------------------------------------
            number, columnPose, rowPose = 1, 0, 2
            oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame)
            buttons = [oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton]
            for i in oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton:
                if i == fourButton:
                    rowPose, columnPose = 1, 0
                elif i == sevenButton:
                    rowPose, columnPose = 0, 0
                i.config(text = number, width = 7, height = 1)
                i.grid(row = rowPose, column = columnPose)
                number += 1
                columnPose += 1
            oneButton.config(command = lambda: self.enteredValue(oneButton.cget("text"))), twoButton.config(command = lambda: self.enteredValue(twoButton.cget("text"))), threeButton.config(command = lambda: self.enteredValue(threeButton.cget("text")))
            fourButton.config(command = lambda: self.enteredValue(fourButton.cget("text"))), fiveButton.config(command = lambda: self.enteredValue(fiveButton.cget("text"))), sixButton.config(command = lambda: self.enteredValue(sixButton.cget("text")))
            sevenButton.config(command = lambda: self.enteredValue(sevenButton.cget("text"))), eightButton.config(command = lambda: self.enteredValue(eightButton.cget("text"))), nineButton.config(command = lambda: self.enteredValue(nineButton.cget("text")))
            zeroButton = tk.Button(bottomFrame, text = 0, width = 7, height = 1, command = lambda: self.enteredValue(zeroButton.cget("text")))
            zeroButton.grid(row = 3,column = 0)
            columnPose, rowPose = 3, 0
            #Function Buttons-----------------------------------------------------------------------------------------
            buttonText, textValue = ["x", "÷", "+", "-", "Ans", "x10^x"], 0
            deleteButton, ACbutton, multiplyButton, divideButton, addButton, minusButton, ansButton, executeButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame)
            deleteButton.config(text = "DEL",width = 7, height = 1, bg = "blue"), ACbutton.config(text = "AC",width = 7, height = 1, bg = "blue"), executeButton.config(text = "EXE",width = 7, height = 1, bg = "blue")
            deleteButton.grid(row = 0, column = 3), ACbutton.grid(row = 0, column = 4), executeButton.grid(row = 3, column = 4)
            for i in multiplyButton, divideButton, addButton, minusButton, ansButton:
                if i == multiplyButton:
                    rowPose, columnPose = 1, 3
                elif i == addButton:
                    rowPose, columnPose = 2, 3
                elif i == ansButton:
                    rowPose, columnPose = 3, 3
                i.config(text = buttonText[textValue],width = 7, height = 1)
                i.grid(row = rowPose, column = columnPose)
                textValue += 1
                columnPose += 1
            multiplyButton.config(command = lambda: self.enteredValue(multiplyButton.cget("text"))), divideButton.config(command = lambda: self.enteredValue(divideButton.cget("text")))
            addButton.config(command = lambda: self.enteredValue(addButton.cget("text"))), minusButton.config(command = lambda: self.enteredValue(minusButton.cget("text")))
            ansButton.config(command = lambda: self.enteredValue(self.lastanwser)),deleteButton.config(command = self.deleteValue), ACbutton.config(command = self.clearValues)
            executeButton.config(command = self.exuecute)
            #Special Buttons-------------------------------------------------------------------------------------------
            decimalButton = tk.Button(bottomFrame, text = ".", width = 7, height = 1, command = lambda: self.enteredValue(decimalButton.cget("text")))
            decimalButton.grid(row = 3,column = 1)
            timesTenButton = tk.Button(bottomFrame, text = "x10^x", width = 7, height = 1, command = lambda: self.enteredValue("x10^"))
            timesTenButton.grid(row = 3,column = 2)            
            bottomFrame.grid(row = 2, column = 0)
        
window()




