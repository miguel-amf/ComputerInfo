import tkinter as tk
from tkinter import *
import subprocess

class MainWindow:
	window = tk.Tk()
	packstack = []
	formatTarget = tk.StringVar(window)
	def __init__(self) :
		self.window.title("BB HOUSE FOGUETE NAO TEM RE")
		return

	def _keyboardTestClick(self):
		#gotta run as a normal user else browser goes sad
		subprocess.run(['sudo','-u', 'mint', 'xdg-open', 'https://www.key-test.ru'])
	
	def setInfoSection(self, info = "NO INFO PARSED"):
		label = tk.Label(self.window, text=info, anchor="w", justify=LEFT)
		#label.pack(anchor='w', side= TOP)
		self.packstack.append(label)

	def setKeytestButton(self, parent = None):
		if parent is None:
			parent = self.window
		button = tk.Button(parent, text="GO TO KEYBOARD TEST", command=self._keyboardTestClick)
		if parent is not self.window :
			return button	
		self.packstack.append(button)

	def _setFormatButton(self, parent = None):
		if parent is None:
			parent = self.window
		button = tk.Button(parent, text="FormatDrive", command=self._keyboardTestClick)
		if parent is not self.window :
			return button	
		self.packstack.append(button)

	def run(self):
		for item in self.packstack:
			item.pack()
		self.window.mainloop()

	def setButtons(self):
		buttonFrame = tk.Frame(self.window)
		buttonKeytest = self._setKeytestButton(buttonFrame)
		buttonKeytest.grid(row=0, column=0)

		buttonFormat = self._setFormatButton(buttonFrame)
		buttonFormat.grid(row=0, column=1)
		self.packstack.append(buttonFrame)

	def setFormatDisks(self):
		formatFrame = tk.Frame(self.window)

		dropDown = tk.OptionMenu(formatFrame, self.formatTarget, "HDD1", "HDD2")
		self.formatTarget.set("HDD1")
		dropDown.grid(row=0, column=0)

		buttonFormat = self._setFormatButton(formatFrame)
		buttonFormat.grid(row=0, column=1)
		self.packstack.append(formatFrame)
