from PySide6 import QtGui,QtCore,QtWidgets
import sys
from bson.objectid import ObjectId

import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyKhoHang"]
collection= db["NhanVien"]


class NhanVien(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.w = 1500
        self.h = 600
        self.setMinimumSize(self.w, self.h)
        self.r = 0
        self.label_title = ["Mã nhân viên", "Tên nhân viên", "Chức vụ"]
        self.setContentsMargins(10, 0, 10, 10)

        # layout chính
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Bảng dữ liệu
        self.tableWidget = QtWidgets.QTableWidget(50, 3)
        self.tableWidget.setMinimumSize(600,300)
        self.tableWidget.setStyleSheet("font-size: 14px")
        #self.tableWidget.setSortingEnabled(True)
        # set tiêu đề cột
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)
        # Kéo độ dài của cột đến cuối
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # Chia đều độ dài của cột
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Tiêu đề bảng
        self.lb_title = QtWidgets.QLabel("Nhân Viên")
        self.lb_title.setStyleSheet("color: blue;"
                                  "font: bold 24px;"
                                  "margin-bottom: 30px")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)

        # Layout tìm kiếm
        self.layout_timkiem = QtWidgets.QGridLayout()
        self.layout_timkiem.setContentsMargins(0, 10, 0, 20)

        # Thanh tìm kiếm
        self.le_thanhtimkiem = QtWidgets.QLineEdit()
        self.le_thanhtimkiem.setStyleSheet("width: 100px;"
                                           "height: 25px;"
                                           "font-size: 14px")

        # ComboBox Tìm kiếm theo
        self.cbb_timkiemtheo = QtWidgets.QComboBox()
        self.cbb_timkiemtheo.setStyleSheet( "height: 25px;"
                                           "font-size: 14px")
        self.cbb_timkiemtheo.setMinimumContentsLength(20)
        self.cbb_timkiemtheo.addItems(self.label_title)
        self.cbb_timkiemtheo.setCurrentIndex(1)

        # buttom tìm kiếm
        self.btn_timkiem = QtWidgets.QPushButton("Tìm kiếm")
        self.btn_timkiem.setIcon(QtGui.QIcon("image\\search.png"))
        self.btn_timkiem.setStyleSheet("font-size: 14px")

        # button refresh
        self.btn_refresh =QtWidgets.QPushButton("Refresh")
        self.btn_refresh.setIcon(QtGui.QIcon("image\\refresh.png"))
        self.btn_refresh.setStyleSheet("font-size: 14px")

        # Chèn Item vào layout tìm kiếm
        self.layout_timkiem.addWidget(self.le_thanhtimkiem, 0, 0)
        self.layout_timkiem.addWidget(self.cbb_timkiemtheo, 0, 1)
        self.layout_timkiem.addWidget(self.btn_timkiem, 0, 2)
        self.layout_timkiem.addWidget(self.btn_refresh,0,3)



        self.layout_thaotac = QtWidgets.QGridLayout()

        # Label Mã loại hàng
        self.lb_ma = QtWidgets.QLabel("Mã nhân viên")
        self.lb_ma.setStyleSheet("font-size: 14px")

        # Label Tên loại hàng
        self.lb_ten = QtWidgets.QLabel("Tên nhân viên")
        self.lb_ten.setStyleSheet("font-size: 14px")

        # Label Chức vụ
        self.lb_chucvu = QtWidgets.QLabel("Chức vụ")
        self.lb_chucvu.setStyleSheet("font-size: 14px")

        # LineEdit Mã nhân viên
        self.le_ma = QtWidgets.QLineEdit()
        self.le_ma.setEnabled(False)
        self.le_ma.setStyleSheet("width: 100px;"
                                 "height: 25px;"
                                 "font-size: 14px")

        # LineEdit Tên nhân viên
        self.le_ten = QtWidgets.QLineEdit()
        self.le_ten.setStyleSheet("width: 100px;"
                               "height: 25px;"
                                  "font-size: 14px")

        # LineEdit Chức vụ
        self.le_chucvu = QtWidgets.QLineEdit()
        self.le_chucvu.setStyleSheet("width: 100px;"
                                  "height: 25px;"
                                  "font-size: 14px")

        # button Thêm
        self.btn_them = QtWidgets.QPushButton("Thêm")
        self.btn_them.setIcon(QtGui.QIcon("image\\plus.png"))
        self.btn_them.setStyleSheet("width: 150px;"
                                    "height: 30px;"
                                    "margin-left: 100px;"
                                    "font-size: 14px")

        # button Sửa
        self.btn_sua = QtWidgets.QPushButton("Sửa")
        self.btn_sua.setIcon(QtGui.QIcon("image\\loop.png"))
        self.btn_sua.setStyleSheet("width: 150px;"
                                   "height: 30px;"
                                   "margin-left: 100px;"
                                   "font-size: 14px")

        # button Xoá
        self.btn_xoa = QtWidgets.QPushButton("Xoá")
        self.btn_xoa.setIcon(QtGui.QIcon("image\\remove.png"))
        self.btn_xoa.setStyleSheet("width: 150px;"
                                   "height: 30px;"
                                   "margin-left: 100px;"
                                   "font-size: 14px"
                                   )

        # chèn Label vào layout_thaotac
        self.layout_thaotac.addWidget(self.lb_ma, 0, 0)
        self.layout_thaotac.addWidget(self.lb_ten, 1, 0)
        self.layout_thaotac.addWidget(self.lb_chucvu, 2, 0)
        # chèn LineEdit vào layout_thaotac
        self.layout_thaotac.addWidget(self.le_ma, 0, 1)
        self.layout_thaotac.addWidget(self.le_ten, 1, 1)
        self.layout_thaotac.addWidget(self.le_chucvu, 2, 1)
        # chèn Button vào layout_thaotac
        self.layout_thaotac.addWidget(self.btn_them, 0, 2)
        self.layout_thaotac.addWidget(self.btn_sua,1,2)
        self.layout_thaotac.addWidget(self.btn_xoa, 2, 2)

        # Chèn các layout vào layout chính
        layout.addWidget(self.lb_title)
        layout.addLayout(self.layout_timkiem)
        layout.addWidget(self.tableWidget)
        layout.addLayout(self.layout_thaotac)


        # Hiện thị dữ liệu
        self.HienThi()

        # signal
        self.btn_them.clicked.connect(self.Them)
        self.btn_sua.clicked.connect(self.Sua)
        self.btn_xoa.clicked.connect(self.Xoa)
        self.tableWidget.clicked.connect(self.SelectedItem)
        self.btn_timkiem.clicked.connect(self.TimKiem)
        self.btn_refresh.clicked.connect(self.HienThi)

    def HienThi(self):
        """Hiện thị dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)
        loaddata = collection.find()
        item_count = loaddata.count()
        if item_count >50:
            self.tableWidget.setRowCount(item_count)
        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["_id"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(data["ten"]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(data["chucvu"]))
            i = i + 1


    def Them(self):
        """Thêm dữ liệu"""

        data = {"ten": self.le_ten.text(),"chucvu":self.le_chucvu.text()}
        collection.insert_one(data)
        self.HienThi()

    def Sua(self):
        """Sửa dữ liệu"""
        if self.le_ma.text():
            collection.update_one({"_id": ObjectId(self.le_ma.text())},{"$set":{"ten": self.le_ten.text(),"chucvu":self.le_chucvu.text()}})
            self.HienThi()
        else:
            QtWidgets.QMessageBox.critical(self,"Thông báo","Không thể sửa khi thiếu mã")

    def Xoa(self):
        """Xoá dữ liệu"""
        collection.delete_one({"_id":ObjectId(self.le_ma.text())})
        self.HienThi()

    def SelectedItem(self, event):
        """Hiện thị dữ liệu ở ô đang chọn trong LineEdit"""
        self.r = event.row()
        try:
            self.le_ma.setText(self.tableWidget.item(self.r, 0).text())
            self.le_ten.setText(self.tableWidget.item(self.r, 1).text())
            self.le_chucvu.setText(self.tableWidget.item(self.r, 2).text())
        except:
            self.le_ma.setText("")
            self.le_ten.setText("")
            self.le_chucvu.setText("")

    def TimKiem(self):
        """Tìm kiếm dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)

        if self.cbb_timkiemtheo.currentIndex() == 0:
            loaddata = collection.find({"_id":ObjectId(self.le_thanhtimkiem.text())})
        elif self.cbb_timkiemtheo.currentIndex() == 1:
            loaddata = collection.find({"ten": self.le_thanhtimkiem.text()})
        else:
            loaddata = collection.find({"chucvu": self.le_thanhtimkiem.text()})

        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["_id"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(data["ten"]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(data["chucvu"]))
            i = i + 1





