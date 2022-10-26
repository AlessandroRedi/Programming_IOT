import numpy as np

class calculator():
    def __init__(self, operation):
        self.operation = operation
        self.numbers = []
        self.op1 = []


    def getoperation(self):
        ####
        if self.op1[0] == 'add':
            self.sumop()
        elif self.op1[0] == 'sub':
            self.sumop()
        elif self.op1[0] == 'mul':
            self.sumop()
        elif self.op1[0] == 'div':
            self.sumop()
        else:
            print("Operation not recognized")

    def dividelist(self):
        dividedList = inputList.split(' ')
        leng = len(dividedList)
        for x in range (leng):
            if dividedList[x].isalpha() == True:
                self.op1.append(dividedList[x])
            else:
                self.numbers.append(dividedList[x])

    def sumop(self):
        ####
        prova = np.array(self.numbers)
        for j in range (len(self.numbers)):
            somma = somma + self.numbers[j]
        #somma = np.sum(float(prova))
        print("The sum is",somma)

    '''def saveFile(self):
        f = open('File.txt','w')
        toWrite=f"{self.name},{self.surname},{self.birthYear}"
        #toWrite= self.name+","+self.surname+","+self.birthYear   #equivalent to the line before
        f.write(toWrite)
        f.close()'''

# This is the main of our program
if __name__ =="__main__":
    inputList = input("Insert the command : ")
    Oper = calculator(inputList)
    Oper.dividelist()
    Oper.getoperation()
    


