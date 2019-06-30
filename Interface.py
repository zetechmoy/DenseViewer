# -*- coding: utf-8 -*-
import sys, math

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon, QPainter, QBrush, QPen, QDrag, QPalette, QImage
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QAction, QGraphicsScene, QGraphicsView, QGraphicsItem, QToolBar, QInputDialog, QFileDialog, QDockWidget
from PyQt5.QtCore import Qt, QSize
from State import State
from keras.models import load_model

class DenseWindow(QMainWindow):#define new class derivated from QMAinWindow class
	def __init__(self):#initialisation function
		super().__init__()#attributes QMainWindow properties to the object
		screen = QApplication.desktop()
		screen_size = screen.screenGeometry()
		self.title="Dense Viewer"
		self.left=50
		self.top=50
		self.width= screen_size.width()
		self.height=screen_size.height()
		self.zoom = 1

		self.model = load_model('yacka_recsys_reg.h5')
		self.initUI()


	def initUI(self):
		self.setGeometry(self.left,self.top,self.width,self.height)

		#--------Graphic scene & view--------
		self.scene = QGraphicsScene()
		self.view = QGraphicsView(self.scene, self)
		self.painter = QPainter()
		self.painter.begin(self.view)
		self.view.setStyleSheet("background-color: rgb(250, 250, 250)")
		self.view.setDragMode(QGraphicsView.RubberBandDrag)
		self.setCentralWidget(self.view)

		self.setWindowTitle(self.title)

		self.showModel(self.model)

		self.show()

	def showModel(self, model):
		weights = model.get_weights()
		max_nb_of_node = max([len(layer) for layer in weights])
		for x in range(1, len(weights), 2):
			layer = weights[x]
			for y, weight in enumerate(layer):
				new_state = State(0, str(round(weight, 4)))
				new_state.setPos(x*75, y*75 + (max_nb_of_node-len(layer))*75/2)
				self.scene.addItem(new_state)

	def wheelEvent(self, event):
		'''Zoom In/Out with CTRL + mouse wheel'''
		if event.modifiers() == Qt.ControlModifier:
			self.zoom = math.pow(2.0, -event.angleDelta().y() / 240.0)
			self.view.scale(self.zoom, self.zoom)
			print("wheelEvent")
		else:
			return QGraphicsView.wheelEvent(self, event)
			print("wheelEvent2")

App = QApplication(sys.argv)
window = DenseWindow()
sys.exit(App.exec_())
