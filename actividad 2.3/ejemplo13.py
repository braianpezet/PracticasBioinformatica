#!/usr/bin/python
##--------------Program Info:-----------------------------------------------##
# Descargado de aca: https://www.r-bloggers.com/2014/12/ants-snakes-and-the-hydrophobic-polar-model/
# Folding but not your Laundry - Using the 2D HP model for showing how protein 
# folding works
#
# File: folding.py
#
# By Mobeen Ludin and Aaron Weeden, 21 May 2013
#
# High-level Algorithm:
#	- Given a string
#	- Generate each possible folding of the string
#	- Count the number of H-H bonds for each folding of the string
#	- Save the foldings with the greatest number of H-H bonds
#	- Throw away the foldings we saved if we find a folding with a bigger 
#          number of H-H bonds
#	- Print the foldings we saved when we are done
#
##------------------------------------------------------------------------------
##----------Python Code for Protein Folding:-----------------------------------
#

import sys
#---Global variable initialization---#
EMPTY = ' ' # This represents an empty character in the grid
best_grids = [] # This is a list of the grids that contain the best foldings

#---Main function definition---#
def main():

	#--Local variable initialization--#
	current_element_idx = 0 # Index of the current element in protein
	#protein = 'HPHPPHHPHPPHPHHPPHPH' # Protein we are folding
	protein = "HHPP" # Protein we are folding
	current_grid = [] # Grid in which we are currently folding
	current_num_H_bonds = max_num_H_bonds = 0 # Counters
	print "Hello protein folders, beginning program" # Print a greeting

	#-Fill the grid with empty characters-#
	# For each row of the grid
	for row in range(len(protein)*2-1):

		# Create a new empty list for that row
		current_grid.append([])

		# For each column of the grid
		for col in  range(len(protein)*2-1):

			# Add an empty character at the given row/column
			current_grid[row].append('*')

	# Start the first protein element in the middle of the grid
	current_row = current_col = int((len(protein)*2-1)/2)

	# Recursively find the best foldings, filling best_grid
	print "Best number of H-H bonds", fold( protein, max_num_H_bonds, current_element_idx, current_grid, current_row, current_col, ' ', current_num_H_bonds )

	#-Print the best grids-#
	# For each of the best grids
	for grid in range(len(best_grids)):
		# Print the index of the grid
		print "Grid ", grid, ":"
		#print best_grids
		# For each row in the grid
		for row in range(len(protein)*2-1):

			# For each column in the grid
			for col in  range(len(protein)*2-1):

				# Print the character at the given row and
				# column
				print best_grids[grid][row][col],

			# Print a line in between the rows
			print ''
#---Fold function definition---#
def fold( protein, max_num_H_bonds, current_element_idx, current_grid, current_row, current_col, direction, current_num_H_bonds ):

	# Determine the new current row and column based on the current
	# direction
	if direction == 'R':
		current_col +=1
	elif direction == 'D':
		current_row +=1
	elif direction == 'L':
		current_col -=1
	elif direction == 'U':
		current_row -=1

	# If we are able to place an element at the current row and column
	if current_grid[current_row][current_col] == '*':

		#-Make a copy of the current grid before we change it-#
		new_grid = []
		for row in range(len(protein)*2-1):
			new_grid.append([])
			for col in range(len(protein)*2-1):
				new_grid[row].append(current_grid[row][col])

		# Place the protein in the new grid
		new_grid[current_row][current_col] = protein[current_element_idx]
	   	# Check for H-H bonds in the current fold
		if protein[current_element_idx]=='H':

			# Check to the left
			if current_col > 0 and new_grid[current_row][current_col-1]=='H':
				current_num_H_bonds +=1

			# Check above
			if current_row > 0 and new_grid[current_row-1][current_col]=='H':
				current_num_H_bonds +=1

			# Check to the right
			if current_col < len(new_grid[current_row]) - 1 and new_grid[current_row][current_col+1]=='H':
				current_num_H_bonds +=1

			# Check below
			if current_row < len(new_grid) - 1 and new_grid[current_row+1][current_col]=='H':
				current_num_H_bonds +=1

		# Move on to the next element index
		current_element_idx +=1

		# If not end of string, choose each direction and recur
		if current_element_idx != len(protein):
			for direction in ['R', 'D', 'L', 'U']:
				max_num_H_bonds = fold( protein, max_num_H_bonds, current_element_idx, new_grid, current_row, current_col, direction, current_num_H_bonds )

		else: 
			# If end of string, check if the current fold has more  
			# H-H bonds than the max we found before.
			# if true update the max.  If we have the same number of
			# H-H bonds, append the current grid to the list of best
			# grids
			if current_num_H_bonds > max_num_H_bonds:
				max_num_H_bonds = current_num_H_bonds
				del best_grids[:]
				best_grids.append(new_grid)
			elif current_num_H_bonds == max_num_H_bonds:
				best_grids.append(new_grid)

	# Return the count of the maximum number of H-H bonds
	return max_num_H_bonds

##---Call main function-----##
main()
