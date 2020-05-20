class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        '''思路是找到以每个柱子为最矮柱子从而找到面积
        方法是维持一个单调递增栈，当不满足单调递增时，弹出栈顶的元素，其面积为栈顶为高，此时的元素减去栈顶元素之后的
        栈顶的位置为高，找到最大值即可
        '''
        heights = [0] + heights + [0] #这个的目的是使得最左和最右的元素的面积可求
        stack, res = [], 0
        lenth = len(heights)
        for i in range(lenth):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res, (i-stack[-1]-1) * heights[top])
            stack.append(i)
        return res
