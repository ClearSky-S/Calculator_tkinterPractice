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
	app.geometry("490x500")

	titleFrame = Frame(app, relief="solid", bg='grey15')
	titleFrame.pack(side="top", fill="both", expand=True)
	inputFrame = Frame(app, relief="solid", bg='grey15')
	inputFrame.pack(side="top", fill="both",padx=10, pady=10)



	# create the text entry box for
	# showing the expression .
	expression_field = Entry(titleFrame, font=("Arial",30),fg='white', bg='grey15',relief=FLAT,insertbackground='white')

	expression_field.pack(fill="both", expand=True, padx=20)

	# create a Buttons and place at a particular
	# location inside the root window .
	# when user press the button, the command or
	# function affiliated to that button is executed .
	button1 = Button(inputFrame, text=' 1 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(1), height=2, width=10, font=("Arial",15))
	button1.grid(row=2, column=0, padx=1, pady=1)


	button2 = Button(inputFrame, text=' 2 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(2), height=2, width=10, font=("Arial",15))
	button2.grid(row=2, column=1, padx=1, pady=1)


	button3 = Button(inputFrame, text=' 3 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(3), height=2, width=10, font=("Arial",15))
	button3.grid(row=2, column=2, padx=1, pady=1)


	button4 = Button(inputFrame, text=' 4 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(4), height=2, width=10, font=("Arial",15))
	button4.grid(row=3, column=0, padx=1, pady=1)


	button5 = Button(inputFrame, text=' 5 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(5), height=2, width=10, font=("Arial",15))
	button5.grid(row=3, column=1, padx=1, pady=1)


	button6 = Button(inputFrame, text=' 6 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(6), height=2, width=10, font=("Arial",15))
	button6.grid(row=3, column=2, padx=1, pady=1)


	button7 = Button(inputFrame, text=' 7 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(7), height=2, width=10, font=("Arial",15))
	button7.grid(row=4, column=0, padx=1, pady=1)


	button8 = Button(inputFrame, text=' 8 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(8), height=2, width=10, font=("Arial",15))
	button8.grid(row=4, column=1, padx=1, pady=1)


	button9 = Button(inputFrame, text=' 9 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(9), height=2, width=10, font=("Arial",15))
	button9.grid(row=4, column=2, padx=1, pady=1)


	button0 = Button(inputFrame, text=' 0 ', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press(0), height=2, width=10, font=("Arial",15))
	button0.grid(row=5, column=0, padx=1, pady=1)


	plus = Button(inputFrame, text=' + ', fg='white', bg='grey8', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
				command=lambda: press("+"), height=2, width=10, font=("Arial",15))
	plus.grid(row=2, column=3, padx=1, pady=1)


	minus = Button(inputFrame, text=' - ', fg='white', bg='grey8', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
				command=lambda: press("-"), height=2, width=10, font=("Arial",15))
	minus.grid(row=3, column=3, padx=1, pady=1)


	multiply = Button(inputFrame, text=' * ', fg='white', bg='grey8', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press("*"), height=2, width=10, font=("Arial",15))
	multiply.grid(row=4, column=3, padx=1, pady=1)


	divide = Button(inputFrame, text=' / ', fg='white', bg='grey8', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
					command=lambda: press("/"), height=2, width=10, font=("Arial",15))
	divide.grid(row=5, column=3, padx=1, pady=1)

	equal = Button(inputFrame, text=' = ', fg='white', bg='grey25', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
				command=equalpress, height=2, width=10, font=("Arial",15))
	equal.grid(row=5, column=2, padx=1, pady=1)
	app.bind("<Return>", equalpress)

	clear = Button(inputFrame, text='Clear', fg='white', bg='black', relief=FLAT, activebackground = 'gray30',  activeforeground = 'white',
				command=clear, height=2, width=10, font=("Arial",15))
	clear.grid(row=5, column=1, padx=1, pady=1)



	# start the inputFrame
	app.mainloop()
