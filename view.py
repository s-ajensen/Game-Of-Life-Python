# View for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

from tkinter import *

colors = ['white', 'grey']


# Create prompt window of type frame
class Prompt(Frame):
    # Define constructor with parameter self
    def __init__(self):
        # Call the Frame constructor as constructor for Prompt
        Frame.__init__(self)
        # Set title of object
        self.master.title("Initialize Grid")

        # Create header label and draw in grid row 0
        header = Label(text="Input Grid Dimensions")
        header.grid(row=0)

        # Create horizontal cells label and draw in grid row 1
        horizontal = Label(text="Horizontal Cells: ")
        horizontal.grid(row=1)

        # Create horizontal input textbox and draw in grid row 1, column 1
        self.hInput = Entry()
        self.hInput.grid(row=1, column=1)

        # Create vertical cells label and draw in grid row 2
        vertical = Label(text="Vertical Cells:")
        vertical.grid(row=2)

        # Create vertical input textbox and draw in grid row 2, column 1
        self.vInput = Entry()
        self.vInput.grid(row=2, column=1)

        # Create submit button with command .__submitCoords__ and draw in grid row 3
        submit = Button(text="Submit", command=lambda: self.__submitCoords__())
        submit.grid(row=3)

    # Define submitCoords method which closes prompt and sets dimension data
    def __submitCoords__(self):
        # Get data from hInput and vInput Entries and convert to integers
        self.verticalCells = int(self.vInput.get())
        self.horizontalCells = int(self.hInput.get())
        # Close Prompt instance
        self.master.destroy()


# Create GridDisplay window of type Frame
class GridDisplay(Frame):
    # Define constructor with parameters for height and width of grid
    def __init__(self, height, width, currentGrid, nextGrid):
        # Call Frame constructor as constructor for GridDisplay
        Frame.__init__(self)
        # Set page title
        self.master.title("Conway's Game of Life")

        # Set height and width parameters to be accessible from any method of GridDisplay
        self.height = height
        self.width = width

        # Create 2D array of buttons with y and x variables for reference
        self.buttons = [[Button(width=2, command=lambda y=row, x=column: self.__toggle__(currentGrid, y, x))
                        for column in range(self.width)]
                        for row in range(self.height)]

        # Draw each index in said 2D array
        for row in range(self.height):
            for column in range(self.width):
                self.buttons[row][column].grid(row=row, column=column, sticky=NSEW)

        # Draw buttons for controls
        # Pause calls self.__pause__(), changing self.isPaused
        pauseButton = Button(text="Pause", command=lambda: self.__pause__())
        # Draw pauseButton below self.buttons
        pauseButton.grid(row=(height + 1), column=(int((width/2)+2)), columnspan=2)
        # Play calls self.__play__(), see self.isPaused
        playButton = Button(text="Play", command=lambda: self.__play__())
        # Draw playButton below self.buttons
        playButton.grid(row=(height + 1), column=(int(width/2)), columnspan=2)
        # Step calls self.__step__(), triggering update to next generation
        stepButton = Button(text="Step", command=lambda: self.__step__(currentGrid, nextGrid))
        # Draw stepButton below self.buttons
        stepButton.grid(row=(height + 1), column=(int(width/2)-2), columnspan=2)
        # Quit calls self.__quit__(), stopping outer simulation loop
        quitButton = Button(text="Quit", command=lambda: self.__quit__())
        # Draw quitButton 2 rows below self.buttons
        quitButton.grid(row=(height + 2), column=(int(width/2 - 1)), columnspan=2)
        # Clear calls self.__clear__(), setting all cells to 0
        clearButton = Button(text="Clear", command=lambda: self.__clear__(currentGrid))
        # Draw clearButton 2 rows below self.buttons
        clearButton.grid(row=(height + 2), column=(int(width/2) + 1), columnspan=2)

        # Definition of simulation state variables, see __pause__(), __play__(), __quit__()
        self.isOpen = 1
        self.isPaused = 1

    # Redraws grid with updated colors
    def __update__(self, grid):
        # Iterate through each cell and update the color
        for row in range(self.height):
            for column in range(self.width):
                self.buttons[row][column].config(bg=colors[grid.__get__(row, column)])
                self.buttons[row][column].grid(row=row, column=column)

    # Define toggle class, given coordinate, changes data in Grid object and updates display
    def __toggle__(self, grid, y, x):
        # If list index is 0 change to 1 and vice versa
        if grid.__get__(y, x) == 0:
            grid.__set__(y, x, 1)
        elif grid.__get__(y, x) == 1:
            grid.__set__(y, x, 0)

        self.__update__(grid)

    # Every time __step__() is called, update the grid 1 generation
    def __step__(self, currentGrid, nextGrid):
        # Iterate through all cells
        for row in range(self.height):
            for column in range(self.width):
                # Set the values in nextGrid to the output of Grid.__nextGen__() given said value
                nextGrid.__set__(row, column, currentGrid.__nextGen__(row, column))

        # Iterate through all cells
        for row in range(self.height):
            for column in range(self.width):
                # Now that nextGrid is created, copy it over the existing values in currentGrid
                currentGrid.__set__(row, column, nextGrid.__get__(row, column))

        # Redraw the grid
        self.__update__(currentGrid)

    # When called, set self.isPaused to 1, see controller.py line 38
    def __pause__(self):
        self.isPaused = 1

    # When called, sets self.isPaused to 0, see controller.py like 38
    def __play__(self):
        self.isPaused = 0

    # When called, sets self.isOpen to 0, will stop outer simulation loop, see controller.py line 36
    def __quit__(self):
        self.isOpen = 0

    # When called, iterate through all cells and set them to 0
    def __clear__(self, currentGrid):
        for row in range(self.height):
            for column in range(self.width):
                currentGrid.__set__(row, column, 0)

        # Update the GUI with changes
        self.__update__(currentGrid)
