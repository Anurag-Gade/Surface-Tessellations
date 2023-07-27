from overlapping_tesselations import *

input_file_path = "/input_dir/mri.nii"
output_file_path = "/output_dir/overtess_1.stl"
offset = 0.1
iters = 100

tesselation_function(input_file_path, output_file_path, offset, iters) 