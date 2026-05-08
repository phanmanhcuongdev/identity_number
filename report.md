# BÁO CÁO BÀI TẬP LỚN NHẬP MÔN TRÍ TUỆ NHÂN TẠO

## Đề tài: Nhận diện chữ số viết tay MNIST sử dụng mạng nơ-ron kết nối đầy đủ cài đặt từ đầu bằng NumPy

Báo cáo trình bày quá trình xây dựng, huấn luyện và đánh giá mô hình mạng nơ-ron nhân tạo kết nối đầy đủ cho bài toán nhận diện chữ số viết tay MNIST. Mô hình được cài đặt từ đầu bằng `NumPy`, không sử dụng framework học sâu bậc cao, nhằm làm rõ bản chất của các bước lan truyền tiến, lan truyền ngược, tính hàm mất mát và cập nhật tham số. Bên cạnh phần thực nghiệm trên dữ liệu MNIST, đề tài còn định hướng tích hợp Web Demo để kiểm thử khả năng nhận diện trên nét vẽ thực tế của người dùng.

---

# Phần mở đầu

Phần mở đầu cung cấp các thông tin hành chính, hình thức và định hướng tổng quan của báo cáo. Các nội dung như trang bìa, phân công nhiệm vụ, lời cảm ơn, mục lục và các danh mục được trình bày nhằm bảo đảm báo cáo có cấu trúc rõ ràng trước khi đi vào phần chuyên môn. Đây là cơ sở để người đọc nắm được thông tin nhóm thực hiện, phạm vi đề tài và cách tổ chức tài liệu.

---

## Trang bìa

**Học viện Công nghệ Bưu chính Viễn thông**  
**Khoa Công nghệ thông tin 1**

**BÁO CÁO BÀI TẬP LỚN**  
**Môn học:** Nhập môn Trí tuệ Nhân tạo

**Đề tài:** Nhận diện chữ số viết tay MNIST sử dụng mạng nơ-ron kết nối đầy đủ cài đặt từ đầu bằng NumPy  
**Mở rộng:** Kèm tính năng Web Demo nhận diện nét vẽ thực tế

**Lớp:** N09  
**Nhóm:** 01  
**Giảng viên hướng dẫn:** ThS. Vũ Hoài Thư

**Thành viên thực hiện:**

| STT | Họ và tên | Mã sinh viên | Vai trò chính |
|---:|---|---|---|
| 1 | Phan Mạnh Cường | B23DCCN115 | Core ANN, xử lý dữ liệu, thực nghiệm |
| 2 | Nguyễn Tuấn Dũng | B23DCCN203 | Lan truyền tiến, trực quan hóa |
| 3 | Trương Minh Sơn | B23DCCN726 | Lan truyền ngược, toán học |
| 4 | Đàm Quang Phong | B23DCCN642 | Lan truyền ngược, đánh giá |

**Hà Nội, 2026**

---

## Phân công nhiệm vụ

Quá trình thực hiện đề tài được phân chia theo các nhóm công việc chính gồm xây dựng mô hình, xử lý dữ liệu, triển khai thuật toán, đánh giá thực nghiệm và trình bày báo cáo. Việc phân công nhiệm vụ giúp bảo đảm mỗi thành viên có trách nhiệm rõ ràng, đồng thời tạo điều kiện để các phần lý thuyết, cài đặt và thực nghiệm được liên kết thống nhất.

| STT | Thành viên | Mã sinh viên | Nhiệm vụ phụ trách |
|---:|---|---|---|
| 1 | Phan Mạnh Cường | B23DCCN115 | Thiết kế lõi ANN bằng `NumPy`, xử lý dữ liệu MNIST, tổ chức thực nghiệm và tổng hợp kết quả huấn luyện |
| 2 | Nguyễn Tuấn Dũng | B23DCCN203 | Phân tích và trình bày lan truyền tiến, hỗ trợ trực quan hóa kết quả, biểu đồ và minh họa dự đoán |
| 3 | Trương Minh Sơn | B23DCCN726 | Phân tích lan truyền ngược, hệ thống hóa công thức toán học, kiểm tra tính đúng đắn của gradient |
| 4 | Đàm Quang Phong | B23DCCN642 | Phân tích lan truyền ngược, đánh giá mô hình, nhận xét kết quả và hỗ trợ phân tích lỗi |

---

## Lời cảm ơn

Nhóm thực hiện xin gửi lời cảm ơn chân thành đến ThS. Vũ Hoài Thư, giảng viên hướng dẫn học phần Nhập môn Trí tuệ Nhân tạo, đã định hướng nội dung, cung cấp nền tảng lý thuyết và hỗ trợ nhóm trong quá trình triển khai bài tập lớn. Nhóm cũng xin cảm ơn Học viện Công nghệ Bưu chính Viễn thông và Khoa Công nghệ thông tin 1 đã tạo điều kiện học tập, thực hành và nghiên cứu trong suốt quá trình thực hiện đề tài. Bên cạnh đó, các thành viên trong nhóm đã phối hợp trong việc phân tích thuật toán, cài đặt mô hình, kiểm thử và hoàn thiện báo cáo. Những đóng góp này là cơ sở quan trọng giúp nhóm hoàn thành đề tài một cách nghiêm túc và có hệ thống.

---

## Mục lục

Mục lục sẽ được tạo tự động bởi LaTeX.

---

## Danh mục hình vẽ

Danh mục hình vẽ sẽ được tạo tự động bởi LaTeX.

---

## Danh mục bảng biểu

Danh mục bảng biểu sẽ được tạo tự động bởi LaTeX.

---

## Danh mục thuật ngữ và từ viết tắt

Danh mục thuật ngữ và từ viết tắt sẽ được tạo tự động bởi LaTeX.

---

# Chương 1. Giới thiệu đề tài

Chương 1 trình bày bối cảnh hình thành đề tài, mục tiêu nghiên cứu, phạm vi thực hiện và định hướng giải pháp tổng quát. Nội dung chương được xây dựng theo trình tự từ nhu cầu thực tế của bài toán nhận diện chữ số viết tay đến lý do lựa chọn mạng nơ-ron kết nối đầy đủ tự cài đặt bằng `NumPy`. Chương này cũng nêu rõ cách nhóm tổ chức quá trình thực nghiệm, đánh giá mô hình và mở rộng kiểm thử bằng Web Demo nhận diện nét vẽ thực tế.

---

## 1.1. Đặt vấn đề

Nhận diện chữ số viết tay là một bài toán kinh điển trong lĩnh vực trí tuệ nhân tạo, học máy và thị giác máy tính. Mặc dù bài toán đã được nghiên cứu rộng rãi, nó vẫn có giá trị học thuật cao vì cho phép người học tiếp cận đầy đủ quy trình xây dựng một mô hình học máy: biểu diễn dữ liệu, thiết kế mô hình, lan truyền tiến, tính sai số, lan truyền ngược, cập nhật tham số và đánh giá kết quả. Trong phạm vi học phần Nhập môn Trí tuệ Nhân tạo, bài toán này phù hợp để minh họa mối liên hệ giữa công thức toán học và triển khai chương trình thực tế.

Với dữ liệu MNIST, mỗi ảnh chữ số viết tay được chuẩn hóa về kích thước $28 \times 28$ và có nhãn thuộc một trong 10 lớp chữ số từ $0$ đến $9$. Đề tài lựa chọn mô hình mạng nơ-ron kết nối đầy đủ nhằm tập trung vào cơ chế cơ bản của ANN trước khi mở rộng sang các kiến trúc phức tạp hơn. Việc tự cài đặt mô hình bằng `NumPy` giúp nhóm hiểu rõ bản chất tính toán thay vì chỉ sử dụng các thư viện học sâu có sẵn.

---

### 1.1.1. Bài toán nhận diện chữ số viết tay trong thực tế

Trong thực tế, chữ số viết tay xuất hiện trong nhiều dạng tài liệu như biểu mẫu khảo sát, phiếu đăng ký, mã bưu chính, số tiền trên chứng từ, mã định danh, phiếu điểm hoặc các tài liệu hành chính cần số hóa. Nếu các thông tin này được nhập thủ công, quá trình xử lý có thể tốn thời gian và dễ phát sinh sai sót. Do đó, việc tự động nhận diện chữ số viết tay có ý nghĩa trong các hệ thống cần chuyển đổi dữ liệu từ dạng giấy hoặc ảnh sang dữ liệu số.

Bài toán nhận diện chữ số viết tay yêu cầu mô hình tiếp nhận ảnh đầu vào và đưa ra nhãn dự đoán tương ứng. Khó khăn của bài toán nằm ở sự đa dạng của nét viết, độ nghiêng, độ dày nét, vị trí chữ số trong khung ảnh và phong cách cá nhân của người viết. Đây là lý do các phương pháp học máy, đặc biệt là mạng nơ-ron nhân tạo, phù hợp hơn so với cách xây dựng luật thủ công cố định.

---

### 1.1.2. Nhu cầu trực quan hóa mô hình nhận diện cho người dùng

Bên cạnh việc đánh giá mô hình trên tập dữ liệu chuẩn, việc trực quan hóa quá trình dự đoán giúp người dùng hiểu rõ hơn cách mô hình hoạt động. Các chỉ số như hàm mất mát và độ chính xác cung cấp đánh giá định lượng, nhưng chưa thể hiện đầy đủ hành vi của mô hình trên từng mẫu cụ thể. Vì vậy, việc hiển thị ảnh đầu vào, nhãn dự đoán, xác suất đầu ra và các trường hợp dự đoán sai là cần thiết để phân tích mô hình một cách trực quan.

Đề tài định hướng bổ sung Web Demo cho phép người dùng tự vẽ chữ số và quan sát kết quả dự đoán. Tính năng này giúp kiểm thử mô hình trên dữ liệu gần với tình huống thực tế hơn so với dữ liệu MNIST đã được chuẩn hóa. Đồng thời, Web Demo cũng làm rõ vai trò của tiền xử lý ảnh như chuyển ảnh về ảnh xám, chuẩn hóa kích thước, căn giữa chữ số, chuẩn hóa pixel và trải phẳng thành vector đầu vào.

---

### 1.1.3. Ý nghĩa của việc tự cài đặt ANN thay vì dùng framework

