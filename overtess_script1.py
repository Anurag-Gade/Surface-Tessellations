import numpy as np
import pyvista as pv
import nibabel as nib
from arr_stacking import *
from skimage import measure

# Load the MRI data
mri_file_path = "/data/pnl/home/ag1666/coeff_dir/data/ABCD/dwi_fodf.nii"

#Loading the brain data
brain = nib.load(mri_file_path)

#Converting to a NumPy array
binary_brain_mask_4d = brain.get_fdata()

binary_brain_mask = np.sum(binary_brain_mask_4d, axis=3)


# print(binary_brain_mask.shape)

# Assuming you have preprocessed and segmented the MRI data,
# you have a binary mask where 1 represents the brain region of interest.
# binary_brain_mask = np.load(mri_file, allow_pickle=True)

# Perform marching cubes to create the surface mesh
vertices, faces, _, _ = measure.marching_cubes(binary_brain_mask, 0.5)

faces_1 = stack_arrs(faces)

# Create a Pyvista mesh from the marching cubes output
mesh = pv.PolyData(vertices, faces_1)

# Optional smoothing or decimation of the mesh
mesh = mesh.smooth(n_iter=100)

# Create overlapping regions by translating the mesh
offset = 0.1  # Adjust the overlap distance as needed
overlap_mesh = mesh.copy()
overlap_mesh.translate([offset, 0, 0])

# Combine the meshes into a single overlapping mesh
final_mesh = mesh + overlap_mesh

# Optional smoothing or decimation of the final mesh
final_mesh = final_mesh.smooth(n_iter=100)

# Save the resulting mesh to a file (e.g., STL or OBJ)
output_mesh_file = "/data/pnl/home/ag1666/coeff_dir/OverlappingTesselations/outputs/overtess_1.stl"
final_mesh.save(output_mesh_file)
