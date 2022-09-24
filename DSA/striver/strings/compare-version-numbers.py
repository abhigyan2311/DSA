from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = list(map(int, version1.split('.'))), list(
            map(int, version2.split('.')))
        # zip will stop combining our iterables as soon as one of them runs out of elements. zip longest will fill with 0
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue
            if rev1 > rev2:
                return 1
            else:
                return -1
        return 0


ans = Solution().compareVersion("0.1", "1.1")
