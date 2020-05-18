class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''思路时将问题转换为找到一个aj,在[1，j-1]内有比他小的数M1，在[j+1,lenth]内有比aj小的数M2,且M2 > M1
        第一步是构建一个最小值列表，即aj左侧的小于等于aj的最小值
        第二步是从后先前构建单调栈，确保栈内的元素大于M1
        第三步如果aj大于M1，又有aj大于栈内的元素，问题即可求解
        '''
        lenth = len(nums)
        if lenth < 2:
            return False
        M1 = [nums[0]]
        for i in range(1, lenth):
            M1.append(min(M1[-1], nums[i]))
        stack = []
        for i in range(lenth - 1, -1, -1):
            if nums[i] > M1[i]:  # 此处确保aj的左边存在一个数小于aj
                while stack and M1[i] >= stack[-1]:  # 此处确保stack里的元素是大于MI[i]的
                    stack.pop()
                if stack and nums[i] > stack[-1]:  # 因为stack里的元素是aj右边的元素，且stack里的元素都大于aj左侧的最小值，所以当aj大于栈顶元素时，找到结果
                    return True
                stack.append(nums[i])
        return False
