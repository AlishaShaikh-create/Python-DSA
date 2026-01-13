def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    # Initialize the Pascal's triangle with an empty list
    triangle = []
 
    # Generate each row of the triangle
    for row_num in range(numRows):
        # Start each row with a list of 1s
        row = [1] * (row_num + 1)
 
        # Update the values of the row based on the previous row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
 
        # Append the generated row to the triangle
        triangle.append(row)
 
    return triangle
print(generate(5))