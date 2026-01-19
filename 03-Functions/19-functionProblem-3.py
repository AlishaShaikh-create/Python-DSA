
def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Divide total people by the capacity to get full rounds
    full_rounds = n // capacity
    
    # If there are any remaining people, add one more round
    if n % capacity != 0:
        return full_rounds + 1
    else:
        return full_rounds
    
print(calculate_lift_rounds(10,3))    