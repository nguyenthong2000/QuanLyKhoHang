from PySide6 import QtGui,QtCore,QtWidgets
import sys
from bson.objectid import ObjectId
from random import randint
import datetime


import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyKhoHang"]
collection= db["ChiTietDonDatHang"]

class ChiTietDonDatHang(QtWidgets.QDialog):
    def __init__(self, madondathang):
        super().__init__()
        self.w = 1500
        self.h = 600
        self.setMinimumSize(self.w, self.h)
        self.r = 0
        self.label_title = ["Mã mặt hàng", "Số lượng","Đơn Giá"]
        self.madondathang = madondathang
        self.listid =[]

        self.setWindowTitle("Quản Lý Kho Hàng")


        self.setContentsMargins(10, 0, 10, 10)

        # layout chính
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Bảng dữ liệu
        self.tableWidget = QtWidgets.QTableWidget(50, 3)
        self.tableWidget.setMinimumSize(600,280)
        self.tableWidget.setStyleSheet("font-size: 14px"
                                       "margin-bottom: 10px")
        #self.tableWidget.setSortingEnabled(True)
        # set tiêu đề cột
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)
        # Kéo độ dài của cột đến cuối
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # Chia đều độ dài của cột
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Tiêu đề bảng
        self.lb_title = QtWidgets.QLabel("Chi Tiết Đơn Đặt Hàng")
        self.lb_title.setStyleSheet("color: blue;"
                                  "font: bold 24px;"
                                  "margin-bottom: 10px")
        self.lb_title.setAlignment(QtCore.Qt.AlignCenter)

        self.lb_title2 = QtWidgets.QLabel("Mã Đơn Hàng: {}".format(self.madondathang))
        self.lb_title2.setStyleSheet(
                                    "font: bold 20px;"
                                    "margin-bottom: 20px")
        self.lb_title2.setAlignment(QtCore.Qt.AlignCenter)

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

        # Label Mã Mặt hàng
        self.lb_ma = QtWidgets.QLabel("Mã Mặt hàng")
        self.lb_ma.setStyleSheet("font-size: 14px")

        # Label Sô lượng
        self.lb_soluong = QtWidgets.QLabel("Số lượng")
        self.lb_soluong.setStyleSheet("font-size: 14px")

        # Label Đơn giá
        self.lb_dongia = QtWidgets.QLabel("Đơn Giá")
        self.lb_dongia.setStyleSheet("font-size: 14px")


        # LineEdit Mã mặt hàng
        self.le_ma = QtWidgets.QLineEdit()
        self.le_ma.setStyleSheet("width: 100px;"
                                 "height: 25px;"
                                 "font-size: 14px")


        # LineEdit số lượng
        self.le_soluong = QtWidgets.QSpinBox()
        self.le_soluong.setStyleSheet("width: 100px;"
                                     "height: 25px;"
                                     "font-size: 14px")

        # LineEdit Đơn giá
        self.le_dongia = QtWidgets.QLineEdit()
        self.le_dongia.setStyleSheet("width: 100px;"
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
        self.layout_thaotac.addWidget(self.lb_soluong, 1, 0)
        self.layout_thaotac.addWidget(self.lb_dongia, 2, 0)


        # chèn LineEdit vào layout_thaotac
        self.layout_thaotac.addWidget(self.le_ma, 0, 1)
        self.layout_thaotac.addWidget(self.le_soluong, 1, 1)
        self.layout_thaotac.addWidget(self.le_dongia, 2, 1)

        # chèn Button vào layout_thaotac
        self.layout_thaotac.addWidget(self.btn_them, 0, 2)
        self.layout_thaotac.addWidget(self.btn_sua,1,2)
        self.layout_thaotac.addWidget(self.btn_xoa, 2, 2)

        # Chèn các layout vào layout chính
        layout.addWidget(self.lb_title)
        layout.addWidget(self.lb_title2)
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
        loaddata = collection.find({"id_madondathang": self.madondathang})
        item_count = loaddata.count()
        if item_count >50:
            self.tableWidget.setRowCount(item_count)
        i = 0
        self.listid.clear()
        for data in loaddata:

            self.listid.append(data["_id"])
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["id_mathang"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data["soluong"])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data["dongia"])))
            i = i + 1


    def Them(self):
        """Thêm dữ liệu"""
        print("a")
        try:
            dongia = float(self.le_dongia.text())
            data = {"id_madondathang":ObjectId(self.madondathang),
                "id_mathang":ObjectId(self.le_ma.text()),
                    "soluong": self.le_soluong.value(),
                    "dongia": dongia}
            collection.insert_one(data)
            self.HienThi()
        except Exception:
            QtWidgets.QMessageBox.about(self,"error","Đơn giá không được nhập chữ")

    def Sua(self):
        """Sửa dữ liệu"""

        if self.le_ma.text():
            dongia = float(self.le_dongia.text())
            collection.update_one({"_id": self.listid[self.r]},
                                  {"$set": {"id_mathang":ObjectId(self.le_ma.text()),
                    "soluong": self.le_soluong.value(),
                    "dongia": dongia}})

            self.HienThi()
        else:
            QtWidgets.QMessageBox.critical(self,"Thông báo","Không thể sửa")


    def Xoa(self):
        """Xoá dữ liệu"""
        try:
            collection.delete_one({"_id":ObjectId(self.listid[self.r])})
            self.HienThi()
        except Exception:
            QtWidgets.QMessageBox.critical(self, "Thông báo", "Không thể xoá")

    def SelectedItem(self, event):
        """Hiện thị dữ liệu ở ô đang chọn trong LineEdit"""
        self.r = event.row()
        try:
            self.le_ma.setText(self.tableWidget.item(self.r, 0).text())
            self.le_soluong.setValue(int(self.tableWidget.item(self.r, 1).text()))
            self.le_dongia.setText(self.tableWidget.item(self.r,2).text())

        except Exception as e:
            print(e)
            self.le_ma.setText("")
            self.le_soluong.setValue(0)
            self.le_dongia.setText("")


    def TimKiem(self):
        """Tìm kiếm dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)

        if self.cbb_timkiemtheo.currentIndex() == 0:
            loaddata = collection.find({"id_mathang":ObjectId(self.le_thanhtimkiem.text())})
        elif self.cbb_timkiemtheo.currentIndex() == 1:
            loaddata = collection.find({"soluong": int(self.le_thanhtimkiem.text())})
        elif self.cbb_timkiemtheo.currentIndex() == 2:
            loaddata = collection.find({"dongia": float(self.le_dongia.text())})

        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["id_mathang"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(data["soluong"])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(data["dongia"])))
            i = i + 1