Việc tự cài đặt mạng nơ-ron bằng `NumPy` có ý nghĩa quan trọng về mặt học thuật. Khi không sử dụng các framework học sâu như TensorFlow, Keras hoặc PyTorch, nhóm trực tiếp triển khai các bước cốt lõi của thuật toán, bao gồm khởi tạo trọng số, lan truyền tiến, hàm kích hoạt, Softmax, hàm mất mát Cross-Entropy, lan truyền ngược và cập nhật tham số bằng Adam Optimizer.

Cách tiếp cận này giúp làm rõ vai trò của từng ma trận trong mô hình, mối quan hệ giữa kích thước dữ liệu và kích thước tham số, cũng như cách gradient được truyền từ tầng đầu ra về tầng ẩn. Qua đó, mô hình không còn được xem như một hộp đen hoàn toàn, mà trở thành một hệ thống tính toán có thể phân tích, kiểm tra và giải thích bằng công thức toán học.

---

## 1.2. Mục tiêu và phạm vi đề tài

Đề tài hướng đến việc xây dựng một mô hình ANN kết nối đầy đủ có khả năng phân loại ảnh chữ số viết tay trên Infinity Dataset gồm 10,000,000 mẫu, được lưu dưới định dạng nhị phân `.npy`. Phiên bản cuối cùng sử dụng kiến trúc ANN sâu gồm ba tầng ẩn và được đánh giá bằng hàm mất mát huấn luyện, hàm mất mát kiểm định, độ chính xác huấn luyện, độ chính xác kiểm định, ma trận nhầm lẫn và các mẫu dự đoán sai.

Phạm vi đề tài tập trung vào mô hình kết nối đầy đủ tự triển khai bằng `NumPy`, không sử dụng CNN, RNN, Transformer hoặc framework học sâu bậc cao cho phần lõi. Mô hình cuối cùng dùng kiến trúc $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$ và được tối ưu bằng Adam Optimizer.

---

### 1.2.1. Mục tiêu xây dựng mô hình phân loại 10 chữ số

Mục tiêu cốt lõi của đề tài là huấn luyện mô hình phân loại ảnh chữ số viết tay thành 10 lớp từ $0$ đến $9$. Mỗi ảnh đầu vào được biểu diễn thành vector $784$ chiều, sau đó đi qua ba tầng ẩn gồm $1024$, $512$ và $256$ neuron trước khi tới tầng đầu ra gồm $10$ neuron.

Kiến trúc mô hình được sử dụng là:

$$
784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10
$$

---

### 1.2.2. Mục tiêu đánh giá thực nghiệm mô hình

Đề tài đánh giá quá trình học bằng hàm mất mát huấn luyện, hàm mất mát kiểm định, độ chính xác huấn luyện và độ chính xác kiểm định theo từng epoch. Kết quả cuối cùng ở epoch 20 đạt độ chính xác huấn luyện $99.44\%$, độ chính xác kiểm định $98.82\%$ và hàm mất mát kiểm định $0.0393$.

---

### 1.2.3. Mục tiêu kiểm thử mô hình trên nét vẽ thực tế

Dữ liệu MNIST đã được chuẩn hóa tốt, trong khi ảnh chữ số do người dùng tự vẽ có nhiều khác biệt về vị trí, kích thước, độ dày nét và màu nền. Vì vậy, đề tài kiểm thử mô hình qua Web Demo với pipeline tiền xử lý bằng `OpenCV`.

---

### 1.2.4. Phạm vi: MNIST, Infinity Dataset, Deep ANN, NumPy, Adam Optimizer

Dữ liệu huấn luyện được tạo bằng `scripts/generate_infinity.py`, sau đó lưu tại `data/train_infinity.npy` và `data/labels_infinity.npy`. Bộ dữ liệu đã sinh sẵn được lưu trên Google Drive tại `https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link` để thuận tiện cho việc tái lập thực nghiệm. Mô hình cuối cùng được lưu tại `weights/model_infinity.npz`. `ann.py` chỉ chứa logic suy luận, còn `scripts/train_infinity.py` chứa logic huấn luyện và lan truyền ngược.

---

## 1.3. Định hướng giải pháp

Định hướng giải pháp của đề tài gồm năm bước chính: chuẩn bị dữ liệu, xây dựng mô hình, huấn luyện, đánh giá và kiểm thử trực quan. Dữ liệu Infinity được tạo bằng `scripts/generate_infinity.py` từ EMNIST digits và các phép augmentation, sau đó được lưu dưới dạng `.npy`, gồm `data/train_infinity.npy` và `data/labels_infinity.npy`. Mô hình ANN được khởi tạo với ba tầng ẩn và được huấn luyện bằng mini-batch Adam Optimizer.

Sau khi huấn luyện, mô hình được đánh giá bằng hàm mất mát, độ chính xác, ma trận nhầm lẫn và các mẫu dự đoán sai. Ở bước mở rộng, mô hình được đưa vào Flask Web Demo để nhận diện chữ số do người dùng tự vẽ sau khi ảnh đã được tiền xử lý về định dạng gần với MNIST.

---

### 1.3.1. Huấn luyện ANN $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$ trên Infinity Dataset

Mô hình được thiết kế với tầng đầu vào gồm $784$ đặc trưng, tương ứng với $784$ pixel của ảnh $28 \times 28$. Ba tầng ẩn lần lượt gồm $1024$, $512$ và $256$ neuron. Tầng đầu ra gồm $10$ neuron, tương ứng với 10 lớp chữ số.

Trong quá trình huấn luyện, các tham số $W^{[1]}$, $b^{[1]}$, $W^{[2]}$, $b^{[2]}$, $W^{[3]}$, $b^{[3]}$, $W^{[4]}$ và $b^{[4]}$ được cập nhật bằng Adam Optimizer.

---

### 1.3.2. Theo dõi hàm mất mát và độ chính xác trong quá trình học

Hàm mất mát và độ chính xác huấn luyện phản ánh mức độ mô hình học được trên tập huấn luyện, trong khi hàm mất mát và độ chính xác kiểm định phản ánh khả năng tổng quát hóa. Các chỉ số này được ghi theo từng epoch trong `train.log`.

---

### 1.3.3. Phân tích lỗi dự đoán bằng ma trận nhầm lẫn và mẫu sai

Ma trận nhầm lẫn và ảnh dự đoán sai được sinh bằng `scripts/generate_report_assets.py` trên 10,000 mẫu cuối của Infinity Dataset, sử dụng trọng số cuối cùng tại `weights/model_infinity.npz`.

---

### 1.3.4. Kiểm thử suy luận trên nét vẽ người dùng

Ảnh người dùng vẽ được tiền xử lý bằng `OpenCV`, đổi kích thước về $28 \times 28$, chuẩn hóa và trải phẳng thành vector $784 \times 1$ trước khi đưa vào `forward_prop`.

---

## 1.4. Bố cục bài tập lớn

Báo cáo được tổ chức theo trình tự từ giới thiệu vấn đề, trình bày cơ sở lý thuyết, mô tả thực nghiệm đến kết luận và hướng phát triển. Chương 1 giới thiệu bối cảnh, mục tiêu, phạm vi và định hướng giải pháp của đề tài. Chương 2 trình bày cơ sở lý thuyết và liên hệ trực tiếp với các thành phần trong mã nguồn. Chương 3 tập trung vào thiết kế thực nghiệm, kết quả huấn luyện, phân tích lỗi và kiểm thử mở rộng. Chương 4 tổng kết các kết quả đạt được, nêu hạn chế và đề xuất hướng phát triển tiếp theo.

---

### 1.4.1. Nội dung Chương 2

Chương 2 trình bày cơ sở lý thuyết cần thiết để hiểu mô hình ANN kết nối đầy đủ dùng trong đề tài. Nội dung bao gồm biểu diễn dữ liệu MNIST, trải phẳng ảnh $28 \times 28$ thành vector $784$ chiều, chuẩn hóa pixel, nhãn số nguyên từ $0$ đến $9$, kiến trúc mạng $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$, lan truyền tiến, ReLU, Softmax, hàm mất mát Cross-Entropy, lan truyền ngược, Adam Optimizer và các chỉ số đánh giá như hàm mất mát và độ chính xác.

---

### 1.4.2. Nội dung Chương 3

Chương 3 trình bày phần thực nghiệm và đánh giá kết quả. Nội dung chương bao gồm môi trường chạy, cách chia tập huấn luyện/kiểm định, cấu hình mô hình, kết quả huấn luyện theo epoch, phân tích hội tụ, ma trận nhầm lẫn, phân tích lỗi và Web Demo.

---

### 1.4.3. Nội dung Chương 4

Chương 4 tổng kết những kết quả đã đạt được của đề tài, bao gồm việc tự xây dựng mô hình ANN bằng `NumPy`, huấn luyện và đánh giá mô hình trên Infinity Dataset, cũng như định hướng kiểm thử trên dữ liệu vẽ tay thực tế. Chương này đồng thời chỉ ra các hạn chế của mô hình kết nối đầy đủ, hạn chế của Adam Optimizer và các rủi ro trong tiền xử lý ảnh vẽ tay. Từ đó, báo cáo đề xuất các hướng phát triển phù hợp như cải thiện pipeline tiền xử lý, bổ sung dữ liệu kiểm thử thực tế và nâng cao khả năng trực quan hóa kết quả.

---
# Chương 2. Cơ sở lý thuyết

Chương này trình bày các khái niệm và công thức nền tảng liên quan đến bài toán nhận diện chữ số viết tay bằng ANN. Nội dung được liên hệ trực tiếp với mã nguồn `ann.py`, trong đó mô hình được cài đặt thủ công bằng `NumPy`, dữ liệu được đọc bằng `NumPy`, và ảnh demo được hiển thị bằng `Matplotlib`. Các thành phần chính gồm tiền xử lý dữ liệu, kiến trúc mạng kết nối đầy đủ, lan truyền tiến, hàm mất mát, lan truyền ngược và cập nhật tham số.

---

## 2.1. Bài toán phân loại ảnh chữ số viết tay

Bài toán nhận diện chữ số viết tay được mô hình hóa là bài toán phân loại đa lớp. Mỗi mẫu đầu vào là một ảnh chữ số viết tay và đầu ra là một nhãn thuộc một trong 10 lớp chữ số từ $0$ đến $9$. Trong phiên bản cuối, đặc trưng ảnh được lưu trong `data/train_infinity.npy`, còn nhãn thật được lưu trong `data/labels_infinity.npy`.

Về mặt toán học, mô hình cần học một hàm ánh xạ:

