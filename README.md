# Blender Version Selector
 Simple python script and batch file to help select which blender version to use
 
 Only tested on windows. It can both just launch blender, and open .blend files. It opens a command window and asks you what version you want to open, and will open the file you just dragged onto or opened with it (if you did, otherwise you just get default cube drip). You can just double click the bat file and make a shortcut to it, or drag a .blend file onto it. You can also associate blend files with it so it does it every time you open a blend file. It opens a command window asking you what version to use based on folder names, so highly recommended to just make it the numbers, not blender-windows64-blablabla since you have to type in the folder name
 
 Not tested on linux, but if you just run the python script in terminal, it should work fine just for opening an empty scene. It should be a pretty simple bash script to get it to do the same thing as the batch file, that is open a specific file.
 
 Put it in a folder with blender versions in subfolders, basically just like this:
 
 Blender Versions
 |----2.92.0
      |----blender.exe
      |----other blender 2.92.0 files
 |----2.93.1
      |----blender.exe
      |----other blender 2.93.1 files
 |----Blender Version Selector.bat
 |----blender_versions.py



It's definitely not perfect, but I'd honestly rather spend my time modelling or doing other stuff, this is basically just a time saver that of course I put too much time into to keep to myself. [As always, relevant XKCD here](https://xkcd.com/1319/). If you want to improve or even just fork go ahead :)
