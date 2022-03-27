class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        i=0
        while(i<len(nums)):
            val = target-nums[i]
            if val in dic:
                return [dic[val],i]
            dic[nums[i]]=i
            i+=1
            
        
        
        