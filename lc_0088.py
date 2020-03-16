def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    nums1index = m-1
    nums2index = n-1
    
    numsindex = m+n-1
    
    while numsindex >= 0:
        if nums1index < 0:
            while (numsindex >= 0):
                nums1[numsindex] = nums2[nums2index]
                nums2index -= 1
                numsindex -= 1
            return nums1
        elif nums2index < 0:
            while (numsindex >= 0):
                nums1[numsindex] = nums1[nums1index]
                nums1index -= 1
                numsindex -= 1
            return nums1
        else:
            if nums1[nums1index] > nums2[nums2index]:
                nums1[numsindex] = nums1[nums1index]
                nums1index -= 1
            else:
                nums1[numsindex] = nums2[nums2index]
                nums2index -= 1
            numsindex -= 1
                
    return nums