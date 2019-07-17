# Patrick Vanegas - Final project

from tkinter import *
import frequency
import turtle
import math
import random

# intitalize a blank window
root = Tk() 

# initialize turtle window
window = turtle.Screen()  

# Create widgets to be viewed on the Tkinter window
label_1 = Label(root, text = "Enter a number less than 54 to get the Nth most frequent letters in Words.txt: ")
entry = Entry(root)

def drawPieChart(central_angles, angle_of_rest, probability_of_rest):
  # reset turtle to redraw the piechart if the user enters a new value for N.
  turtle.reset()

  # set color mode to accept rgb values
  window.colormode(255)
  turtle.fillcolor('gray')
  turtle.speed(10)

  # draw base circle and fill it with color
  turtle.begin_fill()
  turtle.circle(120)
  turtle.end_fill()
  turtle.up()

  angle_counter = 0
  prev_angle = 0

  # draw arc sectors for each probability in the circle
  for index, (letter, angle, probability) in enumerate(central_angles):
    if index == 0:
      # turn radians to degrees
      angle_counter += angle * (360 / math.pi) 
    turtle.fillcolor((random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    turtle.begin_fill()
    turtle.goto(x = 0, y = 120)
    turtle.setheading(angle_counter)
    angle_counter += angle * (360 / math.pi)
    turtle.forward(120)
    turtle.right(270)
    turtle.circle(120, angle * (360 / math.pi))
    turtle.setheading(angle_counter)
    turtle.forward(50)
    turtle.write('{}, {}'.format(letter, round(probability, 3)), font = ("Arial", 10, "normal"))
    turtle.backward(50)
    turtle.setheading(angle * (360 / math.pi) + prev_angle)
    turtle.goto(x = 0, y = 120)
    turtle.end_fill()
    prev_angle += angle_counter

    # draw the arc for the remaining probabilites.
    if index == len(central_angles) - 1:
      turtle.fillcolor('gray')
      turtle.begin_fill()
      turtle.goto(x = 0, y = 120)
      turtle.setheading(angle_counter)
      turtle.forward(120)
      turtle.right(270)
      turtle.circle(120, angle_of_rest * (180 / math.pi) )
      angle_counter += angle_of_rest * (180 / math.pi)
      turtle.setheading(angle_counter)
      turtle.forward(50)
      turtle.write('All other letters, {}'.format(round(probability_of_rest, 3)), font = ("Arial", 10, "normal"))
      turtle.backward(50)
      turtle.setheading(angle_of_rest * (180 / math.pi) + prev_angle)
      turtle.goto(x = 0, y = 120)
      turtle.end_fill()

def calculateFrequencies(arg = None):
  # get the text value from the entry field
  # if the value is not a valid integer, simply return and do nothing.
  try:
    result = int(entry.get())

    # return if the input is greater than 54
    if (result >= 54):
      return
    
    # delete the text in the entry field
    entry.delete(0, END)

    # calculate the most frequent characters
    most_frequent_characters = frequency.getNthMostFrequentCharacters(result)

    # calculate the probability of all other letters not included in the top N.
    probability_of_other_characters = frequency.sumOfAllOtherProbabilites(most_frequent_characters)

    # calculate the central angle of the rest of the letters.
    angle_of_rest = probability_of_other_characters * 2 * math.pi

    # calculate central angles of the most frequenct character's probabilities
    central_angles = frequency.getCentralAngles(most_frequent_characters)

    # draw pie chart
    drawPieChart(central_angles, angle_of_rest, probability_of_other_characters)
  except ValueError:
    return 
  
# When the user presses enter on the entry field, calculate frequencies
entry.bind('<Return>', calculateFrequencies)

# Position widgets on a grid layout
label_1.grid(row=0)
entry.grid(row=0, column=1)

# keep both the turtle and tkinter windows open until user presses the close button on either
root.mainloop() 
window.exitonclick()
