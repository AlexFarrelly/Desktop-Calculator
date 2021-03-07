from tkinter import *
from tkinter import font
import tkinter as tk
import functions as func


class Matrixwindow(tk.Frame):
    def __init__(self):
        GUI = tk.Tk()
        GUI.title("A-level Calculator"), GUI.config(bg = "#171717")
        self.DisplayWindow(GUI) and self.ButtonsFrame(GUI)
    
    class DisplayWindow():
        def __init__(self, GUI):
            super().__init__()
            self.GUI = GUI
            self.inputlist= []
            topFrame = tk.Frame(GUI)
            self.inputLabel = tk.Label(topFrame, text = "", width = 40, height = 4, padx = 6, anchor = "w")
            self.inputLabel.grid(row = 0, column = 0)
            self.anwserLabel = tk.Label(topFrame, text = 0, width = 40, height = 4, padx = 6, anchor = "e")
            self.anwserLabel.grid(row = 1, column = 0)
            topFrame.grid(row = 0, column = 0, padx = 20, pady = 10)

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
            self.anwserLabel.config(text = 0)
            self.enteredValue(None)

        def sdValues(self, value):
            if self.state == False:
                a = func.rationalAprox(str(value))
                self.anwserLabel.configure(text = (a.anwser))
                self.state = True 
            else:
                self.anwserLabel.configure(text = self.lastanwser)
                self.state = False

        def exuecute(self, containsSpecialFunction):
            if containsSpecialFunction == False:
                try:
                    brackets = func.priorityValues(self.inputlist)
                    values = brackets.newEquation
                    self.inputlist = values
                    anws = [str(i) for i in values]
                    anws = "".join(anws)
                    anws = float(anws)
                    if anws % 1 == 0:
                        anws == int(anws)
                    else:
                        anws = float(anws)
                    self.lastanwser = anws
                    self.anwserLabel.config(text = anws)
                except:
                    try:
                        try:
                            a = func.basicFunctions(self.inputlist, 0)
                            while a.done == False:
                                a = func.basicFunctions(a.newvalues, 0)
                            anws = a.anwser
                            self.anwserLabel.config(text = anws)
                            self.lastanwser = anws
                        except:
                            anws = [str(i) for i in self.inputLabel.cget("text")]
                            anws = "".join(anws)
                            if float(anws) % 1 == 0:
                                anws == int(anws)
                            else:
                                anws = float(anws)
                            self.lastanwser = anws
                            self.anwserLabel.config(text = anws)
                    except:
                       ErrorWindow("Syntax Error")
            else:
                pass


    class ButtonsFrame(DisplayWindow):
        def __init__(self, GUI):
            super().__init__(GUI)
            self.inputList, self.state, containsSpecialFunction = [], False, False
            middleFrame = tk.Frame(GUI)
            
##          Special Buttons-----------------------------------------------------------------------------------------
            optionButton, varsButton, menuButton, squareButton, powerButton, exitButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            varibleButton, logButton, naturalLogButton, sinButton, cosButton, tanButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            fractionButton, sdButton, outsideBracketButton, insideBracketButton, commaButton, arrowButton = tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame), tk.Button(middleFrame)
            buttonText, textValue = ["OPTN", "VARS", "MENU", "x^2", "^", "EXIT", "X,θ,T", "log", "ln", "sin", "cos", "tan", "[]/[]", "S<->D", "(", ")", ",", "->"], 0
            rowPose, columnPose = 0, 0
            
            for i in optionButton, varsButton, menuButton, squareButton, powerButton, exitButton, varibleButton, logButton, naturalLogButton, sinButton, cosButton, tanButton, fractionButton, sdButton, outsideBracketButton, insideBracketButton, commaButton, arrowButton:
                if i == squareButton:
                    rowPose, columnPose = 1, 0
                elif i == varibleButton:
                    rowPose, columnPose = 2, 0
                elif i == fractionButton:
                    rowPose, columnPose = 3, 0
                i.config(text = buttonText[textValue], width = 5, height = 1, padx = 4)
                i.grid(row = rowPose, column = columnPose)
                columnPose += 1
                textValue += 1
            sdButton.config(command = lambda: self.sdValues(self.lastanwser)), outsideBracketButton.config(command = lambda: self.enteredValue(outsideBracketButton.cget("text"))), insideBracketButton.config(command = lambda: self.enteredValue(insideBracketButton.cget("text")))
            squareButton.config(command = lambda: (self.enteredValue("^"), self.enteredValue("2"))), powerButton.config(command = lambda: (self.enteredValue("^"))), sinButton.config(command = lambda: (self.enteredValue("sin")))
            cosButton.config(command = lambda: (self.enteredValue("cos"))), tanButton.config(command = lambda: (self.enteredValue("tan")))
            middleFrame.grid(row = 1, column = 0, padx = 20, pady = 10)
            bottomFrame = tk.Frame(GUI)
            
