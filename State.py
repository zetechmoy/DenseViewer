from PyQt5.QtGui import QBrush, QPen, QColor, QFont
from PyQt5.QtWidgets import QLabel, QGraphicsEllipseItem, QGraphicsItem
from PyQt5.QtCore import QPointF, QRectF, Qt
import random

class State(QGraphicsItem):
	"""A class for managing States."""
	#parameters :
	def __init__(self, id = 0, label = '', radius = 30, color = (0, 0, 0), background_color = (255, 255, 255), contour = "simple"):
		super().__init__()
		self.id = id

		self.label = label
		self.radius = radius
		self.color = color
		self.background_color = background_color
		self.contour = contour
		self.rect = self.boundingRect()
		self.backgroundBrush = QBrush(QColor(self.background_color[0], self.background_color[1], self.background_color[2]))
		self.shapePen = QPen(QColor(self.color[0], self.color[1], self.color[2]))
		self.shapePen.setWidth(0.50)
		self.isfinal = False
		self.setPosition((random.randrange(10, 50), random.randrange(10, 50)))
		self.setFlag(QGraphicsItem.ItemIsMovable)
		self.setFlag(QGraphicsItem.ItemIsSelectable)
		self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
		self.setSelected(False)

	#CUSTOM QGRAPHICITEM
	def boundingRect(self):
		return QRectF(-self.radius, -self.radius, self.radius*2, self.radius*2)

	def paint(self, painter, option, widget):
		if self.isSelected():
			self.setColor((255,0,0))
		else:
			self.setColor()
		painter.setPen(self.shapePen)
		painter.setBrush(self.backgroundBrush)
		point = QPointF(0,0)
		painter.drawEllipse(point, self.radius, self.radius)
		if self.isfinal :
			painter.drawEllipse(point, self.radius -5, self.radius -5)
		#print(self.rect)
		font = QFont()
		font.setPointSize(5)
		painter.setFont(font)
		painter.drawText(self.rect, Qt.AlignCenter ,self.label)

	def itemChange(self, change, value):
		if change == QGraphicsItem.ItemPositionHasChanged:
			self.setPos(value)
		return super(State, self).itemChange(change, value)

	#SETTERS
	def setLabel(self, label=""):
		self.label = label

	def setRadius(self, radius=0):
		self.radius = radius

	def setPosition(self, position=(0, 0)):
		#self.pos = QPointF(position[0], position[1])
		#self.rect = QRectF(self.pos().x(), self.pos().y(), self.radius, self.radius)
		#self.move(self.pos().x()+position[0], self.pos().y()+position[1])
		self.setPos(position[0], position[1])

	def setColor(self, color=(0, 0, 0)):
		self.color = color
		self.shapePen = QPen(QColor(self.color[0], self.color[1], self.color[2]))
		self.shapePen.setWidth(1.80)

	def setBackgroundColor(self, color=(0, 0, 0)):
		self.background_color = color
		self.backgroundBrush = QBrush(QColor(self.background_color[0], self.background_color[1], self.background_color[2]))

	def setContour(self, contour="simple"):
		self.contour = contour

	def setFinal(self):
		if self.isfinal :
			self.isfinal = False
		else :
			self.isfinal = True
		self.update()

	#GETTERS
	def getLabel(self):
		return self.label

	def getRadius(self):
		return self.radius

	def getPosition(self):
		return self.pos()

	def getColor(self):
		return self.color

	def getBackgroundColor(self):
		return self.background_color

	def getCoutour(self):
		return self.contour


	#TOOLS
	def showInfos(self):
		print("id : " + str(self.id))
		print("label : " + str(self.label))
		print("radius : " + str(self.radius))
		print("position : " + str(self.pos()))
		print("color : " + str(self.color))
		print("background_color : " + str(self.background_color))
		print("contour : " + str(self.contour))