$$
f_{\theta}: \mathbb{R}^{784} \rightarrow \{0,1,2,3,4,5,6,7,8,9\}
$$

Trong đó $\theta$ gồm bốn tầng trọng số và độ lệch của mô hình Deep ANN.

---

### 2.1.1. Đầu vào của bài toán

Đầu vào của mô hình là ảnh xám kích thước $28 \times 28$, được trải phẳng thành vector $784$ chiều. Trong pha suy luận của `ann.py`, vector này được đưa vào ma trận trọng số đầu tiên `W1` sau khi đã được chuẩn hóa về kích thước $(1024, 784)$.

---

### 2.1.2. Đầu ra của bài toán

Đầu ra là vector xác suất trên 10 lớp chữ số. Trong pha suy luận, tầng cuối sử dụng `W4` kích thước $(10, 256)$ và `b4` kích thước $(10, 1)`. Hàm `get_predictions(A4)` chọn lớp có xác suất lớn nhất bằng `np.argmax(A4, 0)`.

---

### 2.1.3. Đặc điểm của phân loại đa lớp

Mỗi mẫu chỉ thuộc một lớp đúng trong 10 lớp chữ số. Trong huấn luyện, `scripts/train_infinity.py` tính hàm mất mát Cross-Entropy trực tiếp từ xác suất Softmax của lớp đúng.

---

## 2.2. Dữ liệu MNIST mở rộng và tiền xử lý

Dữ liệu được tạo bằng `scripts/generate_infinity.py` và được đọc từ hai file `data/train_infinity.npy` và `data/labels_infinity.npy`. Trong `scripts/train_infinity.py`, dữ liệu đặc trưng được nạp bằng `np.load`, nhãn được đưa về vector một chiều và cường độ pixel được chuẩn hóa về khoảng $[0,1]$ nếu dữ liệu ban đầu còn ở thang $0$ đến $255$.

Với 10,000,000 mẫu, cấu hình thực nghiệm dùng 100,000 mẫu kiểm định và 9,900,000 mẫu huấn luyện. Theo mã nguồn `scripts/train_infinity.py`, các mẫu kiểm định được lấy từ một hoán vị ngẫu nhiên với seed cố định, sau đó phần còn lại được dùng để huấn luyện. Dữ liệu được lưu dưới dạng `.npy` để phù hợp với quy trình huấn luyện bằng `NumPy` và quy mô Infinity Dataset.

Script `scripts/generate_infinity.py` sử dụng EMNIST digits làm dữ liệu gốc, sau đó áp dụng rotation, scaling, elastic distortion và nhiễu Gaussian nhẹ để tạo các biến thể chữ số viết tay. Output mặc định của script là `data/train_infinity.npy` và `data/labels_infinity.npy`. Ngoài cách tự tạo lại dataset, người đọc có thể tải bản đã sinh sẵn từ Google Drive: `https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link`.

---

### 2.2.1. Cấu trúc ảnh $28 \times 28$

Mỗi ảnh chữ số viết tay có kích thước $28 \times 28$, tương ứng với $784$ giá trị pixel. Script huấn luyện kiểm tra dữ liệu có đúng $784$ đặc trưng trước khi huấn luyện.

---

### 2.2.2. Trải phẳng ảnh thành vector 784 chiều

Mạng kết nối đầy đủ nhận vector đặc trưng thay vì ma trận ảnh hai chiều. Do đó ảnh $28 \times 28$ được biểu diễn thành vector $784$ chiều trước khi đi vào tầng đầu vào.

---

### 2.2.3. Chuẩn hóa pixel

Nếu giá trị pixel lớn hơn $1.5$, script chuẩn hóa dữ liệu bằng:

```python
X /= np.float32(255.0)
```

Trong Flask App, ảnh Canvas sau resize cũng được chuẩn hóa bằng `resized.astype(np.float32) / 255.0`.

---

### 2.2.4. Nhãn và hàm mất mát Cross-Entropy

Nhãn trong `data/labels_infinity.npy` là số nguyên từ $0$ đến $9$. Khi huấn luyện, `scripts/train_infinity.py` tính hàm mất mát Cross-Entropy trực tiếp từ xác suất Softmax tại lớp đúng của từng mẫu.

---

## 2.3. Mô hình ANN kết nối đầy đủ

Mô hình cuối cùng là ANN kết nối đầy đủ sâu gồm ba tầng ẩn và một tầng đầu ra. Phần suy luận nằm trong `ann.py`; phần huấn luyện, lan truyền ngược và cập nhật Adam nằm trong `scripts/train_infinity.py`.

Các thành phần chính:
- Tầng đầu vào có $784$ đặc trưng.
- Tầng ẩn 1 có $1024$ neuron.
- Tầng ẩn 2 có $512$ neuron.
- Tầng ẩn 3 có $256$ neuron.
- Tầng đầu ra có $10$ neuron.
- ReLU được dùng ở các tầng ẩn.
- Softmax được dùng ở tầng đầu ra.

---

### 2.3.1. Kiến trúc $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$

Kiến trúc mô hình là:

$$
784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10
$$

---

### 2.3.2. Vai trò của trọng số và độ lệch

Các tham số được học gồm $W^{[1]}$, $b^{[1]}$, $W^{[2]}$, $b^{[2]}$, $W^{[3]}$, $b^{[3]}$, $W^{[4]}$ và $b^{[4]}$, trong đó $W$ là trọng số và $b$ là độ lệch.

---

### 2.3.3. Bảng kích thước các ma trận trong mô hình

| Ký hiệu toán học | Biến trong code | Kích thước | Ý nghĩa |
|---|---|---:|---|
| $X$ | `X` | $784 \times m$ | Ma trận dữ liệu đầu vào |
| $W^{[1]}$ | `W1` | $1024 \times 784$ | Trọng số từ đầu vào sang tầng ẩn 1 |
| $b^{[1]}$ | `b1` | $1024 \times 1$ | Độ lệch tầng ẩn 1 |
| $W^{[2]}$ | `W2` | $512 \times 1024$ | Trọng số từ tầng ẩn 1 sang tầng ẩn 2 |
| $b^{[2]}$ | `b2` | $512 \times 1$ | Độ lệch tầng ẩn 2 |
| $W^{[3]}$ | `W3` | $256 \times 512$ | Trọng số từ tầng ẩn 2 sang tầng ẩn 3 |
| $b^{[3]}$ | `b3` | $256 \times 1$ | Độ lệch tầng ẩn 3 |
| $W^{[4]}$ | `W4` | $10 \times 256$ | Trọng số từ tầng ẩn 3 sang tầng đầu ra |
| $b^{[4]}$ | `b4` | $10 \times 1$ | Độ lệch tầng đầu ra |

---

## 2.4. Lan truyền tiến

Lan truyền tiến trong `ann.py` gồm ba tầng ReLU và một tầng Softmax:

Với một tầng bất kỳ thứ $l$, mô hình trước hết tính tổ hợp tuyến tính giữa đầu vào của tầng và bộ tham số tương ứng:

$$
Z^{[l]} = W^{[l]} \cdot A^{[l-1]} + b^{[l]}
$$

Sau đó, kết quả này được đưa qua hàm kích hoạt:

$$
A^{[l]} = g(Z^{[l]})
$$

Trong đó $A^{[0]}$ chính là ma trận đầu vào $X$, còn $g(\cdot)$ là hàm kích hoạt. Với mô hình trong đề tài, $g(\cdot)$ là ReLU ở các tầng ẩn và Softmax ở tầng đầu ra để tạo phân phối xác suất trên 10 lớp chữ số.

```python
Z1 = W1.dot(X) + b1
A1 = ReLU(Z1)
Z2 = W2.dot(A1) + b2
A2 = ReLU(Z2)
Z3 = W3.dot(A2) + b3
A3 = ReLU(Z3)
Z4 = W4.dot(A3) + b4
A4 = softmax(Z4)
```

Kết quả cuối cùng `A4` là ma trận xác suất kích thước $10 \times m$.

---

## 2.5. Tối ưu hóa bằng Adam Optimizer

Quá trình huấn luyện trong `scripts/train_infinity.py` sử dụng Adam Optimizer. Adam kết hợp ý tưởng momentum và tốc độ học thích nghi bằng cách duy trì moment bậc nhất và moment bậc hai cho từng tham số. Cơ chế này giúp quá trình tối ưu ổn định hơn trên tập dữ liệu lớn, đặc biệt khi huấn luyện theo mini-batch kích thước $4096$.

Các siêu tham số chính:

| Tham số | Giá trị |
|---|---:|
| Epochs | 20 |
| Kích thước mini-batch | 4096 |
| Tốc độ học ban đầu | 0.001 |
| Hệ số suy giảm tốc độ học | 0.92 mỗi epoch |
| Weight decay | $10^{-5}$ |
| $\beta_1$ | 0.9 |
| $\beta_2$ | 0.999 |
| $\epsilon$ | $10^{-8}$ |

---

### 2.5.1. Lan truyền ngược

Lan truyền ngược được triển khai trong `scripts/train_infinity.py` để tính gradient cho `W1`, `b1`, `W2`, `b2`, `W3`, `b3`, `W4` và `b4`. Bản chất của thuật toán là áp dụng quy tắc chuỗi để truyền sai số từ tầng đầu ra ngược về các tầng trước đó, từ đó xác định mỗi tham số ảnh hưởng đến hàm mất mát như thế nào.

Với tầng đầu ra sử dụng Softmax kết hợp hàm mất mát Cross-Entropy, sai số tại tầng cuối được tính gọn như sau:

$$
dZ^{[4]} = A^{[4]} - Y
$$

Trong đó $A^{[4]}$ là xác suất dự đoán của mô hình, còn $Y$ là nhãn đúng được biểu diễn dưới dạng one-hot. Từ sai số này, gradient của trọng số và độ lệch tầng cuối là:

$$
dW^{[4]} = \frac{1}{m} dZ^{[4]} \cdot (A^{[3]})^T
$$

$$
db^{[4]} = \frac{1}{m} \sum_{i=1}^{m} dZ^{[4](i)}
$$

Với các tầng ẩn, sai số được truyền ngược qua trọng số của tầng phía sau và nhân với đạo hàm của hàm kích hoạt. Vì mô hình dùng ReLU ở các tầng ẩn, đạo hàm $g'(Z^{[l]})$ cho biết neuron nào còn truyền gradient:

$$
dZ^{[l]} = (W^{[l+1]}^T \cdot dZ^{[l+1]}) * g'(Z^{[l]})
$$

Gradient của trọng số tại tầng $l$ được tính bằng:

$$
dW^{[l]} = \frac{1}{m} dZ^{[l]} \cdot (A^{[l-1]})^T
$$

Nhờ chuỗi phép tính này, mô hình biết cần điều chỉnh từng ma trận trọng số và độ lệch theo hướng làm giảm hàm mất mát Cross-Entropy.

---

### 2.5.2. Hàm mất mát Cross-Entropy

Hàm mất mát được tính bằng trung bình âm log xác suất của lớp đúng trong mini-batch. Xác suất được lấy từ Softmax đầu ra.

---

### 2.5.3. Mini-batch training

Dữ liệu train được chia thành mini-batch kích thước $4096$. Cách này giúp mô hình học ổn định và phù hợp hơn với Infinity Dataset gồm 10,000,000 mẫu.

---

### 2.5.4. Gradient Descent và Adam Optimizer

Gradient Descent là nguyên lý cập nhật tham số cơ bản trong học máy. Ý tưởng chính là cập nhật tham số theo hướng ngược với gradient của hàm mất mát để dần cực tiểu hóa giá trị mất mát:

$$
\theta = \theta - \eta \cdot d\theta
$$

Trong đó $\theta$ là tham số cần học, $d\theta$ là gradient tương ứng và $\eta$ là tốc độ học. Adam Optimizer là phiên bản nâng cao của Gradient Descent, kết hợp moment bậc nhất, moment bậc hai và hiệu chỉnh độ lệch để việc cập nhật ổn định hơn. Với gradient $g_t$ tại bước cập nhật $t$, các đại lượng chính được tính như sau:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t
$$

$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2
$$

$$
\theta_t = \theta_{t-1} - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}
$$

Trong đó $\hat{m}_t$ và $\hat{v}_t$ là các moment đã hiệu chỉnh độ lệch, $\eta$ là tốc độ học tại thời điểm cập nhật. Tốc độ học tại epoch $e$ là:

$$
lr_e = 0.001 \times 0.92^{e-1}
$$

---

## 2.6. Phương pháp đánh giá

Mô hình được đánh giá bằng hàm mất mát huấn luyện, độ chính xác huấn luyện, hàm mất mát kiểm định và độ chính xác kiểm định sau mỗi epoch. Ngoài ra, `scripts/generate_report_assets.py` sinh ma trận nhầm lẫn và các mẫu dự đoán sai để phục vụ phân tích trực quan.

---

### 2.6.1. Độ chính xác huấn luyện và kiểm định

Độ chính xác được tính bằng tỷ lệ dự đoán đúng trên tổng số mẫu. Ở epoch 20, mô hình đạt độ chính xác huấn luyện $99.44\%$ và độ chính xác kiểm định $98.82\%$.

---

### 2.6.2. Hàm mất mát huấn luyện và kiểm định

Hàm mất mát kiểm định cuối cùng là $0.0393$. Giá trị mất mát thấp cùng với độ chính xác kiểm định cao cho thấy mô hình hội tụ tốt trên tập kiểm định.

---

### 2.6.3. Ma trận nhầm lẫn

Ma trận nhầm lẫn được sinh bằng `scripts/generate_report_assets.py` trên 10,000 mẫu cuối của dataset, sử dụng trọng số cuối cùng `weights/model_infinity.npz`. Đây là tập đánh giá bổ sung hậu huấn luyện, phục vụ việc sinh hình ảnh và báo cáo phân loại chi tiết mà không can thiệp vào logic huấn luyện.

![Confusion Matrix trên tập đánh giá](confusion_matrix.png)

---

### 2.6.4. Phân tích mẫu dự đoán sai

Các mẫu dự đoán sai được lấy từ cùng tập 10,000 mẫu đánh giá bổ sung của Infinity Dataset. Hình minh họa giúp xác định các chữ số có hình dạng dễ gây nhầm lẫn cho mô hình.

![Các mẫu dự đoán sai tiêu biểu](misclassified_samples.png)

---

### 2.6.5. Cơ sở lý thuyết của các chỉ số phân loại

Các chỉ số phân loại được xây dựng từ ma trận nhầm lẫn. Với một lớp đang xét, $TP$ là số mẫu thuộc lớp đó và được dự đoán đúng, $TN$ là số mẫu không thuộc lớp đó và cũng không bị dự đoán nhầm vào lớp đó, $FP$ là số mẫu không thuộc lớp đó nhưng bị dự đoán nhầm thành lớp đó, còn $FN$ là số mẫu thuộc lớp đó nhưng bị dự đoán sang lớp khác.

Accuracy đo tỷ lệ dự đoán đúng trên tổng số mẫu:

$$
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
$$

Precision đo độ chính xác của các dự đoán dương tính, tức trong những mẫu được mô hình dự đoán là một lớp, có bao nhiêu mẫu thật sự thuộc lớp đó:

$$
Precision = \frac{TP}{TP + FP}
$$

Recall đo độ bao phủ, tức khả năng tìm ra toàn bộ mẫu thật sự thuộc một lớp:

$$
Recall = \frac{TP}{TP + FN}
$$

F1-Score là trung bình điều hòa của Precision và Recall, giúp cân bằng hai chỉ số này:

$$
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
$$

Với bài toán phân loại đa lớp gồm 10 chữ số, các chỉ số Precision, Recall và F1-Score được tính cho từng lớp rồi lấy trung bình Macro Average. Cách tính này đối xử công bằng với tất cả các lớp vì mỗi chữ số đóng góp như nhau vào kết quả cuối cùng, không phụ thuộc lớp đó có nhiều hay ít mẫu hơn trong tập đánh giá.

---

# Chương 3. Thực nghiệm và đánh giá kết quả

Chương này trình bày quá trình triển khai, huấn luyện và đánh giá mô hình ANN bằng `NumPy` theo đúng mã nguồn. Các thông tin cố định như cách chia dữ liệu, kiến trúc, tốc độ học, số epoch và phương pháp khởi tạo được lấy trực tiếp từ `scripts/train_infinity.py`, `ann.py` và `scripts/generate_report_assets.py`. Các kết quả thực nghiệm trong chương này được điền từ log terminal và các file ảnh đã tạo sẵn trong thư mục dự án.

---

## 3.1. Thiết kế thực nghiệm

Thiết kế thực nghiệm gồm: tạo Infinity Dataset bằng `scripts/generate_infinity.py`, nạp dữ liệu `.npy`, chuẩn hóa pixel, chia train/validation, khởi tạo tham số, huấn luyện bằng Adam Optimizer, đánh giá theo từng epoch và sinh ảnh báo cáo bằng `scripts/generate_report_assets.py`.

---

### 3.1.1. Môi trường chạy

Mã nguồn sử dụng `NumPy` cho tính toán ma trận, `Matplotlib` và `Seaborn` để trực quan hóa, `scikit-learn` để tính ma trận nhầm lẫn và các chỉ số phân loại, cùng `Flask`, `Pillow` và `OpenCV` cho Web Demo.

---

### 3.1.2. Cách chia tập huấn luyện/kiểm định

Dữ liệu được tạo trước bằng `scripts/generate_infinity.py`, sau đó được đọc từ `data/train_infinity.npy` và `data/labels_infinity.npy`. Với 10,000,000 mẫu, cấu hình huấn luyện dùng 9,900,000 mẫu huấn luyện và 100,000 mẫu kiểm định. Trong `scripts/train_infinity.py`, tập kiểm định được chọn bằng hoán vị ngẫu nhiên với seed $42$, không phải bằng cách lấy tuần tự một đoạn cố định của dataset.

---

### 3.1.3. Quy trình huấn luyện

Mỗi epoch, script xáo trộn tập huấn luyện, chia mini-batch kích thước $4096$, thực hiện lan truyền tiến, lan truyền ngược và cập nhật tham số bằng Adam.

---

### 3.1.4. Quy trình đánh giá

Sau mỗi epoch, script đánh giá hàm mất mát kiểm định và độ chính xác kiểm định. Các biểu đồ được sinh từ `train.log`.

---

## 3.2. Cấu hình mô hình cơ sở

Cấu hình cuối cùng là ANN kết nối đầy đủ sâu $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$ huấn luyện bằng Adam Optimizer.

---

### 3.2.1. Kiến trúc $784 \rightarrow 1024 \rightarrow 512 \rightarrow 256 \rightarrow 10$

Checkpoint `weights/model_infinity.npz` lưu trọng số theo quy ước huấn luyện của `scripts/train_infinity.py`, trong đó mỗi mini-batch có dạng $m \times 784$ và phép nhân được viết là $X @ W$. Vì vậy, kích thước gốc trong checkpoint là:

- `W1`: `(784, 1024)`
- `b1`: `(1024,)`
- `W2`: `(1024, 512)`
- `b2`: `(512,)`
- `W3`: `(512, 256)`
- `b3`: `(256,)`
- `W4`: `(256, 10)`
- `b4`: `(10,)`

Khi chạy suy luận, `ann.py` dùng `_normalize_weight_shape()` để chuyển các ma trận trọng số về quy ước $W^{[l]}A^{[l-1]} + b^{[l]}$, tương ứng với `W1` $(1024, 784)$, `W2` $(512, 1024)$, `W3` $(256, 512)$ và `W4` $(10, 256)$. Các vector độ lệch được `_as_column_bias()` đưa về dạng cột.

---

### 3.2.2. Lịch suy giảm tốc độ học

Tốc độ học ban đầu là $0.001$ và được nhân với hệ số suy giảm $0.92$ sau mỗi epoch:

$$
lr_e = 0.001 \times 0.92^{e-1}
$$

---

### 3.2.3. Số epoch mặc định

Cấu hình cuối cùng huấn luyện trong $20$ epoch với kích thước mini-batch $4096$ và $2417$ mini-batch mỗi epoch.

---

### 3.2.4. Phương pháp khởi tạo tham số

Trọng số được khởi tạo theo He Initialization, với độ lệch chuẩn tỷ lệ theo $\sqrt{2 / n_{in}}$, trong đó $n_{in}$ là số đầu vào của tầng hiện tại. Cách khởi tạo này phù hợp với ReLU vì giúp duy trì phương sai tín hiệu qua nhiều tầng, qua đó giảm nguy cơ giá trị kích hoạt bị suy giảm hoặc bùng nổ trong mạng sâu.

---

## 3.3. Kết quả mô hình Infinity

Kết quả cuối cùng được lấy từ epoch 20 trong `train.log`:

```text
Epoch 020/020 | Batch 02417/02417 | LR 0.000205101 | Loss 0.0177 | Acc 0.9944
Epoch 020 done in 29.0 min | Val Loss 0.0393 | Val Acc 0.9882 | Saved checkpoints_infinity/infinity_epoch_020.npz
```

| Chỉ số | Giá trị |
|---|---:|
| Hàm mất mát huấn luyện | 0.0177 |
| Độ chính xác huấn luyện | 99.44% |
| Hàm mất mát kiểm định | 0.0393 |
| Độ chính xác kiểm định | 98.82% |
| Precision đánh giá bổ sung (Macro) | 99.57% |
| Recall đánh giá bổ sung (Macro) | 99.57% |
| F1-Score đánh giá bổ sung (Macro) | 99.57% |

*Lưu ý: Các chỉ số Precision, Recall và F1-Score được tính trên tập đánh giá bổ sung gồm 10.000 mẫu cuối của dataset bằng `scripts/generate_report_assets.py`. Các chỉ số này được sinh sau huấn luyện, không can thiệp vào `scripts/train_infinity.py`, và được dùng cùng ma trận nhầm lẫn, báo cáo phân loại chi tiết, ảnh dự đoán sai.*

---

### 3.3.1. Bảng hàm mất mát và độ chính xác theo epoch

| Epoch | Hàm mất mát huấn luyện | Hàm mất mát kiểm định | Độ chính xác huấn luyện | Độ chính xác kiểm định |
|---:|---:|---:|---:|---:|
| 1 | 0.1559 | 0.0882 | 95.10% | 97.20% |
| 2 | 0.0755 | 0.0702 | 97.61% | 97.84% |
| 3 | 0.0612 | 0.0630 | 98.07% | 98.01% |
| 4 | 0.0532 | 0.0571 | 98.32% | 98.26% |
| 5 | 0.0478 | 0.0530 | 98.49% | 98.36% |
| 10 | 0.0327 | 0.0451 | 98.95% | 98.63% |
| 15 | 0.0240 | 0.0397 | 99.23% | 98.78% |
| 20 | 0.0177 | 0.0393 | 99.44% | 98.82% |

---

### 3.3.2. Biểu đồ hàm mất mát huấn luyện/kiểm định

![Biểu đồ Train/Dev Loss](loss_curve.png)

Biểu đồ cho thấy hàm mất mát huấn luyện giảm đều từ $0.1559$ xuống $0.0177$, trong khi hàm mất mát kiểm định giảm mạnh ở các epoch đầu và đạt $0.0393$ tại epoch 20. Khoảng cách giữa hai đường mất mát tồn tại nhưng không tăng đột biến, cho thấy mô hình chưa xuất hiện dấu hiệu quá khớp nghiêm trọng. Quy mô 10,000,000 mẫu của Infinity Dataset góp phần giảm rủi ro quá khớp so với các tập dữ liệu nhỏ hơn.

---

### 3.3.3. Biểu đồ độ chính xác huấn luyện/kiểm định

![Biểu đồ Train/Dev Accuracy](accuracy_curve.png)

Biểu đồ độ chính xác cho thấy độ chính xác huấn luyện đạt $99.44\%$ và độ chính xác kiểm định đạt $98.82\%$ ở epoch 20. Chênh lệch $0.62$ điểm phần trăm giữa hai chỉ số này là nhỏ so với quy mô mô hình, qua đó cho thấy khả năng tổng quát hóa tốt trên tập kiểm định.

---

### 3.3.4. Nhận xét về tốc độ hội tụ

Mô hình đạt độ chính xác kiểm định $97.20\%$ sau epoch 1 và vượt $98\%$ từ epoch 3. Từ nửa sau quá trình huấn luyện, độ chính xác kiểm định ổn định quanh $98.7\%$ đến $98.8\%$.

---

## 3.4. Siêu tham số của cấu hình cuối cùng

| Thành phần | Giá trị |
|---|---:|
| Kiến trúc | 784-1024-512-256-10 |
| Optimizer | Adam |
| Epochs | 20 |
| Kích thước mini-batch | 4096 |
| Tốc độ học ban đầu | 0.001 |
| Hệ số suy giảm tốc độ học | 0.92 mỗi epoch |
| Độ chính xác huấn luyện cuối | 99.44% |
| Độ chính xác kiểm định cuối | 98.82% |
| Hàm mất mát kiểm định cuối | 0.0393 |

---

## 3.5. Đánh giá bằng ma trận nhầm lẫn và các chỉ số phân loại chi tiết

Ma trận nhầm lẫn được sinh bằng `scripts/generate_report_assets.py` trên 10,000 mẫu cuối của dataset từ `data/train_infinity.npy` và `data/labels_infinity.npy`, sử dụng mô hình cuối cùng tại `weights/model_infinity.npz`.

---

### 3.5.1. Xây dựng ma trận nhầm lẫn trên 10,000 mẫu đánh giá

![Confusion Matrix](confusion_matrix.png)

Các giá trị lớn trên đường chéo chính thể hiện mô hình nhận diện đúng phần lớn mẫu trong tập đánh giá 10,000 ảnh. Vì ma trận nhầm lẫn chỉ được sinh từ một tập con của Infinity Dataset, hình này đóng vai trò công cụ chẩn đoán trực quan, bổ sung cho độ chính xác kiểm định tổng thể $98.82\%$ ở epoch 20.

---

### 3.5.2. Bảng phân loại chi tiết (Classification Report)

```text
              precision    recall  f1-score   support

           0     0.9990    0.9990    0.9990       975
           1     0.9951    0.9990    0.9970      1012
           2     0.9961    0.9895    0.9928      1043
           3     0.9990    0.9932    0.9961      1033
           4     0.9947    0.9968    0.9957       933
           5     0.9932    0.9980    0.9956      1021
           6     0.9979    0.9959    0.9969       971
           7     0.9894    0.9971    0.9932      1030
           8     0.9970    0.9940    0.9955       998
           9     0.9959    0.9949    0.9954       984

    accuracy                         0.9957     10000
   macro avg     0.9957    0.9957    0.9957     10000
