import numpy as np
import json

class calculator():
    def __init__(self, operation):
        self.operation = operation
        self.numbers = []
        self.op1 = []
        self.dictionaryList = []
        self.result = 0
        self.fine = True

    def json_write(self,file, dictionary):
        self.dictionaryList.append(dictionary)
        json.dump(self.dictionaryList,  open(file, "w"))
        pass

    def getoperation(self):
        ####
        if self.op1[0] == 'add':
            self.add()
        elif self.op1[0] == 'sub':
            self.sub()
        elif self.op1[0] == 'mul':
            self.mul()
        elif self.op1[0] == 'div':
            self.div()
        elif self.op1[0] == 'exit':
            self.fine = False
            print("Closing the calculator")
        else:
            print("Operation not recognized")

    def dividelist(self):
        dividedList = self.operation.split(' ')
        test = True
        leng = len(dividedList)
        for x in range (leng):
            if dividedList[x].isalpha() == True:
                if test == False:
                    self.getoperation()
                self.op1.clear()
                self.op1.append(dividedList[x])
                self.numbers.clear()
                test = False
            else:
                self.numbers.append(float(dividedList[x]))

    def add(self):
        ####
        somma = 0
        somma = np.sum(self.numbers)
        self.result = somma
        '''prova = np.array(self.numbers)
        somma = 0
        for j in range (len(self.numbers)):
            somma = somma + float(self.numbers[j])'''
        print("The sum is",somma)
        Dictionary = {"input": self.numbers,
        "Operator": "add",
        "output": somma}
        self.json_write("calculator_result.json", Dictionary)

    def sub(self):
        ####
        sottr = 0
        sottr = self.numbers[0] - sum(self.numbers[1:])
        self.result = sottr
        print("The sub is",sottr)
        Dictionary = {"input": self.numbers,
        "Operator": "sub",
        "output": sottr}
        self.json_write("calculator_result.json", Dictionary)

    def div(self):
        ####
        div = self.numbers[0]
        for x in self.numbers[1: len(self.numbers)]:
            try:
                div = div/x
            except ZeroDivisionError:
                print("Cannot divide!")
                div = "Error"
                break
        print("The division is",div)
        self.result = div
        Dictionary = {"input": self.numbers,
        "Operator": "div",
        "output": div}
        self.json_write("calculator_result.json", Dictionary)

    def mul(self):
        ####
        mul = 1
        for b in self.numbers: #segue i valori della lista
            mul = mul * b
        print("The multiplication is",mul)
        self.result = mul
        Dictionary = {"input": self.numbers,
        "Operator": "mul",
        "output": mul}
        self.json_write("calculator_result.json", Dictionary)


'''# This is the main of our program
if __name__ =="__main__":
    flag = True
    while flag:
        inputList = input("Insert the command : ")
        Oper = calculator(inputList)
        Oper.dividelist()
        Oper.getoperation()
        flag = Oper.fine'''