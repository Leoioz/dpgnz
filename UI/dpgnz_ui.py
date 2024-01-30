# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dpgnz.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(369, 405)
        MainWindow.setStyleSheet(u"font: 10pt \"\u6c49\u4eea\u6b63\u5706-55W\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 351, 382))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        self.label_6.setMinimumSize(QSize(91, 20))
        self.label_6.setLayoutDirection(Qt.RightToLeft)
        self.label_6.setTextFormat(Qt.AutoText)

        self.verticalLayout.addWidget(self.label_6)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setMinimumSize(QSize(91, 20))
        self.label_11.setLayoutDirection(Qt.RightToLeft)
        self.label_11.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_11)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setMinimumSize(QSize(91, 20))
        self.label_7.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.label_7)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setEnabled(False)
        self.label_12.setMinimumSize(QSize(91, 20))
        font = QFont()
        font.setFamilies([u"\u6c49\u4eea\u6b63\u5706-55W"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(Qt.RightToLeft)
        self.label_12.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_12)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)

        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(91, 20))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(91, 20))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        self.label_10.setMinimumSize(QSize(91, 20))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setMinimumSize(QSize(91, 20))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QSize(91, 20))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QSize(91, 20))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)

        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_5.addWidget(self.label_15)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_5.addWidget(self.label_16)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_5)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_6.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.label_6.setBuddy(self.lineEdit_3)
        self.label_11.setBuddy(self.comboBox)
        self.label_7.setBuddy(self.lineEdit_2)
        self.label_12.setBuddy(self.comboBox_2)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7535\u8111\u4fe1\u606f\u91c7\u96c6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8111\u8d23\u4efb\u4eba\u59d3\u540d\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u4eba\u6240\u5c5e\u90e8\u95e8\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5728\u529e\u516c\u5730\u70b9\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8111\u7c7b\u578b\uff1a", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u59d3\u540d", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.lineEdit_3.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_3.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u7684\u59d3\u540d", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6280\u672f\u90e8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"QA", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"QA", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"QA", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"QA", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"QA", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4f60\u7684\u90e8\u95e8", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lineEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u4f8b\u5982\uff1aYA#2012\uff0c\u529e\u516c\u697c3#301", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u4f60\u529e\u516c\u5730\u70b9", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u53f0\u5f0f\u8ba1\u7b97\u673a", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b14\u8bb0\u672c\u7535\u8111", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u8fd9\u91cc\u8fdb\u884c\u63d0\u4ea4\uff01", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u5982\u4e0b\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4f60\u7684\u7535\u8111\u578b\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u5b89\u88c5\u65f6\u95f4\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"SN\u5e8f\u5217\u53f7\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u786c\u76d8\u5e8f\u5217\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"MAC\u5730\u5740\uff1a", None))
        self.label_5.setText("")
        self.label_8.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
    # retranslateUi

