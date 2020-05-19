class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 题目的意思是找到/x/,如果x为字符串则保留，如果是.则不用理会，如果是..则如果结果
        # 不为空则删去最后一个字符串，同时删除多余的/,结尾不能含有/
        path = path.split('/') #依照/分割字符串
        stack = []
        for i in path:
            if i == '..':
                if stack:
                    stack.pop()
            elif i == '' or i == '.':
                pass
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