weighted avg     0.9957    0.9957    0.9957     10000
```

Mô hình đạt độ cân bằng rất tốt trên mọi lớp chữ số, với F1-score dao động trong khoảng hẹp từ $99.28\%$ đến $99.90\%$. Điều này cho thấy kiến trúc kết nối đầy đủ không bị học lệch hay thiên vị rõ rệt đối với bất kỳ chữ số nào trong tập đánh giá bổ sung. Các lớp có F1-score thấp hơn như chữ số $2$ và $7$ vẫn giữ mức trên $99\%$, nên sai khác giữa các lớp là nhỏ.

---

### 3.5.3. Các lớp chữ số dễ nhận diện

Những chữ số có hình dạng rõ ràng và ít biến thiên theo phong cách viết thường có số lượng dự đoán đúng cao trên đường chéo chính.

---

### 3.5.4. Các cặp chữ số dễ nhầm lẫn

Các lỗi còn lại thường xuất hiện ở những cặp chữ số có hình dạng gần nhau như $4$ và $9$, $3$ và $5$, hoặc $1$ và $7$.

---

### 3.5.5. Nhận xét tổng quan từ ma trận nhầm lẫn

Ma trận nhầm lẫn cho thấy mô hình đạt chất lượng cao nhưng vẫn còn lỗi ở một số mẫu khó. Đây là hạn chế tự nhiên của ANN kết nối đầy đủ khi ảnh bị trải phẳng thành vector $784$ chiều.

---

## 3.6. Phân tích lỗi chi tiết

Phân tích lỗi chi tiết giúp chuyển các con số trong ma trận nhầm lẫn thành nhận xét có ý nghĩa về dữ liệu và mô hình. Thay vì chỉ ghi nhận rằng mô hình dự đoán sai một tỷ lệ nhất định, phần này tập trung vào các mẫu sai cụ thể để hiểu nguyên nhân gây lỗi.

![Một số mẫu dự đoán sai tiêu biểu](misclassified_samples.png)

Các mẫu dự đoán sai cho thấy nhiều lỗi xuất phát từ hình dạng chữ số không điển hình, nét viết mờ, nét viết quá dày hoặc các chữ số có cấu trúc gần giống nhau. Đây là dạng lỗi thường gặp khi sử dụng mô hình kết nối đầy đủ cho ảnh viết tay, vì ảnh đầu vào đã được chuyển thành vector một chiều trước khi đi qua mạng.

---

### 3.6.1. Trường hợp nhầm số 4 và số 9

Số $4$ và số $9$ có thể bị nhầm khi số $4$ được viết với phần nét giao nhau tạo thành vùng gần khép kín, hoặc khi số $9$ có phần vòng phía trên bị hở. Trong không gian pixel sau khi trải phẳng, hai trường hợp này có thể tạo ra các mẫu kích hoạt tương tự nhau, khiến Softmax gán xác suất cao cho lớp sai.

Lỗi này cho thấy mô hình chưa có khả năng biểu diễn rõ ràng cấu trúc hình học như vòng khép kín, hướng nét và quan hệ giữa các bộ phận của chữ số. Đây là hệ quả trực tiếp của việc chuyển ảnh $2D$ thành vector $1D$.

---

### 3.6.2. Trường hợp nhầm số 1 và số 7

Số $1$ và số $7$ thường bị nhầm khi số $1$ được viết nghiêng hoặc có thêm nét ngang phía trên. Ngược lại, số $7$ có thể bị viết đơn giản, thiếu nét ngang rõ ràng hoặc có hình dạng gần giống một nét thẳng nghiêng. Trong các trường hợp này, phân bố pixel tổng thể của hai chữ số trở nên gần nhau.

Với mô hình kết nối đầy đủ, mỗi pixel được xem như một đặc trưng độc lập trong vector đầu vào. Mô hình không có cơ chế riêng để hiểu rằng một nét ngang nhỏ phía trên có thể thay đổi ý nghĩa hình học của chữ số. Do đó, các trường hợp viết không chuẩn dễ dẫn đến dự đoán sai.

---

### 3.6.3. Trường hợp nhầm số 3 và số 5

Số $3$ và số $5$ có thể gây nhầm lẫn khi phần cong dưới hoặc phần thân giữa của hai chữ số có hình dạng tương đồng. Nếu nét ngang của số $5$ không rõ, hoặc số $3$ được viết với phần trên hơi phẳng, hai chữ số có thể tạo ra mẫu pixel gần nhau sau khi resize về kích thước $28 \times 28$.

Trường hợp này cho thấy mô hình có thể nhận diện tốt các mẫu phổ biến nhưng vẫn nhạy cảm với biến dạng hình học. Những lỗi như vậy thường cần được phân tích qua cả ma trận nhầm lẫn và ảnh dự đoán sai để tránh đánh giá mô hình chỉ dựa trên độ chính xác trung bình.

---

### 3.6.4. Nguyên nhân sai số do nét viết và biến dạng hình học

Các sai số thường xuất hiện ở những ảnh có nét viết không rõ ràng, chữ số bị lệch tâm, quá mảnh, quá dày hoặc có hình dạng khác với mẫu điển hình trong MNIST. Khi ảnh bị biến dạng, các đặc trưng pixel mà mô hình đã học có thể không còn khớp với phân phối huấn luyện. Điều này làm xác suất Softmax phân tán hoặc nghiêng về một lớp có hình dạng gần hơn.

Ngoài ra, quá trình resize về $28 \times 28$ có thể làm mất một phần chi tiết nhỏ của nét viết. Với các chữ số phụ thuộc vào chi tiết nhỏ để phân biệt, ví dụ $3$ và $5$ hoặc $1$ và $7$, sự mất mát này có thể làm tăng khả năng dự đoán sai.

---

### 3.6.5. Nguyên nhân sai số do ảnh bị trải phẳng

Hạn chế quan trọng nhất của mô hình là việc trải phẳng ảnh hai chiều thành vector $784$ chiều. Khi thực hiện thao tác này, thông tin về quan hệ không gian giữa các pixel không còn được biểu diễn trực tiếp. Hai pixel ở gần nhau trong ảnh có thể trở thành các vị trí xa nhau trong vector, trong khi mô hình kết nối đầy đủ không có ràng buộc cục bộ như phép tích chập.

Do đó, mô hình có thể học được các mẫu pixel toàn cục nhưng khó học các cấu trúc hình học bền vững như đường cong, giao điểm, vòng khép kín hoặc hướng nét. Đây là nguyên nhân chính dẫn đến các lỗi ở những chữ số có cấu trúc tương tự nhau.

---

## 3.7. Trực quan hóa mô hình

Trực quan hóa mô hình giúp liên hệ giữa kết quả định lượng và hành vi dự đoán thực tế. Trong báo cáo này, các trực quan chính gồm biểu đồ hàm mất mát, biểu đồ độ chính xác, ma trận nhầm lẫn và ảnh dự đoán sai. Các hình ảnh này giúp đánh giá cả quá trình hội tụ lẫn các dạng lỗi còn tồn tại.

---

### 3.7.1. Trực quan hóa trọng số tầng đầu vào

Trọng số từ tầng đầu vào đến tầng ẩn có thể được reshape về dạng ảnh $28 \times 28$ để quan sát các vùng pixel mà một số neuron phản ứng mạnh. Cách trực quan hóa này giúp minh họa rằng mô hình đang học các mẫu pixel toàn cục từ dữ liệu huấn luyện.

Tuy nhiên, do mô hình là kết nối đầy đủ, mỗi neuron tầng ẩn kết nối với toàn bộ $784$ pixel đầu vào. Vì vậy, các trọng số này thường khó diễn giải trực quan hơn so với bộ lọc tích chập. Phần trực quan hóa trọng số có thể được bổ sung trong phụ lục hoặc hướng phát triển để tăng khả năng giải thích của mô hình.

---

### 3.7.2. Trực quan hóa xác suất Softmax của một mẫu dự đoán

Xác suất Softmax cho biết mức độ tự tin tương đối của mô hình đối với từng lớp chữ số. Với một ảnh đầu vào, vector đầu ra $A^{[4]}$ có kích thước $10 \times 1$, trong đó mỗi phần tử tương ứng với xác suất dự đoán cho một lớp. Nhãn dự đoán được chọn bằng `np.argmax` trên vector xác suất này.

Việc trực quan hóa xác suất Softmax đặc biệt hữu ích trong các trường hợp mô hình dự đoán sai. Nếu hai lớp có xác suất gần nhau, điều đó cho thấy mô hình đang phân vân giữa các chữ số có hình dạng tương tự. Nếu một lớp sai có xác suất rất cao, lỗi có thể đến từ tiền xử lý hoặc từ việc ảnh đầu vào khác mạnh so với phân phối MNIST.

---

### 3.7.3. So sánh mẫu dự đoán đúng và sai

So sánh mẫu dự đoán đúng và sai giúp làm rõ mối liên hệ giữa chất lượng ảnh đầu vào và kết quả dự đoán. Các mẫu đúng thường có chữ số rõ ràng, nằm gần trung tâm ảnh và có nét viết tương đối giống phân phối MNIST. Ngược lại, các mẫu sai thường có nét viết méo, lệch tâm hoặc giống với nhiều chữ số khác nhau.

Trong báo cáo, hình `misclassified_samples.png` được dùng để minh họa các mẫu sai tiêu biểu. Khi kết hợp hình này với ma trận nhầm lẫn, có thể xác định không chỉ mô hình sai bao nhiêu mà còn sai theo kiểu nào.

---

### 3.7.4. Nhận xét khả năng học đặc trưng của mô hình

Kết quả thực nghiệm cho thấy mô hình ANN kết nối đầy đủ đã học được các đặc trưng pixel đủ mạnh để đạt độ chính xác huấn luyện $99.44\%$ và độ chính xác kiểm định $98.82\%$ tại epoch $20$ trong cấu hình tốt nhất. Điều này chứng tỏ mô hình có khả năng phân biệt phần lớn chữ số trong Infinity Dataset, dù kiến trúc vẫn dựa trên biểu diễn kết nối đầy đủ của ảnh đã trải phẳng.

Tuy nhiên, khả năng học đặc trưng của mô hình vẫn bị giới hạn bởi biểu diễn đầu vào. Vì ảnh bị trải phẳng, mô hình không bảo toàn đầy đủ cấu trúc không gian của chữ số. Do đó, các lỗi giữa những chữ số có hình dạng gần nhau vẫn xuất hiện và cần được xem là hạn chế tự nhiên của kiến trúc này.

---

## 3.8. Triển khai dự đoán trên nét vẽ thực tế Web Demo

Phần Web Demo mở rộng phạm vi bài toán từ Infinity Dataset sang dữ liệu do người dùng tự vẽ trên Canvas. Đây là dạng dữ liệu ngoài phân phối huấn luyện, thường được gọi là Out-of-Distribution (OOD) data. Ảnh Canvas có thể khác Infinity Dataset về màu nền, độ dày nét, kích thước chữ số, vị trí chữ số và mức độ nhiễu. Vì vậy, mô hình không thể nhận ảnh Canvas thô trực tiếp mà cần pipeline tiền xử lý bằng `OpenCV`.

Pipeline tiền xử lý được thiết kế nhằm đưa ảnh vẽ thực tế về định dạng gần với MNIST: chữ số sáng trên nền tối, kích thước $28 \times 28$, giá trị pixel được chuẩn hóa và đầu vào cuối cùng là vector $784 \times 1$.

![Pipeline tiền xử lý](images/preprocessing_pipeline.png)

---

### 3.8.1. Công cụ thu thập nét vẽ từ người dùng

Canvas trong Web Demo đóng vai trò là vùng thu nhận nét vẽ tự do. Người dùng vẽ một chữ số bằng chuột hoặc thiết bị cảm ứng, sau đó ảnh từ Canvas được gửi về backend hoặc module xử lý ảnh để chuẩn hóa. Ảnh này là dữ liệu thô, chưa có cùng định dạng với MNIST và có thể chứa nhiều yếu tố gây nhiễu.

Do đó, Canvas chỉ là bước thu thập dữ liệu ban đầu. Chất lượng dự đoán phụ thuộc lớn vào quá trình xử lý ảnh sau khi người dùng hoàn tất nét vẽ.

---

### 3.8.2. Khác biệt giữa ảnh vẽ thực tế và ảnh MNIST

Dữ liệu MNIST đã được chuẩn hóa tương đối tốt: chữ số thường nằm gần trung tâm ảnh, có kích thước ổn định và được biểu diễn dưới dạng ảnh xám kích thước $28 \times 28$. Ngược lại, ảnh Canvas có thể có vùng trống lớn, chữ số nằm lệch, nét viết quá mảnh hoặc quá dày, và nền ảnh có thể khác với định dạng mô hình đã học.

Sự khác biệt này tạo ra Data Drift giữa dữ liệu huấn luyện và dữ liệu suy luận thực tế. Nếu không xử lý, mô hình có thể nhận một vector đầu vào có phân phối pixel rất khác so với MNIST, làm giảm độ tin cậy của dự đoán.

---

### 3.8.3. Chuyển ảnh vẽ sang ảnh xám

Bước đầu tiên của pipeline là đọc ảnh hoặc chuyển ảnh Canvas sang ảnh xám. Việc chuyển sang ảnh xám giúp loại bỏ thông tin màu không cần thiết và đưa ảnh về dạng một kênh, phù hợp với định dạng dữ liệu MNIST. Trong `OpenCV`, ảnh xám có thể được đọc hoặc chuyển đổi bằng các hàm xử lý ảnh chuẩn.

Sau bước này, mỗi pixel chỉ còn một giá trị cường độ sáng, giúp các bước tiếp theo như đảo màu, tìm hộp bao và chuẩn hóa được thực hiện nhất quán hơn.

---

### 3.8.4. Nghịch đảo màu về dạng nền đen chữ trắng

MNIST biểu diễn chữ số theo dạng chữ sáng trên nền tối. Trong khi đó, ảnh Canvas thường có thể là nét tối trên nền sáng. Vì vậy, pipeline sử dụng `cv2.bitwise_not` để đảo màu, đưa ảnh về định dạng gần với MNIST hơn.

Bước đảo màu rất quan trọng vì mô hình đã học từ phân phối pixel trong đó vùng chữ số có cường độ cao hơn nền. Nếu giữ nguyên ảnh nền sáng chữ tối, vector đầu vào sẽ bị đảo phân phối so với dữ liệu huấn luyện và có thể làm mô hình dự đoán sai.

---

### 3.8.5. Tìm bounding box vùng chứa chữ số

Sau khi ảnh được đảo màu, pipeline xác định vùng chứa chữ số bằng cách tìm các pixel khác nền. Cụ thể, `cv2.findNonZero` được dùng để lấy tọa độ các pixel thuộc nét vẽ, sau đó `cv2.boundingRect` xác định hình chữ nhật nhỏ nhất bao quanh toàn bộ vùng này.

Bounding box giúp loại bỏ phần nền trống xung quanh chữ số. Nếu không crop theo bounding box, chữ số có thể chiếm diện tích quá nhỏ trong ảnh $28 \times 28$, khiến mô hình khó nhận diện chính xác.

---

### 3.8.6. Cắt ảnh và căn giữa chữ số

Sau khi có bounding box, ảnh được crop để giữ lại vùng chứa chữ số chính. Tuy nhiên, vùng crop có thể không phải hình vuông. Vì vậy, pipeline thêm padding để biến vùng chữ số thành một khung vuông trước khi resize. Bước padding giúp giữ tỷ lệ hình học của chữ số, tránh làm chữ số bị kéo dãn theo chiều ngang hoặc chiều dọc.

Sau khi được đưa vào khung vuông, chữ số được căn giữa để giảm sai lệch vị trí. Đây là bước quan trọng vì mô hình được huấn luyện trên Infinity Dataset theo định dạng gần với MNIST, nơi chữ số thường nằm gần trung tâm ảnh.

---

### 3.8.7. Resize ảnh về kích thước $28 \times 28$

Mô hình ANN yêu cầu đầu vào có đúng $784$ phần tử, tương ứng với ảnh $28 \times 28$. Vì vậy, ảnh sau khi cắt và đệm được đổi kích thước về $28 \times 28$. Bước này bảo đảm kích thước của ảnh tương thích với ma trận trọng số $W^{[1]}$ sau khi nạp bằng `ann.py`, có kích thước $1024 \times 784$.

Việc resize cần được thực hiện sau khi đã crop và pad, vì resize trực tiếp từ toàn bộ ảnh Canvas có thể làm chữ số bị thu nhỏ hoặc biến dạng mạnh.

---

### 3.8.8. Chuẩn hóa và trải phẳng thành vector 784 chiều

Sau khi đổi kích thước, giá trị pixel được chuẩn hóa bằng cách chia cho $255.0$, đưa dữ liệu về khoảng $[0,1]$. Đây là cùng kiểu chuẩn hóa đã sử dụng cho dữ liệu huấn luyện, giúp mô hình nhận đầu vào có thang giá trị nhất quán.

Cuối cùng, ảnh $28 \times 28$ được trải phẳng thành vector $784 \times 1$. Vector này được đưa vào hàm lan truyền tiến `forward_prop` để tính logits, Softmax và nhãn dự đoán. Quy trình này bảo đảm ảnh Canvas sau xử lý có cùng kích thước đầu vào với dữ liệu MNIST.

---

### 3.8.9. Chạy suy luận bằng trọng số đã huấn luyện

Ở giai đoạn suy luận, mô hình sử dụng toàn bộ các tham số đã học gồm $W^{[1]}$, $b^{[1]}$, $W^{[2]}$, $b^{[2]}$, $W^{[3]}$, $b^{[3]}$, $W^{[4]}$ và $b^{[4]}$. Mô hình không cập nhật trọng số trong bước này mà chỉ thực hiện lan truyền tiến để tính xác suất đầu ra.

Nhãn dự đoán được chọn bằng lớp có xác suất Softmax lớn nhất. Việc chỉ thực hiện lan truyền tiến giúp quá trình dự đoán nhanh, phù hợp với yêu cầu phản hồi trong Web Demo.

---

### 3.8.10. Trực quan hóa ảnh trước và sau tiền xử lý

Trực quan hóa pipeline tiền xử lý giúp kiểm tra liệu ảnh Canvas đã được đưa về gần định dạng MNIST hay chưa. Các bước nên được minh họa gồm ảnh gốc, ảnh xám, ảnh sau đảo màu, ảnh sau cắt theo hộp bao, ảnh sau đệm/căn giữa và ảnh cuối cùng $28 \times 28$.

![Pipeline tiền xử lý](images/preprocessing_pipeline.png)

Nếu dự đoán sai, chuỗi hình này giúp xác định lỗi đến từ mô hình hay đến từ tiền xử lý. Ví dụ, nếu hộp bao bị ảnh hưởng bởi nhiễu hoặc chấm thừa, ảnh sau đổi kích thước có thể làm chữ số chính bị thu nhỏ, từ đó gây sai lệch dự đoán.

---

### 3.8.11. Biểu đồ xác suất Softmax đầu ra

Biểu đồ xác suất Softmax đầu ra giúp quan sát mức độ tự tin của mô hình trên dữ liệu Canvas. Nếu xác suất cao nhất vượt trội so với các lớp còn lại, mô hình đang dự đoán với độ tự tin tương đối cao. Nếu nhiều lớp có xác suất gần nhau, mô hình đang phân vân, thường do chữ số có hình dạng không rõ hoặc nằm giữa nhiều lớp.

Với dữ liệu ngoài phân phối huấn luyện (Out-of-Distribution, OOD), biểu đồ Softmax đặc biệt hữu ích vì nó cho biết mô hình chỉ sai nhãn hay còn thiếu tự tin về cấu trúc đầu vào. Đây là thông tin quan trọng để cải thiện tiền xử lý và thu thập thêm dữ liệu kiểm thử.

---

### 3.8.12. Nhận xét kết quả trên nét vẽ thực tế

Kết quả trên nét vẽ thực tế phụ thuộc mạnh vào pipeline tiền xử lý. Khi ảnh được đảo màu đúng, cắt chính xác, đệm hợp lý, đổi kích thước về $28 \times 28$ và chuẩn hóa đúng thang giá trị, mô hình có khả năng xử lý dữ liệu Canvas tốt hơn. Ngược lại, các nhiễu nhỏ hoặc dấu chấm thừa có thể làm hộp bao sai, khiến chữ số bị lệch hoặc thu nhỏ sau đổi kích thước.

Do đó, Web Demo cho thấy bài toán nhận diện chữ số thực tế không chỉ phụ thuộc vào mô hình ANN, mà còn phụ thuộc vào toàn bộ pipeline xử lý dữ liệu đầu vào. Đây là bài học quan trọng khi đưa mô hình học máy từ dữ liệu chuẩn sang môi trường sử dụng thực tế.

---

## 3.9. Đánh giá tổng hợp thực nghiệm

Tổng hợp kết quả thực nghiệm cho thấy mô hình ANN kết nối đầy đủ sâu tự cài đặt bằng `NumPy` đạt hiệu năng cao trên Infinity Dataset. Các thông số chi tiết về kiến trúc, siêu tham số và kết quả cuối cùng đã được trình bày trong các mục 3.2 đến 3.4; phần này tập trung vào ý nghĩa thực nghiệm và các hạn chế chính của mô hình.

---

### 3.9.1. Cấu hình mô hình tốt nhất

Cấu hình được chọn là mô hình Infinity đã trình bày ở Chương 3, gồm ba tầng ẩn và được huấn luyện bằng Adam Optimizer trên dữ liệu `.npy`. Mô hình cuối cùng được lưu tại `weights/model_infinity.npz`.

---

### 3.9.2. Ưu điểm của mô hình sau thực nghiệm

Mô hình đạt độ chính xác cao trong khi vẫn giữ được cách triển khai minh bạch bằng `NumPy`. Tốc độ suy luận nhanh vì dự đoán chỉ cần các phép nhân ma trận và hàm kích hoạt cơ bản.

---

### 3.9.3. Hạn chế rút ra từ thực nghiệm

Mô hình kết nối đầy đủ làm mất cấu trúc không gian hai chiều khi trải phẳng ảnh. Vì vậy, mô hình vẫn có thể nhầm các chữ số có cấu trúc gần nhau.

---

### 3.9.4. Bài học kỹ thuật từ quá trình thử nghiệm

Hiệu quả của mô hình phụ thuộc đồng thời vào kiến trúc, dữ liệu, bộ tối ưu và tiền xử lý. Với dữ liệu thực tế từ Canvas, tiền xử lý là thành phần bắt buộc để giảm khác biệt phân phối giữa dữ liệu người dùng và dữ liệu huấn luyện.

---
# Chương 4. Kết luận và hướng phát triển

Chương cuối tổng kết kết quả chính của đề tài dựa trên mô hình Infinity, log huấn luyện 20 epoch và các ảnh đánh giá sinh từ mô hình cuối cùng.

---

## 4.1. Kết luận

Đề tài đã xây dựng thành công mô hình ANN kết nối đầy đủ sâu bằng `NumPy` và huấn luyện mô hình Infinity bằng Adam Optimizer trên dữ liệu `.npy`. Các thông số kiến trúc, siêu tham số và kết quả định lượng cuối cùng đã được trình bày chi tiết trong Chương 3.

---

### 4.1.1. Kết quả xây dựng ANN NumPy

`ann.py` được module hóa cho suy luận, bao gồm ReLU, Softmax, `forward_prop`, `load_model` và `get_predictions`. Logic huấn luyện và cập nhật tham số nằm trong `scripts/train_infinity.py`.

---

### 4.1.2. Kết quả đánh giá thực nghiệm

Ma trận nhầm lẫn và các mẫu dự đoán sai cho thấy mô hình nhận diện đúng phần lớn mẫu trong tập đánh giá 10,000 ảnh từ Infinity Dataset. Các lỗi còn lại chủ yếu xuất hiện ở những chữ số có hình dạng gần nhau.

---

### 4.1.3. Kết quả kiểm thử trên nét vẽ thực tế

Web Demo sử dụng Flask để nhận ảnh Canvas, tiền xử lý bằng `OpenCV`, sau đó gọi mô hình tại `weights/model_infinity.npz` để dự đoán.

---

### 4.1.4. Đóng góp nổi bật của đề tài

Đề tài đóng góp một pipeline hoàn chỉnh gồm huấn luyện ANN sâu, lưu mô hình, sinh ảnh báo cáo tự động và triển khai Web Demo nhận diện chữ số viết tay.

---

## 4.2. Hạn chế

Dù đạt kết quả cao, mô hình vẫn có một số hạn chế xuất phát từ kiến trúc kết nối đầy đủ, chi phí dữ liệu lớn và pipeline tiền xử lý ảnh thực tế.

---

### 4.2.1. Hạn chế trong khả năng tổng quát hóa

Việc trải phẳng ảnh $28 \times 28$ thành vector $784$ chiều làm mất cấu trúc không gian cục bộ giữa các pixel. Vì vậy, một số cặp chữ số có hình dạng gần nhau vẫn có thể bị nhầm lẫn.

---

### 4.2.2. Hạn chế khi nhận diện nét vẽ ngoài phân phối MNIST

Dữ liệu Canvas có thể khác dữ liệu huấn luyện về độ dày nét, vị trí chữ số, kích thước chữ số và nhiễu nền. Pipeline tiền xử lý giúp giảm khác biệt này nhưng không loại bỏ hoàn toàn rủi ro.

---

### 4.2.3. Hạn chế của quá trình tối ưu bằng Adam

Adam Optimizer giúp quá trình huấn luyện ổn định hơn trên dữ liệu lớn, nhưng vẫn cần lựa chọn tốc độ học, hệ số suy giảm tốc độ học, weight decay và kích thước mini-batch phù hợp. Mô hình ANN sâu cũng có nhiều tham số, làm tăng chi phí tính toán và bộ nhớ.

---

### 4.2.4. Hạn chế của tiền xử lý ảnh vẽ tay

Pipeline tiền xử lý phụ thuộc vào bước bounding box. Nếu ảnh có nhiễu hoặc nét thừa ở xa chữ số chính, vùng crop có thể bị sai và ảnh sau resize có thể không còn giống phân phối MNIST.

---

## 4.3. Hướng phát triển

Các hướng phát triển gồm cải thiện tiền xử lý, xây dựng tập kiểm thử Canvas có nhãn, thử nghiệm CNN và tăng khả năng giải thích kết quả dự đoán.

---

### 4.3.1. Tăng độ ổn định của pipeline tiền xử lý ảnh

Có thể bổ sung giảm nhiễu, chuẩn hóa độ dày nét và căn giữa dựa trên tâm khối lượng pixel để ảnh sau resize ổn định hơn.

---

### 4.3.2. Bổ sung bộ dữ liệu kiểm thử từ nét vẽ người dùng

Cần xây dựng tập `Dev_Canvas` gồm các mẫu chữ số do người dùng thật vẽ để đánh giá khách quan hơn hiệu quả của Web Demo.

---

### 4.3.3. Tối ưu tốc độ dự đoán real-time

Model nên tiếp tục được load một lần khi Flask server khởi động và giữ trong bộ nhớ để giảm latency.

---

### 4.3.4. Cải thiện khả năng giải thích kết quả dự đoán

Hệ thống có thể bổ sung biểu đồ xác suất Softmax cho từng ảnh đầu vào, activation heatmaps hoặc trực quan hóa trọng số tầng đầu vào.

---

# Tài liệu tham khảo

[1] Y. LeCun, C. Cortes, and C. J. C. Burges, "The MNIST database of handwritten digits," 1998. [Online]. Available: http://yann.lecun.com/exdb/mnist/

[2] K. He, X. Zhang, S. Ren, and J. Sun, "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification," in *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, 2015.

[3] NumPy Developers, "NumPy Documentation," [Online]. Available: https://numpy.org/doc/

[4] OpenCV Team, "OpenCV Documentation," [Online]. Available: https://docs.opencv.org/

[5] Học viện Công nghệ Bưu chính Viễn thông, "Bài giảng Nhập môn Trí tuệ nhân tạo," Khoa Công nghệ thông tin 1, PTIT.

---

# Phụ lục

Phụ lục trình bày các nội dung kỹ thuật bổ trợ cho phần chính của báo cáo, bao gồm mã nguồn suy luận, mô tả script tạo dataset, mô tả script huấn luyện, bảng kết quả thực nghiệm, ma trận nhầm lẫn, mẫu dự đoán sai và pipeline tiền xử lý ảnh Canvas.

---

## Phụ lục A. Mã nguồn suy luận trong `ann.py`

`ann.py` hiện được module hóa cho suy luận, không còn chứa logic đọc dữ liệu huấn luyện hoặc huấn luyện. Nội dung chính gồm ReLU, Softmax, `forward_prop`, `load_model` và `get_predictions`.

```python
import numpy as np


