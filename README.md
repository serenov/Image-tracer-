# Image-tracer
A simple game for tracing coordinates of a shape in an image defining a path for fourier series manually.
Implemented using pygame library.

## ABOUT THE GAME
It contains a magnified frame of the image with 9 by 9 pixels, the image pixels with solid fill i.e, alpha 255, given black color rest given white.
Using control keys one could traverse a certain shape in that image, which is useful for defining path that fourier epicycles.

## CONTROLS
controls are very intuitive as the offset are in sequence with keypad
7 8 9 are used to go back one step in y direction and -1 0 1 in x direction
similarlly 4 5 6 go -1 0 1 in x direction
1 2 3 going one step forward in y and -1 0 1 in x

### control for logs:
"d" for poping the present coordinates from the log.<br/>
spacebar for emptying the log.<br/>
press any key for displaying logs object array.<br/>
