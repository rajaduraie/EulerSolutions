""" A 20 x 20 matrix is present in a file. 
The max product of 4 elements in one of the four directions
( sideways, downwards, diagnally up, diagnally down ) needs to
be found 
"""



import os

def calculate_max_grid_product ():

  # Get all elements in a two dimensional array
  # The file named matrix.txt needs to be locally placed.
  # that will have all the required elements in matrix form

  matrix = [[0 for x in range(20)] for x in xrange(20)]
  f = open('matrix.txt', 'r')
  for i in range(20):
    line = f.readline()
    elements = line.split(' ')
    for j in range(20):
      matrix[i][j] = int(elements[j])

  
  max = 0
  for i in range(20):
    for j in xrange(20):

      # find_largest in rows
      if (j < 17):
        if (matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3] > max):
          max = matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]

      # find largest in columns
      if (i < 17):
        if (matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j] > max):
          max = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]

      # find largest diagnally downwards

      if (i < 17 and j < 17):
        if (matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3] > max):
          max = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]

      # find largest diagnally upwards

      if (i > 2 and j < 17):
        if (matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3] > max):
          max = matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
        
  print max

calculate_max_grid_product()