def ReLU(Z):
    return np.maximum(Z, 0)


def softmax(Z):
    Z_shifted = Z - np.max(Z, axis=0, keepdims=True)
    A = np.exp(Z_shifted) / np.sum(np.exp(Z_shifted), axis=0, keepdims=True)
    return A


def forward_prop(W1, b1, W2, b2, W3, b3, W4, b4, X):
    # Layer 1: 1024 neurons
    Z1 = W1.dot(X) + b1
    A1 = ReLU(Z1)

    # Layer 2: 512 neurons
    Z2 = W2.dot(A1) + b2
    A2 = ReLU(Z2)

    # Layer 3: 256 neurons
    Z3 = W3.dot(A2) + b3
    A3 = ReLU(Z3)

    # Layer 4: 10 neurons (Output)
    Z4 = W4.dot(A3) + b4
    A4 = softmax(Z4)

    return Z1, A1, Z2, A2, Z3, A3, Z4, A4


def _as_column_bias(b):
    return np.asarray(b).reshape(-1, 1)


def _normalize_weight_shape(W, expected_shape, name):
    W = np.asarray(W)
    if W.shape == expected_shape:
        return W

    transposed_shape = (expected_shape[1], expected_shape[0])
    if W.shape == transposed_shape:
        return W.T

    raise ValueError(f"{name} has shape {W.shape}, expected {expected_shape}.")


