class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ind = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[ind]
            j = i
            while j >= 1 and nums1[j] < nums1[j - 1]:
                nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]
                j -= 1
            
            ind += 1
        