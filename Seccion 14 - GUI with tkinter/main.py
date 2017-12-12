from tkinter import *


window=Tk()

def km_to_mile():
	miles = float(gui.e1_value.get())*1.606
	gui.t1.insert(END, miles)

def kg_To_Gram(value):
	return value*1000

def kg_To_Pound(value):
	return value*2.20462

def kg_To_Ounce(value):
	return value*35.274

def convert_Input():
	kgs_value = float(gui.e1_value.get())
	grams = kg_To_Gram(kgs_value)
	pounds = kg_To_Pound(kgs_value)
	ounces = kg_To_Ounce(kgs_value)
	
	gui.grams.insert(END, grams)
	gui.pounds.insert(END, pounds)
	gui.ounces.insert(END, ounces)
	
	
	
class UI:
	def __init__(self):
		
		self.t1=Label(window, height=1, width=20, text="Kg")
		self.t1.grid(row=0, column=0)
		
		self.e1_value = StringVar()
		self.e1=Entry(window,textvariable=self.e1_value)
		self.e1.grid(row=0, column=1)
		
		self.b1=Button(window, text="Execute", command=convert_Input)
		self.b1.grid(row=0, column=2)
		
		#grams
		self.grams=Entry(window)
		self.grams.grid(row=1, column=0)
		
		#pounds
		self.pounds=Entry(window)
		self.pounds.grid(row=1, column=1)
		
		#ounces
		self.ounces=Entry(window)
		self.ounces.grid(row=1, column=2)
		
		
		
		

def main():
	global gui 
	gui = UI()
	window.mainloop()
	
	
main()