##          Number Buttons------------------------------------------------------------------------------------------
            number, columnPose, rowPose = 1, 0, 2
            oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame)
            buttons = [oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton]
            
##          This Creates all the grid configs for all the buttons in the main button frame----------------------------------------------------------------- 
            for i in oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton:
                if i == fourButton:
                    rowPose, columnPose = 1, 0
                elif i == sevenButton:
                    rowPose, columnPose = 0, 0
                i.config(text = number, width = 7, height = 1)
                i.grid(row = rowPose, column = columnPose)
                number += 1
                columnPose += 1

##          Commands for all the buttons in the main button frame----------------------------------------------------
            oneButton.config(command = lambda: self.enteredValue(oneButton.cget("text"))), twoButton.config(command = lambda: self.enteredValue(twoButton.cget("text"))), threeButton.config(command = lambda: self.enteredValue(threeButton.cget("text")))
            fourButton.config(command = lambda: self.enteredValue(fourButton.cget("text"))), fiveButton.config(command = lambda: self.enteredValue(fiveButton.cget("text"))), sixButton.config(command = lambda: self.enteredValue(sixButton.cget("text")))
            sevenButton.config(command = lambda: self.enteredValue(sevenButton.cget("text"))), eightButton.config(command = lambda: self.enteredValue(eightButton.cget("text"))), nineButton.config(command = lambda: self.enteredValue(nineButton.cget("text")))
            zeroButton = tk.Button(bottomFrame, text = 0, width = 7, height = 1, command = lambda: self.enteredValue(zeroButton.cget("text")))
            zeroButton.grid(row = 3,column = 0)
            columnPose, rowPose = 3, 0
            
##          Function Buttons-----------------------------------------------------------------------------------------
            buttonText, textValue = ["x", "÷", "+", "-", "Ans", "x10^x"], 0
            deleteButton, ACbutton, multiplyButton, divideButton, addButton, minusButton, ansButton, executeButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame)
            deleteButton.config(text = "DEL",width = 7, height = 1, bg = "blue"), ACbutton.config(text = "AC",width = 7, height = 1, bg = "blue"), executeButton.config(text = "EXE",width = 7, height = 1, bg = "blue")
            deleteButton.grid(row = 0, column = 3), ACbutton.grid(row = 0, column = 4), executeButton.grid(row = 3, column = 4)

##          This Creates all the grid configs for all the buttons in the function button frame-------------------------------
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
            executeButton.config(command = lambda: self.exuecute(containsSpecialFunction))
            
##          Special Buttons-------------------------------------------------------------------------------------------
            decimalButton = tk.Button(bottomFrame, text = ".", width = 7, height = 1, command = lambda: self.enteredValue(decimalButton.cget("text")))
            decimalButton.grid(row = 3,column = 1)
            timesTenButton = tk.Button(bottomFrame, text = "x10^x", width = 7, height = 1, command = lambda: (self.enteredValue("x"), self.enteredValue("10"), self.enteredValue("^")))
            timesTenButton.grid(row = 3,column = 2)            
            bottomFrame.grid(row = 2, column = 0, padx = 20, pady = 10)

class ErrorWindow():
    def __init__(self, error):
        errorFont = font.Font(family="Helvetica",size=36,weight="bold")
        ErrorUI = tk.Toplevel()
        ErrorUI.title("ERROR")
        Message = tk.Label(ErrorUI,text= error, font = errorFont).grid(row = 1, column = 1,)
        Button = tk.Button(ErrorUI,text = "Ok", command = lambda: ErrorUI.destroy()).grid(row=2, column = 1)
        
        











        
        
Matrixwindow()
