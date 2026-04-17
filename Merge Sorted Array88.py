class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x=[]

        for i in range(m):
            x.append(nums1[i])
        for j in range(n):
            x.append(nums2[j])

        x.sort()

        for i in range(len(x)):
            nums1[i]=x[i]

            

        
