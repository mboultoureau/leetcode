class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        nb_rows = [0] * len(mat)
        nb_cols = [0] * len(mat[0])
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    nb_rows[i] += 1
                    nb_cols[j] += 1

        result = 0
        for i in range(len(mat)):
            if nb_rows[i] != 1:
                continue
            
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and nb_rows[i] == 1 and nb_cols[j] == 1:
                    result += 1
                    break
        
        return result