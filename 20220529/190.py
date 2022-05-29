class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(31, -1, -1):
            bit = (n >> i) % 2
            print(i, bit)
            res += 2**(32-i) * bit
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(11111111111111111111111111111101))
