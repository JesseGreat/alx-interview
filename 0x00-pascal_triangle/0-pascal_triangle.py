#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]] #initialize the first row with [1]

    for row in range (1, n):
        prev_row = triangle[-1]
        current_row = [1] #The first element of each row is always 1
        
        #Calculate the values for the current row based on the previous row
        for i in range (1, row):
            current_row.append(prev_row[i - 1] + prev_row[i])
        
        current_row.append(1) #The last element of each row is always 1
        triangle.append(current_row)
    
    return triangle