# Image-tracer
A simple game for tracing coordinates of a shape in an image by manual traversal, the game logs the traversed coordinates into the python dictionary. The coordinates logged are used to define a discrete Fourier series associated with the coordinates.<br />
the game is implemented using pygame library.

## ABOUT THE GAME
It contains a 9 by 9 pixels magnified frame of the selected image, the pixels in the image with solid fill i.e, alpha 255, given black color and rest given white.
Using control keys one could traverse a certain shape in that image, which is useful for defining a path that fourier epicycles goes through.

## CONTROLS
controls are very intuitive as the offset are in sequence with keypad
7 8 9 are used to go back one step in y direction and -1 0 1 in x direction
similarlly 4 5 6 go -1 0 1 in x direction
1 2 3 going one step forward in y and -1 0 1 in x

### control for logs:
"d" for poping the present coordinates from the log dictionary.<br/>
spacebar for emptying the log dictionary.<br/>
press any key (other than the keys mentioned above) for displaying logs object array.<br/>
