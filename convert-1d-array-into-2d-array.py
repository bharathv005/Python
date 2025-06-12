class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original) != m*n:
            return []
        res=[]

        for r in range(m):
            start=r*n
            end=start+n
            res.append(original[start:end])
        return res
