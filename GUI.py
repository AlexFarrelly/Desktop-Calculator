from tkinter import *
import tkinter as tk

class window():
    def __init__(self):
        GUI = tk.Tk()
        GUI.title(""), GUI.config(bg = "#171717")
        self.DisplayWindow(GUI)
        self.SpecialButtons(GUI)
        self.MainButtonFrame(GUI)

    
    class DisplayWindow():
        def __init__(self, GUI):
            topFrame = tk.Frame(GUI)
            inputLabel = tk.Label(topFrame, width = 40, height = 3, padx = 6).grid(row = 2, column = 0)
            anwserLabel = tk.Label(topFrame, width = 40, height = 3, padx = 6).grid(row = 0, column = 0)
            topFrame.grid(row = 0, column = 0)

    class SpecialButtons():
        def __init__(self, GUI):
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
            

    class MainButtonFrame():
        def __init__(self, GUI):
            bottomFrame = tk.Frame(GUI, bg = "white")
            #Number Buttons------------------------------------------------------------------------------------------
            number, columnPose, rowPose = 1, 0, 2
            oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame)
            for i in oneButton, twoButton, threeButton, fourButton, fiveButton, sixButton, sevenButton, eightButton, nineButton:
                if i == fourButton:
                    rowPose, columnPose = 1, 0
                elif i == sevenButton:
                    rowPose, columnPose = 0, 0
                i.config(text = number, width = 7, height = 1)
                i.grid(row = rowPose, column = columnPose)
                number += 1
                columnPose += 1
            zeroButton = tk.Button(bottomFrame, text = 0, width = 7, height = 1).grid(row = 3,column = 0)
            columnPose, rowPose = 3, 0
            #Function Buttons-----------------------------------------------------------------------------------------
            buttonText, textValue = ["x", "÷", "+", "-", ".", "x10^x","(-)"], 0
            deleteButton, ACbutton, multiplyButton, divideButton, addButton, minusButton, negitiveButton, executeButton = tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame), tk.Button(bottomFrame),tk.Button(bottomFrame), tk.Button(bottomFrame)
            deleteButton.config(text = "DEL",width = 7, height = 1, bg = "blue"), ACbutton.config(text = "AC",width = 7, height = 1, bg = "blue"), executeButton.config(text = "EXE",width = 7, height = 1, bg = "blue")
            deleteButton.grid(row = 0, column = 3), ACbutton.grid(row = 0, column = 4), executeButton.grid(row = 3, column = 4)
            for i in multiplyButton, divideButton, addButton, minusButton, negitiveButton:
                if i == multiplyButton:
                    rowPose, columnPose = 1, 3
                elif i == addButton:
                    rowPose, columnPose = 2, 3
                elif i == negitiveButton:
                    rowPose, columnPose = 3, 3
                i.config(text = buttonText[textValue],width = 7, height = 1)
                i.grid(row = rowPose, column = columnPose)
                textValue += 1
                columnPose += 1
            #Special Buttons-------------------------------------------------------------------------------------------
            decimalButton = tk.Button(bottomFrame, text = ".", width = 7, height = 1).grid(row = 3,column = 1)
            timesTenButton = tk.Button(bottomFrame, text = "x10^x", width = 7, height = 1).grid(row = 3,column = 2)            
            bottomFrame.grid(row = 2, column = 0)
            
       
window()




