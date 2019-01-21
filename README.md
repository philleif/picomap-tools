# picomap-tools
Toolkit for making tiny projection maps.

Requirements:
- Python
- MoviePy
- Imagemagick
- ffmpeg

Optional:
- Meshmixer (http://meshlab.sourceforge.net/)

# Setup
$ git submodule init
$ git submodule update

# Find loop point & extract video
`python bin/process-video.py "media/fish.mp4"`

# Video to B&W
`ffmpeg -i media/test.mp4 -vf hue=s=0 -c:a copy media/bw.mp4`

# Video to images
`ffmpeg -i media/bw.mp4 -vf fps=5 -vsync 0 media/out%d.png`

# Blend images
`convert media/out*.png -evaluate-sequence mean media/averageresult.png`

# Make depth map
https://github.com/lixx2938/MegaDepth

# Convert to STL
https://github.com/philleif/img2stl

# Clean STL
1. Open Meshlab
2. Import the .stl file (File>Import Mesh ...)
3. Select all points ( Filers>Selection>Select all )
4. Compute normal ( Filters>Normals, Curvature, and Orientation> Compute normal for point set)
5. Create a surfaces ( Filters>Remeshing, Simplification, and Reconstruction>Surface Reconstruction: Poisson )
6. Export Mesh as an .stl file ( File>Export Mesh... )

Or use the included Meshlab script (simplify-stl.mlx):
`./Applications/meshlab.app/Contents/Frameworks/Applications/meshlab.app/Contents/MacOS/meshlabserver -i media/output.stl -o ~/output-simplified.stl -s ~/simplify-stl.mlx -om vn`

# References
"An Algorithm to Extract Looping GIFs From Videos": http://zulko.github.io/blog/2015/02/01/extracting-perfectly-looping-gifs-from-videos-with-python-and-moviepy/

"Creating a smooth surface from huge number of vertices"
https://blender.stackexchange.com/questions/48735/creating-a-smooth-surface-from-huge-number-of-vertices

