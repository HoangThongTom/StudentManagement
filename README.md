# Hệ thống Quản lý Sinh viên

## Giới thiệu

Hệ thống Quản lý Sinh viên là một ứng dụng web được phát triển bằng **Python**, **Flask** và **MySQL** nhằm hỗ trợ quản lý thông tin sinh viên, giảng viên, môn học, lớp học phần, điểm học tập và phân công giảng dạy. Hệ thống cung cấp giao diện trực quan, dễ sử dụng, giúp việc quản lý dữ liệu trở nên thuận tiện và hiệu quả.

---

## Chức năng chính

### Dashboard
- Thống kê tổng số sinh viên.
- Thống kê tổng số giảng viên.
- Thống kê tổng số môn học.
- Hiển thị điểm trung bình (GPA).
- Hiển thị danh sách sinh viên gần đây.

### Quản lý sinh viên
- Thêm sinh viên.
- Chỉnh sửa thông tin sinh viên.
- Xóa sinh viên.
- Tìm kiếm sinh viên.
- Xem danh sách sinh viên.

### Quản lý giảng viên
- Thêm giảng viên.
- Chỉnh sửa giảng viên.
- Xóa giảng viên.
- Tìm kiếm giảng viên.
- Xem danh sách giảng viên.

### Quản lý môn học
- Thêm môn học.
- Chỉnh sửa môn học.
- Xóa môn học.
- Tìm kiếm môn học.
- Xem danh sách môn học.

### Quản lý lớp học phần
- Thêm lớp học phần.
- Chỉnh sửa lớp học phần.
- Xóa lớp học phần.
- Xem danh sách lớp học phần.

### Quản lý điểm học tập
- Thêm điểm.
- Chỉnh sửa điểm.
- Xóa điểm.
- Xem danh sách điểm.

### Quản lý phân công giảng dạy
- Phân công giảng viên phụ trách môn học.
- Xóa phân công.
- Xem danh sách phân công.

---

## Công nghệ sử dụng

- Python 3
- Flask
- SQLAlchemy
- MySQL
- PyMySQL
- HTML5
- CSS3
- Bootstrap 5
- Jinja2

---

## Cấu trúc dự án

```text
StudentManagement/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── create_table.sql
│   ├── insert_data.sql
│   └── query_test.sql
│
├── models/
│   ├── assignment.py
│   ├── classroom.py
│   ├── lecturer.py
│   ├── score.py
│   ├── student.py
│   └── subject.py
│
├── routes/
│   ├── assignment.py
│   ├── classroom.py
│   ├── dashboard.py
│   ├── lecturer.py
│   ├── score.py
│   ├── student.py
│   └── subject.py
│
├── templates/
│   ├── assignment/
│   ├── classroom/
│   ├── lecturer/
│   ├── score/
│   ├── student/
│   ├── subject/
│   ├── base.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│
└── utils/
    └── database.py
```

---

## Hướng dẫn cài đặt

### 1. Sao chép dự án

```bash
git clone https://github.com/HoangThongTom/StudentManagement.git
```

### 2. Di chuyển vào thư mục dự án

```bash
cd StudentManagement
```

### 3. Tạo môi trường ảo

```bash
python -m venv venv
```

### 4. Kích hoạt môi trường ảo

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 5. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 6. Tạo cơ sở dữ liệu

Mở MySQL và thực hiện lần lượt:

1. `create_table.sql`
2. `insert_data.sql`

### 7. Cấu hình kết nối

Chỉnh sửa thông tin trong file `.env` hoặc `config.py` cho phù hợp với máy của bạn.

Ví dụ:

```text
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=QuanLySinhVien
```

### 8. Chạy chương trình

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập:

```text
http://127.0.0.1:5000
```

---

## Cơ sở dữ liệu

Hệ thống sử dụng **MySQL**.

Các bảng dữ liệu chính:

- SINHVIEN
- GIANGVIEN
- KHOAHOC
- LOPHOCPHAN
- KETQUAHOCTAP
- PHUTRACH

---

## Thành viên nhóm

| STT | Họ và tên |
|:--:|------------------------|
| 1 | Lâm Văn Hậu |
| 2 | Trần Thanh Tâm |
| 3 | Trần Hoàng Thông |
| 4 | Ngô Huỳnh Thu Loan |
| 5 | Lê Tấn Phát |

---

## Hướng phát triển

- Xây dựng chức năng đăng nhập và phân quyền người dùng.
- Thống kê dữ liệu bằng biểu đồ trực quan.
- Xuất báo cáo ra Excel hoặc PDF.
- Thêm chức năng phân trang cho danh sách dữ liệu.
- Gửi thông báo qua Email.
- Xây dựng RESTful API.
- Hỗ trợ tải lên ảnh đại diện sinh viên và giảng viên.
- Tối ưu giao diện trên thiết bị di động (Responsive).

---

## Giấy phép

Dự án được thực hiện phục vụ mục đích học tập và nghiên cứu tại Trường Đại học Giao thông Vận tải Thành phố Hồ Chí Minh (UTH).