def load_model(filename="model_infinity.npz"):
    data = np.load(filename)

    W1 = _normalize_weight_shape(data["W1"], (1024, 784), "W1")
    W2 = _normalize_weight_shape(data["W2"], (512, 1024), "W2")
    W3 = _normalize_weight_shape(data["W3"], (256, 512), "W3")
    W4 = _normalize_weight_shape(data["W4"], (10, 256), "W4")

    return (
        W1,
        _as_column_bias(data["b1"]),
        W2,
        _as_column_bias(data["b2"]),
        W3,
        _as_column_bias(data["b3"]),
        W4,
        _as_column_bias(data["b4"]),
    )


def get_predictions(A4):
    return np.argmax(A4, 0)
```

---

## Phụ lục B. Script huấn luyện `scripts/train_infinity.py`

Trước khi huấn luyện, dataset được tạo bằng `scripts/generate_infinity.py`. Script này sử dụng EMNIST digits làm dữ liệu gốc và sinh thêm biến thể bằng rotation, scaling, elastic distortion và nhiễu Gaussian nhẹ. Hai file đầu ra mặc định là `data/train_infinity.npy` và `data/labels_infinity.npy`. Dataset đã sinh sẵn được lưu tại Google Drive: `https://drive.google.com/drive/folders/1tYDnYPMoEaS70Fgb2cK29Fft5eoG4fvz?usp=drive_link`.

