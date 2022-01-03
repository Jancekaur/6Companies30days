class Solution:

    def doOverlap(self, L1, R1, L2, R2):
        lt1 = L1[0]
        tp1 = L1[1]
        rt1 = R1[0]
        bt1 = R1[1]

        lt2 = L2[0]
        tp2 = L2[1]
        rt2 = R2[0]
        bt2 = R2[1]

        if (lt1 > rt2 or tp1 < bt2 or lt2 > rt1 or tp2 < bt1):
            return 0
        else:
            return 1

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p = [0] * 2
        q = [0] * 2
        r = [0] * 2
        s = [0] * 2
        p[0], p[1], q[0], q[1], r[0], r[1], s[0], s[1] = map(int, input().strip().split(" "))
        ob = Solution()
        ans = ob.doOverlap(p, q, r, s)
        print(ans)
