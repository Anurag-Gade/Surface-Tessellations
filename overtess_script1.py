import numpy as np
import pyvista as pv
import nibabel as nib
from arr_stacking import *
from skimage import measure

# Load the MRI data which is a NIftI file (.nii)
mri_file_path = "/data_dir/mri.nii"

#Loading the brain data 
brain = nib.load(mri_file_path)

#Converting to a NumPy array
binary_brain_mask_inp = brain.get_fdata()

binary_brain_mask = np.sum(binary_brain_mask_inp, axis=3)


# print(binary_brain_mask.shape)

# Creating the surface mesh using the marching cubes algorithm
vertices, faces, _, _ = measure.marching_cubes(binary_brain_mask, 0.5)

faces_1 = stack_arrs(faces)

# Using the output from the marching cubes algorithm, a PyVista mesh is created
mesh = pv.PolyData(vertices, faces_1)

# Mesh Decimation
mesh = mesh.smooth(n_iter=100)

# Overlapping regions are created using mesh translation

# type(offset) -> float
# Offset adjusts the overlapping distance.

offset = 0.1  
overlap_mesh = mesh.copy()
overlap_mesh.translate([offset, 0, 0])

# Mesh combination
final_mesh = mesh + overlap_mesh

# Final mesh decimation
final_mesh = final_mesh.smooth(n_iter=100)

# Saving the required file in the ".stl" format
output_mesh_file = "/output_dir/overtess_1.stl"
final_mesh.save(output_mesh_file)
