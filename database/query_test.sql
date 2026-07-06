USE QuanLySinhVien;
SELECT 
    sv.MaSV AS `Mã Sinh Viên`,
    sv.HoTen AS `Họ Và Tên`,
    kh.TenKhoaHoc AS `Tên Môn Học`,
    gv.TenGV AS `Giảng Viên Hướng Dẫn`,
    kq.DiemSo AS `Điểm Số`,
    kq.XepLoai AS `Xếp Loại`
FROM KETQUAHOCTAP kq
INNER JOIN SINHVIEN sv ON kq.MaSV = sv.MaSV
INNER JOIN LOPHOCPHAN lhp ON kq.MaLHP = lhp.MaLHP
INNER JOIN KHOAHOC kh ON lhp.MaKhoaHoc = kh.MaKhoaHoc
INNER JOIN GIANGVIEN gv ON lhp.MaGV = gv.MaGV
WHERE lhp.MaLHP = 'LHP_02';