# Blender Image Renderer 📸

Blender Image Renderer is a blender tool used to create rotated rendered images of models.

## Requirements 🔧

In order for Blender Image Renderer to work correctly your .blend files would require the following.

1. An object with the appropriate name 
2. A Camera in your scene (At the angle you want your images to be rendered)
3. (Optional) Light/Plane

***Note:*** ***This tool uses all your custom render settings as well origin/pivot points, If you would like to change these change the appropriate settings in your .blend files.***

## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/Chrisdafur3/Blender-Image-Renderer.git`

2. Navigate to the directory

    `cd "Blender-Image-Renderer\Main Application"`

3. Run:

    `backrun.exe`
    
## Instructions 💻

"Choose Path": Select a folder containing all .blend files

"Choose Directory": Select an output directory where all rendered images will be saved

"Name of Object": Name of the object in your .blend file that you want rendered

"Amount of Steps": Number of images you want rendered (Amount of steps around your rotation angle)

"Object Rotation": The amount of rotation you want applied to your object

"Filename_n": The name you want to call your images

<p align="center">
<img align="center" src=".Images/blender_script.PNG" width="900">
</p>

<p align="center">
<img align="center" src=".Images/output_folders.PNG" width="900">
</p>

<p align="center">
<img align="center" src=".Images/output_images(1).PNG" width="900">
</p>

<p align="center">
<img align="center" src=".Images/output_images(2).PNG" width="900">
</p>

<p align="center">
<img align="center" src=".Images/output_images(3).PNG" width="900">
</p>
