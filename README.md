# GameOfLife
Building my own iteration of Conway's Game of Life as a resume building exercise.

After recently being furloughed by the Astronomical Society of the Pacific and NASA I decided I wanted to spruce up my Python skills as I had been coding in exclusively Java for the last year.  I came across the Wiki for [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) and it appeared to be something I should be able to bang together in a few days.

# Relevant Information
This script was written for Python 3.7.5
I use [virtualenv](https://virtualenv.pypa.io/en/latest/) to manage development environments.  I recommend you do too.

# Instructions
1. Download the project
2. Activate your virtual environment.
3. Navigate to the game_of_life.py file in your filesystem
4. Type ```python game_of_life.py```
5. Follow the on screen instructions

# Upcoming Improvements
1. Reading up on the PyQt5 library to enhance the graphics from terminal/text to something much more appealing. 
2. Adding the ability for the user to create their own starting 'soups' as currently the code randomizes a soup upon initalization
3. Adding functionality to write soups/seeds to a text file for later recall/display
4. Possibly adding the ability to modify the standard rules (i.e. change the number of neighbors that instigate continued life, instantiated life or death.
