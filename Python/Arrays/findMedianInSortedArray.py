def findMedianSortedArrays(nums1, nums2) -> float:
    new = []
    for i in nums1:
        new.append(i)
    for i in nums2:
        new.append(i)
            
    new = sorted(new)
        
    if len(new) % 2 == 0:
        div = len(new) // 2
        out = (new[div] + new[div - 1]) / 2
            
    else:
        div = len(new) // 2
        out = float(new[div])
            
    return out
            

