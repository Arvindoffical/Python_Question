class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        def ismax(matrix, min_val, index):
            for row in matrix:
                if row[index] > min_val:
                    return False
            return True

        list = []
        
        for row in matrix:
            min_val = min(row)
            index = row.index(min_val)
            
            if ismax(matrix, min_val, index):
                print(min_val)
                list.append(min_val)
        
        return list

        