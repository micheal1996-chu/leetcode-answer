class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 利用左乘和右乘来处理,不能乘自己
        lenth = len(nums)
        k = 1
        res = [1] * lenth
        for i in range(lenth): #右乘
            res[i] = k
            k *= nums[i]  #k用来记录num[i]左侧的结果
        k = 1
        for i in range(lenth-1, -1, -1): #左乘
            res[i] *= k
            k *= nums[i]  #k用来记录num[i]右侧的结果
        return res
