class Solution():
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num = target - numbers[i]
            j = i + 1
            while j < len(numbers): 
                if numbers[j] == num: return [i + 1, j + 1]
                j += 1