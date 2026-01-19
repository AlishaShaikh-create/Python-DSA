# Rotate the list

def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # TODO: Implement this function
    new_lst=[]
    for i in range(D, len(ARR)):
        new_lst.append(ARR[i])
    for j in range(0, D):
        new_lst.append(ARR[j])
    return new_lst 

ARR = [1, 2, 3, 4, 5]
print(rotate_left(ARR,2))



def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # Handle the rotation
    D = D % len(ARR)  # Handle cases where D is larger than the size of the list
    return ARR[D:] + ARR[:D]

ARR = [1, 2, 3, 4, 5]
print(rotate_left(ARR,1))
