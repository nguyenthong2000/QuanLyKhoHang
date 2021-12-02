import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://hoangthong:hoangthong16@onmyojibot.fgbvh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client["QuanLyKhoHang"]
collection= db["DonDatHang"]
db_NhanVien = db["NhanVien"]
db_NCC = db["NhaCungCap"]
db_Kho = db["Kho"]
db_MatHang = db["MatHang"]


find_ncc = db_NCC.find()
ncc = list(find_ncc)

print((ncc[10])["_id"])