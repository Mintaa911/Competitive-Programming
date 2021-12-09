class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        i = 0
        while nums2 and i < len(nums1):
            j = 0
            while nums2 and j < len(nums2):
                if nums1[i] == nums2[j]:
                    if nums2[j] not in intersection:
                        intersection.append(nums2[j])
                    nums2.pop(j)
                    break
                j += 1
            i += 1
        return intersection
