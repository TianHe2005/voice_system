# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(654, 469)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-1, -1, 141, 471))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(161, 105, 227, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(8, 53, 121, 31))
        self.pushButton.setStyleSheet(u"")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(8, 104, 121, 31))
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(8, 155, 121, 31))
        self.widget_2 = QWidget(Widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(139, -1, 521, 471))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(-1, -1, 521, 471))
        self.pushButton_4 = QPushButton(self.widget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(170, 130, 141, 31))
        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(170, 220, 141, 31))
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 180, 241, 20))
        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(170, 310, 141, 31))
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 270, 271, 21))
        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(169, 381, 221, 21))
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(10, 10, 511, 461))
        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(140, 220, 171, 20))
        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(140, 280, 171, 21))
        self.pushButton_10 = QPushButton(self.widget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(140, 330, 171, 31))
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 20, 61, 20))
        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(70, 50, 61, 20))
        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(70, 80, 61, 20))
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 30, 40, 12))
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 60, 40, 12))
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 250, 241, 21))
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 302, 251, 20))
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(9, -1, 511, 481))
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton_11 = QPushButton(self.tab_2)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(150, 50, 161, 31))
        self.pushButton_12 = QPushButton(self.tab_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(151, 165, 161, 31))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(150, 90, 301, 31))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(151, 200, 291, 31))
        self.pushButton_13 = QPushButton(self.tab_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(151, 246, 161, 31))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(151, 281, 291, 31))
        self.pushButton_14 = QPushButton(self.tab_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(151, 326, 161, 31))
        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(150, 140, 191, 20))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(70, 140, 71, 20))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u8bed\u97f3\u5206\u5272", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"\u8bed\u97f3\u9884\u5904\u7406", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"\u8bf4\u8bdd\u4eba\u8bc6\u522b", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u9700\u8981\u5206\u5272\u7684\u8bed\u97f3\u6587\u4ef6", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u9700\u8981\u4fdd\u5b58\u7684\u6587\u4ef6\u5939", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u8def\u5f84", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u5206\u5272", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u8def\u5f84", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u9700\u8981\u5904\u7406\u7684\u8bed\u97f3\u6587\u4ef6\u5939", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u9700\u8981\u4fdd\u5b58\u7684\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.pushButton_10.setText(QCoreApplication.translate("Widget", u"\u542f\u52a8\u9884\u5904\u7406", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"\u58f0\u9053\u6570", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"\u91c7\u6837\u7387", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u8def\u5f84", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"\u8def\u5f84", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"\u8bf4\u8bdd\u4eba\u5bf9\u6bd4", None))
        self.pushButton_11.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u6a21\u677f\u8bed\u97f3", None))
        self.pushButton_12.setText(QCoreApplication.translate("Widget", u"\u9009\u62e9\u9700\u8981\u8bc6\u522b\u7684\u8bed\u97f3\u6587\u4ef6\u5939", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_13.setText(QCoreApplication.translate("Widget", u"\u4fdd\u5b58\u6587\u4ef6\u5939", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_14.setText(QCoreApplication.translate("Widget", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"\u8f93\u5165\u8bf4\u8bdd\u4eba\u540d\u79f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Widget", u"\u8bf4\u8bdd\u4eba\u6279\u91cf\u5bf9\u6bd4", None))
    # retranslateUi

