class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.arr = nums
        temp = set()
        for i in range(len(self.arr)):
            if self.arr[i] in temp:
                return True
            temp.add(self.arr[i])
        return False