class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):


        res = 1
        for i in range(31, 0, -1):
            bit = n >> i
            res = res * 2**bit
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(11111111111111111111111111111101))