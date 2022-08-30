# 414. Third Maximum Number
# 주어진 배열에서 3번째로 큰 숫자 출력
# 배열의 길이가 3보다 작으면 제일 큰 수 출력

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
                
        s = sorted(set(nums))
        
        if len(s) > 2:
            return s[len(s) - 3]
        else:
            return s[len(s) - 1]