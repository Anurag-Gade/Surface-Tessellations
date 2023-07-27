# Surface-Tessellations

A tessellation or tiling is essentially covering the surface of a 3D object with shapes (tiles). This code demonstrates the surface tessellation of an MR brain image, with overlapping tiles. To achieve overlaps in the tiles, an offset has been added. Below is an example of a surface tessellated brain scan.

<p align="center">
  <img width="460" height="300" src="https://github.com/Anurag-Gade/Surface-Tessellations/assets/88252632/d42664d9-7c1e-47df-b8a6-f8447349bfdf">
</p>

To obtain the surface tesselation, load the 3D file by mentioning the path. The output path, where the `.stl` file gets saved needs to be mentioned as well. The input file must be in a format which is convertable to a NumPy array. 

The overall structure of this project is as follows:

```
├── README.md 
├── arr_stacking.py
├── main.py
├── overlapping_tessellations
```        

Run `main.py` after mentioning the appropriate file paths, and parameters. 

If the script executes seamlessly, the below message will appear on the terminal.
```
>>> python main.py
Tesselation Saved!!!
```

`overlapping_tessellations.py` contains the script to create tesselations. `arr_stacking.py` contains the script to prepare the face input suitable for the PyVista's PolyData function. `main.py` is the runner script.

*Required packages and libraries*

- `numpy`
- `pyvista`
- `nibabel`
- `skimage`
