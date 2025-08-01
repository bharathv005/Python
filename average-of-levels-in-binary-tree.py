class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        output=[]
        curr=[root]
        while curr:
            new_level=[]
            curr_sum=0
            for i in curr:
                if i.left:
                    new_level.append(i.left)
                if i.right:
                    new_level.append(i.right)
                curr_sum+=i.val
            output.append(curr_sum/float(len(curr)))
            curr=new_level
        return output
