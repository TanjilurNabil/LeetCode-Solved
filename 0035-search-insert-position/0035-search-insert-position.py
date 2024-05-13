class Solution(object):
    def searchInsert(self,nums,target):
        return self.find(nums, target)
    
    def binary_search(self,lo, hi, condition):
        while lo <= hi:
            mid = (lo+hi)//2
            result = condition(mid)
            if result == 'found':
                return mid
            elif result == 'left':
                hi = mid-1
            else:
                lo = mid+1   
        return self.indexOfInsert(lo, hi, result)
    
    def find(self,nums, target): 
        def condition(mid):
            if nums[mid] == target:
                if mid > 0 and nums[mid-1] == target:
                    return 'left'
                return 'found'
            elif nums[mid] < target:
                return 'right'
            else:
                return 'left'
        return self.binary_search(0, len(nums)-1, condition)
    
    def indexOfInsert(self,lo, hi, result):
        if result == "right":
            return hi+1
        else:
            return lo