# Method `__init__`

Phương thức `__init__` trong Python là một phương thức đặc biệt được gọi khi một đối tượng mới của một `class` được tạo. Đây được gọi là `function` khởi tạo (constructor). Hàm này thường được sử dụng để khởi tạo các thuộc tính của đối tượng



Tin nhắn đã nhận. Phương thức `__init__` trong Python là một phương thức đặc biệt được gọi khi một đối tượng mới của một lớp được tạo. Đây được gọi là hàm khởi tạo (constructor). Hàm này thường được sử dụng để khởi tạo các thuộc tính của đối tượng.

Dưới đây là cú pháp cơ bản của phương thức `__init__`:

```python  
class ClassName:  
def __init__(self, parameter1, parameter2,...):  
self.attribute1 = parameter1  
self.attribute2 = parameter2  
...  
```

Trong đó:  
- `ClassName` là tên của lớp.  
- `__init__` là tên của hàm khởi tạo.  
- `self` là tham chiếu đến đối tượng hiện tại của `class` và được sử dụng để truy cập các biến thuộc về `class` đó. eg: ta có `class` trên là : `ClassName` vậy tham chiếu là gì?.
  -  Khi chúng ta gọi `func` trong `class`: `ClassName` thì `func` đó sẽ lấy các `value` tương ứng có trong `class` `cha`   
- `parameter1, parameter2,...` là các tham số tùy chọn, thường là các giá trị để gán cho các thuộc tính của đối tượng được tạo ra.

Ví dụ, ta có thể tạo một lớp `Person` với hai thuộc tính `name` và `age` như sau:

```python  
class Person:  
def __init__(self, name, age):  
self.name = name  
self.age = age  
```

Sau đó, ta có thể tạo một đối tượng của lớp `Person` và truy cập các thuộc tính của nó như sau:

```python  
p1 = Person("John", 36)  
print(p1.name) # Output: John  
print(p1.age) # Output: 36  
```

Lưu ý rằng Python không cho phép có nhiều hơn một hàm `__init__` trong một lớp và hàm `__init__` không được phép trả về giá trị. Message has links.

