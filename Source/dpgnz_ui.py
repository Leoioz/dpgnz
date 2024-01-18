'''
MIT License

Copyright (c) 2024 Leoioz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dpgnz_uic.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,QFile,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
from PySide6.QtUiTools import QUiLoader

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(242, 336)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(242, 336))
        Form.setMouseTracking(False)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(False)
        self.label_5.setMinimumSize(QSize(120, 20))
        self.label_5.setTextFormat(Qt.AutoText)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(False)
        self.label_6.setMinimumSize(QSize(120, 20))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.comboBox)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(False)
        self.label_7.setMinimumSize(QSize(120, 20))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)
        self.label_11.setMinimumSize(QSize(120, 20))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_11)

        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.comboBox_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"\u5e7c\u5706"])
        font.setPointSize(18)
        self.pushButton.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.pushButton)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setMinimumSize(QSize(120, 20))
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(120, 20))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setMinimumSize(QSize(120, 20))
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_2)

        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        self.label_10.setMinimumSize(QSize(120, 20))
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_10)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setMinimumSize(QSize(120, 20))
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QSize(120, 20))
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMinimumSize(QSize(120, 20))
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u673a\u4fe1\u606f\u91c7\u96c6", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7535\u8111\u8d23\u4efb\u4eba\u59d3\u540d\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u8d23\u4efb\u4eba\u6240\u5c5e\u90e8\u95e8\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u6280\u672f\u90e8", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"QA", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"\u8d23\u4efb\u4eba\u6240\u5728\u529e\u516c\u5730\u70b9\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7535\u8111\u7c7b\u578b\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u53f0\u5f0f\u8ba1\u7b97\u673a", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u7b14\u8bb0\u672c\u7535\u8111", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u70b9\u51fb\u8fd9\u91cc\u8fdb\u884c\u63d0\u4ea4\uff01", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u4fe1\u606f\u7ed3\u679c\u5982\u4e0b\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4f60\u7684\u7535\u8111\u578b\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u5b89\u88c5\u65f6\u95f4\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"SN\u5e8f\u5217\u53f7\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u7535\u8111\u786c\u76d8\u5e8f\u5217\u53f7\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"IP\u5730\u5740\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7535\u8111MAC\u5730\u5740\uff1a", None))
    # retranslateUi

