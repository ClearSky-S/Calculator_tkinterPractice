# Python program to create a simple inputFrame
# calculator using Tkinter


# import everything from tkinter module
from tkinter import *
from tkinter import messagebox



# Function to update expressiom
# in the text entry box
def press(num):
	expression_field.insert(len(expression_field.get()),str(num))
	expression_field.icursor(len(expression_field.get()))  # reset cursor to the end

# Function to evaluate the final expression
def equalpress(event=None):

	# Try and except statement is used
	# for handling the errors like zero
	# division error etc.


	# Put that code inside the try block
	# which may generate the error
	try:

		exp = expression_field.get()
		print(exp)
		expression_field.delete(0, len(expression_field.get()))
		expression_field.insert(0,str(eval(exp)))
		print(eval(exp))



	# if error is generate then handle
	# by the except block
	except:
		messagebox.showerror("Error", "Invalid Input")




# Function to clear the contents
# of text entry box
def clear():
	expression_field.delete(0, len(expression_field.get()))





# Driver code
if __name__ == "__main__":
	# create a inputFrame window
	app = Tk()


	# set the background colour of inputFrame window
	app.configure(background="grey15")


	# set the title of inputFrame window
	app.title("Simple Calculator")


	# set the configuration of inputFrame window
	app.geometry("180x150")

	titleFrame = Frame(app)
	titleFrame.pack()
	inputFrame = Frame(app)
	inputFrame.pack()




	# create the text entry box for
	# showing the expression .
	expression_field = Entry(titleFrame)
	expression_field.pack()

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(inputFrame, text=' 1 ',	command=lambda: press(1))
	button1.grid(row=2, column=0)


	button2 = Button(inputFrame, text=' 2 ',	command=lambda: press(2))
	button2.grid(row=2, column=1)


	button3 = Button(inputFrame, text=' 3 ',	command=lambda: press(3))
	button3.grid(row=2, column=2)


	button4 = Button(inputFrame, text=' 4 ',	command=lambda: press(4))
	button4.grid(row=3, column=0)


	button5 = Button(inputFrame, text=' 5 ',	command=lambda: press(5))
	button5.grid(row=3, column=1)


	button6 = Button(inputFrame, text=' 6 ',	command=lambda: press(6))
	button6.grid(row=3, column=2)


	button7 = Button(inputFrame, text=' 7 ',	command=lambda: press(7))
	button7.grid(row=4, column=0)


	button8 = Button(inputFrame, text=' 8 ',	command=lambda: press(8))
	button8.grid(row=4, column=1)


	button9 = Button(inputFrame, text=' 9 ',	command=lambda: press(9))
	button9.grid(row=4, column=2)


	button0 = Button(inputFrame, text=' 0 ',	command=lambda: press(0))
	button0.grid(row=5, column=0)


	plus = Button(inputFrame, text=' + ',command=lambda: press("+"))
	plus.grid(row=2, column=3)


	minus = Button(inputFrame, text=' - ',command=lambda: press("-"))
	minus.grid(row=3, column=3)


	multiply = Button(inputFrame, text=' * ',	command=lambda: press("*"))
	multiply.grid(row=4, column=3)


	divide = Button(inputFrame, text=' / ',	command=lambda: press("/"))
	divide.grid(row=5, column=3)

	equal = Button(inputFrame, text=' = ',	command=equalpress)
	equal.grid(row=5, column=2)
	app.bind("<Return>", equalpress)

	clear = Button(inputFrame, text='Clear',command=clear)
	clear.grid(row=5, column=1)



	# start the inputFrame
	app.mainloop()
