from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        n = len(nums)
        nums = [0, 1, ..., n-1]

        Compute prefix products

        Compute suffix products

        output[i] = prefix[i] * suffix[i]
        """
        # Get the length of the input array
        n = len(nums)
        # Initialize the output array with 1s; this will hold the final products
        output = [1] * n
        # First pass: Compute prefix products
        # We use output to store prefix products temporarily
        for i in range(1, n):  # Iterate from index 1 to n-1
            output[i] = nums[i-1] * output[i-1]  # output[i] = product of all elements before index i
            print(output)  # Debug print (can be removed)

        # Initialize suffix product
        suffix = 1
        # Second pass: Compute suffix products and multiply with prefixes
        for i in range(n-1, -1, -1):  # Iterate from the last index down to 0
            output[i] *= suffix  # Multiply prefix product with suffix product
            suffix *= nums[i]  # Update suffix for the next iteration (moving left)

        # Return the output array containing products except self
        return output