# Câu 1: 
### Python là một ngôn ngữ thông dịch, điều này nghĩa là ngôn ngữ này trực tiếp chạy từng dòng mã. Nếu có lỗi trong mã chương trình, nó sẽ ngừng chạy. Do đó, lập trình viên có thể nhanh chóng tìm ra lỗi trong đoạn mã.

# Câu 2:

### 1. Các kiểu dữ liệu trong Python

#### Kiểu dữ liệu cơ bản:

| Kiểu dữ liệu | Ví dụ             | Mô tả       |
| ------------ | ----------------- | ----------- |
| `int`        | `1`, `-10`, `200` | Số nguyên   |
| `float`      | `3.14`, `-0.5`    | Số thực     |
| `bool`       | `True`, `False`   | Kiểu logic  |
| `str`        | `'abc'`, "hello"  | Chuỗi ký tự |

#### Kiểu dữ liệu cấu trúc:

| Kiểu dữ liệu | Ví dụ       | Mô tả                     |
| ------------ | ----------- | ------------------------- |
| `list`       | `[1, 2, 3]` | Danh sách có thể thay đổi |
| `tuple`      | `(1, 2)`    | Danh sách không đổi       |
| `dict`       | `{"a": 1}`  | Từ điển (key-value)       |
| `set`        | `{1, 2, 3}` | Tập hợp không trùng lặp   |


### 2. Các toán tử trong Python

#### Toán tử số học:

```python
+, -, *, /, //, %, **
```

#### Toán tử so sánh:

```python
==, !=, >, <, >=, <=
```

#### Toán tử logic:

```python
and, or, not
```

#### Toán tử gán:

```python
=, +=, -=, *=, /=, //=, %=, **=
```


### 3. Mệnh đề điều kiện và vòng lặp

#### Câu lệnh rẽ nhánh (if):

```python
x = 10
if x > 5:
    print("Lớn hơn 5")
elif x == 5:
    print("Bằng 5")
else:
    print("Nhỏ hơn 5")
```

#### Vòng lặp `for`:

```python
for i in range(5):
    print(i)
```

#### Vòng lặp `while`:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### Lệnh điều khiển vòng lặp:

```python
break     # Thoát vòng lặp
continue  # Bỏ qua lần lặp hiện tại
```


### 4. Kiểu dữ liệu `True`, `False`

#### Kiểu `bool`:

```python
True, False
```

#### Quy tắc chuyển về bool:

| Biểu thức                            | Bool value |
| ------------------------------------ | ---------- |
| `0`, `0.0`, `""`, `[]`, `{}`, `None` | `False`    |
| Các giá trị khác                     | `True`     |

#### Ví dụ:

```python
bool(0)      # False
bool(3.14)   # True
bool("")     # False
bool("abc")  # True
```

