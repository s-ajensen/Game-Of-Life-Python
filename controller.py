# Controller for Conway's Game of Life Final Project, Samuel Jensen, 11/20/2017

import view
import model
import tkinter
import time


# Function encapsulating the event loop
def simLoop():
    # Instantiate the Tk class as the main window
    root = tkinter.Tk()
    # Set window dimensions and position
    root.geometry("325x100+300+300")

    # Instantiate the Prompt window
    prompt = view.Prompt()
    # Start the tkinter event loop
    root.mainloop()
    # Once data is submitted and window is closed, generate lists from inputted data
    # currentGen will be the list interacted with
    currentGen = model.Grid(prompt.verticalCells, prompt.horizontalCells)
    # nextGen will be the list which is generated from parsing currentGen
    nextGen = model.Grid(prompt.verticalCells, prompt.horizontalCells)

    # Instantiate the Tk class as new main window
    grid = tkinter.Tk()

    # Instantiate the GridDisplay window
    gridDisplay = view.GridDisplay(prompt.verticalCells, prompt.horizontalCells, currentGen, nextGen)

    # Draw the grid window
    gridDisplay.grid()

    # While the quit button hasn't been pressed
    while gridDisplay.isOpen == 1:
        # Check if the sim is paused
        if gridDisplay.isPaused != 1:
            # If not then step through to next generation every 0.4 seconds
            gridDisplay.__step__(currentGen, nextGen)
            gridDisplay.grid()
            time.sleep(0.4)
        # If so then display the gridDisplay GUI which checks for user input
        gridDisplay.grid()
        # Run tkinter eventloop checks
        grid.update_idletasks()
        grid.update()
