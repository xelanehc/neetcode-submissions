class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 1, n - 2
        peak = 0
        while l <= r:
            m = l + (r - l) // 2
            vl = mountainArr.get(m - 1)
            vm = mountainArr.get(m)
            vr = mountainArr.get(m + 1)
            if vl < vm < vr:
                l = m + 1
            elif vl > vm > vr:
                r = m - 1
            else:
                peak = m
                break
        
        l, r = 0, peak
        while l <= r:
            m = l + (r - l) // 2
            vm = mountainArr.get(m)
            if vm == target:
                return m
            elif vm < target:
                l = m + 1
            else:
                r = m - 1

        l, r = peak, n - 1
        while l <= r:
            m = l + (r - l) // 2
            vm = mountainArr.get(m)
            if vm == target:
                return m
            elif vm < target:
                r = m - 1
            else:
                l = m + 1
        
        return -1