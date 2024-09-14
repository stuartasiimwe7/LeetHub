'''
You're given an array called nums and an integer val. 
TASK:
>Go through nums and remove all occurrences of val.  
>After that, rearrange nums so that the first k elements contain 
only the values that are not equal to val
>where k is the count of these remaining elements. 

>Finally, return the value of k
NB:
The order of the remaining numbers doesn’t matter, 
and you don’t need to worry about the leftover spaces in the list. 

'''

class Solution (object):
    def removeElement(self,nums,val):
        k = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[k] = nums[i]
                k +=1
            
            return k