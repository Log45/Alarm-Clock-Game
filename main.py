from tkinter import *
from tkinter import messagebox
import random as rand

print("For the best experience, select\nthe same number of rows as columns.\n(The higher the number, "
      "the harder the game will be).")

score_limit = 5

row_length = int(input("How many rows?"))
column_length = int(input("How many columns?"))
number_of_buttons_var = row_length * column_length

font = ("Times", 20)


def return_button(button):
  return Button(
    width = 16,
    height = 8,
    command = lambda: check_press(button),
    bg="Gray"
  )


# This list is used to store the number of buttons that will be on the GUI.
# This is later called by the for loop that creates the buttons; the amount of values
# in this list determines the amount of buttons on the stage, each value can also act
# as a label for which button is which on the screen.
Number_of_Buttons = []
i = 1
# Using a while loop allows me to change how many buttons are in the game
while i <= number_of_buttons_var:
  Number_of_Buttons.append(i)
  i+=1


def change_color(random_button):
  Buttons[random_button].config(bg="gray")


score = 0


def update_score():
  global score
  score += 1
  score_label.config(text="Score: " + str(score))


# This list is used to store the buttons that are randomly selected to be red.
# This list and its values are used to determine if the buttons presed are the same as the red buttons.
Red_Buttons = []


def random_red():
  Button_list = list(Buttons)
  if len(buttons_pressed) == len(buttons_to_press) or len(buttons_pressed) == 0 or len(buttons_pressed) == 1:
    if score <= score_limit:
      random_button = rand.randint(0, (number_of_buttons_var))
      red_button = Buttons[random_button]
      Red_Buttons.append(red_button)
      Buttons[random_button].config(bg="red")
      root.after(1000, lambda: change_color(random_button))
    else:
      print("You win!!")
      exit()
  else:
    print("keep going")


def check_press(button):
  buttons_to_press = Red_Buttons
  print(f"Button {button} pressed.")
  global button_int
  button_int = button
  pressed_button_var = Buttons[button_int]
  buttons_pressed.append(pressed_button_var)
  if buttons_pressed[-1] == buttons_to_press[len(buttons_pressed)-1]:
    if len(buttons_pressed) == len(buttons_to_press):
      buttons_pressed.clear()
      update_score()
      random_red()
  else:
    print("You Lose!")
    exit()


def start():
  print("start")
  random_red()


root = Tk()
root.title("WAKE UP!!!")

# The idea of using a for loop to distinguish each button is also thanks to Alexander Day,
# I have made changes to it by adding "row_var", "column_var", and by using an if statement
# to determine the coordinates of the buttons.
Buttons = {}  # this is a dictionary to store the buttons created by the return_button function
row_var = 2  # this value determines the starting row of the GUI for the buttons
column_var = 0  # this value determines the starting column of the GUI for the buttons

# This for loop takes the Number_of_Buttons list and creates a button for each of the values in that list.
for button in Number_of_Buttons:
  Buttons[button] = return_button(button)
  Buttons[button].grid(row=row_var, column=column_var)
  column_var += 1
  if column_var == column_length:
    row_var += 1
    column_var = 0

score_label = Label(text="Score: "+str(score), font=font)
score_label.grid(row=0, column=0, columnspan=column_length)

Start_Button = Button(text="Start", font=font, bg="Gray", command=start)
Start_Button.grid(row=1, column=0, columnspan=column_length)

# This list stores the values of the buttons that are pressed.
buttons_pressed = []
buttons_to_press = []

messagebox.showinfo(title="instructions", message="Good Morning! To play: Press start and wait for a square to flash "
                                                  "red. You must press the squares in the sequence in which they "
                                                   "flashed. If you see any red pop up in the console, you must start "
                                                   "the sequence again from the beginning. Please wait a second"
                                                   " between each press to ensure that it is processed.")

root.mainloop()