Script huấn luyện chịu trách nhiệm nạp `data/train_infinity.npy`, `data/labels_infinity.npy`, khởi tạo mô hình, chạy lan truyền tiến, lan truyền ngược, cập nhật Adam, đánh giá kiểm định và lưu checkpoint.

```text
Architecture: 784 -> 1024 -> 512 -> 256 -> 10
Optimizer: Adam
Epochs: 20
Mini-batch size: 4096
Initial learning rate: 0.001
Learning rate decay: 0.92 per epoch
Model path: weights/model_infinity.npz
```

---

## Phụ lục C. Bảng kết quả thực nghiệm đầy đủ

| Epoch | Hàm mất mát huấn luyện | Hàm mất mát kiểm định | Độ chính xác huấn luyện | Độ chính xác kiểm định |
|---:|---:|---:|---:|---:|
| 1 | 0.1559 | 0.0882 | 95.10% | 97.20% |
| 2 | 0.0755 | 0.0702 | 97.61% | 97.84% |
| 3 | 0.0612 | 0.0630 | 98.07% | 98.01% |
| 4 | 0.0532 | 0.0571 | 98.32% | 98.26% |
| 5 | 0.0478 | 0.0530 | 98.49% | 98.36% |
| 6 | 0.0435 | 0.0500 | 98.62% | 98.42% |
| 7 | 0.0403 | 0.0474 | 98.72% | 98.57% |
| 8 | 0.0374 | 0.0451 | 98.80% | 98.58% |
| 9 | 0.0349 | 0.0444 | 98.89% | 98.62% |
| 10 | 0.0327 | 0.0451 | 98.95% | 98.63% |
| 11 | 0.0307 | 0.0418 | 99.02% | 98.73% |
| 12 | 0.0289 | 0.0414 | 99.07% | 98.73% |
| 13 | 0.0272 | 0.0406 | 99.13% | 98.76% |
| 14 | 0.0255 | 0.0405 | 99.18% | 98.77% |
| 15 | 0.0240 | 0.0397 | 99.23% | 98.78% |
| 16 | 0.0226 | 0.0396 | 99.28% | 98.76% |
| 17 | 0.0212 | 0.0387 | 99.32% | 98.82% |
| 18 | 0.0200 | 0.0400 | 99.36% | 98.79% |
| 19 | 0.0188 | 0.0391 | 99.40% | 98.84% |
| 20 | 0.0177 | 0.0393 | 99.44% | 98.82% |

---

## Phụ lục D. Ma trận nhầm lẫn và ảnh dự đoán sai bổ sung

Ma trận nhầm lẫn và ảnh dự đoán sai được sinh từ 10,000 mẫu cuối của Infinity Dataset bằng `scripts/generate_report_assets.py`.

![Confusion Matrix](confusion_matrix.png)

![Một số mẫu dự đoán sai tiêu biểu](misclassified_samples.png)

---

## Phụ lục E. Minh họa pipeline tiền xử lý nét vẽ thực tế

Pipeline xử lý ảnh Canvas gồm giải mã ảnh, chuyển sang ảnh xám, đảo màu, ngưỡng hóa, tìm hộp bao, cắt, đệm thành ảnh vuông, đổi kích thước về $28 \times 28$, chuẩn hóa và trải phẳng thành vector $784 \times 1$.

![Pipeline tiền xử lý](images/preprocessing_pipeline.png)
