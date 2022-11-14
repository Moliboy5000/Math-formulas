class Matrix:
    def __init__(self,dimensions,entries):
        self.dimensions = dimensions
        self.entries = entries

    def printMatrix(self):
        for i in range(len(self.entries)):
            print(self.entries[i])

    def trace(self):
        total = 0
        for i in range(len(self.entries)):
            total += self.entries[i][i]
        return total

    def addMatrices(self,B):
        result = []
        for i in range(len(self.entries)):
            newRow = []
            for j in range(len(self.entries[i])):
                newRow.append(self.entries[i][j] + B[i][j])
            result.append(newRow)
        return result
    
    def subtractMatrices(self,B):
        result = []
        for i in range(len(self.entries)):
            newRow = []
            for j in range(len(self.entries[i])):
                newRow.append(self.entries[i][j] - B[i][j])
            result.append(newRow)
        return result
    
    def multiplyByNum(self,num):
        result = []
        for i in range(len(self.entries)):
            newRow = []
            for j in range(len(self.entries[i])):
                newRow.append(self.entries[i][j] * num)
            result.append(newRow)
        return result
    
    def multiplyMatrices(self,B):
        result = []
        for i in range(len(self.entries)):
            newRow = []
            for j in range(len(B[0])):
                total = 0
                for k in range(len(self.entries[0])):
                    total += self.entries[i][k] * B[k][j]
                newRow.append(total)
            result.append(newRow)
        return result

A = Matrix([4,4],[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

A.printMatrix()





                