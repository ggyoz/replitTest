# 349. Intersection of Two Arrays
# 배열 교집합 찾기

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        intersection = list(set(nums1) & set(nums2))
        
        return intersection