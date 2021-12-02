from PySide6 import QtGui,QtCore,QtWidgets
import sys
from bson.objectid import ObjectId
from random import randint

import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyKhoHang"]
collection= db["NhaCungCap"]


class NhaCungCap(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.w = 1500
        self.h = 600
        self.setMinimumSize(self.w, self.h)
        self.r = 0
        self.label_title = ["Mã nhà cung cấp", "Tên nhà cung cấp", "Địa chỉ","Điện thoại", "Fax", "Mã số thuế"]
        self.setContentsMargins(10, 0, 10, 10)

        # layout chính
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Bảng dữ liệu
        self.tableWidget = QtWidgets.QTableWidget(50, 6)
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
        self.lb_title = QtWidgets.QLabel("Nhà Cung Cấp")
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

        # Label Mã NCC
        self.lb_ma = QtWidgets.QLabel("Mã NCC")
        self.lb_ma.setStyleSheet("font-size: 14px")

        # Label Tên NCC
        self.lb_ten = QtWidgets.QLabel("Tên NCC")
        self.lb_ten.setStyleSheet("font-size: 14px")

        # Label Địa chỉ
        self.lb_diachi = QtWidgets.QLabel("Địa Chỉ")
        self.lb_diachi.setStyleSheet("font-size: 14px")

        # Label Địa chỉ
        self.lb_dienthoai = QtWidgets.QLabel("Điện thoại")
        self.lb_dienthoai.setStyleSheet("font-size: 14px")

        # Label Fax
        self.lb_fax = QtWidgets.QLabel("Fax")
        self.lb_fax.setStyleSheet("font-size: 14px")

        # Label Mã số thuế
        self.lb_masothue = QtWidgets.QLabel("Mã số Thuế")
        self.lb_masothue.setStyleSheet("font-size: 14px")

        # LineEdit Mã NCC
        self.le_ma = QtWidgets.QLineEdit()
        self.le_ma.setEnabled(False)
        self.le_ma.setStyleSheet("width: 100px;"
                                 "height: 25px;"
                                 "font-size: 14px")

        # LineEdit Tên NCC
        self.le_ten = QtWidgets.QLineEdit()
        self.le_ten.setStyleSheet("width: 100px;"
                               "height: 25px;"
                                  "font-size: 14px")

        # LineEdit Địa chỉ
        self.le_diachi = QtWidgets.QLineEdit()
        self.le_diachi.setStyleSheet("width: 100px;"
                                  "height: 25px;"
                                  "font-size: 14px")

        # LineEdit Điện thoại
        self.le_dienthoai = QtWidgets.QLineEdit()
        self.le_dienthoai.setStyleSheet("width: 100px;"
                                     "height: 25px;"
                                     "font-size: 14px")

        # LineEdit Fax
        self.le_fax = QtWidgets.QLineEdit()
        self.le_fax.setStyleSheet("width: 100px;"
                                     "height: 25px;"
                                     "font-size: 14px")

        # LineEdit Mã số thuế
        self.le_masothue = QtWidgets.QLineEdit()
        self.le_masothue.setStyleSheet("width: 100px;"
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
        self.layout_thaotac.addWidget(self.lb_diachi, 2, 0)
        self.layout_thaotac.addWidget(self.lb_dienthoai, 0, 2)
        self.layout_thaotac.addWidget(self.lb_fax, 1, 2)
        self.layout_thaotac.addWidget(self.lb_masothue, 2, 2)

        # chèn LineEdit vào layout_thaotac
        self.layout_thaotac.addWidget(self.le_ma, 0, 1)
        self.layout_thaotac.addWidget(self.le_ten, 1, 1)
        self.layout_thaotac.addWidget(self.le_diachi, 2, 1)
        self.layout_thaotac.addWidget(self.le_dienthoai, 0, 3)
        self.layout_thaotac.addWidget(self.le_fax, 1, 3)
        self.layout_thaotac.addWidget(self.le_masothue, 2, 3)

        # chèn Button vào layout_thaotac
        self.layout_thaotac.addWidget(self.btn_them, 0, 4)
        self.layout_thaotac.addWidget(self.btn_sua,1,4)
        self.layout_thaotac.addWidget(self.btn_xoa, 2, 4)

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
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(data["tennhacungcap"]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(data["diachi"]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(data["dienthoai"]))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(data["fax"]))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(data["masothue"]))
            i = i + 1


    def Them(self):
        """Thêm dữ liệu"""
        data = {"tennhacungcap": self.le_ten.text(), "diachi":self.le_diachi.text(), "dienthoai": self.le_dienthoai.text(),
                "fax": self.le_fax.text(), "masothue":self.le_masothue.text()}
        collection.insert_one(data)
        self.HienThi()

    def Sua(self):
        """Sửa dữ liệu"""
        if self.le_ma.text():
            collection.update_one({"_id": ObjectId(self.le_ma.text())},
                                  {"$set":{"tennhacungcap": self.le_ten.text(),"diachi":self.le_diachi.text(),
                                           "dienthoai": self.le_dienthoai.text(),"fax": self.le_fax.text(), "masothue":self.le_masothue.text()}})
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
            self.le_diachi.setText(self.tableWidget.item(self.r,2).text())
            self.le_dienthoai.setText(self.tableWidget.item(self.r, 3).text())
            self.le_fax.setText(self.tableWidget.item(self.r, 4).text())
            self.le_masothue.setText(self.tableWidget.item(self.r, 5).text())
        except:
            self.le_ma.setText("")
            self.le_ten.setText("")
            self.le_diachi.setText("")
            self.le_dienthoai.setText("")
            self.le_fax.setText("")
            self.le_masothue.setText("")

    def TimKiem(self):
        """Tìm kiếm dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)

        if self.cbb_timkiemtheo.currentIndex() == 0:
            loaddata = collection.find({"_id":ObjectId(self.le_thanhtimkiem.text())})
        elif self.cbb_timkiemtheo.currentIndex() == 1:
            loaddata = collection.find({"tennhacungcap": self.le_thanhtimkiem.text()})
        elif self.cbb_timkiemtheo.currentIndex() == 2:
            loaddata = collection.find({"diachi": self.le_thanhtimkiem.text()})
        elif self.cbb_timkiemtheo.currentIndex() == 3:
            loaddata = collection.find({"dienthoai": self.le_thanhtimkiem.text()})
        elif self.cbb_timkiemtheo.currentIndex() == 4:
            loaddata = collection.find({"fax": self.le_thanhtimkiem.text()})
        else:
            loaddata = collection.find({"masothue": self.le_thanhtimkiem.text()})

        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["_id"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(data["tennhacungcap"]))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(data["diachi"]))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(data["dienthoai"]))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(data["dienthoai"]))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(data["masothue"]))
            i = i + 1





