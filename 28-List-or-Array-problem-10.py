def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    # TODO: Implement this function
    set1=set(nums1)
    set2=set(nums2)
    set3=set1.intersection(set2)
    list1=list(set3)
    return list1

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

