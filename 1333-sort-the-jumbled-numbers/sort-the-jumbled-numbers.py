class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = [0] * len(nums)
        num_map = defaultdict(list)
        
        for i in range(len(nums)):
            number = nums[i]
            idx = 1
            mapped_number = 0
            
            while number > 0:
                remainder = number % 10
                mapped_number += mapping[remainder] * idx
                number //= 10
                idx *= 10
            
            if nums[i] == 0:
                mapped_number = mapping[0]
            
            mapped[i] = mapped_number
            num_map[mapped[i]].append(nums[i])
        
        sorted_mapped = sorted(mapped)
        idx = 0
        
        for value in sorted_mapped:
            if value in num_map:
                for val in num_map[value]:
                    nums[idx] = val
                    idx += 1
                del num_map[value]
        
        return nums      