class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join('1' if x=='0' else '0' for x in bin(N)[2:]),2)