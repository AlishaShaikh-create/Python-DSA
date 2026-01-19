
def rotate_list(lst, k):
    # Handling the case where the list is empty
    if not lst:
        return []
    
    # Modulo to handle the case where k is greater than the length of the list
    k = k % len(lst)
    
    # Brute force approach using loops
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
    
    return lst