class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        #1 step is to sort the array becuz two pointers only works on sorted array
        nums.sort()


        #2 step for loop for i which only goes till len(nums - 2) index 
        # for example if array is size 6 ->  6 - 2 = 4 (i will only go till 4th index)
        #because you need two values ahead of i for the left and right pointer
        for i in range(len(nums) - 2):

            #3. check for i duplicates

            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            
            #4. make the pointers 

            left = i + 1
            right = len(nums) - 1
            
            # 5. run the loop until left and right pointers dont reach 
            # once they reach, i  will do a new value
            while left < right:
                
                #6. calculate the total
                total = nums[i] + nums[left] + nums[right]

                #here are things to check now when calcualting the triplets:
                #7. check first if total is equal to 0, if it is then:
                '''
                - append the triplet to the result list 
                - check for duplicates next for the left and right pointers 
                - if left and right have not met, and left is equal to the next left value, increment left by 1 value
                - if left and right have not met, and right is equal to the (next aka backawards) value, decrement right by 1 value
                - if left and right have no duplicates then skip the while loops and just increment left by 1 and decrement right by 1 
                '''
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        #this moves u to the last duplicate (so its still on the duplicate)
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # this moves u to the last duplicate (so its still on the duplicate)
                        right -= 1
                    #you increment/decrement so you can move ahead from the last duplicate value
                    left += 1 
                    right -= 1
                elif total < 0:
                    left += 1 
                else:
                    right -= 1 
        return result
                







        