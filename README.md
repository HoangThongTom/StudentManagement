# Hệ thống Quản lý Sinh viên

## Giới thiệu

Hệ thống Quản lý Sinh viên là một ứng dụng web được xây dựng bằng Python và Flask nhằm hỗ trợ quản lý thông tin sinh viên, môn học và điểm số. Hệ thống áp dụng cơ chế phân quyền người dùng (Role-Based Access Control - RBAC) để đảm bảo mỗi người dùng chỉ được thực hiện các chức năng phù hợp với vai trò của mình.

## Chức năng chính
* Phân quyền người dùng (RBAC).
* Quản lý sinh viên:

  * Thêm sinh viên.
  * Chỉnh sửa thông tin sinh viên.
  * Xóa sinh viên.
  * Xem danh sách sinh viên.
* Quản lý môn học:

  * Thêm môn học.
  * Chỉnh sửa môn học.
  * Xóa môn học.
  * Xem danh sách môn học.
* Quản lý điểm:

  * Thêm điểm.
  * Cập nhật điểm.
  * Xóa điểm.
  * Xem danh sách điểm.
* Tìm kiếm sinh viên.
* Giao diện thân thiện, dễ sử dụng.

## Công nghệ sử dụng

* Python 3
* Flask
* SQLite
* SQLAlchemy
* HTML5
* CSS3
* Bootstrap 5
* Jinja2

## Cấu trúc dự án

```text
StudentManagement/
│
├── app.py
├── models.py
├── config.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── students/
│   ├── courses/
│   └── scores/
│
├── static/
│   ├── css/
│ 
├── database/
│
└── README.md
```

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

### 6. Chạy chương trình

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập:

```text
http://127.0.0.1:5000
```

## Cơ sở dữ liệu

Hệ thống sử dụng **SQLite** làm cơ sở dữ liệu.

Các bảng dữ liệu chính gồm:

* Người dùng (Users)
* Sinh viên (Students)
* Môn học (Courses)
* Điểm số (Scores)

## Thành viên nhóm

| STT |        Họ và tên     | 
| --- | ---------------------|  
|  1  |  Lâm Văn Hậu         |      
|  2  |  Trần Thanh Tâm      |      
|  3  |  Trần Hoàng Thông    |      
|  4  |  Ngô Huỳnh Thu Loan  |      
|  5  |  Lê Tấn Phát         |      

## Hướng phát triển

* Xuất báo cáo ra Excel hoặc PDF.
* Thống kê dữ liệu bằng biểu đồ.
* Bổ sung trang hồ sơ sinh viên.
* Gửi thông báo qua email.
* Xây dựng REST API.
* Chức năng quên và đặt lại mật khẩu.
* Đăng nhập và đăng xuất hệ thống.

## Giấy phép

Dự án được thực hiện phục vụ mục đích học tập và nghiên cứu.
