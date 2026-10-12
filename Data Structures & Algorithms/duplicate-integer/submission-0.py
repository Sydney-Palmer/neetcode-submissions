class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkingNumber = set()
        duplicate = False
        for number in nums:
            if number in checkingNumber:
                duplicate = True
                break
            checkingNumber.add(number)
        return duplicate