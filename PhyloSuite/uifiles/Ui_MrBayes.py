# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\codes\PhyloSuite\uifiles\MrBayes.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MrBayes(object):
    def setupUi(self, MrBayes):
        MrBayes.setObjectName("MrBayes")
        MrBayes.resize(574, 636)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(MrBayes)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(MrBayes)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 556, 618))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit = InputQLineEdit(self.groupBox_4)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.label_9 = ClickedLableGif(self.groupBox_4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.comboBox_5 = CheckableComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_2.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setToolTip("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout.addWidget(self.comboBox_7, 0, 1, 1, 1)
        self.pushButton_partition = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_partition.sizePolicy().hasHeightForWidth())
        self.pushButton_partition.setSizePolicy(sizePolicy)
        self.pushButton_partition.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/pie-chart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_partition.setIcon(icon)
        self.pushButton_partition.setCheckable(True)
        self.pushButton_partition.setObjectName("pushButton_partition")
        self.gridLayout.addWidget(self.pushButton_partition, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_10.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout.addWidget(self.comboBox_10, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_2.addWidget(self.label_28)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setMinimum(2)
        self.spinBox.setMaximum(64)
        self.spinBox.setProperty("value", 4)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 2, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 3, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout.addWidget(self.comboBox_6, 3, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setWrapping(True)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(999999999)
        self.spinBox_2.setSingleStep(1)
        self.spinBox_2.setProperty("value", 2000000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_4.addWidget(self.spinBox_2, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 3, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(99999999)
        self.spinBox_6.setProperty("value", 100)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout_4.addWidget(self.spinBox_6, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 2)
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy)
        self.spinBox_7.setWrapping(True)
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(9999)
        self.spinBox_7.setSingleStep(1)
        self.spinBox_7.setProperty("value", 2)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout_4.addWidget(self.spinBox_7, 1, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 3, 1, 2)
        self.spinBox_8 = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy)
        self.spinBox_8.setWrapping(True)
        self.spinBox_8.setMinimum(1)
        self.spinBox_8.setMaximum(9999)
        self.spinBox_8.setSingleStep(1)
        self.spinBox_8.setProperty("value", 4)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout_4.addWidget(self.spinBox_8, 1, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.buttonGroup = QtWidgets.QButtonGroup(MrBayes)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox)
        self.gridLayout_4.addWidget(self.checkBox, 2, 0, 1, 2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_2.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_2.setSizePolicy(sizePolicy)
        self.doubleSpinBox_2.setMaximum(1.0)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setProperty("value", 0.25)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 2, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup.addButton(self.checkBox_2)
        self.gridLayout_4.addWidget(self.checkBox_2, 2, 3, 1, 1)
        self.spinBox_10 = QtWidgets.QSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_10.sizePolicy().hasHeightForWidth())
        self.spinBox_10.setSizePolicy(sizePolicy)
        self.spinBox_10.setWrapping(True)
        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(999999999)
        self.spinBox_10.setSingleStep(1)
        self.spinBox_10.setProperty("value", 250)
        self.spinBox_10.setObjectName("spinBox_10")
        self.gridLayout_4.addWidget(self.spinBox_10, 2, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 3, 3, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_8, 3, 2, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_9, 3, 5, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = ArrowPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_continue = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_continue.sizePolicy().hasHeightForWidth())
        self.pushButton_continue.setSizePolicy(sizePolicy)
        self.pushButton_continue.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_continue.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/Play-pause_button_play_stop_blue_pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_continue.setIcon(icon2)
        self.pushButton_continue.setAutoExclusive(False)
        self.pushButton_continue.setObjectName("pushButton_continue")
        self.gridLayout_3.addWidget(self.pushButton_continue, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/picture/resourses/Eye_Care_Services-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_2 = ArrowPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_6 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setIcon(icon3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)

        self.retranslateUi(MrBayes)
        self.pushButton_partition.toggled['bool'].connect(self.comboBox_7.setDisabled)
        self.checkBox_4.toggled['bool'].connect(self.comboBox_10.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MrBayes)
        MrBayes.setTabOrder(self.pushButton_3, self.pushButton_9)
        MrBayes.setTabOrder(self.pushButton_9, self.lineEdit)
        MrBayes.setTabOrder(self.lineEdit, self.pushButton_2)
        MrBayes.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, MrBayes):
        _translate = QtCore.QCoreApplication.translate
        MrBayes.setWindowTitle(_translate("MrBayes", "MrBayes"))
        self.groupBox_4.setTitle(_translate("MrBayes", "Input"))
        self.label_5.setText(_translate("MrBayes", "Alignment File:"))
        self.lineEdit.setPlaceholderText(_translate("MrBayes", "The file should be NEXUS format"))
        self.label_31.setText(_translate("MrBayes", "Outgroup(s):"))
        self.label_14.setText(_translate("MrBayes", "<html><head/><body><p>Click <a href=\"http://mrbayes.sourceforge.net/\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a> to learn more about <span style=\" font-weight:600; color:#ff0000;\">MrBayes</span></p></body></html>"))
        self.checkBox_3.setText(_translate("MrBayes", "Save Log"))
        self.label_9.setToolTip(_translate("MrBayes", "Brief example"))
        self.groupBox.setTitle(_translate("MrBayes", "Parameters"))
        self.label_25.setText(_translate("MrBayes", "Models:"))
        self.pushButton_partition.setText(_translate("MrBayes", "Partition Models"))
        self.checkBox_4.setText(_translate("MrBayes", "Threads:"))
        self.label_28.setText(_translate("MrBayes", "Gamma categories:"))
        self.label_26.setText(_translate("MrBayes", "State freq:"))
        self.comboBox_4.setItemText(0, _translate("MrBayes", "dirichlet(1.0,1.0,1.0,1.0)"))
        self.comboBox_4.setItemText(1, _translate("MrBayes", "fixed(equal)"))
        self.comboBox_4.setItemText(2, _translate("MrBayes", "fixed(empirical)"))
        self.label_27.setToolTip(_translate("MrBayes", "Rate Variation"))
        self.label_27.setText(_translate("MrBayes", "Rate Var.:"))
        self.comboBox_6.setItemText(0, _translate("MrBayes", "equal (No rate variation across sites)"))
        self.comboBox_6.setItemText(1, _translate("MrBayes", "gamma (+G, Gamma-distributed variation)"))
        self.comboBox_6.setItemText(2, _translate("MrBayes", "lnorm (Log Normal-distributed variation)"))
        self.comboBox_6.setItemText(3, _translate("MrBayes", "propinv (+I, Proportion of sites invariable)"))
        self.comboBox_6.setItemText(4, _translate("MrBayes", "invgamma (+I+G, Proportion invariable, remaining gamma)"))
        self.comboBox_6.setItemText(5, _translate("MrBayes", "adgamma (Autocorrelated variation)"))
        self.groupBox_5.setTitle(_translate("MrBayes", "MCMC Settings"))
        self.label.setText(_translate("MrBayes", "Generations:"))
        self.label_2.setText(_translate("MrBayes", "Sampling Freq:"))
        self.label_3.setText(_translate("MrBayes", "Number of Runs:"))
        self.label_4.setText(_translate("MrBayes", "Number of Chains:"))
        self.checkBox.setText(_translate("MrBayes", "Burnin Fraction:"))
        self.checkBox_2.setText(_translate("MrBayes", "Burnin:"))
        self.label_6.setToolTip(_translate("MrBayes", "Type of consensus tree"))
        self.label_6.setText(_translate("MrBayes", "Contype:"))
        self.label_7.setToolTip(_translate("MrBayes", "Format of consensus tree"))
        self.label_7.setText(_translate("MrBayes", "Conformat:"))
        self.comboBox_8.setItemText(0, _translate("MrBayes", "Halfcompat"))
        self.comboBox_8.setItemText(1, _translate("MrBayes", "Allcompat"))
        self.comboBox_9.setItemText(0, _translate("MrBayes", "Simple"))
        self.comboBox_9.setItemText(1, _translate("MrBayes", "Figtree"))
        self.groupBox_3.setTitle(_translate("MrBayes", "Run"))
        self.pushButton.setText(_translate("MrBayes", "Start"))
        self.pushButton_continue.setText(_translate("MrBayes", "Continue Previous Analysis"))
        self.pushButton_10.setText(_translate("MrBayes", "Show MrBayes Data Block"))
        self.pushButton_2.setText(_translate("MrBayes", "Stop"))
        self.groupBox_6.setTitle(_translate("MrBayes", "Progress"))
        self.label_8.setText(_translate("MrBayes", "Bayesian inference"))
        self.pushButton_9.setText(_translate("MrBayes", "Show log"))

from src.CustomWidget import ArrowPushButton, CheckableComboBox, ClickedLableGif, InputQLineEdit
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MrBayes = QtWidgets.QDialog()
    ui = Ui_MrBayes()
    ui.setupUi(MrBayes)
    MrBayes.show()
    sys.exit(app.exec_())
