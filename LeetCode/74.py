class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            for col in row:
                if col == target:
                    return True
        return False
