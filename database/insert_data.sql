-- 1. Nạp dữ liệu danh mục Khóa học
INSERT INTO KHOAHOC (MaKhoaHoc, TenKhoaHoc, MoTa, SoTinChi) VALUES
('KH001', 'Nhập môn Lập trình', 'Cung cấp tư duy thuật toán và lập trình căn bản.', 3),
('KH002', 'Cơ sở dữ liệu', 'Kiến thức về mô hình quan hệ, ngôn ngữ SQL và thiết kế bảng.', 3);

-- 2. Nạp dữ liệu lý lịch Giảng viên mẫu
INSERT INTO GIANGVIEN (MaGV, TenGV, BoMon, Email, ChuyenNganh, SoDienThoai) VALUES
('GV101', 'Nguyễn Văn A', 'Khoa Khoa học máy tính', 'nguyenvana@edu.vn', 'Kỹ thuật phần mềm', '0909123456'),
('GV102', 'Trần Thị B', 'Khoa Hệ thống thông tin', 'tranthib@edu.vn', 'An toàn thông tin', '0918765432');

-- 3. Nạp dữ liệu danh sách Sinh viên mẫu
INSERT INTO SINHVIEN (MaSV, HoTen, GioiTinh, NgaySinh, NganhHoc, Email, SoDienThoai, DiaChi, NamNhapHoc, TrangThaiHocTap) VALUES
('SV2001', 'Phạm Minh Triết', 'Nam', '2004-03-15', 'Công nghệ thông tin', 'triet.pm@student.edu.vn', '0933111222', 'Quận 1, TP.HCM', 2022, 'Đang học'),
('SV2002', 'Hoàng Khánh Linh', 'Nữ', '2004-07-22', 'Khoa học dữ liệu', 'linh.hk@student.edu.vn', '0944222333', 'Quận 7, TP.HCM', 2022, 'Đang học'),
('SV2003', 'Nguyễn Hải Đăng', 'Nam', '2004-11-05', 'An toàn thông tin', 'dang.nh@student.edu.vn', '0955333444', 'Thủ Đức, TP.HCM', 2022, 'Đang học'),
('SV2004', 'Vũ Phương Thảo', 'Nữ', '2004-01-30', 'Công nghệ thông tin', 'thao.vp@student.edu.vn', '0966444555', 'Bình Thạnh, TP.HCM', 2022, 'Đang học'),
('SV2005', 'Đỗ Gia Bảo', 'Nam', '2004-05-18', 'Hệ thống thông tin', 'bao.dg@student.edu.vn', '0977555666', 'Quận 3, TP.HCM', 2022, 'Đang học');

-- 4. Nạp dữ liệu Lớp học phần mẫu
INSERT INTO LOPHOCPHAN (MaLHP, ThoiGianHoc, DiaDiemHoc, MaGV, MaKhoaHoc) VALUES
('LHP_01', 'Thứ 3, Tiết 1-3', 'Phòng thực hành máy tính PM02', 'GV101', 'KH001'),
('LHP_02', 'Thứ 5, Tiết 4-6', 'Giảng đường lý thuyết A101', 'GV102', 'KH002');

-- 5. Nạp dữ liệu bảng điểm Kết quả học tập thử nghiệm
INSERT INTO KETQUAHOCTAP (MaSV, MaLHP, DiemSo, XepLoai) VALUES
('SV2001', 'LHP_02', 8.50, 'Giỏi'),
('SV2002', 'LHP_02', 9.00, 'Giỏi'),
('SV2003', 'LHP_02', 6.50, 'Khá'),
('SV2004', 'LHP_02', 10.00, 'Xuất sắc'),
('SV2005', 'LHP_02', 4.50, 'Trung bình');

-- 6. Nạp dữ liệu phân công phụ trách chuyên môn (Mối quan hệ N:N)
INSERT INTO PHUTRACH (MaGV, MaKhoaHoc) VALUES
('GV101', 'KH001'),
('GV102', 'KH002');