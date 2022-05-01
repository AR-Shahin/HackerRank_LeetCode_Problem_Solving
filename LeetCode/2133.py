class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)
        arr = [i+1 for i in range(N)]
        #print(arr)
        for i in range(N):
            if sorted(matrix[i]) != arr:     
                return False
        
        for i in range(N):
            temp = []
            for j in range(N):
                temp.append(matrix[j][i])
            if sorted(temp) != arr:
                return False
        return True


class Solution:
    def checkValid(self, matrix):
        
        temp = matrix[0]
        flag = True
        temp.sort()
        for row in matrix:
            row.sort()
            for col in row:
                if col not in temp:
                    flag = False
        
        return True if flag else False
