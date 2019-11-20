# import everything from tkinter module 
import random, string
from tkinter import *    

# create a tkinter window 
root = Tk()               
root.title('Samuel\'s Random Password Generator')

passwordTextBoxLabel = Label(root, text="Password Length: ")
passwordTextBoxLabel.place(x = 15, y = 15)

entryBox = Entry(root)
entryBox.place(x = 115, y = 15)

def InputNumber():
	theInput = entryBox.get()
	try:
		theInput = int(theInput)
	except:
		passwordContent.set("That's an invalid input! Please enter a valid number for the lenght of your password.")
	if(theInput > 127):
		passwordContent.set("Oops! Sorry. That password is a bit unwieldy. Try a number below 128")
	elif(theInput < 8):
		passwordContent.set("Oops! Sorry. That password is too short to be secure. Try a longer password.")
	else:
		return theInput

def StringGenerator():
	listOfLetters = []
	letter = "a"
	passwordString = ""

	for i in range(InputNumber()):
		letter = random.choice(string.printable)
		while(letter == "\n" or letter == " " or letter == "\t" or letter == "\r" or letter == "\x0b" or letter == "\x0c"):
			letter = random.choice(string.printable)
		listOfLetters.append(letter)
		passwordString = ''.join(listOfLetters)
		passwordContent.set(passwordString)

# Open window having dimension 900x200 
root.geometry('900x200')  

# Create a Button 
btn = Button(root, text = 'Generate Password', bd = '5', command=StringGenerator)  

# Set the position of button on the top of window.    
btn.place(x = 15, y = 45)

instructions = "This program will generate a password composed of random characters. Please enter the password\'s desired lenght in the textbox above."
passwordContent = StringVar(root, value = instructions)
passwordLabel = Entry(root, textvariable=passwordContent)
passwordLabel.place(x = 15, y = 90, height = 80, width = 850)

root.mainloop() 