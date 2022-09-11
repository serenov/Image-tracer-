# Image-tracer
A simple game for tracing coordinates of a shape in an image by manual traversal, the game logs the traced path's coordinates into the python dictionary. The coordinates logged are used to define Fourier series<br />
the game was implemented using pygame library.

## ABOUT THE GAME
The game has a 9 x 9 magnified frame view of the selected image, the pixels in the image with solid fill (i.e, alpha 255) assigned black color and the rest assigned white.
Using control keys one could trace the path of a certain shape in the image, which is useful for defining the path for fourier epicycles.

## CONTROLS
Controls are very intuitive, as the directions are mapped directly to the keypad's keys position.<br/>
7 8 9 keys are used to go one step backward in y direction and -1 0 1 to move in x direction.<br/>
similarlly 4 5 6 go -1 0 1 in x direction. <br/>
1 2 3 going one step forward in y and -1 0 1 in x

### control for logs:
"d" for poping the recently added record from the log.<br/>
spacebar for emptying the log.<br/>
press any key (other than the keys mentioned in "CONTROLS" section) for displaying logs.<br/>
