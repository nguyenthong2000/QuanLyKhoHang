from PySide6 import QtGui,QtCore,QtWidgets
import sys
from bson.objectid import ObjectId
from random import randint
import datetime


import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyKhoHang"]
collection= db["DonDatHang"]
db_NhanVien = db["NhanVien"]
db_NCC = db["NhaCungCap"]
db_Kho = db["Kho"]
db_MatHang = db["MatHang"]

class DonDatHang(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.w = 1500
        self.h = 600
        self.setMinimumSize(self.w, self.h)
        self.r = 0
        self.label_title = ["Mã đơn đặt hàng", "Nhà cung cấp","Kho", "Ngày nhập","Hình thức thanh toán", "Phương pháp vận chuyển","Nhân Viên"]

        # lấy ncc
        self.ncc = dict()
        for item in db_NCC.find():
            self.ncc[item["_id"]] = item["tennhacungcap"]

        # lấy kho
        self.kho = dict()
        for item in db_Kho.find():
            self.kho[item["_id"]] = item["tenkho"]


        # lấy nhân viên
        self.nhanvien = dict()
        for item in db_NhanVien.find():
            self.nhanvien[item["_id"]] = item["ten"]

        self.setContentsMargins(10, 0, 10, 10)

        # layout chính
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        # Bảng dữ liệu
        self.tableWidget = QtWidgets.QTableWidget(50, 7)
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
        self.lb_title = QtWidgets.QLabel("Mặt Hàng")
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

        # Label Mã Đơn đặt hàng
        self.lb_ma = QtWidgets.QLabel("Mã đơn đặt hàng")
        self.lb_ma.setStyleSheet("font-size: 14px")

        # Label NCC
        self.lb_ncc = QtWidgets.QLabel("Nhà cung cấp")
        self.lb_ncc.setStyleSheet("font-size: 14px")

        # Label Kho
        self.lb_kho = QtWidgets.QLabel("Kho")
        self.lb_kho.setStyleSheet("font-size: 14px")

        # Label Ngày nhập
        self.lb_ngaynhap = QtWidgets.QLabel("Ngày nhập")
        self.lb_ngaynhap.setStyleSheet("font-size: 14px")


        # Label Hình thức thanh toán
        self.lb_hinhthucthanhtoan = QtWidgets.QLabel("Hình thức thanh toán")
        self.lb_hinhthucthanhtoan.setStyleSheet("font-size: 14px")

        # Label Phương thức vận chuyển
        self.lb_phuongthucvanchuyen = QtWidgets.QLabel("Phương thức vận chuyển")
        self.lb_phuongthucvanchuyen.setStyleSheet("font-size: 14px")

        # Label Nhân Viên
        self.lb_nhanvien = QtWidgets.QLabel("Nhân Viên")
        self.lb_nhanvien.setStyleSheet("font-size: 14px")


        # LineEdit Mã đơn đặt hàng
        self.le_ma = QtWidgets.QLineEdit()
        self.le_ma.setEnabled(False)
        self.le_ma.setStyleSheet("width: 100px;"
                                 "height: 25px;"
                                 "font-size: 14px")

        # cbb NCC
        self.cbb_ncc = QtWidgets.QComboBox()

        self.cbb_ncc.addItems(self.ncc.values())
        self.cbb_ncc.setCurrentIndex(0)
        self.cbb_ncc.setStyleSheet("width:20px;"
                                           "height: 25px;"
                                           "font-size: 14px")

        # ccb kho
        self.cbb_kho = QtWidgets.QComboBox()
        self.cbb_kho.addItems(self.kho.values())
        self.cbb_kho.setCurrentIndex(0)
        self.cbb_kho.setStyleSheet("width:20px;"
                                  "height: 25px;"
                                  "font-size: 14px")

        # DateTimeEdit Ngày nhập
        self.de_ngaynhap = QtWidgets.QDateTimeEdit()
        self.de_ngaynhap.setStyleSheet("width: 100px;"
                                     "height: 25px;"
                                     "font-size: 14px")

        # LineEdit Hình thức thanh toán
        self.le_hinhthucthanhtoan = QtWidgets.QLineEdit()
        self.le_hinhthucthanhtoan.setStyleSheet("width: 100px;"
                                     "height: 25px;"
                                     "font-size: 14px")

        # LineEdit Phương thức vận chuyển
        self.le_phuongthucvanchuyen = QtWidgets.QLineEdit()
        self.le_phuongthucvanchuyen.setStyleSheet("width: 100px;"
                                                "height: 25px;"
                                                "font-size: 14px")

        # ccb nhân viên
        self.cbb_nhanvien = QtWidgets.QComboBox()
        self.cbb_nhanvien.addItems(self.nhanvien.values())
        self.cbb_nhanvien.setCurrentIndex(0)
        self.cbb_nhanvien.setStyleSheet("width:20px;"
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
        self.layout_thaotac.addWidget(self.lb_ncc, 1, 0)
        self.layout_thaotac.addWidget(self.lb_kho, 2, 0)
        self.layout_thaotac.addWidget(self.lb_ngaynhap, 3, 0)
        self.layout_thaotac.addWidget(self.lb_hinhthucthanhtoan, 0, 2)
        self.layout_thaotac.addWidget(self.lb_phuongthucvanchuyen,1, 2)
        self.layout_thaotac.addWidget(self.lb_nhanvien, 2, 2)

        # chèn LineEdit vào layout_thaotac
        self.layout_thaotac.addWidget(self.le_ma, 0, 1)
        self.layout_thaotac.addWidget(self.cbb_ncc, 1, 1)
        self.layout_thaotac.addWidget(self.cbb_kho, 2, 1)
        self.layout_thaotac.addWidget(self.de_ngaynhap, 3, 1)
        self.layout_thaotac.addWidget(self.le_hinhthucthanhtoan, 0, 3)
        self.layout_thaotac.addWidget(self.le_phuongthucvanchuyen, 1, 3)
        self.layout_thaotac.addWidget(self.cbb_nhanvien, 2, 3)

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
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.ncc.get(data["id_ncc"])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.kho.get(data["id_kho"])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data["Ngaynhap"])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(data["hinhthucthanhtoan"]))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(data["phuongthucvanchuyen"]))
            self.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(self.nhanvien.get(data["id_nhanvien"])))
            i = i + 1


    def Them(self):
        """Thêm dữ liệu"""
        date = datetime.datetime(self.de_ngaynhap.date().year(), self.de_ngaynhap.date().month(),
                                 self.de_ngaynhap.date().day(), self.de_ngaynhap.dateTime().time().hour(),
                                 self.de_ngaynhap.dateTime().time().minute())
        data = {"id_ncc": list(self.ncc.keys())[self.cbb_ncc.currentIndex()],
                "id_kho": list(self.kho.keys())[self.cbb_kho.currentIndex()],
                "Ngaynhap": date,
                "hinhthucthanhtoan": self.le_hinhthucthanhtoan.text(),
                "phuongthucvanchuyen": self.le_phuongthucvanchuyen.text(),
                "id_nhanvien": list(self.nhanvien.keys())[self.cbb_nhanvien.currentIndex()]}
        collection.insert_one(data)
        self.HienThi()


    def Sua(self):
        """Sửa dữ liệu"""

        if self.le_ma.text():
            date = datetime.datetime(self.de_ngaynhap.date().year(), self.de_ngaynhap.date().month(),
                                     self.de_ngaynhap.date().day(), self.de_ngaynhap.dateTime().time().hour(),
                                     self.de_ngaynhap.dateTime().time().minute())
            collection.update_one({"_id": ObjectId(self.le_ma.text())},
                                  {"$set":{"id_ncc":  list(self.ncc.keys())[self.cbb_ncc.currentIndex()], "id_kho": list(self.kho.keys())[self.cbb_kho.currentIndex()], "Ngaynhap": date,
                "hinhthucthanhtoan": self.le_hinhthucthanhtoan.text(), "phuongthucvanchuyen": self.le_phuongthucvanchuyen.text(), "id_nhanvien":list(self.nhanvien.keys())[self.cbb_nhanvien.currentIndex()]}})
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
            self.cbb_ncc.setCurrentText(self.tableWidget.item(self.r, 1).text())
            self.cbb_kho.setCurrentText(self.tableWidget.item(self.r,2).text())
            ngaynhap = self.tableWidget.item(self.r,3).text()
            self.de_ngaynhap.setDateTime(QtCore.QDateTime(QtCore.QDate(int(ngaynhap[0:4]),int(ngaynhap[5:7]),int(ngaynhap[8:10])),QtCore.QTime(int(ngaynhap[11:13]),int(ngaynhap[14:16]))))
            self.le_hinhthucthanhtoan.setText(self.tableWidget.item(self.r, 4).text())
            self.le_phuongthucvanchuyen.setText(self.tableWidget.item(self.r, 5).text())
            self.cbb_nhanvien.setCurrentText(self.tableWidget.item(self.r, 6).text())
        except Exception as e:
            print(e)
            self.le_ma.setText("")
            self.cbb_ncc.setCurrentText("")
            self.cbb_kho.setCurrentText("")
            self.le_hinhthucthanhtoan.setText("")
            self.le_phuongthucvanchuyen.setText("")
            self.cbb_nhanvien.setCurrentText("")

    def TimKiem(self):
        """Tìm kiếm dữ liệu"""
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(self.label_title)

        if self.cbb_timkiemtheo.currentIndex() == 0:
            loaddata = collection.find({"_id":ObjectId(self.le_thanhtimkiem.text())})
        elif self.cbb_timkiemtheo.currentIndex() == 1:
            loaddata = collection.find({"ten": self.le_thanhtimkiem.text()})
        elif self.cbb_timkiemtheo.currentIndex() == 2:

            loaddata = collection.find({"id_loaihang": list(self.loaihang.keys())[self.tenloaihang.index(self.le_thanhtimkiem.text())]})
        elif self.cbb_timkiemtheo.currentIndex() == 3:
            loaddata = collection.find({"donvitinh": self.le_thanhtimkiem.text()})
        else:
            loaddata = collection.find({"dongia": self.le_thanhtimkiem.text()})


        i = 0
        for data in loaddata:
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data["_id"])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.ncc.get(data["id_ncc"])))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(self.kho.get(data["id_kho"])))
            self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(data["Ngaynhap"])))
            self.tableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem(data["hinhthucthanhtoan"]))
            self.tableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem(data["phuongthucvanchuyen"]))
            self.tableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem(self.nhanvien.get(data["id_nhanvien"])))
            i = i + 1





