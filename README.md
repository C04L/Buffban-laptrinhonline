# Buffban-laptrinhonline.club
Tool buff bẩn web laptrinhonline với một số options có sẵn, không khuyến khích lạm dụng và chỉ dùng với mục đích tham khảo

# Cài đặt
```
install.bat
```
# Yêu cầu
```
pip 23.3.1
python3
//Còn lại sẽ được cài trong install.bat
```
# Sử dụng
Chỉnh ngôn ngữ mặc định của tài khoản laptrinhonline thành C++
Nếu có thêm bài làm thì import vào folder "dapan" với tên file giống tên tiêu đề của problem (chỉ source của C++)
```
//Xem tính năng
python buffban.py -h
```
Lần đầu sử dụng sẽ mở trình duyệt mới để đăng nhập tài khoản, khởi tạo cookies. Sau đấy thì không cần đăng nhập lại. Nếu muốn sử dụng tài khoản khác thì xóa file cookies.pickle
```
options:
  -h, --help           lệnh help
  -s SLEEP, --sleep SLEEP    Thời gian nghỉ giữa các lần submit bài (Mặc định là 2)
                       
  -c COOKIES_FILE, --cookies_file COOKIES_FILE
                        File nhị phân chứa cookies để đăng nhập vào trình duyệt. Mặc định tại folder chứa file python
  -l LOGIN, --login LOGIN
                       Tên đăng nhập dùng để login (không có cũng được)
  -m MAX, --max MAX     lượng bài tối đa bạn muốn submit (mặc định/tối đa: 510)
  -p PASSWORD, --password PASSWORD
                        Mật khẩu dùng để login (không có cũng được)
```
CHỈ SỬ DỤNG CHO MỤC ĐÍCH THAM KHẢO, MỌI TRƯỜNG HỢP LẠM DỤNG THÌ BẠN TỰ CHỊU TRÁCH NHIỆM
