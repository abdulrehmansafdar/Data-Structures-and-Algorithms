from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 673)
        MainWindow.setStyleSheet("background: #222831;\n"
"color:whitesmoke;\n"
"")
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ProductName = QtWidgets.QLabel(parent=self.centralwidget)
        self.ProductName.setGeometry(QtCore.QRect(200, 70, 171, 20))
        self.ProductName.setStyleSheet("color: whitesmoke;\n"
"            font-size: 25px;\n"
"            text-align: center;")
        self.ProductName.setObjectName("ProductName")
        self.Price = QtWidgets.QLabel(parent=self.centralwidget)
        self.Price.setGeometry(QtCore.QRect(310, 170, 61, 20))
        self.Price.setStyleSheet("color: whitesmoke;\n"
"            font-size: 20px;\n"
"            text-align: center;")
        self.Price.setObjectName("Price")
        self.Quantity = QtWidgets.QLabel(parent=self.centralwidget)
        self.Quantity.setGeometry(QtCore.QRect(280, 120, 91, 20))
        self.Quantity.setStyleSheet("color: whitesmoke;\n"
"            font-size: 20px;\n"
"            text-align: center;")
        self.Quantity.setObjectName("Quantity")
        self.txt_product = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_product.setGeometry(QtCore.QRect(380, 60, 361, 31))
        self.txt_product.setStyleSheet("\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 10px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 2px auto; \n"
"    border-radius: 10px;\n"
"   \n"
"")
        self.txt_product.setObjectName("txt_product")
        self.txt_quantity = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_quantity.setGeometry(QtCore.QRect(380, 110, 361, 31))
        self.txt_quantity.setStyleSheet("\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 10px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 2px auto; \n"
"    border-radius: 10px;\n"
"   \n"
"")
        self.txt_quantity.setObjectName("txt_quantity")
        self.txt_price = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.txt_price.setGeometry(QtCore.QRect(380, 160, 361, 31))
        self.txt_price.setStyleSheet("\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 10px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 2px auto; \n"
"    border-radius: 10px;\n"
"   \n"
"")
        self.txt_price.setObjectName("txt_price")
        self.Data_view = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.Data_view.setGeometry(QtCore.QRect(130, 310, 821, 271))
        self.Data_view.setStyleSheet("QTableWidget {\n"
"    background-color:#222831;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    gridline-color: #ccc;\n"
"color:whitesmoke;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #141E27;\n"
"    padding: 5px;\n"
"    border: 1px solid #ccc;\n"
"    font-size: 18px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 10px;\n"
"    border: 1px solid #ccc;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #0078d7;\n"
"    color: whitesmoke;\n"
"}")
        self.Data_view.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.Data_view.setObjectName("Data_view")
        self.Data_view.setColumnCount(3)  # Set the number of columns
        self.Data_view.setHorizontalHeaderLabels(["Product", "Quantity", "Price"])  # Set column headers
        self.Data_view.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.Add_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(280, 230, 131, 41))
        self.Add_button.setStyleSheet("QPushButton {\n"
"    background-color: whitesmoke;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"color: #222831;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.Add_button.setObjectName("Add_button")
        self.Update_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Update_button.setGeometry(QtCore.QRect(440, 230, 181, 41))
        self.Update_button.setStyleSheet("QPushButton {\n"
"    background-color: whitesmoke;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"color: #222831;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.Update_button.setObjectName("Update_button")
        self.Delete_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Delete_button.setGeometry(QtCore.QRect(650, 230, 131, 41))
        self.Delete_button.setStyleSheet("QPushButton {\n"
"    background-color: whitesmoke;\n"
"    font-size: 20px;\n"
"    text-align: center;\n"
"    border: 1px solid #ccc;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"color: #222831;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #e0e0e0;\n"
"}")
        self.Delete_button.setObjectName("Delete_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProductName.setText(_translate("MainWindow", "Product Name: "))
        self.Price.setText(_translate("MainWindow", "Price:"))
        self.Quantity.setText(_translate("MainWindow", "Quantity:"))
        self.Add_button.setText(_translate("MainWindow", "Add"))
        self.Update_button.setText(_translate("MainWindow", "Update"))
        self.Delete_button.setText(_translate("MainWindow", "Delete"))