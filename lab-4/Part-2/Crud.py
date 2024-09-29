import csv
import os
from PyQt6 import QtWidgets,QtCore
from Crud_UI import Ui_MainWindow

class CrudApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Product Management")
        self.setFixedSize(1021, 673)
        # Connect buttons to their functions
        self.Add_button.clicked.connect(self.add_data)
        self.Update_button.clicked.connect(self.update_data)
        self.Delete_button.clicked.connect(self.delete_data)
        # Connect item clicked signal to show_data function
        self.Data_view.itemClicked.connect(self.show_data)

        # Load existing data into the table
        self.load_data()

    def load_data(self):
        if not os.path.exists('products.csv'):
            with open('products.csv','w'):
                pass  # create   file if it doesn't exist
        self.Data_view.setRowCount(0) # clear the table first
        with open('products.csv','r') as file:
            reader = csv.reader(file)
            for row_number,row_data in enumerate(csv.reader(file)):
                if any(row_data):
                    self.Data_view.insertRow(row_number)
                    for column_number,column_data in enumerate(row_data):
                        self.Data_view.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(column_data))
                

    def add_data(self):
        product = self.txt_product.toPlainText()
        if not product:
            QtWidgets.QMessageBox.warning(self,"Error","Invalid product")
            return
        quantity = self.txt_quantity.toPlainText()
        # check if the quantity field is empty or is integer
        if not quantity or not quantity.isdigit():
            QtWidgets.QMessageBox.warning(self,"Error","Invalid quantity")
            return
        price = self.txt_price.toPlainText()
        # check if the price field is empty or is integer
        if not price or not price.isdigit():
            QtWidgets.QMessageBox.warning(self,"Error","Invalid price")
            return
        
        with open('products.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([product,quantity,price])
        self.load_data()
        self.clear_fields()

    def update_data(self):
        selected_row = self.Data_view.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self,"Error","No row selected")
            return
        product = self.txt_product.toPlainText()
        if not product:
            QtWidgets.QMessageBox.warning(self,"Error","Invalid product")
            return
        quantity = self.txt_quantity.toPlainText()
        # check if the quantity field is empty or is integer
        if not quantity or not quantity.isdigit():
            QtWidgets.QMessageBox.warning(self,"Error","Invalid quantity")
            return
        price = self.txt_price.toPlainText()
        # check if the price field is empty or is float
        if not price or not price.isdigit():
            QtWidgets.QMessageBox.warning(self,"Error","Invalid price")
            return

        
        self.Data_view.setItem(selected_row, 0, QtWidgets.QTableWidgetItem(product))
        self.Data_view.setItem(selected_row, 1, QtWidgets.QTableWidgetItem(quantity))
        self.Data_view.setItem(selected_row, 2, QtWidgets.QTableWidgetItem(f"{int(price)}"))  # Store as integer
        self.save_csv()

    def delete_data(self):
        selected_row = self.Data_view.currentRow()
        if selected_row == -1:
            QtWidgets.QMessageBox.warning(self,"Error","No row selected")
            return
        self.Data_view.removeRow(selected_row)
        self.save_csv()

    def save_csv(self):
        with open('products.csv','w',newline='') as file:
            writer = csv.writer(file)
            for row in range(self.Data_view.rowCount()):
                row_data = [self.Data_view.item(row,column).text() for column in range(self.Data_view.columnCount())]
                row_data[2] = str(int(float(row_data[2])))  # Ensure it's stored without decimal
                writer.writerow(row_data)

    def clear_fields(self):
        # Clear the input fields after adding or updating
        self.txt_product.clear()
        self.txt_quantity.clear()
        self.txt_price.clear()


    #  function to show the selected row data in the text fields
    def show_data(self):
        selected_row = self.Data_view.currentRow()
        if selected_row == -1:
            return
        self.txt_product.setPlainText(self.Data_view.item(selected_row,0).text())
        self.txt_quantity.setPlainText(self.Data_view.item(selected_row,1).text())
        # set the price field to the float value of the selected row as it is stored as a string with a dot
        self.txt_price.setPlainText(self.Data_view.item(selected_row,2).text())
        



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = CrudApp()
    window.show()
    app.exec()




