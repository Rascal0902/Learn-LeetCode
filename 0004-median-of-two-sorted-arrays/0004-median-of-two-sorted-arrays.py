class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merge = nums1 + nums2
        temp = sorted(merge)
        cnt = len(temp)
        
        if cnt % 2 == 0:
            return float((temp[(cnt - 1) // 2] + temp[(cnt + 1) // 2]) / 2.0)
        
        else:
            return float(temp[cnt // 2])

        