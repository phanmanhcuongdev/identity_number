# BÁO CÁO BÀI TẬP LỚN NHẬP MÔN TRÍ TUỆ NHÂN TẠO

## Đề tài: Nhận diện chữ số viết tay sử dụng mạng nơ-ron nhân tạo xây dựng từ đầu bằng NumPy

**Học viện Công nghệ Bưu chính Viễn thông** **Khoa Công nghệ thông tin 1** **Lớp:** N09  
**Nhóm:** 01  
**Giảng viên hướng dẫn:** ThS. Vũ Hoài Thư  

---

## Thành viên nhóm

| STT | Họ và tên | Mã sinh viên | Nhiệm vụ chính |
|---:|---|---|---|
| 1 | Phan Mạnh Cường | B23DCCN115 | Lan truyền tiến, xử lý dữ liệu, thực nghiệm |
| 2 | Nguyễn Tuấn Dũng | B23DCCN203 | Lan truyền tiến, trực quan hóa kết quả |
| 3 | Trương Minh Sơn | B23DCCN726 | Lan truyền ngược, công thức toán học |
| 4 | Đàm Quang Phong | B23DCCN642 | Lan truyền ngược, đánh giá mô hình |

---

## Mục lục

- [Chương 1. Giới thiệu và phát biểu bài toán](#chương-1-giới-thiệu-và-phát-biểu-bài-toán)
- [Chương 2. Dữ liệu, tiền xử lý và biểu diễn đặc trưng](#chương-2-dữ-liệu-tiền-xử-lý-và-biểu-diễn-đặc-trưng)
- [Chương 3. Kiến trúc mạng nơ-ron fully connected](#chương-3-kiến-trúc-mạng-nơ-ron-fully-connected)
- [Chương 4. Lan truyền tiến](#chương-4-lan-truyền-tiến)
- [Chương 5. Hàm mất mát Cross-Entropy](#chương-5-hàm-mất-mát-cross-entropy)
- [Chương 6. Lan truyền ngược](#chương-6-lan-truyền-ngược)
- [Chương 7. Tối ưu hóa bằng Batch Gradient Descent](#chương-7-tối-ưu-hóa-bằng-batch-gradient-descent)
- [Chương 8. Cài đặt thực nghiệm bằng NumPy](#chương-8-cài-đặt-thực-nghiệm-bằng-numpy)
- [Chương 9. Kết quả thực nghiệm và phân tích](#chương-9-kết-quả-thực-nghiệm-và-phân-tích)
- [Chương 10. Thí nghiệm siêu tham số](#chương-10-thí-nghiệm-siêu-tham-số)
- [Chương 11. Demo trực quan](#chương-11-demo-trực-quan)
- [Chương 12. Hạn chế và kết luận](#chương-12-hạn-chế-và-kết-luận)

---

# Chương 1. Giới thiệu và phát biểu bài toán

**[Tham chiếu Slide học tập: `0_Introduction`, `4_Machine Learning`]**

Chương này trình bày bối cảnh, mục tiêu và cách mô hình hóa bài toán nhận diện chữ số viết tay dưới góc nhìn học máy. Thay vì chỉ mô tả bài toán bằng ngôn ngữ tự nhiên, báo cáo phát biểu bài toán dưới dạng phân loại đa lớp có giám sát. Đây là bước nền tảng để liên kết dữ liệu đầu vào, mô hình học máy, quá trình huấn luyện và tiêu chí đánh giá kết quả.

## 1.1. Bối cảnh nhận dạng chữ số viết tay trong trí tuệ nhân tạo

Nhận dạng chữ số viết tay là một bài toán kinh điển trong lĩnh vực trí tuệ nhân tạo và thị giác máy tính. Bài toán này có mục tiêu xây dựng một hệ thống có khả năng tiếp nhận ảnh chữ số viết tay và xác định chữ số tương ứng trong tập các lớp từ 0 đến 9. Mặc dù dữ liệu MNIST đã được chuẩn hóa, sự khác biệt về nét viết, độ nghiêng, độ đậm nhạt và phong cách cá nhân vẫn khiến bài toán có ý nghĩa thực nghiệm rõ ràng.

Bài toán này thuộc nhóm nhận dạng mẫu, trong đó hệ thống cần học quy luật từ dữ liệu quá khứ để đưa ra dự đoán cho dữ liệu mới. Trong phạm vi đề tài, nhóm tập trung vào mô hình mạng nơ-ron nhân tạo fully connected được xây dựng từ đầu bằng NumPy, không sử dụng các framework học sâu bậc cao như TensorFlow, Keras hoặc PyTorch.

> 🛑 **[HÀNH ĐỘNG]**: Chèn hình minh họa một số ảnh chữ số viết tay MNIST tại đây. Giải thích chi tiết: Hình cần cho thấy cùng một chữ số có thể được viết theo nhiều kiểu khác nhau, từ đó dẫn vào nhu cầu sử dụng mô hình học máy thay vì luật lập trình thủ công.

## 1.2. Phát biểu bài toán dưới dạng học có giám sát

Dưới góc nhìn học máy, nhận diện chữ số viết tay là bài toán học có giám sát. Mỗi mẫu huấn luyện bao gồm một ảnh đầu vào và một nhãn đúng tương ứng. Mô hình cần học một hàm ánh xạ từ không gian đặc trưng của ảnh sang tập nhãn rời rạc gồm 10 chữ số.

Tập dữ liệu huấn luyện được ký hiệu là:

$$
\mathcal{D} = \{(x^{(i)}, y^{(i)})\}_{i=1}^{m}
$$

Trong đó:

$$
x^{(i)} \in \mathbb{R}^{784}
$$

là vector đặc trưng biểu diễn ảnh thứ $i$, còn:

$$
y^{(i)} \in \{0,1,2,3,4,5,6,7,8,9\}
$$

là nhãn thật của ảnh đó.

Mục tiêu của mô hình là học một hàm dự đoán:

$$
f_{\theta}: \mathbb{R}^{784} \rightarrow \{0,1,2,3,4,5,6,7,8,9\}
$$

Trong đó $\theta$ là tập toàn bộ tham số học được của mạng nơ-ron, bao gồm các ma trận trọng số và vector bias.

## 1.3. Phân tích theo khung Task, Performance, Experience

Theo cách mô tả kinh điển của học máy, một bài toán học cần xác định rõ ba thành phần: nhiệm vụ cần học, tiêu chí đánh giá hiệu năng và kinh nghiệm học được từ dữ liệu. Đối với đề tài này, ba thành phần đó được cụ thể hóa như sau.

| Thành phần | Mô tả trong đề tài |
|---|---|
| Task | Nhận dạng chữ số viết tay từ ảnh mức xám kích thước $28 \times 28$ |
| Performance | Accuracy, Loss, Confusion Matrix và phân tích mẫu sai |
| Experience | 38,000 ảnh huấn luyện có nhãn và 4,000 ảnh dev có nhãn |

Việc mô hình hóa theo khung Task, Performance, Experience giúp báo cáo tránh cách trình bày cảm tính. Mô hình không chỉ được đánh giá bằng việc chạy được code, mà cần được đánh giá bằng số liệu cụ thể trên tập dữ liệu độc lập.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng Task, Performance, Experience đã điền đầy đủ tại đây. Giải thích chi tiết: Bảng cần làm rõ đề tài là một bài toán học có giám sát, trong đó dữ liệu có nhãn được dùng để cải thiện hiệu năng dự đoán.

## 1.4. Mục tiêu nghiên cứu của đề tài

Mục tiêu chính của đề tài không phải là đạt độ chính xác cao nhất bằng mọi cách, mà là xây dựng và phân tích một mạng nơ-ron fully connected từ đầu bằng NumPy. Việc tự cài đặt các bước lan truyền tiến, tính hàm mất mát, lan truyền ngược và cập nhật trọng số giúp nhóm hiểu rõ bản chất toán học bên trong quá trình huấn luyện.

Cụ thể, đề tài hướng đến các mục tiêu sau:

- Mô hình hóa bài toán nhận diện chữ số viết tay dưới dạng bài toán phân loại đa lớp.
- Xây dựng mạng nơ-ron có kiến trúc $784 \rightarrow 128 \rightarrow 10$.
- Cài đặt lan truyền tiến, hàm mất mát Cross-Entropy, lan truyền ngược và Batch Gradient Descent bằng NumPy.
- Đánh giá mô hình bằng loss, accuracy, confusion matrix và phân tích mẫu sai.
- Khảo sát ảnh hưởng của learning rate và số neuron tầng ẩn đến kết quả huấn luyện.

## 1.5. Phạm vi và giới hạn của đề tài

Đề tài giới hạn trong mạng nơ-ron fully connected với một tầng ẩn. Ảnh đầu vào được flatten thành vector 784 chiều, sau đó đưa qua một tầng ẩn ReLU và một tầng đầu ra Softmax. Nhóm không sử dụng các kiến trúc ngoài phạm vi như CNN, RNN hoặc Transformer trong phần triển khai chính.

Việc giới hạn phạm vi giúp báo cáo tập trung vào bản chất cốt lõi của ANN: biểu diễn dữ liệu bằng vector, nhân ma trận, kích hoạt phi tuyến, tính loss, tính gradient và cập nhật tham số. Đây là những thành phần nền tảng để hiểu các mô hình học sâu phức tạp hơn sau này.

---

# Chương 2. Dữ liệu, tiền xử lý và biểu diễn đặc trưng

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Chương này trình bày cách dữ liệu ảnh chữ số viết tay được chuyển đổi thành dạng phù hợp cho mạng nơ-ron fully connected. Trong học máy, chất lượng biểu diễn dữ liệu đầu vào có ảnh hưởng trực tiếp đến khả năng học của mô hình. Do đó, các bước flatten, normalize và one-hot encoding cần được mô tả rõ ràng cả về mặt thao tác lập trình lẫn ý nghĩa toán học.

## 2.1. Cấu trúc bộ dữ liệu

Bộ dữ liệu sử dụng trong đề tài gồm các ảnh chữ số viết tay mức xám kích thước $28 \times 28$ pixel. Mỗi ảnh trong tập huấn luyện có nhãn tương ứng thuộc một trong mười lớp từ 0 đến 9. Trong quá trình thực nghiệm, dữ liệu có nhãn được chia thành tập train và tập dev để đánh giá khả năng tổng quát hóa của mô hình.

Cấu trúc chia dữ liệu được sử dụng như sau:

| Tập dữ liệu | Số lượng mẫu | Có nhãn | Vai trò |
|---|---:|---|---|
| Train | 38,000 | Có | Dùng để cập nhật trọng số |
| Dev | 4,000 | Có | Dùng để đánh giá mô hình trong quá trình huấn luyện |
| Test | 10,000 | Không | Dùng để demo dự đoán trực quan |

Tập test trong đề tài không có nhãn đi kèm, vì vậy không được sử dụng để tính accuracy. Các chỉ số đánh giá định lượng như loss, accuracy và confusion matrix phải được tính trên tập train hoặc tập dev.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng mô tả train, dev và test tại đây. Giải thích chi tiết: Bảng cần nhấn mạnh rằng tập test không có nhãn nên không dùng để tính accuracy, tránh nhầm lẫn giữa demo dự đoán và đánh giá mô hình.

## 2.2. Mẫu, đặc trưng và nhãn

Trong học máy, mỗi ảnh được xem là một mẫu dữ liệu. Các pixel của ảnh đóng vai trò là đặc trưng, còn chữ số tương ứng là nhãn phân loại. Với ảnh kích thước $28 \times 28$, sau khi trải phẳng, mỗi mẫu được biểu diễn bởi một vector gồm 784 phần tử.

Một ảnh đầu vào được ký hiệu:

$$
x^{(i)} = [p_1, p_2, p_3, \ldots, p_{784}]^T
$$

Trong đó $p_j$ là giá trị pixel thứ $j$ của ảnh. Với $m$ mẫu dữ liệu, ma trận đầu vào được biểu diễn dưới dạng:

$$
X = [x^{(1)}, x^{(2)}, x^{(3)}, \ldots, x^{(m)}] \in \mathbb{R}^{784 \times m}
$$

Nhãn của các mẫu được biểu diễn dưới dạng vector one-hot. Với một batch gồm $m$ mẫu, ma trận nhãn $Y$ có shape $(10, m)$:

$$
Y \in \mathbb{R}^{10 \times m}
$$

Cách biểu diễn này cho phép toàn bộ batch dữ liệu được xử lý bằng các phép toán ma trận, giúp quá trình huấn luyện hiệu quả hơn so với việc xử lý từng mẫu riêng lẻ.

## 2.3. Flatten ảnh $28 \times 28$ thành vector 784 chiều

Mạng fully connected yêu cầu dữ liệu đầu vào ở dạng vector một chiều. Vì vậy, mỗi ảnh hai chiều kích thước $28 \times 28$ được trải phẳng thành vector cột có 784 phần tử. Quá trình này không làm thay đổi giá trị pixel, nhưng làm mất cấu trúc không gian hai chiều ban đầu của ảnh.

Công thức biểu diễn:

$$
28 \times 28 = 784
$$

$$
x^{(i)} \in \mathbb{R}^{28 \times 28} \rightarrow x^{(i)} \in \mathbb{R}^{784}
$$

> 🛑 **[HÀNH ĐỘNG]**: Chèn hình minh họa quá trình flatten tại đây. Giải thích chi tiết: Hình cần thể hiện ảnh $28 \times 28$ được trải thành vector 784 chiều, qua đó giải thích vì sao input layer của mạng có 784 neuron.

## 2.4. Chuẩn hóa giá trị pixel

Giá trị pixel ban đầu nằm trong khoảng từ 0 đến 255. Nếu đưa trực tiếp các giá trị này vào mạng, các phép nhân ma trận có thể tạo ra giá trị trung gian lớn, làm quá trình tối ưu kém ổn định. Vì vậy, dữ liệu được chuẩn hóa về khoảng $[0,1]$.

Công thức chuẩn hóa:

$$
x_{\text{norm}} = \frac{x}{255}
$$

Sau chuẩn hóa:

$$
0 \leq x_{\text{norm}} \leq 1
$$

Việc chuẩn hóa giúp các giá trị đầu vào có cùng thang đo, hỗ trợ quá trình gradient descent hội tụ ổn định hơn.

## 2.5. One-hot encoding cho nhãn phân loại

Do bài toán có 10 lớp rời rạc, nhãn số nguyên cần được chuyển thành vector one-hot để phù hợp với đầu ra Softmax. Mỗi vector one-hot có 10 phần tử, trong đó phần tử tương ứng với lớp đúng bằng 1 và các phần tử còn lại bằng 0. Với một batch gồm $m$ mẫu, các vector one-hot được ghép theo cột để tạo thành ma trận nhãn $Y$ có shape $(10, m)$.

Ví dụ, nếu nhãn thật là chữ số 3, vector one-hot tương ứng là:

$$
\begin{aligned}
y &= 3 \Rightarrow
Y =
\begin{bmatrix}
0 \\
0 \\
0 \\
1 \\
0 \\
0 \\
0 \\
0 \\
0 \\
0
\end{bmatrix}
\end{aligned}
$$

Trong cài đặt thực tế, số lớp cần được cố định là 10. Không nên xác định số lớp bằng giá trị lớn nhất xuất hiện trong một batch nhỏ, vì batch đó có thể thiếu một số lớp.

> 🛑 **[HÀNH ĐỘNG]**: Chèn ví dụ one-hot encoding cho nhãn 0, 3 và 9 tại đây. Giải thích chi tiết: Ví dụ cần cho thấy nhãn rời rạc được chuyển thành vector để tính Cross-Entropy với đầu ra Softmax.

---

# Chương 3. Kiến trúc mạng nơ-ron fully connected

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Chương này mô tả kiến trúc mạng nơ-ron được sử dụng trong đề tài. Mạng được thiết kế theo dạng fully connected gồm một tầng đầu vào, một tầng ẩn và một tầng đầu ra. Tất cả các phép tính trong mạng được biểu diễn dưới dạng ma trận để phù hợp với cài đặt NumPy.

## 3.1. Cấu trúc tổng quát của mô hình

Mô hình ANN trong đề tài có kiến trúc:

$$
784 \rightarrow 128 \rightarrow 10
$$

Trong đó:

- Tầng đầu vào gồm 784 neuron, tương ứng với 784 pixel của ảnh sau khi flatten.
- Tầng ẩn gồm 128 neuron, sử dụng hàm kích hoạt ReLU.
- Tầng đầu ra gồm 10 neuron, sử dụng hàm Softmax để sinh xác suất cho 10 lớp chữ số.

Kiến trúc này đủ đơn giản để cài đặt từ đầu bằng NumPy, nhưng vẫn thể hiện được các thành phần cốt lõi của mạng nơ-ron: trọng số, bias, hàm kích hoạt, lan truyền tiến, lan truyền ngược và tối ưu hóa.

> 🛑 **[HÀNH ĐỘNG]**: Chèn sơ đồ kiến trúc mạng $784 \rightarrow 128 \rightarrow 10$ tại đây. Giải thích chi tiết: Sơ đồ cần thể hiện rõ input layer, hidden layer, output layer, ReLU và Softmax.

## 3.2. Ký hiệu tham số của mô hình

Toàn bộ tri thức mà mô hình học được từ dữ liệu nằm trong các tham số. Với mạng gồm một tầng ẩn, tập tham số được ký hiệu:

$$
\theta = \{W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\}
$$

Trong đó:

- $W^{[1]}$ là ma trận trọng số nối tầng đầu vào với tầng ẩn.
- $b^{[1]}$ là vector bias của tầng ẩn.
- $W^{[2]}$ là ma trận trọng số nối tầng ẩn với tầng đầu ra.
- $b^{[2]}$ là vector bias của tầng đầu ra.

Các tham số này ban đầu được khởi tạo ngẫu nhiên hoặc theo một quy tắc xác định, sau đó được cập nhật dần trong quá trình huấn luyện để giảm sai số dự đoán.

## 3.3. Bảng kích thước các ma trận

Việc xác định đúng kích thước ma trận là yêu cầu bắt buộc khi cài đặt ANN từ đầu. Nếu sai kích thước, các phép nhân ma trận trong forward propagation và backward propagation sẽ không thực hiện được.

| Ký hiệu | Kích thước | Ý nghĩa |
|---|---:|---|
| $X$ | $784 \times m$ | Ma trận dữ liệu đầu vào |
| $Y$ | $10 \times m$ | Ma trận nhãn one-hot |
| $W^{[1]}$ | $128 \times 784$ | Trọng số từ input sang hidden |
| $b^{[1]}$ | $128 \times 1$ | Bias tầng hidden |
| $Z^{[1]}$ | $128 \times m$ | Giá trị tuyến tính tầng hidden |
| $A^{[1]}$ | $128 \times m$ | Kích hoạt tầng hidden |
| $W^{[2]}$ | $10 \times 128$ | Trọng số từ hidden sang output |
| $b^{[2]}$ | $10 \times 1$ | Bias tầng output |
| $Z^{[2]}$ | $10 \times m$ | Logits tầng output |
| $A^{[2]}$ | $10 \times m$ | Xác suất dự đoán |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng kích thước ma trận dưới dạng LaTeX hoặc bảng Markdown tại đây. Giải thích chi tiết: Bảng cần giúp người đọc kiểm tra được mọi phép nhân ma trận trong mô hình đều hợp lệ.

## 3.4. Vai trò của trọng số $W$ và bias $b$

Trong mạng nơ-ron, trọng số $W$ quyết định mức độ ảnh hưởng của đầu vào hoặc kích hoạt tầng trước đến neuron tầng sau. Bias $b$ đóng vai trò dịch chuyển ngưỡng kích hoạt, giúp mô hình linh hoạt hơn khi biểu diễn các quan hệ trong dữ liệu.

Một neuron đơn lẻ thực hiện phép tính:

$$
z = w^T x + b
$$

Sau đó giá trị $z$ được đưa qua hàm kích hoạt:

$$
a = f(z)
$$

Trong mạng nhiều neuron, phép tính này được mở rộng thành dạng ma trận để xử lý toàn bộ batch dữ liệu cùng lúc.

## 3.5. Khởi tạo tham số và He Initialization

Khởi tạo tham số ảnh hưởng lớn đến khả năng hội tụ của mô hình. Nếu trọng số quá lớn, giá trị kích hoạt và gradient có thể trở nên bất ổn. Nếu trọng số quá nhỏ, tín hiệu lan truyền qua các tầng có thể bị suy giảm.

Với tầng ẩn sử dụng ReLU, phương pháp He Initialization thường phù hợp hơn so với khởi tạo ngẫu nhiên đơn giản. Công thức khởi tạo cho tầng thứ nhất là:

$$
W^{[1]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{784}}\right)
$$

Với tầng thứ hai:

$$
W^{[2]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{128}}\right)
$$

Bias có thể được khởi tạo bằng 0:

$$
b^{[1]} = 0,\quad b^{[2]} = 0
$$

Trong NumPy, khởi tạo có thể viết theo dạng:

```python
W1 = np.random.randn(128, 784) * np.sqrt(2 / 784)
b1 = np.zeros((128, 1))
W2 = np.random.randn(10, 128) * np.sqrt(2 / 128)
b2 = np.zeros((10, 1))
```

> 🛑 **[HÀNH ĐỘNG]**: Chèn đoạn so sánh giữa khởi tạo cũ và He Initialization tại đây. Giải thích chi tiết: Cần chỉ ra vì sao khởi tạo phù hợp với ReLU giúp tín hiệu ổn định hơn trong quá trình học.

## 3.6. Hàm kích hoạt ReLU ở tầng ẩn

Hàm ReLU được sử dụng ở tầng ẩn để đưa tính phi tuyến vào mô hình. Nếu không có hàm kích hoạt phi tuyến, toàn bộ mạng nhiều tầng sẽ tương đương với một phép biến đổi tuyến tính duy nhất, làm giảm khả năng biểu diễn của mô hình.

Hàm ReLU được định nghĩa:

$$
ReLU(z) = \max(0,z)
$$

Đạo hàm của ReLU là:

$$
\begin{aligned}
ReLU'(z) &= 1, \quad z > 0 \\
ReLU'(z) &= 0, \quad z \leq 0
\end{aligned}
$$

ReLU có ưu điểm là tính toán đơn giản và giúp giảm bớt hiện tượng gradient quá nhỏ so với một số hàm kích hoạt bão hòa như sigmoid trong các mạng nhiều tầng.

## 3.7. Hàm Softmax ở tầng đầu ra

Tầng đầu ra sử dụng Softmax để chuyển logits thành phân phối xác suất trên 10 lớp chữ số. Mỗi phần tử đầu ra biểu diễn mức tin cậy của mô hình rằng ảnh đầu vào thuộc về lớp tương ứng.

Với vector logits $z$, xác suất của lớp $k$ được tính:

$$
\begin{aligned}
Softmax(z_k) &= \frac{e^{z_k}}{\sum_{j=1}^{10} e^{z_j}}
\end{aligned}
$$

Đầu ra Softmax thỏa mãn:

$$
0 \leq A^{[2]}_k \leq 1
$$

và:

$$
\sum_{k=1}^{10} A^{[2]}_k = 1
$$

Nhờ đó, nhãn dự đoán cuối cùng được chọn bằng lớp có xác suất lớn nhất.

---

# Chương 4. Lan truyền tiến

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Lan truyền tiến là quá trình đưa dữ liệu đầu vào đi qua các tầng của mạng để tạo ra dự đoán. Đây là pha suy luận của mô hình, trong đó các tham số hiện tại được sử dụng để tính logits và xác suất đầu ra. Chương này trình bày toàn bộ công thức forward propagation dưới dạng vector hóa để khớp với cài đặt NumPy.

## 4.1. Ý nghĩa của lan truyền tiến

Trong quá trình lan truyền tiến, dữ liệu đầu vào $X$ được nhân với ma trận trọng số, cộng bias, đưa qua hàm kích hoạt và cuối cùng chuyển thành xác suất dự đoán. Quá trình này chưa cập nhật trọng số mà chỉ dùng các tham số hiện tại để tính đầu ra.

Với mạng fully connected trong đề tài, lan truyền tiến gồm hai tầng chính:

- Tầng ẩn: biến đổi dữ liệu pixel thành biểu diễn trung gian.
- Tầng đầu ra: biến biểu diễn trung gian thành xác suất thuộc 10 lớp.

## 4.2. Tính toán tại tầng ẩn

Tại tầng ẩn, mô hình thực hiện phép biến đổi tuyến tính:

$$
Z^{[1]} = W^{[1]}X + b^{[1]}
$$

Sau đó áp dụng hàm ReLU:

$$
A^{[1]} = ReLU(Z^{[1]})
$$

Trong đó:

$$
W^{[1]} \in \mathbb{R}^{128 \times 784}
$$

$$
X \in \mathbb{R}^{784 \times m}
$$

nên:

$$
Z^{[1]} \in \mathbb{R}^{128 \times m}
$$

Since $W^{[1]}X$ results in a $(128, m)$ matrix and $b^{[1]}$ is a $(128, 1)$ vector, NumPy automatically utilizes Broadcasting to add the bias vector to every column of the batch without needing explicit loops.

Kết quả $A^{[1]}$ là biểu diễn trung gian của dữ liệu sau khi đi qua tầng ẩn.

## 4.3. Tính toán tại tầng đầu ra

Tại tầng đầu ra, mô hình tiếp tục thực hiện phép biến đổi tuyến tính:

$$
Z^{[2]} = W^{[2]}A^{[1]} + b^{[2]}
$$

Sau đó áp dụng Softmax:

$$
A^{[2]} = Softmax(Z^{[2]})
$$

Trong đó:

$$
W^{[2]} \in \mathbb{R}^{10 \times 128}
$$

$$
A^{[1]} \in \mathbb{R}^{128 \times m}
$$

nên:

$$
Z^{[2]} \in \mathbb{R}^{10 \times m}
$$

Mỗi cột của $A^{[2]}$ là một vector xác suất 10 chiều tương ứng với một ảnh đầu vào.

## 4.4. Quy tắc dự đoán nhãn

Sau khi có xác suất đầu ra $A^{[2]}$, mô hình chọn lớp có xác suất lớn nhất làm nhãn dự đoán. Quy tắc dự đoán được viết:

$$
\hat{y}^{(i)} = \arg\max_{k \in \{0,1,2,3,4,5,6,7,8,9\}} A_k^{[2],(i)}
$$

Trong cài đặt NumPy, thao tác này tương ứng với việc lấy chỉ số có giá trị lớn nhất theo trục lớp:

```python
predictions = np.argmax(A2, axis=0)
```

Kết quả dự đoán sau đó được so sánh với nhãn thật để tính accuracy.

## 4.5. Bẫy học thuật: tràn số trong Softmax

Công thức Softmax nguyên bản có sử dụng hàm mũ $e^z$. Nếu giá trị logits $z$ quá lớn, phép tính $e^z$ có thể vượt quá giới hạn biểu diễn số của máy tính và gây ra hiện tượng overflow. Đây là vấn đề thường gặp khi chuyển từ công thức toán học sang cài đặt thực tế bằng NumPy.

Để ổn định số học, Softmax được viết lại bằng cách trừ đi giá trị lớn nhất trong mỗi cột logits. Với mẫu thứ $i$, giá trị $\max(Z^{[2],(i)})$ được lấy theo cột tương ứng với riêng mẫu đó, tức là lấy cực đại trên 10 logits của mẫu $i$:

$$
Softmax(z_k^{(i)}) =
\frac{\exp\left(z_k^{(i)} - \max\left(Z^{[2],(i)}\right)\right)}
{\sum_{j=1}^{10} \exp\left(z_j^{(i)} - \max\left(Z^{[2],(i)}\right)\right)}
$$

Việc trừ $\max(Z^{[2],(i)})$ không làm thay đổi kết quả Softmax vì cả tử số và mẫu số đều được nhân với cùng một hệ số trong từng mẫu. Tuy nhiên, thao tác này giúp các giá trị đưa vào hàm mũ nhỏ hơn, tránh overflow. Trong NumPy, phép lấy cực đại theo từng mẫu được cài đặt bằng `np.max(Z, axis=0, keepdims=True)`, trong đó `axis=0` nghĩa là lấy theo chiều hàng cho từng cột mẫu.

Cài đặt ổn định bằng NumPy:

```python
def softmax(Z):
    Z_shifted = Z - np.max(Z, axis=0, keepdims=True)
    exp_Z = np.exp(Z_shifted)
    return exp_Z / np.sum(exp_Z, axis=0, keepdims=True)
```

> 🛑 **[HÀNH ĐỘNG]**: Chèn đoạn giải thích hoặc bảng so sánh Softmax thường và Softmax ổn định tại đây. Giải thích chi tiết: Cần chỉ ra rằng đây là khác biệt giữa việc biết công thức và việc cài đặt công thức an toàn trong máy tính.

## 4.6. Tổng hợp công thức lan truyền tiến

Toàn bộ quá trình lan truyền tiến của mô hình được tóm tắt như sau:

$$
Z^{[1]} = W^{[1]}X + b^{[1]}
$$

$$
A^{[1]} = ReLU(Z^{[1]})
$$

$$
Z^{[2]} = W^{[2]}A^{[1]} + b^{[2]}
$$

$$
A^{[2]} = Softmax(Z^{[2]})
$$

Các công thức này tương ứng trực tiếp với hàm `forward_prop()` trong source code NumPy.

> 🛑 **[HÀNH ĐỘNG]**: Chèn sơ đồ forward propagation tại đây. Giải thích chi tiết: Sơ đồ cần thể hiện dòng dữ liệu đi từ $X$ sang $Z^{[1]}$, $A^{[1]}$, $Z^{[2]}$, $A^{[2]}$.

---

# Chương 5. Hàm mất mát Cross-Entropy

**[Tham chiếu Slide học tập: `3_Prob Inference`, `4_Machine Learning`]**

Hàm mất mát là thước đo mức độ sai lệch giữa dự đoán của mô hình và nhãn thật. Trong bài toán phân loại đa lớp, Cross-Entropy thường được sử dụng cùng với Softmax vì nó đo trực tiếp mức độ mô hình gán xác suất cho lớp đúng. Chương này trình bày công thức Cross-Entropy và ý nghĩa của nó trong quá trình huấn luyện.

## 5.1. Vai trò của hàm mất mát

Accuracy cho biết tỷ lệ dự đoán đúng, nhưng không phản ánh đầy đủ mức độ tự tin của mô hình. Ví dụ, hai mô hình cùng dự đoán đúng một ảnh, nhưng một mô hình gán xác suất 0.95 cho lớp đúng trong khi mô hình còn lại chỉ gán 0.51. Cross-Entropy cho phép đánh giá sâu hơn bằng cách xét xác suất mô hình gán cho nhãn thật.

Trong quá trình huấn luyện, mục tiêu của mô hình là tìm bộ tham số $\theta$ sao cho hàm mất mát đạt giá trị nhỏ nhất:

$$
\theta^* = \arg\min_{\theta} J(\theta)
$$

## 5.2. Cross-Entropy cho một mẫu

Với một mẫu dữ liệu, hàm mất mát Cross-Entropy được định nghĩa:

$$
\begin{aligned}
L^{(i)} &= -\sum_{k=1}^{10} y^{(i)}_k \log(\hat{y}^{(i)}_k + \epsilon)
\end{aligned}
$$

Trong đó:

- $y^{(i)}_k$ là nhãn thật ở dạng one-hot.
- $\hat{y}^{(i)}_k$ là xác suất mô hình dự đoán mẫu thứ $i$ thuộc lớp $k$.
- $\epsilon$ là hằng số nhỏ để tránh lỗi $\log(0)$.

Nếu mô hình gán xác suất cao cho lớp đúng, giá trị loss sẽ nhỏ. Nếu mô hình gán xác suất thấp cho lớp đúng, loss sẽ lớn.

## 5.3. Cross-Entropy cho toàn bộ batch

Với $m$ mẫu dữ liệu, hàm mất mát trung bình trên toàn batch là:

$$
J(\theta) =
-\frac{1}{m}
\sum_{i=1}^{m}
\sum_{k=1}^{10}
Y_k^{(i)} \log\left(A_k^{[2],(i)} + \epsilon\right)
$$

Trong đó $A^{[2]}$ là đầu ra Softmax của mô hình. Công thức này là cơ sở để tính loss trong quá trình huấn luyện và theo dõi mức độ hội tụ của mô hình qua từng iteration.

## 5.4. Ý nghĩa phạt mạnh dự đoán sai nhưng tự tin

Cross-Entropy đặc biệt hữu ích vì nó phạt mạnh các dự đoán sai nhưng có độ tự tin cao. Nếu nhãn thật là 7 nhưng mô hình chỉ gán xác suất rất nhỏ cho lớp 7, giá trị loss sẽ rất lớn.

| Nhãn thật | Xác suất mô hình gán cho nhãn thật | Giá trị loss tương đối |
|---:|---:|---|
| 7 | 0.90 | Thấp |
| 7 | 0.10 | Cao |
| 7 | 0.001 | Rất cao |

Điều này giúp mô hình không chỉ học để dự đoán đúng, mà còn học để phân phối xác suất hợp lý hơn.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng minh họa Cross-Entropy với các xác suất khác nhau tại đây. Giải thích chi tiết: Bảng cần làm rõ vì sao dự đoán sai nhưng tự tin bị phạt nặng.

## 5.5. Cài đặt hàm mất mát trong NumPy

Trong code NumPy, Cross-Entropy được tính bằng cách nhân ma trận one-hot với log của xác suất dự đoán, sau đó lấy tổng và chia cho số mẫu:

```python
epsilon = 1e-8
loss = -np.sum(one_hot_Y * np.log(A2 + epsilon)) / m
```

Hằng số $\epsilon$ giúp tránh trường hợp lấy log của 0. Đây là một chi tiết kỹ thuật nhỏ nhưng quan trọng để đảm bảo chương trình không sinh ra giá trị vô hạn hoặc không xác định.

---

# Chương 6. Lan truyền ngược

**[Tham chiếu Slide học tập: `4_Machine Learning`, `1_Search`]**

Lan truyền ngược là thành phần quan trọng nhất trong quá trình huấn luyện mạng nơ-ron. Nếu lan truyền tiến tạo ra dự đoán, thì lan truyền ngược cho biết từng tham số đã góp phần gây ra sai số như thế nào. Chương này trình bày các đạo hàm cần thiết để cập nhật trọng số và bias của mạng.

## 6.1. Ý nghĩa của lan truyền ngược

Lan truyền ngược là quá trình tính gradient của hàm mất mát theo từng tham số của mô hình. Các gradient này cho biết hướng và mức độ cần điều chỉnh tham số để làm giảm loss.

Các đại lượng cần tính gồm:

$$
\begin{aligned}
&\frac{\partial J}{\partial W^{[1]}},\quad
\frac{\partial J}{\partial b^{[1]}},\quad
\frac{\partial J}{\partial W^{[2]}},\quad
\frac{\partial J}{\partial b^{[2]}}
\end{aligned}
$$

Trong code, các đại lượng này được ký hiệu lần lượt là:

$$
dW^{[1]},\quad db^{[1]},\quad dW^{[2]},\quad db^{[2]}
$$

## 6.2. Quy tắc chuỗi trong Backpropagation

Backpropagation dựa trên quy tắc chuỗi của đạo hàm. Vì loss phụ thuộc vào đầu ra, đầu ra phụ thuộc vào các tầng trước, và các tầng trước phụ thuộc vào tham số, nên gradient được tính bằng cách lan truyền đạo hàm ngược từ output về input.

Ví dụ, gradient của loss theo $W^{[2]}$ có thể hiểu theo dạng:

$$
\begin{aligned}
\frac{\partial J}{\partial W^{[2]}} &= \frac{\partial J}{\partial Z^{[2]}} \frac{\partial Z^{[2]}}{\partial W^{[2]}}
\end{aligned}
$$

Tương tự, gradient tại tầng ẩn cần đi qua đạo hàm của ReLU và ma trận trọng số tầng sau.

## 6.3. Gradient tại tầng đầu ra

Với sự kết hợp giữa Softmax và Cross-Entropy, đạo hàm tại tầng đầu ra có dạng rút gọn rất quan trọng:

$$
dZ^{[2]} = A^{[2]} - Y
$$

Trong đó:

- $A^{[2]}$ là xác suất dự đoán của mô hình.
- $Y$ là nhãn thật ở dạng one-hot.
- $dZ^{[2]}$ biểu diễn sai số tại tầng đầu ra.

Công thức này cho thấy nếu xác suất dự đoán gần với nhãn thật, sai số sẽ nhỏ. Nếu xác suất dự đoán khác xa nhãn thật, sai số sẽ lớn và dẫn đến cập nhật tham số mạnh hơn.

## 6.4. Gradient của $W^{[2]}$ và $b^{[2]}$

Từ $dZ^{[2]}$, gradient của ma trận trọng số tầng đầu ra được tính:

$$
dW^{[2]} = \frac{1}{m} dZ^{[2]}(A^{[1]})^T
$$

Gradient của bias tầng đầu ra:

$$
db^{[2]} = \frac{1}{m}\sum_{i=1}^{m} dZ^{[2],(i)}
$$

Trong NumPy, tổng của $dZ^{[2]}$ để tính $db^{[2]}$ phải được thực hiện theo chiều ngang trên các cột mẫu bằng `np.sum(dZ2, axis=1, keepdims=True) / m`. Tham số `keepdims=True` ngăn mảng bị suy giảm thành rank-1 array có shape $(n,)$ và duy trì đúng shape vector cột $(n, 1)$ để cập nhật tham số bias.

Kích thước của các đại lượng:

$$
dZ^{[2]} \in \mathbb{R}^{10 \times m}
$$

$$
(A^{[1]})^T \in \mathbb{R}^{m \times 128}
$$

nên:

$$
dW^{[2]} \in \mathbb{R}^{10 \times 128}
$$

đúng bằng kích thước của $W^{[2]}$.

## 6.5. Lan truyền lỗi về tầng ẩn

Sai số từ tầng đầu ra được lan truyền ngược về tầng ẩn thông qua ma trận trọng số $W^{[2]}$. Vì tầng ẩn sử dụng ReLU, gradient còn phải nhân với đạo hàm của ReLU.

Công thức:

$$
dZ^{[1]} = (W^{[2]})^T dZ^{[2]} \odot ReLU'(Z^{[1]})
$$

Trong đó $\odot$ là phép nhân từng phần tử. Thành phần $ReLU'(Z^{[1]})$ quyết định neuron nào ở tầng ẩn có đóng góp vào quá trình cập nhật.

## 6.6. Gradient của $W^{[1]}$ và $b^{[1]}$

Sau khi có $dZ^{[1]}$, gradient của trọng số tầng ẩn được tính:

$$
dW^{[1]} = \frac{1}{m} dZ^{[1]}X^T
$$

Gradient của bias tầng ẩn:

$$
db^{[1]} = \frac{1}{m}\sum_{i=1}^{m} dZ^{[1],(i)}
$$

Trong NumPy, tổng của $dZ^{[1]}$ để tính $db^{[1]}$ cũng phải được thực hiện theo chiều ngang trên các cột mẫu bằng `np.sum(dZ1, axis=1, keepdims=True) / m`. Tham số `keepdims=True` ngăn mảng bị suy giảm thành rank-1 array có shape $(n,)$ và duy trì đúng shape vector cột $(n, 1)$ để cập nhật tham số bias.

Kích thước của các đại lượng:

$$
dZ^{[1]} \in \mathbb{R}^{128 \times m}
$$

$$
X^T \in \mathbb{R}^{m \times 784}
$$

nên:

$$
dW^{[1]} \in \mathbb{R}^{128 \times 784}
$$

đúng bằng kích thước của $W^{[1]}$.

## 6.7. Hệ phương trình Backpropagation đầy đủ

Toàn bộ quá trình lan truyền ngược được tóm tắt bằng hệ phương trình sau:

$$
dZ^{[2]} = A^{[2]} - Y
$$

$$
dW^{[2]} = \frac{1}{m} dZ^{[2]} (A^{[1]})^T
$$

$$
db^{[2]} = \frac{1}{m} \sum_{i=1}^{m} dZ^{[2],(i)}
$$

$$
dZ^{[1]} = (W^{[2]})^T dZ^{[2]} \odot ReLU'(Z^{[1]})
$$

$$
dW^{[1]} = \frac{1}{m} dZ^{[1]} X^T
$$

$$
db^{[1]} = \frac{1}{m} \sum_{i=1}^{m} dZ^{[1],(i)}
$$

Hệ công thức này tương ứng trực tiếp với hàm `backward_prop()` trong code NumPy.

> 🛑 **[HÀNH ĐỘNG]**: Chèn sơ đồ lan truyền ngược tại đây. Giải thích chi tiết: Sơ đồ cần thể hiện sai số đi từ $A^{[2]} - Y$ về $W^{[2]}$, $b^{[2]}$, $W^{[1]}$, $b^{[1]}$.

## 6.8. Bảng đối chiếu gradient và ý nghĩa

| Ký hiệu | Kích thước | Ý nghĩa |
|---|---:|---|
| $dZ^{[2]}$ | $10 \times m$ | Sai số tại tầng đầu ra |
| $dW^{[2]}$ | $10 \times 128$ | Gradient của trọng số tầng đầu ra |
| $db^{[2]}$ | $10 \times 1$ | Gradient của bias tầng đầu ra |
| $dZ^{[1]}$ | $128 \times m$ | Sai số lan về tầng ẩn |
| $dW^{[1]}$ | $128 \times 784$ | Gradient của trọng số tầng ẩn |
| $db^{[1]}$ | $128 \times 1$ | Gradient của bias tầng ẩn |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng đối chiếu gradient tại đây. Giải thích chi tiết: Bảng cần giúp người đọc thấy mọi gradient đều có kích thước khớp với tham số tương ứng.

---

# Chương 7. Tối ưu hóa bằng Batch Gradient Descent

**[Tham chiếu Slide học tập: `1_Search`, `4_Machine Learning`]**

Sau khi tính được gradient, mô hình cần cập nhật tham số để làm giảm hàm mất mát. Quá trình này có thể xem như một bài toán tìm kiếm trong không gian tham số, trong đó mục tiêu là tìm bộ trọng số và bias giúp mô hình dự đoán tốt nhất trên dữ liệu huấn luyện. Chương này trình bày thuật toán Batch Gradient Descent và vai trò của learning rate.

## 7.1. Huấn luyện như một bài toán tối ưu

Tập tham số của mạng được ký hiệu:

$$
\theta = \{W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\}
$$

Mục tiêu huấn luyện là tìm bộ tham số tối ưu:

$$
\theta^* = \arg\min_{\theta} J(\theta)
$$

Trong đó $J(\theta)$ là hàm mất mát Cross-Entropy trung bình trên tập huấn luyện. Quá trình huấn luyện không tìm lời giải bằng vét cạn, mà sử dụng gradient để đi dần theo hướng làm giảm loss.

## 7.2. Công thức cập nhật tham số

Với mỗi tầng $l$, tham số được cập nhật theo công thức:

$$
\begin{aligned}
W^{[l]} &:= W^{[l]} - \alpha dW^{[l]} \\
b^{[l]} &:= b^{[l]} - \alpha db^{[l]}
\end{aligned}
$$

Trong đó:

- $\alpha$ là learning rate.
- $dW^{[l]}$ là gradient của loss theo $W^{[l]}$.
- $db^{[l]}$ là gradient của loss theo $b^{[l]}$.

Công thức này cho thấy tham số được điều chỉnh ngược chiều gradient, vì gradient chỉ hướng tăng nhanh nhất của hàm mất mát.

## 7.3. Batch Gradient Descent

Trong Batch Gradient Descent, mỗi lần cập nhật tham số sử dụng toàn bộ tập huấn luyện. Với $m$ mẫu, gradient được tính trung bình trên tất cả các mẫu trước khi cập nhật.

Ưu điểm của Batch Gradient Descent là gradient ổn định vì được tính trên toàn bộ dữ liệu. Tuy nhiên, chi phí tính toán cho mỗi lần cập nhật có thể cao hơn so với các phương pháp cập nhật theo từng mẫu hoặc từng mini-batch.

Trong đề tài này, Batch Gradient Descent phù hợp vì mục tiêu chính là minh họa rõ ràng cơ chế học của mạng nơ-ron từ đầu.

## 7.4. Vai trò của learning rate $\alpha$

Learning rate quyết định độ lớn của mỗi bước cập nhật tham số. Nếu learning rate quá nhỏ, mô hình học chậm và cần nhiều iteration để hội tụ. Nếu learning rate quá lớn, quá trình cập nhật có thể dao động hoặc khiến loss tăng.

Ba trường hợp thường gặp:

| Learning rate | Hiện tượng |
|---:|---|
| Quá nhỏ | Loss giảm chậm, thời gian huấn luyện dài |
| Phù hợp | Loss giảm ổn định, accuracy tăng dần |
| Quá lớn | Loss dao động hoặc phân kỳ |

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ minh họa ảnh hưởng của learning rate tại đây. Giải thích chi tiết: Biểu đồ cần so sánh loss curve khi learning rate nhỏ, vừa và lớn.

## 7.5. Liên hệ với hàm cập nhật trong code

Trong source code NumPy, cập nhật tham số được thực hiện bằng các dòng lệnh:

```python
W1 = W1 - alpha * dW1
b1 = b1 - alpha * db1
W2 = W2 - alpha * dW2
b2 = b2 - alpha * db2
```

Các dòng này tương ứng trực tiếp với công thức Gradient Descent. Đây là bước biến gradient tính được từ Backpropagation thành thay đổi thực tế trong mô hình.

---

# Chương 8. Cài đặt thực nghiệm bằng NumPy

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Chương này trình bày cách triển khai các công thức toán học thành chương trình NumPy. Việc cài đặt từ đầu giúp nhóm quan sát trực tiếp từng bước của quá trình học thay vì phụ thuộc vào thư viện học sâu bậc cao. Mỗi hàm trong code đều cần được đối chiếu với một thành phần toán học tương ứng.

## 8.1. Môi trường thực nghiệm

Thực nghiệm được thực hiện trong môi trường Python với các thư viện xử lý dữ liệu và tính toán cơ bản. Nhóm không sử dụng framework học sâu để đảm bảo toàn bộ quá trình huấn luyện được cài đặt thủ công.

| Thành phần | Mô tả |
|---|---|
| Ngôn ngữ lập trình | Python |
| Tính toán ma trận | NumPy |
| Đọc dữ liệu | Pandas |
| Trực quan hóa | Matplotlib |
| Framework học sâu | Không sử dụng TensorFlow, Keras, PyTorch |
| Phần cứng | Workstation Dual Xeon, 64GB RAM |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng môi trường thực nghiệm tại đây. Giải thích chi tiết: Bảng cần chứng minh việc triển khai là từ đầu bằng NumPy, không dựa vào framework học sâu.

## 8.2. Pipeline huấn luyện tổng quát

Quá trình huấn luyện mô hình gồm các bước chính: đọc dữ liệu, tiền xử lý, khởi tạo tham số, lan truyền tiến, tính loss, lan truyền ngược, cập nhật tham số, đánh giá trên tập dev và lưu mô hình.

Pipeline tổng quát:

$$
\begin{aligned}
\text{Load data} &\rightarrow \text{Preprocess} \rightarrow \text{Initialize parameters} \rightarrow \text{Forward} \\
&\rightarrow \text{Loss} \rightarrow \text{Backward} \rightarrow \text{Update} \rightarrow \text{Evaluate} \rightarrow \text{Save model}
\end{aligned}
$$

> 🛑 **[HÀNH ĐỘNG]**: Chèn sơ đồ pipeline huấn luyện tại đây. Giải thích chi tiết: Sơ đồ cần thể hiện vòng lặp huấn luyện lặp lại qua nhiều iteration.

## 8.3. Bảng ánh xạ công thức toán học với hàm code

| Thành phần toán học | Hàm trong code | Vai trò |
|---|---|---|
| $Z^{[1]} = W^{[1]}X + b^{[1]}$ | `forward_prop()` | Tính tuyến tính tầng ẩn |
| $A^{[1]} = ReLU(Z^{[1]})$ | `ReLU()` | Kích hoạt tầng ẩn |
| $A^{[2]} = Softmax(Z^{[2]})$ | `softmax()` | Tạo xác suất đầu ra |
| $J(\theta)$ | `compute_loss()` | Tính Cross-Entropy Loss |
| $dW, db$ | `backward_prop()` | Tính gradient |
| $W := W - \alpha dW$ | `update_params()` | Cập nhật tham số |
| $\hat{y} = \arg\max(A^{[2]})$ | `get_predictions()` | Dự đoán nhãn |
| Accuracy | `get_accuracy()` | Đánh giá tỷ lệ đúng |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng ánh xạ công thức với code tại đây. Giải thích chi tiết: Bảng cần cho thấy code không phải script rời rạc mà là hiện thực hóa trực tiếp của công thức toán học.

## 8.4. Tính tái lập của thí nghiệm

Để kết quả thực nghiệm có thể kiểm chứng lại, quá trình xáo trộn dữ liệu và khởi tạo tham số cần được cố định bằng seed. Nếu không có seed, mỗi lần chạy có thể tạo ra split dữ liệu và trọng số ban đầu khác nhau, dẫn tới kết quả không ổn định.

Trong code nên thiết lập:

```python
np.random.seed(42)
```

Việc cố định seed không làm mô hình tốt hơn, nhưng giúp quá trình phân tích khoa học trở nên minh bạch và tái lập được.

## 8.5. Lưu và tải mô hình bằng file `.npz`

Sau khi huấn luyện, các tham số đã học được có thể được lưu vào file `.npz`. File này chứa các ma trận trọng số và vector bias, cho phép tái sử dụng mô hình mà không cần huấn luyện lại từ đầu.

Các tham số cần lưu gồm:

$$
W^{[1]},\quad b^{[1]},\quad W^{[2]},\quad b^{[2]}
$$

Ngoài ra, nên lưu thêm metadata như input size, hidden size, output size, learning rate và số iteration để tránh nhầm lẫn khi tải mô hình.

Ví dụ:

```python
np.savez(
    filename,
    W1=W1,
    b1=b1,
    W2=W2,
    b2=b2,
    input_size=784,
    hidden_size=128,
    output_size=10,
    learning_rate=alpha,
    iterations=iterations
)
```

> 🛑 **[HÀNH ĐỘNG]**: Chèn đoạn giải thích file `.npz` tại đây. Giải thích chi tiết: Cần chỉ ra rằng tri thức của mô hình sau huấn luyện được lưu trong trọng số và bias, không nằm trong dữ liệu gốc.

## 8.6. Lưu lịch sử huấn luyện

Để vẽ biểu đồ loss và accuracy, quá trình huấn luyện cần lưu lại lịch sử qua từng iteration. Nếu chỉ in kết quả ra console, báo cáo sẽ không có dữ liệu để phân tích quá trình hội tụ.

Các giá trị cần lưu gồm:

- Iteration.
- Train loss.
- Dev loss.
- Train accuracy.
- Dev accuracy.

Cấu trúc history có thể gồm:

```python
history = {
    "iteration": [],
    "train_loss": [],
    "dev_loss": [],
    "train_acc": [],
    "dev_acc": []
}
```

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng mô tả các trường trong history tại đây. Giải thích chi tiết: Bảng cần cho thấy mỗi biểu đồ trong Chương 9 được sinh từ dữ liệu nào trong quá trình training.

---

# Chương 9. Kết quả thực nghiệm và phân tích

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Chương này trình bày các kết quả định lượng và định tính của mô hình. Một mô hình học máy không chỉ cần chạy được, mà phải được đánh giá bằng số liệu, biểu đồ và phân tích lỗi. Các kết quả trong chương này được lấy từ quá trình huấn luyện và đánh giá trên tập train và dev.

## 9.1. Cấu hình thực nghiệm chính

Cấu hình thực nghiệm chính được sử dụng làm mốc đánh giá cho mô hình ANN. Các siêu tham số như số neuron tầng ẩn, learning rate và số iteration cần được ghi rõ để kết quả có thể tái lập.

| Tham số | Giá trị |
|---|---:|
| Input size | 784 |
| Hidden neurons | 128 |
| Output classes | 10 |
| Learning rate | 0.1 |
| Iterations | 500 |
| Train samples | 38,000 |
| Dev samples | 4,000 |
| Activation hidden | ReLU |
| Activation output | Softmax |
| Loss function | Cross-Entropy |
| Optimizer | Batch Gradient Descent |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng cấu hình thực nghiệm chính tại đây. Giải thích chi tiết: Bảng cần giúp người đọc biết chính xác mô hình được huấn luyện với thiết lập nào.

## 9.2. Phân tích Train Loss và Dev Loss

Loss là chỉ số quan trọng để theo dõi quá trình hội tụ của mô hình. Nếu quá trình huấn luyện diễn ra đúng, train loss thường có xu hướng giảm qua các iteration. Dev loss giúp đánh giá mô hình có tổng quát hóa tốt trên dữ liệu chưa dùng để cập nhật trọng số hay không.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ Train Loss và Dev Loss theo iteration tại đây. Giải thích chi tiết: Biểu đồ cần chỉ ra loss có giảm ổn định hay không, có dấu hiệu dao động hay tăng trở lại trên tập dev hay không.

Nhận xét mẫu cần điền sau khi có kết quả thực nghiệm:

Trong giai đoạn đầu, loss giảm nhanh do mô hình bắt đầu học được các đặc trưng phân biệt cơ bản giữa các chữ số. Ở các iteration sau, tốc độ giảm loss chậm lại, cho thấy mô hình dần tiến gần tới vùng hội tụ. Nếu khoảng cách giữa train loss và dev loss nhỏ, mô hình có khả năng tổng quát hóa tương đối tốt.

## 9.3. Phân tích Train Accuracy và Dev Accuracy

Accuracy đo tỷ lệ mẫu được dự đoán đúng. Trong bài toán nhận dạng chữ số viết tay, accuracy là chỉ số dễ hiểu và phù hợp để đánh giá hiệu năng phân loại. Tuy nhiên, accuracy cần được xem cùng với loss để có cái nhìn đầy đủ hơn về quá trình học.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ Train Accuracy và Dev Accuracy theo iteration tại đây. Giải thích chi tiết: Biểu đồ cần cho thấy accuracy tăng như thế nào qua quá trình huấn luyện và khoảng cách giữa train accuracy với dev accuracy.

Nhận xét mẫu cần điền sau khi có kết quả thực nghiệm:

Train accuracy tăng dần qua các iteration cho thấy mô hình đang cải thiện khả năng phân loại trên dữ liệu huấn luyện. Dev accuracy phản ánh khả năng dự đoán trên dữ liệu chưa dùng để cập nhật trọng số. Nếu train accuracy cao nhưng dev accuracy thấp hơn nhiều, mô hình có thể đang bị overfitting.

## 9.4. Bảng kết quả cuối cùng

Sau khi huấn luyện xong, cần tổng hợp các chỉ số cuối cùng trên tập train và dev. Bảng kết quả giúp người đọc nhanh chóng nắm được hiệu năng của mô hình.

| Metric | Train | Dev |
|---|---:|---:|
| Loss | [Điền train loss cuối cùng] | [Điền dev loss cuối cùng] |
| Accuracy | [Điền train accuracy cuối cùng] | [Điền dev accuracy cuối cùng] |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng kết quả cuối cùng tại đây. Giải thích chi tiết: Bảng cần lấy số liệu thật từ code sau khi huấn luyện, không ghi ước lượng chung chung.

## 9.5. Confusion Matrix

Confusion Matrix cho biết mô hình thường nhầm lớp nào với lớp nào. Với bài toán 10 chữ số, confusion matrix có kích thước $10 \times 10$, trong đó hàng biểu diễn nhãn thật và cột biểu diễn nhãn dự đoán.

Công thức:

$$
\begin{aligned}
C_{ij} &= \big| \{x : y_{\text{true}} = i, y_{\text{pred}} = j\} \big|
\end{aligned}
$$

Trong đó $C_{ij}$ là số mẫu thuộc lớp thật $i$ nhưng được dự đoán thành lớp $j$.

> 🛑 **[HÀNH ĐỘNG]**: Chèn Confusion Matrix $10 \times 10$ trên tập dev tại đây. Giải thích chi tiết: Ma trận cần giúp phân tích các cặp số dễ nhầm như 4 với 9, 3 với 5, 1 với 7.

Nhận xét mẫu cần điền sau khi có confusion matrix:

Các giá trị lớn trên đường chéo chính cho thấy mô hình dự đoán đúng phần lớn các mẫu. Các giá trị ngoài đường chéo cho thấy những cặp lớp dễ bị nhầm lẫn. Những nhầm lẫn này thường xảy ra với các chữ số có hình dạng tương tự hoặc nét viết không rõ ràng.

## 9.6. Phân tích mẫu sai

Phân tích mẫu sai giúp hiểu rõ giới hạn của mô hình. Một số mẫu có thể bị dự đoán sai do nét viết quá mờ, bị nghiêng, thiếu nét hoặc có hình dạng gần với chữ số khác. Đây là phần quan trọng để chứng minh nhóm không chỉ nhìn vào accuracy mà còn hiểu cách mô hình thất bại.

> 🛑 **[HÀNH ĐỘNG]**: Chèn grid các ảnh dự đoán sai tại đây. Giải thích chi tiết: Mỗi ảnh cần hiển thị nhãn thật, nhãn dự đoán và confidence để phân tích nguyên nhân sai.

Mẫu nhận xét cho một ảnh sai:

Mẫu có nhãn thật là 1 nhưng mô hình dự đoán là 7. Nguyên nhân có thể do phần nét trên của chữ số bị kéo ngang, làm hình dạng tổng thể gần với chữ số 7. Vì mô hình fully connected xử lý ảnh sau khi flatten, mô hình không trực tiếp khai thác quan hệ không gian cục bộ giữa các pixel như các kiến trúc chuyên biệt cho ảnh.

## 9.7. Nhận xét tổng quát về kết quả

Kết quả thực nghiệm cho thấy mạng fully connected có thể học được các đặc trưng cơ bản của chữ số viết tay từ dữ liệu MNIST. Tuy nhiên, hiệu năng của mô hình phụ thuộc vào cách khởi tạo, learning rate, số neuron tầng ẩn và số iteration. Các biểu đồ loss, accuracy và confusion matrix cung cấp bằng chứng cụ thể để đánh giá quá trình học của mô hình.

---

# Chương 10. Thí nghiệm siêu tham số

**[Tham chiếu Slide học tập: `4_Machine Learning`, `1_Search`]**

Siêu tham số là các giá trị được lựa chọn trước khi huấn luyện và không được học trực tiếp từ dữ liệu. Trong đề tài này, hai siêu tham số quan trọng được khảo sát là learning rate và số neuron tầng ẩn. Việc thay đổi các siêu tham số giúp đánh giá độ nhạy của mô hình và lựa chọn cấu hình phù hợp hơn.

## 10.1. Mục tiêu của thí nghiệm siêu tham số

Mục tiêu của thí nghiệm siêu tham số là so sánh các cấu hình khác nhau để quan sát ảnh hưởng của chúng đến loss và accuracy. Nếu chỉ chạy một cấu hình duy nhất, báo cáo không đủ cơ sở để kết luận mô hình được lựa chọn là hợp lý.

Các thí nghiệm cần trả lời hai câu hỏi chính:

- Learning rate nào giúp mô hình hội tụ ổn định?
- Số neuron tầng ẩn bao nhiêu là phù hợp với bài toán và dữ liệu hiện tại?

## 10.2. Thí nghiệm thay đổi learning rate

Learning rate ảnh hưởng trực tiếp đến tốc độ và độ ổn định của quá trình tối ưu. Trong thí nghiệm này, số neuron tầng ẩn được giữ cố định là 128, còn learning rate được thay đổi.

| Thí nghiệm | Hidden neurons | Learning rate | Iterations |
|---|---:|---:|---:|
| LR-1 | 128 | 0.01 | 500 |
| LR-2 | 128 | 0.1 | 500 |
| LR-3 | 128 | 0.5 | 500 |

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ so sánh loss theo learning rate tại đây. Giải thích chi tiết: Biểu đồ cần cho thấy learning rate nhỏ học chậm, learning rate phù hợp hội tụ ổn định, learning rate quá lớn có thể dao động.

Nhận xét mẫu cần điền sau khi có kết quả:

Với learning rate nhỏ, loss giảm chậm và mô hình cần nhiều iteration hơn để đạt accuracy tốt. Với learning rate phù hợp, loss giảm ổn định và dev accuracy tăng đều. Với learning rate quá lớn, loss có thể dao động, cho thấy bước cập nhật vượt quá hướng tối ưu.

## 10.3. Thí nghiệm thay đổi số neuron tầng ẩn

Số neuron tầng ẩn quyết định năng lực biểu diễn của mô hình. Nếu số neuron quá ít, mô hình có thể không học đủ đặc trưng của dữ liệu. Nếu số neuron quá nhiều, mô hình có thể tăng chi phí tính toán và có nguy cơ học quá sát dữ liệu huấn luyện.

| Thí nghiệm | Hidden neurons | Learning rate | Iterations |
|---|---:|---:|---:|
| H-1 | 64 | 0.1 | 500 |
| H-2 | 128 | 0.1 | 500 |
| H-3 | 256 | 0.1 | 500 |

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ so sánh accuracy theo số neuron tầng ẩn tại đây. Giải thích chi tiết: Biểu đồ cần cho thấy mô hình có cải thiện khi tăng số neuron hay không, đồng thời theo dõi khoảng cách giữa train và dev accuracy.

## 10.4. Bảng tổng hợp kết quả thí nghiệm

Sau khi chạy các cấu hình, cần tổng hợp kết quả vào một bảng để so sánh trực tiếp.

| Experiment | Hidden | Learning rate | Train Acc | Dev Acc | Train Loss | Dev Loss | Nhận xét |
|---|---:|---:|---:|---:|---:|---:|---|
| LR-1 | 128 | 0.01 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |
| LR-2 | 128 | 0.1 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |
| LR-3 | 128 | 0.5 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |
| H-1 | 64 | 0.1 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |
| H-2 | 128 | 0.1 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |
| H-3 | 256 | 0.1 | [Điền] | [Điền] | [Điền] | [Điền] | [Điền nhận xét] |

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng tổng hợp kết quả thí nghiệm siêu tham số tại đây. Giải thích chi tiết: Bảng phải sử dụng số liệu thật từ code, không được ghi nhận xét chung chung.

## 10.5. Nhận xét overfitting và underfitting

Dựa trên train accuracy, dev accuracy, train loss và dev loss, có thể nhận xét mô hình đang ở trạng thái underfitting, overfitting hoặc tổng quát hóa tốt.

| Hiện tượng | Dấu hiệu |
|---|---|
| Underfitting | Train accuracy thấp và dev accuracy thấp |
| Overfitting | Train accuracy cao nhưng dev accuracy thấp hơn đáng kể |
| Tổng quát hóa tốt | Train accuracy và dev accuracy cùng cao, khoảng cách nhỏ |

Nhận xét mẫu:

Nếu mô hình có train accuracy thấp, điều đó cho thấy mô hình chưa học đủ từ dữ liệu huấn luyện. Nếu train accuracy cao nhưng dev accuracy thấp, mô hình có thể đang ghi nhớ dữ liệu train thay vì học quy luật tổng quát. Cấu hình tốt là cấu hình đạt dev accuracy cao và khoảng cách giữa train với dev không quá lớn.

---

# Chương 11. Demo trực quan

**[Tham chiếu Slide học tập: `4_Machine Learning`]**

Demo trực quan giúp người xem hiểu mô hình hoạt động trên dữ liệu ảnh thật như thế nào. Thay vì chỉ in ra vài dòng text, demo cần hiển thị ảnh, nhãn thật, nhãn dự đoán, confidence và trạng thái đúng hoặc sai. Đây là phần thể hiện khả năng kết nối giữa mô hình toán học và kết quả quan sát được.

## 11.1. Demo nhiều ảnh cùng lúc

Mô hình sau khi huấn luyện được sử dụng để dự đoán nhiều ảnh từ tập dev hoặc test. Với tập dev, có thể hiển thị cả nhãn thật và nhãn dự đoán. Với tập test không có nhãn, chỉ hiển thị nhãn dự đoán và confidence.

Mỗi ảnh nên hiển thị các thông tin:

- True label.
- Predicted label.
- Confidence.
- Đúng hoặc sai.

> 🛑 **[HÀNH ĐỘNG]**: Chèn grid $4 \times 4$ ảnh dự đoán tại đây. Giải thích chi tiết: Mỗi ô ảnh cần có tiêu đề gồm nhãn thật, nhãn dự đoán và confidence.

## 11.2. Quy ước màu đúng và sai

Để demo dễ quan sát, các dự đoán đúng và sai nên được phân biệt bằng màu sắc. Dự đoán đúng có thể hiển thị tiêu đề màu xanh, dự đoán sai có thể hiển thị tiêu đề màu đỏ.

Quy ước:

| Trạng thái | Cách hiển thị |
|---|---|
| Dự đoán đúng | Tiêu đề màu xanh |
| Dự đoán sai | Tiêu đề màu đỏ |

> 🛑 **[HÀNH ĐỘNG]**: Chèn hình demo có màu xanh và đỏ tại đây. Giải thích chi tiết: Hình cần cho thấy mô hình không chỉ dự đoán mà còn có cơ chế trực quan hóa đúng sai.

## 11.3. Hiển thị confidence của mô hình

Confidence là xác suất lớn nhất trong vector Softmax đầu ra:

$$
confidence = \max_{k} A^{[2]}_k
$$

Confidence giúp đánh giá mức độ tự tin của mô hình. Một dự đoán sai với confidence cao là trường hợp đáng chú ý, vì mô hình không chỉ sai mà còn rất tự tin vào kết quả sai.

> 🛑 **[HÀNH ĐỘNG]**: Chèn ví dụ dự đoán đúng confidence cao, dự đoán đúng confidence thấp và dự đoán sai confidence cao tại đây. Giải thích chi tiết: Cần phân tích sự khác nhau giữa đúng sai và mức độ tự tin của mô hình.

## 11.4. Demo mẫu sai tiêu biểu

Bên cạnh các mẫu đúng, báo cáo cần trình bày một số mẫu sai tiêu biểu. Phân tích mẫu sai giúp chỉ ra giới hạn của mô hình và chứng minh nhóm có đánh giá sâu hơn thay vì chỉ khoe accuracy.

Mẫu phân tích:

Ảnh có nhãn thật là 4 nhưng mô hình dự đoán là 9. Quan sát trực quan cho thấy nét viết phía trên của chữ số 4 bị khép lại, làm hình dạng gần giống chữ số 9. Đây là kiểu nhầm lẫn hợp lý vì mô hình fully connected xử lý toàn bộ ảnh dưới dạng vector, không trực tiếp phân tích cấu trúc nét viết theo vùng cục bộ.

> 🛑 **[HÀNH ĐỘNG]**: Chèn 6 đến 12 ảnh dự đoán sai tiêu biểu tại đây. Giải thích chi tiết: Mỗi ảnh cần có phần mô tả nguyên nhân có thể gây nhầm lẫn như nét mờ, nghiêng, thiếu nét hoặc giống lớp khác.

## 11.5. Quy trình demo trong chương trình

Quy trình demo gồm các bước:

1. Tải mô hình đã huấn luyện từ file `.npz`.
2. Chọn ảnh từ tập dev hoặc test.
3. Thực hiện forward propagation để lấy xác suất dự đoán.
4. Lấy nhãn dự đoán bằng `argmax`.
5. Hiển thị ảnh cùng nhãn dự đoán và confidence.

Quy trình này cho thấy mô hình sau huấn luyện có thể được sử dụng lại mà không cần cập nhật trọng số.

---

# Chương 12. Hạn chế và kết luận

**[Tham chiếu Slide học tập: `0_Introduction`, `4_Machine Learning`]**

Chương cuối tổng kết những kết quả đạt được, phân tích hạn chế và nêu phạm vi cải tiến hợp lý. Kết luận cần dựa trên số liệu thực nghiệm đã trình bày ở các chương trước, không nên chỉ viết cảm tính. Đồng thời, báo cáo cần chỉ ra giới hạn tự nhiên của mạng fully connected khi xử lý ảnh.

## 12.1. Kết quả đạt được

Đề tài đã xây dựng được một mạng nơ-ron nhân tạo fully connected từ đầu bằng NumPy để nhận diện chữ số viết tay. Mô hình sử dụng kiến trúc $784 \rightarrow 128 \rightarrow 10$, hàm kích hoạt ReLU ở tầng ẩn, Softmax ở tầng đầu ra, Cross-Entropy Loss và Batch Gradient Descent.

Mẫu câu kết luận cần điền số liệu thật:

Với cấu hình $784 \rightarrow 128 \rightarrow 10$, learning rate $\alpha = [Điền]$ và số iteration $[Điền]$, mô hình đạt train accuracy là $[Điền]$ và dev accuracy là $[Điền]$. Kết quả này cho thấy mô hình có khả năng học được các đặc trưng cơ bản của chữ số viết tay từ dữ liệu huấn luyện.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng tóm tắt kết quả tốt nhất tại đây. Giải thích chi tiết: Bảng cần ghi cấu hình tốt nhất, train accuracy, dev accuracy, train loss và dev loss.

## 12.2. Ý nghĩa học thuật của đề tài

Điểm quan trọng của đề tài là nhóm đã tự cài đặt các thành phần lõi của mạng nơ-ron thay vì sử dụng framework có sẵn. Qua đó, nhóm hiểu rõ cách dữ liệu được biểu diễn thành ma trận, cách lan truyền tiến tạo ra dự đoán, cách Cross-Entropy đo sai số, cách Backpropagation tính gradient và cách Gradient Descent cập nhật trọng số.

Các thành phần đã được cài đặt và phân tích gồm:

- Tiền xử lý dữ liệu ảnh.
- Khởi tạo tham số.
- Forward propagation.
- Softmax ổn định số học.
- Cross-Entropy Loss.
- Backward propagation.
- Batch Gradient Descent.
- Lưu và tải mô hình.
- Trực quan hóa quá trình học.
- Confusion Matrix và phân tích mẫu sai.

## 12.3. Hạn chế của mô hình fully connected

Mặc dù mô hình đạt kết quả nhất định, mạng fully connected có hạn chế khi xử lý ảnh. Do ảnh được flatten thành vector 784 chiều, cấu trúc không gian hai chiều của ảnh không còn được biểu diễn trực tiếp. Điều này khiến mô hình khó khai thác các đặc trưng cục bộ như cạnh, góc, nét cong hoặc quan hệ giữa các vùng lân cận.

Hạn chế chính:

$$
\begin{aligned}
&x \in \mathbb{R}^{28 \times 28} \rightarrow x \in \mathbb{R}^{784}
\end{aligned}
$$

Quá trình flatten giúp dữ liệu phù hợp với ANN fully connected, nhưng làm mất thông tin về vị trí tương đối giữa các pixel. Đây là một trong những nguyên nhân khiến mô hình dễ nhầm lẫn với các chữ số có nét viết bất thường hoặc hình dạng gần giống nhau.

## 12.4. Hạn chế của thực nghiệm

Bên cạnh hạn chế về kiến trúc, thực nghiệm cũng có một số giới hạn. Số lượng siêu tham số được khảo sát còn ít, số iteration có thể chưa đủ tối ưu cho mọi cấu hình, và mô hình chưa sử dụng các kỹ thuật regularization như dropout hoặc weight decay. Tuy nhiên, các giới hạn này phù hợp với phạm vi của đề tài nhập môn, trong đó mục tiêu chính là hiểu bản chất của ANN từ đầu.

Các hạn chế thực nghiệm gồm:

- Chỉ khảo sát một tầng ẩn.
- Chỉ dùng Batch Gradient Descent.
- Chưa khảo sát nhiều seed khác nhau.
- Chưa đánh giá trên tập test có nhãn độc lập.
- Chưa sử dụng regularization.

## 12.5. Hướng cải tiến trong phạm vi hợp lý

Trong phạm vi tiếp tục phát triển từ mô hình hiện tại, nhóm có thể cải tiến bằng cách tăng số thí nghiệm siêu tham số, bổ sung regularization, thử mini-batch gradient descent, cải thiện trực quan hóa và phân tích thêm các mẫu sai. Các cải tiến này vẫn giữ trọng tâm ở mạng fully connected và không làm lệch phạm vi đề tài.

Một số hướng cải tiến:

- Thử nhiều learning rate hơn.
- Thử nhiều số neuron tầng ẩn hơn.
- Thêm mini-batch gradient descent.
- Thêm regularization để giảm overfitting.
- Lưu nhiều checkpoint mô hình.
- Phân tích confidence của các dự đoán sai.
- Tăng chất lượng biểu đồ và demo trực quan.

## 12.6. Kết luận chung

Thông qua đề tài, nhóm đã xây dựng được một hệ thống nhận diện chữ số viết tay dựa trên mạng nơ-ron fully connected từ đầu bằng NumPy. Báo cáo không chỉ trình bày kết quả dự đoán, mà còn phân tích toàn bộ quá trình học từ dữ liệu đầu vào đến cập nhật tham số. Việc kết hợp công thức toán học, code NumPy, biểu đồ thực nghiệm và phân tích lỗi giúp đề tài thể hiện rõ mối liên hệ giữa lý thuyết học máy trên lớp và triển khai thực tế.

Kết luận quan trọng nhất là mạng nơ-ron không phải một hộp đen tuyệt đối. Với mô hình đơn giản $784 \rightarrow 128 \rightarrow 10$, ta có thể theo dõi rõ từng bước: dữ liệu được vector hóa, trọng số được khởi tạo, dự đoán được sinh ra, sai số được đo bằng Cross-Entropy, gradient được lan truyền ngược và tham số được cập nhật bằng Gradient Descent. Đây là nền tảng để tiếp tục học các mô hình học sâu phức tạp hơn trong tương lai.

---

# Phụ lục A. Công thức tổng hợp

## A.1. Forward Propagation

$$
Z^{[1]} = W^{[1]}X + b^{[1]}
$$

$$
A^{[1]} = ReLU(Z^{[1]})
$$

$$
Z^{[2]} = W^{[2]}A^{[1]} + b^{[2]}
$$

$$
A^{[2]} = Softmax(Z^{[2]})
$$

## A.2. ReLU

$$
ReLU(z) = \max(0,z)
$$

$$
\begin{aligned}
ReLU'(z) &= 1, \quad z > 0 \\
ReLU'(z) &= 0, \quad z \leq 0
\end{aligned}
$$

## A.3. Softmax

$$
\begin{aligned}
Softmax(z_k) &= \frac{e^{z_k}}{\sum_{j=1}^{10} e^{z_j}}
\end{aligned}
$$

## A.4. Softmax ổn định số học

$$
Softmax(z_k^{(i)}) =
\frac{\exp\left(z_k^{(i)} - \max\left(Z^{[2],(i)}\right)\right)}
{\sum_{j=1}^{10} \exp\left(z_j^{(i)} - \max\left(Z^{[2],(i)}\right)\right)}
$$

## A.5. Cross-Entropy Loss

$$
J(\theta) =
-\frac{1}{m}
\sum_{i=1}^{m}
\sum_{k=1}^{10}
Y_k^{(i)} \log\left(A_k^{[2],(i)} + \epsilon\right)
$$

## A.6. Backward Propagation

$$
dZ^{[2]} = A^{[2]} - Y
$$

$$
dW^{[2]} = \frac{1}{m} dZ^{[2]} (A^{[1]})^T
$$

$$
db^{[2]} = \frac{1}{m} \sum_{i=1}^{m} dZ^{[2],(i)}
$$

$$
dZ^{[1]} = (W^{[2]})^T dZ^{[2]} \odot ReLU'(Z^{[1]})
$$

$$
dW^{[1]} = \frac{1}{m} dZ^{[1]} X^T
$$

$$
db^{[1]} = \frac{1}{m} \sum_{i=1}^{m} dZ^{[1],(i)}
$$

## A.7. Gradient Descent

$$
W^{[l]} := W^{[l]} - \alpha dW^{[l]}
$$

$$
b^{[l]} := b^{[l]} - \alpha db^{[l]}
$$

## A.8. He Initialization

$$
W^{[1]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{784}}\right)
$$

$$
W^{[2]} \sim \mathcal{N}\left(0, \sqrt{\frac{2}{128}}\right)
$$

---

# Phụ lục B. Checklist hoàn thiện báo cáo

| Hạng mục | Trạng thái |
|---|---|
| Có phát biểu bài toán theo học có giám sát | [Điền] |
| Có Task, Performance, Experience | [Điền] |
| Có bảng kích thước ma trận | [Điền] |
| Có công thức Forward Propagation | [Điền] |
| Có giải thích Softmax và xác suất | [Điền] |
| Có giải thích overflow trong Softmax | [Điền] |
| Có Cross-Entropy Loss | [Điền] |
| Có công thức Backpropagation đầy đủ | [Điền] |
| Có Gradient Descent và learning rate | [Điền] |
| Có He Initialization | [Điền] |
| Có biểu đồ Train Loss và Dev Loss | [Điền] |
| Có biểu đồ Train Accuracy và Dev Accuracy | [Điền] |
| Có Confusion Matrix | [Điền] |
| Có phân tích mẫu sai | [Điền] |
| Có thí nghiệm learning rate | [Điền] |
| Có thí nghiệm số neuron tầng ẩn | [Điền] |
| Có demo ảnh đúng sai kèm confidence | [Điền] |
| Có kết luận dựa trên số liệu thật | [Điền] |
