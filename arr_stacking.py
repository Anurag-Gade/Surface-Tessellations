# Preprocessing Stacker Function

import numpy as np

# The below function takes in a 2D array as an input, inserts the number of elements which the subarray contains in the index position '0', which is the starting of the subarray, and horizontally stacks 
# the new subarrays, which then can be used as an input to **pyvista.PolyData**.

def stack_arrs(input_arr):
    	
	test_arr = np.asarray(input_arr)

	test_arr = test_arr.tolist()
	# print(test_arr)
	empty_arr = []
	for i in test_arr:
	    
	    i.insert(0,len(i))
	    # print(i)
	    empty_arr.append(i) 
    

	filled_arr = np.asarray(empty_arr) 
	big_array = np.hstack(filled_arr) 

	return big_array
