# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_settingsWindowWidget(object):
    def setupUi(self, settingsWindowWidget):
        settingsWindowWidget.setObjectName("settingsWindowWidget")
        settingsWindowWidget.resize(587, 455)
        self.filterTab = QtWidgets.QWidget()
        self.filterTab.setObjectName("filterTab")
        self.filterWidget = QtWidgets.QWidget(self.filterTab)
        self.filterWidget.setGeometry(QtCore.QRect(-1, -1, 581, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filterWidget.sizePolicy().hasHeightForWidth())
        self.filterWidget.setSizePolicy(sizePolicy)
        self.filterWidget.setObjectName("filterWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.filterWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.applyFilterButton = QtWidgets.QPushButton(self.filterWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applyFilterButton.sizePolicy().hasHeightForWidth())
        self.applyFilterButton.setSizePolicy(sizePolicy)
        self.applyFilterButton.setObjectName("applyFilterButton")
        self.gridLayout.addWidget(self.applyFilterButton, 4, 4, 1, 1)
        self.totalTimeLabel = QtWidgets.QLabel(self.filterWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTimeLabel.sizePolicy().hasHeightForWidth())
        self.totalTimeLabel.setSizePolicy(sizePolicy)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.gridLayout.addWidget(self.totalTimeLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 5)
        self.compareTotalTimeDropdown = QtWidgets.QComboBox(self.filterWidget)
        self.compareTotalTimeDropdown.setObjectName("compareTotalTimeDropdown")
        self.compareTotalTimeDropdown.addItem("")
        self.compareTotalTimeDropdown.addItem("")
        self.gridLayout.addWidget(self.compareTotalTimeDropdown, 0, 1, 1, 1)
        self.totalTimeField = QtWidgets.QLineEdit(self.filterWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTimeField.sizePolicy().hasHeightForWidth())
        self.totalTimeField.setSizePolicy(sizePolicy)
        self.totalTimeField.setObjectName("totalTimeField")
        self.gridLayout.addWidget(self.totalTimeField, 0, 2, 1, 1)
        self.activeTotalTimeCheckbox = QtWidgets.QCheckBox(self.filterWidget)
        self.activeTotalTimeCheckbox.setObjectName("activeTotalTimeCheckbox")
        self.gridLayout.addWidget(self.activeTotalTimeCheckbox, 0, 3, 1, 1)
        settingsWindowWidget.addTab(self.filterTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.settingsWidget = QtWidgets.QWidget(self.settingsTab)
        self.settingsWidget.setGeometry(QtCore.QRect(-1, -1, 581, 431))
        self.settingsWidget.setObjectName("settingsWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.thresholdLabel = QtWidgets.QLabel(self.settingsWidget)
        self.thresholdLabel.setObjectName("thresholdLabel")
        self.gridLayout_2.addWidget(self.thresholdLabel, 1, 0, 1, 1)
        self.thresholdField = QtWidgets.QLineEdit(self.settingsWidget)
        self.thresholdField.setClearButtonEnabled(True)
        self.thresholdField.setObjectName("thresholdField")
        self.gridLayout_2.addWidget(self.thresholdField, 1, 1, 1, 1)
        self.applySettingsButton = QtWidgets.QPushButton(self.settingsWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.applySettingsButton.sizePolicy().hasHeightForWidth())
        self.applySettingsButton.setSizePolicy(sizePolicy)
        self.applySettingsButton.setObjectName("applySettingsButton")
        self.gridLayout_2.addWidget(self.applySettingsButton, 4, 2, 1, 1)
        self.nsPerFrameField = QtWidgets.QLineEdit(self.settingsWidget)
        self.nsPerFrameField.setClearButtonEnabled(True)
        self.nsPerFrameField.setObjectName("nsPerFrameField")
        self.gridLayout_2.addWidget(self.nsPerFrameField, 0, 1, 1, 1)
        self.nsPerFrameLabel = QtWidgets.QLabel(self.settingsWidget)
        self.nsPerFrameLabel.setObjectName("nsPerFrameLabel")
        self.gridLayout_2.addWidget(self.nsPerFrameLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 2)
        settingsWindowWidget.addTab(self.settingsTab, "")

        self.retranslateUi(settingsWindowWidget)
        settingsWindowWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(settingsWindowWidget)

    def retranslateUi(self, settingsWindowWidget):
        _translate = QtCore.QCoreApplication.translate
        settingsWindowWidget.setWindowTitle(_translate("settingsWindowWidget", "Preferences"))
        self.applyFilterButton.setText(_translate("settingsWindowWidget", "Apply"))
        self.totalTimeLabel.setText(_translate("settingsWindowWidget", "total time:"))
        self.compareTotalTimeDropdown.setCurrentText(_translate("settingsWindowWidget", "greater"))
        self.compareTotalTimeDropdown.setItemText(0, _translate("settingsWindowWidget", "greater"))
        self.compareTotalTimeDropdown.setItemText(1, _translate("settingsWindowWidget", "smaller"))
        self.totalTimeField.setText(_translate("settingsWindowWidget", "0"))
        self.activeTotalTimeCheckbox.setText(_translate("settingsWindowWidget", "active"))
        settingsWindowWidget.setTabText(settingsWindowWidget.indexOf(self.filterTab), _translate("settingsWindowWidget", "Filters"))
        self.thresholdLabel.setText(_translate("settingsWindowWidget", "Threshold:"))
        self.thresholdField.setText(_translate("settingsWindowWidget", "0.0"))
        self.applySettingsButton.setText(_translate("settingsWindowWidget", "Apply"))
        self.nsPerFrameField.setText(_translate("settingsWindowWidget", "1.0"))
        self.nsPerFrameLabel.setText(_translate("settingsWindowWidget", "Nanoseconds per frame:"))
        settingsWindowWidget.setTabText(settingsWindowWidget.indexOf(self.settingsTab), _translate("settingsWindowWidget", "Settings"))

