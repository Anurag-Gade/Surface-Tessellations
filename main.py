from overlapping_tesselations import *
import argparse

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = "Surface Tessellations")

parser.add_argument('--input_path', action= 'store', required=True,
                    type=str, help='Path to an input nifti file')

parser.add_argument('--output_file_path', action='store', required=True,
                    type=str, help='Output file path')

parser.add_argument('--offset', action='store', default=0.1,
                    type=float, help='Overlapping offset')

parser.add_argument('--iterations', action='store', default=100,
                    type=int, help='Mesh decimation parameter')

args = parser.parse_args() 

input_path = args.input_path
output_file_path = args.output_file_path
offset = args.offset
iterations = args.iterations


# type(offset) -> float
    # Offset adjusts the overlapping distance.
'''
type(offset) -> float
The variable "offset" adjusts the overlapping distance
'''


tesselation_function(input_path, output_file_path, offset, iters) 
