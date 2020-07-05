class Solution(object):
    def plusOne(self, digits):
        temp = []
        digits.reverse()
        for i in range(len(digits)):
            val = digits[i]
            for j in range(i):
                val = val*10
            temp.append(val)

        val = 0
        for i in temp:
            val = val + i
        val = val + 1
        temp = []
        val = str(val)
        for i in range(len(val)):
            temp.append(int(val[i]))

        return temp




s = Solution()
s.plusOne([1,2,3])