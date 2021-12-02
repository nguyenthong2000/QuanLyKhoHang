import sys
from PySide6 import QtGui,QtCore,QtWidgets

import pymongo
from pymongo import MongoClient

from loaihang import LoaiHang
from kho import Kho
from nhacungcap import NhaCungCap
from nhanvien import NhanVien
from mathang import MatHang
from dondathang import DonDatHang

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = LoaiHang()

        self.menu = self.menuBar()
        self.trangthai = 0
        self.setWindowTitle("Quản Lý Kho Hàng")

        # Menu File
        file_menu = self.menu.addMenu("File")

        # Menu Quản lý
        quanly_menu = self.menu.addMenu("Quản lý")

        # Hành động Exit
        exit_action = QtWidgets.QWidgetAction(self)
        exit_action.setText("Exit app")
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(lambda: QtWidgets.QApplication.quit())

        # Thêm hành động vào menu File
        file_menu.addAction(exit_action)

        # Hành động mở bảng Kho
        kho_action = QtWidgets.QWidgetAction(self)
        kho_action.setText("Kho")
        kho_action.setShortcut("Ctrl+K")
        kho_action.triggered.connect(lambda : self.setCentralWidget(Kho()))

        # Hành động mở bảng NCC
        ncc_action = QtWidgets.QWidgetAction(self)
        ncc_action.setText("Nhà cung cấp")
        ncc_action.triggered.connect(lambda : self.setCentralWidget(NhaCungCap()))

        # Hành động mở bảng Nhân Viên
        nhanvien_action = QtWidgets.QWidgetAction(self)
        nhanvien_action.setText("Nhân Viên")
        nhanvien_action.triggered.connect(lambda: self.setCentralWidget(NhanVien()))

        # Hành động mở bảng Mặt Hàng
        mathang_action = QtWidgets.QWidgetAction(self)
        mathang_action.setText("Mặt Hàng")
        mathang_action.triggered.connect(lambda: self.setCentralWidget(MatHang()))

        # Hành động mở bảng Đơn đặt hàng
        dondathang_action = QtWidgets.QWidgetAction(self)
        dondathang_action.setText("Đơn Đặt Hàng")
        dondathang_action.triggered.connect(lambda: self.setCentralWidget(DonDatHang()))

        # Thêm hành động vào menu Quản Lý
        quanly_menu.addAction(kho_action)
        quanly_menu.addAction(ncc_action)
        quanly_menu.addAction(nhanvien_action)
        quanly_menu.addAction(mathang_action)
        quanly_menu.addAction(dondathang_action)


        self.setCentralWidget(self.layout)
        self.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    sys.exit(app.exec())
