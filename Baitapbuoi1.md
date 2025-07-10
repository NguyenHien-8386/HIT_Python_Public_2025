Câu 1:

- Python là ngôn ngữ thông dịch vì nó chạy trực tiếp qua trình thông dịch mà không cần biên dịch sang mã máy, mặc dù có bước biên dịch tạm thời sang bytecode trung gian.
- tại vì : Python là ngôn ngữ thông dịch vì mục tiêu thiết kế là đơn giản, dễ dùng, chạy linh hoạt và thuận tiện cho lập trình viên – đặc biệt phù hợp với học tập, thử nghiệm, web, AI,...
  Nó không tạo ra file thực thi trực tiếp như C/C++ mà chạy thông qua máy ảo (PVM) → đó là lý do cốt lõi.

  Câu 2:

* Các kiểu dữu liệu trong Python là:

Trong Python, có nhiều kiểu dữ liệu khác nhau được sử dụng để lưu trữ và xử lý thông tin. Dưới đây là các kiểu dữ liệu chính:

1. Kiểu dữ liệu cơ bản
   int: Số nguyên (e.g., 1, -5, 100).
   float: Số thực (e.g., 3.14, -0.5, 2.0).
   complex: Số phức (e.g., 1+2j, 3-4j).
   bool: Giá trị logic (True, False).
   str: Chuỗi ký tự (e.g., "Hello", 'Python').
2. Kiểu dữ liệu cấu trúc
   list: Danh sách (e.g., [1, 2, 3], ['a', 'b', 'c']).
   tuple: Bộ giá trị không thay đổi (e.g., (1, 2, 3), ('x', 'y', 'z')).
   set: Tập hợp không có thứ tự, không trùng lặp (e.g., {1, 2, 3}, {'a', 'b', 'c'}).
   dict: Từ điển (cặp key-value) (e.g., {'name': 'Alice', 'age': 25}).
3. Kiểu dữ liệu đặc biệt
   NoneType: Đại diện cho giá trị không có (e.g., None).
4. Kiểu dữ liệu nâng cao
   bytes: Dữ liệu nhị phân (e.g., b'hello').
   bytearray: Giống bytes nhưng có thể thay đổi.
   memoryview: Cung cấp giao diện bộ nhớ của đối tượng nhị phân.
5. Kiểu dữ liệu do người dùng định nghĩa
   Class/Objects: Bạn có thể tạo kiểu dữ liệu riêng bằng cách định nghĩa lớp (class).

- Các toán tử trong python là:

* toán tử số học:

1. toán tử cộng ( + ) vd: a + b
2. toán tử trừ ( - ) vd: 2 - b
3. toán tử nhân ( _ ) vd: a _ b
4. toán tử chia lấy phần thực ( / ) vd: a / b
5. toán tử chia lấy phần nguyên ( // ) vd: a // b
6. toán tử chia lấy dư ( % ) vd: a % b
7. toán tử lũy thừa ( ** ) vd:a ** b ( a mũ b)

- toán tử so sánh:

1. toán tử bằng ( == ) vd: a == b
2. toán tử khác ( != ) vd: a != b
3. toán tử lớn hơn ( > ) vd: a > b
4. toán tử nhỏ hơn ( < ) vd: a < b
5. toán tử lớn hơn bằng ( >= ) vd: a >= b
6. toán tử nhỏ hơn bằng ( <= ) vd: a <= b

- toán tử logic:

1. toán tử and ( and ) vd: a < 10 and b > 5
2. toán tử hoặc ( or ) vd: a > 3 or b < 4
3. toán tử phủ định ( not) vd: not( a > 5 )

- toán tử gán:

1. toán tử gán ( = ) vd: a = 12
2. tón tử cộng rồi gán ( += ) vd: a += 3
3. toán tử trừ rồi gán ( -= ) vd a -= 4
4. toán tử chia lấy phần thực rồi gán ( /= ) vd: a /= 3
5. toán tử chia lấy phần nguyên rồi gán ( //= )vd a //= 6
6. toán tử chia lấy phần dư rồi gán ( %= ) vd: a %= 7
7. toán tử nhân rồi gán ( _= ) vd: a _= 4
8. toán tử lấy lũy thừ rồi gán ( **=) vd: a **= 3

- toán tư kiểm tra:

1. kiểm tra phần tử thuộc tập: ( in ) vd: 'a' in 'abc'
2. không thuộc tập ( not in ) vd: 'a' not in 'xyz'

- toán tử so sánh đối tượng:

1. ( is ) cùng đối tượng trong bộ nhớ vd: a is b
2. ( not is ) không cùng đối tượng trong bộ nhớ vd: a not is b

- toán tử bit:

1. toán tử & ( and ) vd a & b
2. toán tử ` vd: OR
3. toán tử ^ ( XOR ) vd: a ^ b
4. toán tử ~ ( NOT phủ dịnh ) vd: ~a
5. toán tử dịch trái << vd: <<2
6. toán tử dịch phải: >> vd: >>3

- mệnh đề diều kiện:
  if điều_kiện_1: # khối lệnh 1
  elif điều_kiện_2: # khối lệnh 2
  else: # khối lệnh 3
- vòng lặp for:
  for biến in dãy: # khối lệnh
  vd1: for i in range(5):
  print(i) # In ra: 0 1 2 3 4 ( từng dòng )
  vd2:for ch in "Hiến":
  print(ch) # In ra: H I Ế N ( từng dòng)
- vòng lặp while:
  while điều_kiện: # khối lệnh
  vd1: i = 1
  while i <= 5:
  print(i)
  i += 1
  //
  các từ khóa điều khiển vòng lặp:

* break: thoát khỏi vòng lặp
* continue: bỏ qua vòng lặp hiện tại, tiếp tục lần sau
* pass: bỏ qua không làm gì cả
  vd1: for i in range(10):
  if i == 5:
  break
  print(i) # In ra: 0 1 2 3 4
  vd2: for i in range(5):
  if i == 2:
  continue
  print(i) # In ra: 0 1 3 4
  //
* Kiểu dữ liệu True, False:

- chỉ có 2 giá trị tru, false
- dùng trong điêu kiện, so sánh, vòng lặp
- khi là true khi nào là false

* Python coi một số giá trị là False, còn lại là True khi ép kiểu
  // Sử dụng True và False trong điều kiện
  vd!: x = 10
  if x > 5:
  print("x lớn hơn 5") # vì x > 5 trả về True
  // So sánh trả về True hoặc False
  vd2: a = 3
  b = 5
  print(a == b) # False
  print(a < b) # True
  // Toán tử logic trả về True hoặc False
  vd3: x = 7
  print(x > 5 and x < 10) # True
  print(not x == 7) # False
