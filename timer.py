# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# Window settings
		self.title = "Timer"
		self.left = 100
		self.top = 100
		self.width = 400
		self.height = 600

		# count variable
		self.counter = 0
		# start flag
		self.start = False

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		self.setGeometry(self.left, self.top, self.width, self.height)
		self.setWindowTitle(self.title)

		# creating push button to get time in seconds
		button = QPushButton("Set time(s)", self)

		# setting geometry to the push button
		button.setGeometry(125, 100, 150, 50)

		# adding action to the button
		button.clicked.connect(self.get_minutes)

		# creating label to show the seconds
		self.label = QLabel("Set time", self)

		# setting geometry of label
		self.label.setGeometry(100, 200, 200, 50)

		# setting border to the label
		self.label.setStyleSheet("border : 3px solid black")

		# setting font to the label
		self.label.setFont(QFont('Times', 15))

		# setting alignment ot the label
		self.label.setAlignment(Qt.AlignCenter)

		# creating start button
		start_button = QPushButton("Start", self)

		# setting geometry to the button
		start_button.setGeometry(125, 350, 150, 40)

		# adding action to the button
		start_button.clicked.connect(self.start_action)

		# creating pause button
		pause_button = QPushButton("Pause", self)

		# setting geometry to the button
		pause_button.setGeometry(125, 400, 150, 40)

		# adding action to the button
		pause_button.clicked.connect(self.pause_action)

		# creating reset button
		reset_button = QPushButton("Reset", self)

		# setting geometry to the button
		reset_button.setGeometry(125, 450, 150, 40)

		# adding action to the button
		reset_button.clicked.connect(self.reset_action)

		# creating a timer object
		self.timer = QtCore.QTimer()
		self.time = QtCore.QTime(0,0,0)
		print(type(self.time))
		# adding action to timer
		self.timer.timeout.connect(self.showTime)

		# update the timer every second
		self.timer.start(1000)

	# method called by timer
	def showTime(self):

		# checking if flag is true
		if self.start:
			# incrementing the counter
			self.time = self.time.addSecs(-1)

			# timer is completed
			if self.time == QtCore.QTime(0,0,0):
				print("Done")

				# making flag false
				self.start = False
				self.counter += 1
				print("Complete number {}".format(counter))
				# setting text to the label
				self.label.setText("Completed !!!! ")

		if self.start:
			# showing text
			self.label.setText(self.time.toString("hh:mm:ss"))


	# method called by the push button
	def get_minutes(self):

		# making flag false
		self.start = False

		# getting minutes and flag
		minutes, done = QInputDialog.getInt(self, 'Minutes', 'Enter Minutes:')

		# if flag is true
		if done:
			# changing the value of count
			print("Done check")
			print(type(self.time))
			self.count = minutes * 600
			self.time = self.time.addSecs(minutes * 60)

			# setting text to the label
			print("Add time = " + str(minutes * 60))
			print(self.time.toString("hh:mm:ss"))

			self.label.setText(self.time.toString("hh:mm:ss"))

	def start_action(self):
		print("button clicked")

		# making flag true
		self.start = True
		# self.time.start()

		# count = 0
		if self.count == 0:
			self.start = False

	def pause_action(self):

		# making flag false
		self.start = False

	def reset_action(self):

		# making flag false
		self.start = False

		# setting count value to 0
		self.count = 0
		self.time = QtCore.QTime(0,0,0)

		# setting label text
		self.label.setText("##TIME##")

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
