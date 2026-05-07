# BÁO CÁO BÀI TẬP LỚN NHẬP MÔN TRÍ TUỆ NHÂN TẠO

## Đề tài: Nhận diện chữ số viết tay MNIST sử dụng mạng nơ-ron Fully Connected code từ đầu bằng NumPy

> 🛑 **[HÀNH ĐỘNG]**: Hoàn thiện toàn bộ báo cáo theo đúng cấu trúc dưới đây, bảo đảm văn phong học thuật, trình bày rõ ràng, có hình ảnh, bảng biểu, công thức, kết quả thực nghiệm và phân tích lỗi đầy đủ.

---

# Phần mở đầu

Phần mở đầu có vai trò chuẩn hóa hình thức báo cáo trước khi đi vào nội dung chuyên môn. Các thành phần trong phần này cần được trình bày thống nhất, đầy đủ và đúng quy cách của mẫu báo cáo bài tập lớn.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày các thành phần chuẩn của báo cáo gồm bìa, phân công nhiệm vụ, lời cảm ơn, mục lục, danh mục hình, danh mục bảng và danh mục thuật ngữ viết tắt.

---

## Trang bìa

Trang bìa là phần nhận diện chính thức của báo cáo, thể hiện thông tin về học phần, đề tài, nhóm thực hiện và giảng viên hướng dẫn. Nội dung trang bìa cần được trình bày trang trọng, rõ ràng và không thêm các thông tin ngoài phạm vi yêu cầu.

> 🛑 **[HÀNH ĐỘNG]**: Ghi đầy đủ tên học viện, khoa, môn học, tên đề tài, lớp, nhóm, giảng viên hướng dẫn và danh sách sinh viên thực hiện.

---

## Phân công nhiệm vụ

Phần phân công nhiệm vụ giúp thể hiện vai trò của từng thành viên trong quá trình thực hiện đề tài. Nội dung nên được trình bày dưới dạng bảng để người đọc dễ theo dõi mức độ đóng góp của từng thành viên.

> 🛑 **[HÀNH ĐỘNG]**: Lập bảng phân công rõ từng thành viên phụ trách các phần như lý thuyết ANN, lan truyền tiến, lan truyền ngược, thực nghiệm, phân tích lỗi và demo dự đoán nét vẽ.

---

## Lời cảm ơn

Lời cảm ơn là phần thể hiện thái độ nghiêm túc và sự ghi nhận đối với những cá nhân, tổ chức đã hỗ trợ quá trình thực hiện bài tập lớn. Nội dung cần ngắn gọn, khách quan và tránh các câu sáo rỗng hoặc cảm xúc quá mức.

> 🛑 **[HÀNH ĐỘNG]**: Viết ngắn gọn 100–150 từ, cảm ơn giảng viên hướng dẫn, nhà trường và các thành viên đã phối hợp thực hiện đề tài.

---

## Mục lục

Mục lục giúp người đọc nắm được cấu trúc tổng thể của báo cáo và nhanh chóng tra cứu các phần nội dung. Khi hoàn thiện báo cáo, mục lục cần được cập nhật theo đúng số trang và đúng thứ bậc tiêu đề.

> 🛑 **[HÀNH ĐỘNG]**: Tự động liệt kê đầy đủ các chương, mục và tiểu mục theo đúng cấu trúc báo cáo.

---

## Danh mục hình vẽ

Danh mục hình vẽ giúp hệ thống hóa các hình minh họa, biểu đồ và sơ đồ được sử dụng trong báo cáo. Mỗi hình được đưa vào báo cáo phải có chú thích rõ ràng và được nhắc tới trong phần nội dung.

> 🛑 **[HÀNH ĐỘNG]**: Liệt kê các hình như sơ đồ kiến trúc ANN, biểu đồ loss/accuracy, confusion matrix, ảnh dự đoán sai và pipeline xử lý ảnh vẽ tay.

---

## Danh mục bảng biểu

Danh mục bảng biểu giúp tổng hợp các bảng dữ liệu, bảng cấu hình và bảng kết quả thực nghiệm. Các bảng cần có tên rõ ràng, trình bày thống nhất và được phân tích trong phần nội dung chính.

> 🛑 **[HÀNH ĐỘNG]**: Liệt kê các bảng như bảng kích thước ma trận, bảng hyperparameter, bảng kết quả theo iteration và bảng so sánh cấu hình.

---

## Danh mục thuật ngữ và từ viết tắt

Danh mục thuật ngữ và từ viết tắt giúp người đọc hiểu nhất quán các khái niệm kỹ thuật được sử dụng trong báo cáo. Các thuật ngữ nên được giải thích ngắn gọn, chính xác và bám sát nội dung đề tài.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích các thuật ngữ như ANN, MNIST, ReLU, Softmax, Cross-Entropy, BGD, Accuracy, Confusion Matrix và Bounding Box.

---

# Chương 1. Giới thiệu đề tài

Chương này trình bày bối cảnh hình thành đề tài, mục tiêu nghiên cứu, phạm vi thực hiện và định hướng giải pháp tổng quát. Nội dung cần được viết theo mạch lập luận từ vấn đề thực tế đến phương pháp tiếp cận, không đi quá sâu vào chi tiết thuật toán.

> 🛑 **[HÀNH ĐỘNG]**: Dẫn dắt bài toán nhận diện chữ số viết tay, xác định mục tiêu, phạm vi, định hướng giải pháp và bố cục báo cáo.

---

## 1.1. Đặt vấn đề

Nhận diện chữ số viết tay là một bài toán cơ bản nhưng có ý nghĩa quan trọng trong lĩnh vực thị giác máy tính và học máy. Phần này cần làm rõ vì sao bài toán có giá trị thực tiễn và vì sao nó phù hợp với học phần Nhập môn Trí tuệ Nhân tạo.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày bối cảnh số hóa dữ liệu viết tay và nhu cầu tự động nhận diện chữ số trong các hệ thống xử lý thông tin.

---

### 1.1.1. Bài toán nhận diện chữ số viết tay trong thực tế

Trong nhiều hệ thống xử lý thông tin, dữ liệu viết tay vẫn xuất hiện dưới nhiều dạng khác nhau và cần được chuyển đổi sang dữ liệu số. Việc tự động nhận diện chữ số giúp giảm thao tác nhập liệu thủ công và hạn chế sai sót do con người.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích các tình huống như biểu mẫu, mã bưu chính, số tiền, mã định danh hoặc phiếu khảo sát cần nhận diện chữ số viết tay.

---

### 1.1.2. Nhu cầu trực quan hóa mô hình nhận diện cho người dùng

Một mô hình học máy không chỉ cần đạt kết quả định lượng trên tập dữ liệu chuẩn mà còn cần được kiểm chứng qua các tình huống đầu vào trực quan. Việc cho phép người dùng tự vẽ chữ số giúp quá trình đánh giá trở nên sinh động và gần với thực tế hơn.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích vì sao ngoài việc đánh giá bằng tập dữ liệu chuẩn, cần có cách kiểm thử trực quan bằng nét vẽ thực tế của người dùng.

---

### 1.1.3. Ý nghĩa của việc tự cài đặt ANN thay vì dùng framework

Việc tự cài đặt mạng nơ-ron bằng NumPy giúp làm rõ bản chất toán học và quy trình học của mô hình. Thay vì sử dụng các thư viện học sâu có sẵn, đề tài tập trung vào việc hiểu từng bước tính toán bên trong mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Làm rõ giá trị học thuật của việc tự triển khai lan truyền tiến, lan truyền ngược và cập nhật trọng số bằng NumPy.

---

## 1.2. Mục tiêu và phạm vi đề tài

Phần này xác định rõ những kết quả mà đề tài cần đạt được và các giới hạn được đặt ra để bảo đảm tính khả thi. Mục tiêu cần cụ thể, đo được và bám sát nội dung học phần.

> 🛑 **[HÀNH ĐỘNG]**: Xác định rõ nhóm sẽ xây dựng mô hình gì, đánh giá ra sao và giới hạn đề tài ở mức nào.

---

### 1.2.1. Mục tiêu xây dựng mô hình phân loại 10 chữ số

Mục tiêu cốt lõi của đề tài là xây dựng một mô hình có khả năng nhận ảnh chữ số viết tay và dự đoán nhãn tương ứng. Mô hình cần phân biệt được 10 lớp chữ số từ 0 đến 9.

> 🛑 **[HÀNH ĐỘNG]**: Nêu mục tiêu huấn luyện mô hình phân loại ảnh chữ số viết tay thành 10 lớp từ 0 đến 9.

---

### 1.2.2. Mục tiêu đánh giá thực nghiệm mô hình

Bên cạnh việc xây dựng mô hình, đề tài cần đánh giá mô hình bằng các chỉ số định lượng và phân tích lỗi cụ thể. Việc đánh giá thực nghiệm giúp xác định mô hình học tốt ở đâu và còn hạn chế ở những trường hợp nào.

> 🛑 **[HÀNH ĐỘNG]**: Nêu mục tiêu đo loss, accuracy, so sánh siêu tham số, phân tích confusion matrix và đánh giá các trường hợp dự đoán sai.

---

### 1.2.3. Mục tiêu kiểm thử mô hình trên nét vẽ thực tế

Dữ liệu MNIST đã được chuẩn hóa, trong khi nét vẽ thực tế của người dùng có thể khác biệt đáng kể. Do đó, đề tài cần bổ sung bước kiểm thử trên nét vẽ tự do để đánh giá khả năng ứng dụng của mô hình sau tiền xử lý.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày mục tiêu đưa mô hình đã huấn luyện vào dự đoán các chữ số do người dùng tự vẽ để kiểm tra khả năng hoạt động ngoài dữ liệu MNIST.

---

### 1.2.4. Phạm vi: MNIST, Fully Connected ANN, NumPy, Batch Gradient Descent

Phạm vi của đề tài được giới hạn ở mô hình ANN Fully Connected đơn giản nhằm tập trung vào nền tảng toán học và quy trình huấn luyện. Đề tài không sử dụng các framework học sâu để xây dựng lõi mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Khẳng định đề tài chỉ sử dụng ANN Fully Connected kiến trúc $784 \rightarrow 128 \rightarrow 10$, tự cài đặt bằng NumPy và huấn luyện bằng Batch Gradient Descent.

---

## 1.3. Định hướng giải pháp

Định hướng giải pháp trình bày cách tiếp cận tổng quát để giải quyết bài toán đã nêu. Phần này chỉ mô tả phương pháp ở mức khái quát, chưa đi sâu vào công thức và cài đặt chi tiết.

> 🛑 **[HÀNH ĐỘNG]**: Tóm tắt cách nhóm giải quyết bài toán từ dữ liệu, mô hình, huấn luyện, đánh giá đến dự đoán nét vẽ thực tế.

---

### 1.3.1. Huấn luyện ANN $784 \rightarrow 128 \rightarrow 10$ trên MNIST

Mô hình được thiết kế với một tầng đầu vào, một tầng ẩn và một tầng đầu ra. Cấu trúc này đủ đơn giản để tự cài đặt nhưng vẫn có khả năng học các quan hệ phi tuyến trong dữ liệu chữ số viết tay.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày kiến trúc mạng gồm 784 đầu vào, 128 neuron tầng ẩn và 10 neuron đầu ra.

---

### 1.3.2. Theo dõi loss và accuracy trong quá trình học

Quá trình huấn luyện cần được theo dõi bằng các chỉ số định lượng để đánh giá mức độ hội tụ của mô hình. Việc ghi nhận loss và accuracy theo thời gian giúp nhận biết mô hình đang học hiệu quả hay gặp vấn đề về tối ưu.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả việc ghi nhận train/dev loss và train/dev accuracy theo từng mốc iteration để đánh giá quá trình hội tụ.

---

### 1.3.3. Phân tích lỗi dự đoán bằng confusion matrix và mẫu sai

Kết quả accuracy tổng quát không đủ để mô tả toàn bộ hành vi của mô hình. Vì vậy, cần sử dụng confusion matrix và các mẫu dự đoán sai để phân tích sâu các trường hợp nhầm lẫn giữa các chữ số.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày định hướng dùng confusion matrix và các ảnh dự đoán sai để tìm ra các cặp chữ số dễ nhầm.

---

### 1.3.4. Kiểm thử inference trên nét vẽ người dùng

Sau khi mô hình được huấn luyện, việc kiểm thử trên nét vẽ tự do giúp đánh giá khả năng xử lý dữ liệu ngoài tập chuẩn. Trọng tâm của bước này là chuyển đổi nét vẽ thực tế về định dạng gần giống MNIST trước khi đưa vào mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Giới thiệu định hướng chuyển nét vẽ tự do thành ảnh $28 \times 28$ chuẩn MNIST rồi đưa vào mô hình để dự đoán.

---

## 1.4. Bố cục bài tập lớn

Báo cáo được tổ chức thành các chương theo trình tự từ bối cảnh, cơ sở lý thuyết, thực nghiệm đến kết luận. Cách tổ chức này giúp người đọc theo dõi được toàn bộ quá trình từ xây dựng mô hình đến đánh giá và kiểm thử thực tế.

> 🛑 **[HÀNH ĐỘNG]**: Viết thành đoạn văn liền mạch, giới thiệu nội dung các chương còn lại của báo cáo.

---

### 1.4.1. Nội dung Chương 2

Chương 2 đóng vai trò nền tảng, trình bày các kiến thức cần thiết để hiểu mô hình ANN được sử dụng trong đề tài. Các nội dung lý thuyết cần được chọn lọc, không trình bày lan man ngoài phạm vi mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Giới thiệu Chương 2 trình bày cơ sở lý thuyết về dữ liệu MNIST, ANN, lan truyền tiến, lan truyền ngược và các độ đo đánh giá.

---

### 1.4.2. Nội dung Chương 3

Chương 3 là trọng tâm của báo cáo, trình bày quy trình thực nghiệm và các kết quả đạt được. Chương này cần có bảng, biểu đồ, confusion matrix và phân tích lỗi cụ thể.

> 🛑 **[HÀNH ĐỘNG]**: Giới thiệu Chương 3 trình bày thiết kế thực nghiệm, kết quả huấn luyện, so sánh siêu tham số, phân tích lỗi và dự đoán nét vẽ thực tế.

---

### 1.4.3. Nội dung Chương 4

Chương 4 tổng hợp những kết quả quan trọng nhất của đề tài và chỉ ra các giới hạn còn tồn tại. Phần hướng phát triển cần bám sát các hạn chế đã được phân tích trong Chương 3.

> 🛑 **[HÀNH ĐỘNG]**: Giới thiệu Chương 4 tổng kết kết quả đạt được, chỉ ra hạn chế và đề xuất hướng phát triển.

---

# Chương 2. Cơ sở lý thuyết

Chương này trình bày các khái niệm và công thức nền tảng liên quan đến bài toán nhận diện chữ số viết tay bằng ANN. Nội dung được liên hệ trực tiếp với mã nguồn `ann.py`, trong đó mô hình được cài đặt thủ công bằng `NumPy`, dữ liệu được đọc bằng `Pandas`, và ảnh demo được hiển thị bằng `Matplotlib`. Các thành phần chính gồm tiền xử lý dữ liệu, kiến trúc mạng Fully Connected, lan truyền tiến, hàm mất mát, lan truyền ngược và cập nhật tham số.

---

## 2.1. Bài toán phân loại ảnh chữ số viết tay

Bài toán nhận diện chữ số viết tay trong đề tài được mô hình hóa là bài toán phân loại đa lớp. Mỗi mẫu đầu vào là một ảnh chữ số viết tay và đầu ra là một nhãn thuộc một trong 10 lớp chữ số từ $0$ đến $9$. Trong mã nguồn, nhãn thật được lấy từ cột đầu tiên của `train.csv`, còn các cột còn lại là đặc trưng pixel của ảnh.

Về mặt toán học, mô hình cần học một hàm ánh xạ:

$$
f_{\theta}: \mathbb{R}^{784} \rightarrow \{0,1,2,3,4,5,6,7,8,9\}
$$

Trong đó $\theta$ là tập tham số của mạng, gồm $W^{[1]}$, $b^{[1]}$, $W^{[2]}$ và $b^{[2]}$.

---

### 2.1.1. Đầu vào của bài toán

Đầu vào của mô hình là ảnh chữ số viết tay mức xám kích thước $28 \times 28$. Trong `ann.py`, ảnh được đưa vào mạng dưới dạng vector có $784$ phần tử, phù hợp với ma trận trọng số đầu tiên `W1` có shape `(128, 784)`.

Công thức chuyển đổi kích thước ảnh là:

$$
28 \times 28 = 784
$$

Do đó, mỗi ảnh được biểu diễn dưới dạng:

$$
x^{(i)} \in \mathbb{R}^{784}
$$

Trong code, dữ liệu đặc trưng được lấy bằng `X_dev = data_dev[1:n]`, `X_train = data_train[1:n]` và `X_test = test_data / 255.`. Việc bỏ dòng đầu tiên trong `data_dev` và `data_train` phản ánh rằng dòng đầu tiên sau khi chuyển vị là nhãn, còn các dòng còn lại là pixel.

---

### 2.1.2. Đầu ra của bài toán

Đầu ra của mô hình là vector xác suất trên 10 lớp chữ số. Trong `ann.py`, tầng cuối có ma trận `W2` shape `(10, 128)` và bias `b2` shape `(10, 1)`, vì vậy logits tầng đầu ra có 10 hàng, tương ứng với 10 chữ số.

Với một mẫu $i$, đầu ra xác suất có dạng:

$$
A^{[2],(i)} \in \mathbb{R}^{10}
$$

Nhãn dự đoán được lấy bằng hàm `get_predictions(A2)`, trong đó code sử dụng:

```python
np.argmax(A2, 0)
```

Điều này có nghĩa là mô hình chọn chỉ số lớp có xác suất lớn nhất theo từng cột mẫu.

---

### 2.1.3. Đặc điểm của phân loại đa lớp

Bài toán này là bài toán phân loại đa lớp, trong đó mỗi ảnh chỉ thuộc đúng một lớp trong 10 lớp chữ số. Vì mỗi mẫu chỉ có một nhãn đúng, nhãn số nguyên cần được chuyển thành vector one-hot khi tính Cross-Entropy Loss.

Trong `ann.py`, hàm `one_hot(Y)` tạo ma trận nhãn bằng các bước:

```python
one_hot_Y = np.zeros((Y.size, Y.max() + 1))
one_hot_Y[np.arange(Y.size), Y] = 1
one_hot_Y = one_hot_Y.T
```

Sau khi chuyển vị, ma trận one-hot có dạng:

$$
Y \in \mathbb{R}^{10 \times m}
$$

Trong đó $m$ là số mẫu trong batch hoặc tập dữ liệu đang xét.

---

## 2.2. Dữ liệu MNIST và tiền xử lý

Dữ liệu được đọc từ hai file `train.csv` và `test.csv`. Trong `ann.py`, file `train.csv` được đọc bằng `pd.read_csv('train.csv')`, sau đó chuyển sang mảng `NumPy` bằng `np.array(data)`. Dữ liệu có nhãn được xáo trộn bằng `np.random.shuffle(data)` trước khi chia thành tập dev và tập train.

Code chia dữ liệu như sau:

```python
data_dev = data[0:4000].T
data_train = data[4000:m].T
```

Vì vậy, tập dev gồm 4000 mẫu đầu tiên sau khi shuffle, còn tập train gồm các mẫu còn lại từ vị trí 4000 đến hết dữ liệu. File `test.csv` được đọc riêng, shuffle, lấy 10000 mẫu đầu và chỉ dùng để demo dự đoán trực quan vì trong code không có nhãn test.

---

### 2.2.1. Cấu trúc ảnh $28 \times 28$

Mỗi ảnh chữ số viết tay có kích thước $28 \times 28$, tương ứng với $784$ giá trị pixel. Trong code, cấu trúc này được xác nhận trực tiếp ở hàm `test_prediction`, nơi một ảnh test được reshape để hiển thị:

```python
current_image = current_image.reshape((28, 28)) * 255
```

Điều này cho thấy dữ liệu đầu vào ban đầu là vector $784$ chiều, nhưng có thể khôi phục về ảnh $28 \times 28$ để trực quan hóa.

---

### 2.2.2. Flatten ảnh thành vector 784 chiều

Mạng Fully Connected không xử lý trực tiếp ma trận ảnh hai chiều mà nhận vector đặc trưng. Vì vậy, ảnh $28 \times 28$ được biểu diễn thành vector $784$ chiều trước khi đi vào tầng đầu vào.

Biểu diễn toán học:

$$
x^{(i)} \in \mathbb{R}^{28 \times 28}
\rightarrow
x^{(i)} \in \mathbb{R}^{784}
$$

Trong code, việc dữ liệu đã ở dạng các cột pixel trong CSV cho phép lấy trực tiếp các đặc trưng bằng `data_train[1:n]` và `data_dev[1:n]` sau khi chuyển vị.

---

### 2.2.3. Normalize pixel

Trong `ann.py`, các giá trị pixel được chuẩn hóa bằng cách chia cho $255$:

```python
X_dev = X_dev / 255.
X_train = X_train / 255.
X_test = test_data / 255.
```

Do giá trị pixel ảnh xám thường nằm trong khoảng từ $0$ đến $255$, phép chia này đưa dữ liệu về khoảng $[0,1]$:

$$
0 \leq x_{\text{norm}} \leq 1
$$

Việc chuẩn hóa giúp các giá trị đầu vào có cùng thang đo, làm cho quá trình tính toán ma trận và cập nhật gradient ổn định hơn.

---

### 2.2.4. One-hot encoding nhãn

Nhãn ban đầu trong `train.csv` là số nguyên từ $0$ đến $9$. Để tính Cross-Entropy Loss, code chuyển nhãn thành ma trận one-hot bằng hàm `one_hot(Y)`.

Nếu có $m$ mẫu, sau khi chuyển đổi, ma trận nhãn có dạng:

$$
Y \in \mathbb{R}^{10 \times m}
$$

Trong đó mỗi cột là vector one-hot của một mẫu. Cách triển khai trong code dùng `np.zeros`, `np.arange` và phép gán chỉ số để đặt giá trị $1$ tại vị trí lớp đúng.

---

## 2.3. Mô hình ANN Fully Connected

Mô hình trong `ann.py` là mạng nơ-ron Fully Connected gồm một tầng ẩn. Các phép tính được cài đặt thủ công bằng `NumPy`, không sử dụng framework học sâu như TensorFlow, Keras hoặc PyTorch.

Mạng gồm các thành phần chính:
- Tầng đầu vào có $784$ đặc trưng.
- Tầng ẩn có $128$ neuron.
- Tầng đầu ra có $10$ neuron.
- Hàm kích hoạt tầng ẩn là `ReLU`.
- Hàm đầu ra là `softmax`.

---

### 2.3.1. Kiến trúc $784 \rightarrow 128 \rightarrow 10$

Kiến trúc mô hình được xác định trực tiếp từ hàm `init_params()`:

```python
W1 = np.random.rand(128, 784) - 0.5
b1 = np.random.rand(128, 1) - 0.5
W2 = np.random.rand(10, 128) - 0.5
b2 = np.random.rand(10, 1) - 0.5
```

Vì vậy, kiến trúc mạng là:

$$
784 \rightarrow 128 \rightarrow 10
$$

Tầng đầu vào nhận vector ảnh $784$ chiều. Tầng ẩn gồm $128$ neuron. Tầng đầu ra gồm $10$ neuron, tương ứng với 10 lớp chữ số.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 2.3.2. Vai trò của trọng số và bias

Trong mô hình, trọng số và bias là các tham số được học trong quá trình huấn luyện. Ma trận `W1` biến đổi đầu vào $X$ sang tầng ẩn, còn `b1` dịch chuyển giá trị tuyến tính tại tầng ẩn. Tương tự, `W2` và `b2` biến đổi kích hoạt tầng ẩn thành logits đầu ra.

Các tham số của mô hình là:

$$
\theta = \{W^{[1]}, b^{[1]}, W^{[2]}, b^{[2]}\}
$$

Trong code, các tham số tương ứng là `W1`, `b1`, `W2`, `b2`. Chúng được cập nhật trong hàm `update_params`.

---

### 2.3.3. Bảng kích thước các ma trận trong mô hình

Các kích thước dưới đây được suy ra trực tiếp từ `init_params()`, `forward_prop()` và cách dữ liệu được tổ chức theo cột mẫu trong `ann.py`.

| Ký hiệu toán học | Biến trong code | Kích thước | Ý nghĩa |
|---|---|---:|---|
| $X$ | `X` | $784 \times m$ | Ma trận dữ liệu đầu vào |
| $Y$ | `one_hot_Y` | $10 \times m$ | Ma trận nhãn one-hot |
| $W^{[1]}$ | `W1` | $128 \times 784$ | Trọng số từ input sang hidden |
| $b^{[1]}$ | `b1` | $128 \times 1$ | Bias tầng ẩn |
| $Z^{[1]}$ | `Z1` | $128 \times m$ | Giá trị tuyến tính tầng ẩn |
| $A^{[1]}$ | `A1` | $128 \times m$ | Kích hoạt tầng ẩn sau ReLU |
| $W^{[2]}$ | `W2` | $10 \times 128$ | Trọng số từ hidden sang output |
| $b^{[2]}$ | `b2` | $10 \times 1$ | Bias tầng đầu ra |
| $Z^{[2]}$ | `Z2` | $10 \times m$ | Logits đầu ra |
| $A^{[2]}$ | `A2` | $10 \times m$ | Xác suất dự đoán |

---

## 2.4. Lan truyền tiến

Lan truyền tiến được cài đặt trong hàm `forward_prop(W1, b1, W2, b2, X)`. Hàm này nhận tham số hiện tại và dữ liệu đầu vào, sau đó trả về `Z1`, `A1`, `Z2`, `A2`.

Code thực hiện:

```python
Z1 = W1.dot(X) + b1
A1 = ReLU(Z1)
Z2 = W2.dot(A1) + b2
A2 = softmax(Z2)
```

---

### 2.4.1. Tính toán tầng ẩn

Tại tầng ẩn, code tính:

```python
Z1 = W1.dot(X) + b1
```

Công thức toán học tương ứng:

$$
Z^{[1]} = W^{[1]}X + b^{[1]}
$$

Với $W^{[1]} \in \mathbb{R}^{128 \times 784}$ và $X \in \mathbb{R}^{784 \times m}$, kết quả $W^{[1]}X$ có kích thước $128 \times m$. Bias $b^{[1]}$ có kích thước $128 \times 1$ và được NumPy broadcast theo từng cột mẫu khi cộng vào $Z^{[1]}$.

---

### 2.4.2. Hàm kích hoạt ReLU

Hàm ReLU được cài đặt trong `ann.py` như sau:

```python
def ReLU(Z):
    return np.maximum(Z, 0)
```

Công thức toán học:

$$
ReLU(z) = \max(0,z)
$$

ReLU giữ nguyên các giá trị dương và đưa các giá trị âm về $0$. Nhờ đó, mô hình có khả năng biểu diễn quan hệ phi tuyến thay vì chỉ là tổ hợp tuyến tính của đầu vào.

---

### 2.4.3. Tính toán tầng đầu ra

Sau khi có kích hoạt tầng ẩn $A^{[1]}$, code tính logits tầng đầu ra:

```python
Z2 = W2.dot(A1) + b2
```

Công thức toán học:

$$
Z^{[2]} = W^{[2]}A^{[1]} + b^{[2]}
$$

Với $W^{[2]} \in \mathbb{R}^{10 \times 128}$ và $A^{[1]} \in \mathbb{R}^{128 \times m}$, logits $Z^{[2]}$ có kích thước $10 \times m$.

---

### 2.4.4. Softmax và xác suất dự đoán

Hàm `softmax(Z)` trong `ann.py` được viết như sau:

```python
def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
```

Công thức tương ứng:

$$
A^{[2]} = Softmax(Z^{[2]})
$$

Với mỗi cột mẫu, Softmax chuyển logits thành xác suất dự đoán trên 10 lớp chữ số. Nhãn dự đoán được lấy bằng `np.argmax(A2, 0)` trong hàm `get_predictions(A2)`.

Lưu ý: mã nguồn hiện tại dùng công thức Softmax trực tiếp bằng `np.exp(Z)` và không trừ `np.max(Z, axis=0, keepdims=True)` trước khi lấy hàm mũ.

---

## 2.5. Hàm mất mát và lan truyền ngược

Sau khi lan truyền tiến tạo ra $A^{[2]}$, mô hình tính sai số bằng Cross-Entropy Loss và dùng lan truyền ngược để tính gradient cho từng tham số. Các hàm liên quan trong `ann.py` gồm `compute_loss`, `backward_prop` và `update_params`.

---

### 2.5.1. Cross-Entropy Loss

Hàm mất mát được cài đặt trong `compute_loss(A2, Y)`. Code chuyển nhãn sang one-hot, thêm hằng số `epsilon = 1e-8` để tránh `log(0)`, rồi tính trung bình loss trên $m$ mẫu.

Code:

```python
epsilon = 1e-8
loss = -np.sum(one_hot_Y * np.log(A2 + epsilon)) / m
```

Công thức toán học:

$$
J(\theta) =
-\frac{1}{m}
\sum_{i=1}^{m}
\sum_{k=1}^{10}
Y_k^{(i)} \log\left(A_k^{[2],(i)} + \epsilon\right)
$$

Loss càng nhỏ thì phân phối xác suất dự đoán càng gần với nhãn thật dạng one-hot.

---

### 2.5.2. Gradient tại tầng đầu ra

Trong `backward_prop`, gradient tại tầng đầu ra được tính bằng:

```python
dZ2 = A2 - one_hot_Y
```

Công thức:

$$
dZ^{[2]} = A^{[2]} - Y
$$

Đây là sai lệch giữa xác suất dự đoán và nhãn thật dạng one-hot. Công thức này là dạng rút gọn thường dùng khi kết hợp Softmax với Cross-Entropy.

---

### 2.5.3. Gradient tại tầng ẩn

Lan truyền lỗi về tầng ẩn được cài đặt bằng:

```python
dZ1 = W2.T.dot(dZ2) * ReLU_deriv(Z1)
```

Trong đó `ReLU_deriv(Z)` được định nghĩa:

```python
def ReLU_deriv(Z):
    return Z > 0
```

Công thức toán học:

$$
dZ^{[1]} = (W^{[2]})^T dZ^{[2]} \odot ReLU'(Z^{[1]})
$$

Toán tử $\odot$ biểu diễn phép nhân từng phần tử. Đạo hàm ReLU xác định neuron nào có giá trị tuyến tính dương và được phép truyền gradient.

---

### 2.5.4. Cập nhật tham số bằng Batch Gradient Descent

Trong code, gradient được tính trên toàn bộ ma trận $X$ được truyền vào `gradient_descent`, do đó cách cập nhật tương ứng với Batch Gradient Descent trên tập dữ liệu đầu vào của hàm.

Các gradient được tính:

```python
dW2 = 1 / m * dZ2.dot(A1.T)
db2 = 1 / m * np.sum(dZ2, axis=1, keepdims=True)
dW1 = 1 / m * dZ1.dot(X.T)
db1 = 1 / m * np.sum(dZ1, axis=1, keepdims=True)
```

Cập nhật tham số được thực hiện trong `update_params`:

```python
W1 = W1 - alpha * dW1
b1 = b1 - alpha * db1
W2 = W2 - alpha * dW2
b2 = b2 - alpha * db2
```

Công thức tổng quát:

$$
W^{[l]} := W^{[l]} - \alpha dW^{[l]}
$$

$$
b^{[l]} := b^{[l]} - \alpha db^{[l]}
$$

Trong đó $\alpha$ là learning rate.

---

## 2.6. Phương pháp đánh giá

Trong `ann.py`, mô hình được đánh giá bằng loss và accuracy trên tập train và tập dev trong quá trình huấn luyện. Các giá trị này được in ra sau mỗi 10 iteration.

Code kiểm tra theo chu kỳ:

```python
if i % 10 == 0:
```

Các hàm đánh giá chính là `compute_loss`, `get_predictions` và `get_accuracy`.

---

### 2.6.1. Train accuracy và dev accuracy

Accuracy được tính trong hàm `get_accuracy(predictions, Y)`:

```python
return np.sum(predictions == Y) / Y.size
```

Train accuracy dùng dự đoán từ $A^{[2]}$ trên tập train. Dev accuracy được tính bằng cách forward lại trên `X_dev`:

```python
_, _, _, A2_dev = forward_prop(W1, b1, W2, b2, X_dev)
dev_pred = get_predictions(A2_dev)
dev_acc = get_accuracy(dev_pred, Y_dev)
```

Train accuracy phản ánh khả năng học trên tập huấn luyện, còn dev accuracy phản ánh khả năng tổng quát hóa trên dữ liệu không dùng trực tiếp để cập nhật trọng số.

---

### 2.6.2. Train loss và dev loss

Train loss được tính bằng:

```python
train_loss = compute_loss(A2, Y)
```

Dev loss được tính bằng:

```python
dev_loss = compute_loss(A2_dev, Y_dev)
```

Việc theo dõi train loss và dev loss giúp đánh giá quá trình hội tụ. Nếu train loss giảm nhưng dev loss không giảm tương ứng, mô hình có thể có dấu hiệu overfitting.

---

### 2.6.3. Confusion matrix

Trong `ann.py` hiện tại không có hàm xây dựng confusion matrix. Vì vậy, nội dung confusion matrix và hình minh họa cần được bổ sung từ kết quả chạy terminal hoặc script đánh giá riêng.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 2.6.4. Phân tích mẫu dự đoán sai

Trong `ann.py` hiện tại có hàm `test_prediction(index, W1, b1, W2, b2)` để hiển thị ảnh test và dự đoán nhãn. Tuy nhiên, tập `test.csv` trong code không có nhãn thật đi kèm, nên không thể xác định mẫu dự đoán sai trên test bằng code hiện tại. Việc phân tích mẫu sai cần thực hiện trên tập dev có nhãn sau khi lấy dự đoán và so sánh với `Y_dev`.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

# Chương 3. Thực nghiệm và đánh giá kết quả

Chương này trình bày quá trình triển khai, huấn luyện và đánh giá mô hình ANN bằng `NumPy` theo đúng mã nguồn `ann.py`. Các thông tin cố định như cách chia dữ liệu, kiến trúc, learning rate, số iteration và phương pháp khởi tạo được lấy trực tiếp từ code. Các kết quả cần chạy chương trình như accuracy cuối cùng, loss cuối cùng, biểu đồ và confusion matrix không được tự suy đoán.

---

## 3.1. Thiết kế thực nghiệm

Thiết kế thực nghiệm trong `ann.py` gồm các bước: đọc dữ liệu CSV, shuffle dữ liệu train, chia tập dev/train, chuẩn hóa pixel, khởi tạo tham số, huấn luyện bằng Batch Gradient Descent, in loss/accuracy định kỳ, lưu mô hình vào `model_weights.npz` và demo dự đoán trên `test.csv`.

---

### 3.1.1. Môi trường chạy

Mã nguồn sử dụng Python cùng các thư viện:
- `NumPy` cho tính toán ma trận.
- `Pandas` để đọc file `train.csv` và `test.csv`.
- `Matplotlib` để hiển thị ảnh demo.
- `os` để kiểm tra file `model_weights.npz`.

Cấu hình phần cứng thực nghiệm được ghi nhận là: Workstation Dual Xeon 2676, 64GB RAM, GPU GTX 1050Ti.

Lưu ý: code hiện tại chỉ dùng `NumPy` CPU, không có lệnh sử dụng GPU.

---

### 3.1.2. Cách chia tập train/dev/test demo

Trong `ann.py`, dữ liệu có nhãn được đọc từ `train.csv`:

```python
data = pd.read_csv('train.csv')
data = np.array(data)
m, n = data.shape
np.random.shuffle(data)
```

Sau khi shuffle, code chia dữ liệu:

```python
data_dev = data[0:4000].T
data_train = data[4000:m].T
```

Tập dev gồm 4000 mẫu đầu tiên sau khi shuffle. Tập train gồm các mẫu từ vị trí 4000 đến hết dữ liệu.

Nhãn và đặc trưng được tách như sau:

```python
Y_dev = data_dev[0]
X_dev = data_dev[1:n]
Y_train = data_train[0]
X_train = data_train[1:n]
```

Tập test được đọc từ `test.csv`, shuffle, lấy 10000 mẫu đầu và chuẩn hóa:

```python
test_data = pd.read_csv('test.csv')
test_data = np.array(test_data)
np.random.shuffle(test_data)
test_data = test_data[0:10000].T
X_test = test_data / 255.
```

Trong code hiện tại, `test.csv` chỉ được dùng để demo dự đoán và hiển thị ảnh, không dùng để tính accuracy vì không có nhãn test trong chương trình.

---

### 3.1.3. Quy trình huấn luyện

Quy trình huấn luyện được cài đặt trong hàm `gradient_descent(X, Y, alpha, iterations)`. Mỗi iteration thực hiện các bước:

1. Lan truyền tiến bằng `forward_prop`.
2. Tính gradient bằng `backward_prop`.
3. Cập nhật tham số bằng `update_params`.
4. Mỗi 10 iteration, in train loss, train accuracy, dev loss và dev accuracy.

Code chính:

```python
for i in range(iterations):
    Z1, A1, Z2, A2 = forward_prop(W1, b1, W2, b2, X)
    dW1, db1, dW2, db2 = backward_prop(Z1, A1, Z2, A2, W1, W2, X, Y)
    W1, b1, W2, b2 = update_params(W1, b1, W2, b2, dW1, db1, dW2, db2, alpha)
```

---

### 3.1.4. Quy trình đánh giá

Trong quá trình huấn luyện, code đánh giá mô hình sau mỗi 10 iteration. Train metrics được tính trên $X$ và $Y$ truyền vào `gradient_descent`. Dev metrics được tính bằng cách forward trên `X_dev` và so sánh với `Y_dev`.

Các chỉ số được in:
- `Train loss`
- `Train accurancy`
- `Dev loss`
- `Dev accurancy`

Trong code hiện tại chưa có hàm confusion matrix và chưa có cơ chế lưu lịch sử metrics ra file. Vì vậy, bảng kết quả, biểu đồ và confusion matrix cần lấy từ terminal hoặc bổ sung script đánh giá riêng.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

## 3.2. Cấu hình mô hình cơ sở

Cấu hình baseline trong `ann.py` được xác định tại đoạn cuối file. Nếu tồn tại `model_weights.npz`, code tải mô hình đã lưu. Nếu chưa tồn tại, code huấn luyện mô hình bằng `gradient_descent(X_train, Y_train, 0.1, 500)` và lưu lại tham số.

```python
if os.path.exists("model_weights.npz"):
    W1, b1, W2, b2 = load_model()
else:
    W1, b1, W2, b2 = gradient_descent(X_train, Y_train, 0.1, 500)
    save_model(W1, b1, W2, b2)
```

---

### 3.2.1. Kiến trúc $784 \rightarrow 128 \rightarrow 10$

Baseline sử dụng kiến trúc:

$$
784 \rightarrow 128 \rightarrow 10
$$

Kiến trúc này được xác nhận bởi shape của các tham số trong `init_params()`:
- `W1`: `(128, 784)`
- `b1`: `(128, 1)`
- `W2`: `(10, 128)`
- `b2`: `(10, 1)`

Tầng ẩn dùng ReLU, tầng đầu ra dùng Softmax.

---

### 3.2.2. Learning rate mặc định

Learning rate mặc định trong baseline là:

$$
\alpha = 0.1
$$

Giá trị này được truyền trực tiếp trong lệnh:

```python
gradient_descent(X_train, Y_train, 0.1, 500)
```

Trong code, biến learning rate được đặt tên là `alpha` và được dùng trong `update_params`.

---

### 3.2.3. Số iteration mặc định

Số iteration baseline là:

$$
500
$$

Giá trị này cũng được truyền trực tiếp trong:

```python
gradient_descent(X_train, Y_train, 0.1, 500)
```

Code ghi log sau mỗi 10 iteration bằng điều kiện:

```python
if i % 10 == 0:
```

Vì vậy, các mốc log gồm $0$, $10$, $20$, ..., $490$.

---

### 3.2.4. Phương pháp khởi tạo trọng số

Các tham số được khởi tạo trong `init_params()` bằng `np.random.rand(...) - 0.5`. Cụ thể:

```python
W1 = np.random.rand(128, 784) - 0.5
b1 = np.random.rand(128, 1) - 0.5
W2 = np.random.rand(10, 128) - 0.5
b2 = np.random.rand(10, 1) - 0.5
```

Điều này có nghĩa là các giá trị ban đầu nằm trong khoảng xấp xỉ $[-0.5, 0.5)$. Code hiện tại không sử dụng He Initialization hoặc Xavier Initialization.

---

## 3.3. Kết quả mô hình cơ sở

Kết quả mô hình cơ sở được lấy từ log terminal do người thực hiện cung cấp sau khi chạy `ann.py` với cấu hình baseline: kiến trúc $784 \rightarrow 128 \rightarrow 10$, learning rate $\alpha = 0.1$ và $500$ iteration. Chương trình ghi log mỗi 10 iteration, gồm train loss, train accuracy, dev loss và dev accuracy.

---

### 3.3.1. Bảng loss và accuracy theo iteration

| Iteration | Train loss | Train accuracy | Dev loss | Dev accuracy |
|---:|---:|---:|---:|---:|
| 0 | 8.8319745875 | 0.0839473684 | 6.3236312161 | 0.1205000000 |
| 10 | 2.0601055767 | 0.5059736842 | 1.9383351488 | 0.5235000000 |
| 20 | 1.3548867758 | 0.6357368421 | 1.3215172169 | 0.6457500000 |
| 30 | 1.0742107321 | 0.6975789474 | 1.0636665554 | 0.7010000000 |
| 40 | 0.9173033143 | 0.7366578947 | 0.9175688388 | 0.7402500000 |
| 50 | 0.8160732271 | 0.7637368421 | 0.8224562096 | 0.7607500000 |
| 60 | 0.7449111917 | 0.7841052632 | 0.7549011624 | 0.7760000000 |
| 70 | 0.6915044129 | 0.7985789474 | 0.7038544335 | 0.7905000000 |
| 80 | 0.6496005244 | 0.8104473684 | 0.6637046194 | 0.8027500000 |
| 90 | 0.6155761687 | 0.8203421053 | 0.6310096661 | 0.8112500000 |
| 100 | 0.5872707761 | 0.8280263158 | 0.6037528838 | 0.8195000000 |
| 110 | 0.5632610588 | 0.8347368421 | 0.5805957747 | 0.8260000000 |
| 120 | 0.5425123746 | 0.8408421053 | 0.5605776108 | 0.8310000000 |
| 130 | 0.5243117696 | 0.8456578947 | 0.5430453543 | 0.8372500000 |
| 140 | 0.5081966087 | 0.8505263158 | 0.5275446226 | 0.8445000000 |
| 150 | 0.4938069594 | 0.8547368421 | 0.5136913978 | 0.8462500000 |
| 160 | 0.4808417525 | 0.8583947368 | 0.5011965103 | 0.8505000000 |
| 170 | 0.4690785829 | 0.8616842105 | 0.4898537461 | 0.8520000000 |
| 180 | 0.4583462056 | 0.8647894737 | 0.4795031388 | 0.8555000000 |
| 190 | 0.4484894106 | 0.8680263158 | 0.4700064761 | 0.8577500000 |
| 200 | 0.4393805345 | 0.8706578947 | 0.4612569672 | 0.8607500000 |
| 210 | 0.4309355676 | 0.8728421053 | 0.4531484749 | 0.8635000000 |
| 220 | 0.4230737462 | 0.8750000000 | 0.4456039018 | 0.8667500000 |
| 230 | 0.4157138650 | 0.8771052632 | 0.4385447609 | 0.8690000000 |
| 240 | 0.4088059462 | 0.8792631579 | 0.4319254067 | 0.8710000000 |
| 250 | 0.4022981703 | 0.8808157895 | 0.4257004191 | 0.8715000000 |
| 260 | 0.3961569271 | 0.8824473684 | 0.4198415896 | 0.8735000000 |
| 270 | 0.3903464381 | 0.8841842105 | 0.4143232492 | 0.8735000000 |
| 280 | 0.3848408212 | 0.8855263158 | 0.4091180204 | 0.8750000000 |
| 290 | 0.3796220680 | 0.8870263158 | 0.4041979582 | 0.8760000000 |
| 300 | 0.3746652468 | 0.8886052632 | 0.3995328319 | 0.8780000000 |
| 310 | 0.3699420061 | 0.8903157895 | 0.3950742899 | 0.8797500000 |
| 320 | 0.3654347287 | 0.8914736842 | 0.3908175582 | 0.8807500000 |
| 330 | 0.3611285841 | 0.8926578947 | 0.3867538342 | 0.8822500000 |
| 340 | 0.3570055197 | 0.8940526316 | 0.3828682644 | 0.8835000000 |
| 350 | 0.3530523811 | 0.8953157895 | 0.3791511268 | 0.8842500000 |
| 360 | 0.3492598518 | 0.8964736842 | 0.3755824364 | 0.8857500000 |
| 370 | 0.3456094937 | 0.8973421053 | 0.3721472420 | 0.8872500000 |
| 380 | 0.3420952881 | 0.8983421053 | 0.3688492215 | 0.8880000000 |
| 390 | 0.3387110131 | 0.8993947368 | 0.3656814511 | 0.8892500000 |
| 400 | 0.3354521004 | 0.9000000000 | 0.3626256426 | 0.8902500000 |
| 410 | 0.3323059564 | 0.9008947368 | 0.3596734568 | 0.8917500000 |
| 420 | 0.3292641978 | 0.9015789474 | 0.3568170097 | 0.8935000000 |
| 430 | 0.3263162773 | 0.9027894737 | 0.3540503845 | 0.8947500000 |
| 440 | 0.3234622658 | 0.9038421053 | 0.3513723770 | 0.8952500000 |
| 450 | 0.3206984619 | 0.9047105263 | 0.3487892165 | 0.8957500000 |
| 460 | 0.3180185803 | 0.9054210526 | 0.3462960735 | 0.8962500000 |
| 470 | 0.3154140023 | 0.9060526316 | 0.3438729534 | 0.8985000000 |
| 480 | 0.3128841153 | 0.9068947368 | 0.3415244827 | 0.8995000000 |
| 490 | 0.3104269388 | 0.9077105263 | 0.3392493940 | 0.8997500000 |

Ở mốc log cuối cùng, mô hình đạt train loss $0.3104269388$, train accuracy $0.9077105263$, dev loss $0.3392493940$ và dev accuracy $0.8997500000$.

---

### 3.3.2. Biểu đồ train/dev loss

Từ log terminal, train loss giảm từ $8.8319745875$ tại iteration $0$ xuống $0.3104269388$ tại iteration $490$. Dev loss giảm từ $6.3236312161$ xuống $0.3392493940$. Hai đường loss cùng giảm đều, trong đó dev loss luôn gần train loss ở giai đoạn cuối, cho thấy quá trình huấn luyện có xu hướng hội tụ ổn định.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.3.3. Biểu đồ train/dev accuracy

Từ log terminal, train accuracy tăng từ $0.0839473684$ tại iteration $0$ lên $0.9077105263$ tại iteration $490$. Dev accuracy tăng từ $0.1205000000$ lên $0.8997500000$. Khoảng cách giữa train accuracy và dev accuracy ở mốc cuối là khoảng $0.0079605263$, cho thấy mô hình chưa có dấu hiệu overfitting mạnh trong lần chạy baseline này.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.3.4. Nhận xét về tốc độ hội tụ

Mô hình cải thiện rất nhanh trong giai đoạn đầu. Từ iteration $0$ đến $100$, train loss giảm từ $8.8319745875$ xuống $0.5872707761$, còn dev accuracy tăng từ $0.1205000000$ lên $0.8195000000$. Sau khoảng iteration $200$, tốc độ cải thiện chậm lại, thể hiện qua việc loss tiếp tục giảm nhưng với biên độ nhỏ hơn. Đến iteration $490$, mô hình đạt dev accuracy $0.8997500000$, cho thấy cấu hình baseline đã học được đặc trưng phân loại cơ bản của chữ số viết tay và tiến gần vùng hội tụ.

---

## 3.4. So sánh siêu tham số

Trong `ann.py` hiện tại, chỉ có một cấu hình huấn luyện baseline được gọi trực tiếp: learning rate $\alpha = 0.1$, số iteration $500$, hidden size $128$. Code chưa có vòng lặp tự động để so sánh nhiều learning rate, nhiều số neuron tầng ẩn hoặc nhiều số iteration.

Vì vậy, các kết quả so sánh siêu tham số cần được sinh từ terminal sau khi chạy thêm các cấu hình thực nghiệm.

---

### 3.4.1. Ảnh hưởng của learning rate

Code hiện tại chỉ chạy baseline với:

$$
\alpha = 0.1
$$

Các learning rate khác như $0.01$, $0.05$ hoặc $0.2$ chưa được chạy tự động trong `ann.py`.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.4.2. Ảnh hưởng của số neuron tầng ẩn

Code hiện tại cố định hidden size bằng $128$ thông qua shape của `W1`, `b1`, `W2`:

```python
W1 = np.random.rand(128, 784) - 0.5
b1 = np.random.rand(128, 1) - 0.5
W2 = np.random.rand(10, 128) - 0.5
```

Các cấu hình hidden layer như $64$ hoặc $256$ neuron chưa được chạy tự động trong `ann.py`.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.4.3. Ảnh hưởng của số iteration

Code hiện tại chạy baseline với:

$$
iterations = 500
$$

Các giá trị iteration khác chưa được chạy tự động trong `ann.py`.

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.4.4. So sánh các cấu hình thực nghiệm

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---

### 3.4.5. Lựa chọn cấu hình cuối cùng

[CHỜ ĐIỀN SỐ LIỆU/ẢNH TỪ TERMINAL]

---
## 3.5. Đánh giá bằng confusion matrix

Confusion matrix giúp phân tích hiệu năng của mô hình theo từng lớp chữ số. Đây là công cụ quan trọng để phát hiện các nhóm chữ số thường bị nhầm lẫn với nhau.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày confusion matrix để phân tích chi tiết hiệu năng theo từng lớp chữ số.

---

### 3.5.1. Xây dựng confusion matrix trên tập dev

Confusion matrix cần được xây dựng trên tập dev có nhãn để phản ánh khách quan khả năng tổng quát hóa. Khi trình bày, cần giải thích rõ ý nghĩa của hàng, cột và đường chéo chính.

> 🛑 **[HÀNH ĐỘNG]**: Chèn confusion matrix của mô hình cuối cùng trên tập dev và giải thích cách đọc hàng/cột.

---

### 3.5.2. Các lớp chữ số dễ nhận diện

Một số chữ số có hình dạng đặc trưng rõ ràng nên thường được mô hình nhận diện tốt hơn. Việc xác định các lớp này giúp chỉ ra điểm mạnh của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Chỉ ra các chữ số có tỷ lệ dự đoán đúng cao và phân tích vì sao hình dạng của chúng tương đối rõ ràng.

---

### 3.5.3. Các cặp chữ số dễ nhầm lẫn

Các cặp chữ số có cấu trúc hình học gần nhau thường tạo ra lỗi dự đoán. Phân tích các cặp này giúp hiểu sâu hơn giới hạn của ANN Fully Connected khi xử lý ảnh đã flatten.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích các cặp như 4–9, 1–7, 3–5 hoặc các cặp xuất hiện rõ trong confusion matrix thực tế.

---

### 3.5.4. Nhận xét tổng quan từ confusion matrix

Sau khi phân tích từng nhóm lỗi, cần tổng hợp lại các nhận xét chính từ confusion matrix. Phần này nên liên hệ với kiến trúc mô hình và đặc điểm dữ liệu đầu vào.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết điểm mạnh và điểm yếu của mô hình dựa trên phân bố lỗi giữa các lớp.

---

## 3.6. Phân tích lỗi chi tiết

Phân tích lỗi chi tiết giúp chuyển các sai số định lượng thành nhận xét có ý nghĩa về dữ liệu và mô hình. Phần này cần sử dụng ảnh minh họa cụ thể thay vì chỉ mô tả chung chung.

> 🛑 **[HÀNH ĐỘNG]**: Đi sâu vào các trường hợp dự đoán sai để giải thích nguyên nhân từ nét viết và giới hạn của ANN Fully Connected.

---

### 3.6.1. Trường hợp nhầm số 4 và số 9

Số 4 và số 9 có thể bị nhầm khi nét viết của số 4 tạo thành vùng khép kín hoặc khi số 9 bị viết hở. Đây là cặp lỗi phù hợp để phân tích ảnh hưởng của hình dạng và nét nối.

> 🛑 **[HÀNH ĐỘNG]**: Chèn ảnh mẫu sai nếu có, phân tích phần vòng khép kín hoặc nét nối khiến số 4 bị nhìn giống số 9 hoặc ngược lại.

---

### 3.6.2. Trường hợp nhầm số 1 và số 7

Số 1 và số 7 thường bị nhầm khi số 1 có nét nghiêng hoặc có gạch ngang phía trên. Sự tương đồng về bố cục pixel sau khi flatten có thể làm mô hình khó phân biệt hai lớp này.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích các chữ số 1 có nét nghiêng hoặc nét ngang phía trên dễ bị mô hình gán thành số 7.

---

### 3.6.3. Trường hợp nhầm số 3 và số 5

Số 3 và số 5 có thể chia sẻ các vùng nét cong tương tự, đặc biệt ở phần thân giữa và phần dưới. Khi nét viết không rõ ràng, mô hình có thể nhầm lẫn giữa hai chữ số này.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích nét cong và phần thân chữ số khiến số 3 và số 5 có vùng pixel tương đồng.

---

### 3.6.4. Nguyên nhân sai số do nét viết và biến dạng hình học

Nét viết của từng người có sự khác biệt về độ nghiêng, độ dày và vị trí trong khung ảnh. Những biến dạng này làm cho dữ liệu thực tế lệch khỏi phân phối chuẩn của tập MNIST.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích ảnh hưởng của độ nghiêng, độ dày nét, lệch tâm, méo hình và phong cách viết cá nhân đến dự đoán.

---

### 3.6.5. Nguyên nhân sai số do ảnh bị flatten

Khi ảnh hai chiều bị flatten thành vector một chiều, quan hệ không gian cục bộ giữa các pixel không còn được biểu diễn trực tiếp. Đây là một trong những hạn chế quan trọng của ANN Fully Connected khi xử lý dữ liệu ảnh.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích việc flatten làm mất quan hệ không gian cục bộ giữa các pixel, khiến mô hình khó học đặc trưng hình học của chữ số.

---

## 3.7. Trực quan hóa mô hình

Trực quan hóa mô hình giúp người đọc hiểu rõ hơn mô hình đã học được gì và cách nó đưa ra dự đoán. Các hình ảnh trực quan cần được giải thích, không chỉ chèn vào báo cáo như minh họa rời rạc.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày các hình ảnh giúp diễn giải mô hình đã học được gì và dự đoán như thế nào.

---

### 3.7.1. Trực quan hóa trọng số tầng đầu vào

Trọng số kết nối từ input tới hidden layer có thể được reshape về dạng ảnh $28 \times 28$ để quan sát mô hình phản ứng với các vùng pixel nào. Cách trực quan hóa này giúp minh họa khả năng học đặc trưng thô của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Chuyển một số vector trọng số liên quan đến input thành ảnh $28 \times 28$ để quan sát vùng pixel mô hình chú ý.

---

### 3.7.2. Trực quan hóa xác suất Softmax của một mẫu dự đoán

Biểu đồ xác suất Softmax cho thấy mức độ tự tin của mô hình đối với từng lớp chữ số. Biểu đồ này hữu ích trong việc phân tích các trường hợp mô hình dự đoán chắc chắn hoặc còn phân vân.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ cột xác suất 10 lớp cho một ảnh đầu vào để minh họa mức tự tin của mô hình.

---

### 3.7.3. So sánh mẫu dự đoán đúng và sai

Việc đặt các mẫu đúng và sai cạnh nhau giúp người đọc nhận ra sự khác biệt về hình dạng và xác suất dự đoán. Đây là cách trực quan để liên hệ kết quả định lượng với đặc điểm dữ liệu.

> 🛑 **[HÀNH ĐỘNG]**: Đặt cạnh nhau một số ảnh đúng và sai, kèm nhãn thật, nhãn dự đoán và xác suất cao nhất.

---

### 3.7.4. Nhận xét khả năng học đặc trưng của mô hình

Sau các hình trực quan, cần đưa ra nhận xét tổng hợp về khả năng biểu diễn của ANN. Phần này nên chỉ ra mô hình học được các mẫu pixel tổng quát nhưng vẫn bị giới hạn bởi cấu trúc Fully Connected.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích mô hình đã học được các mẫu pixel tổng quát nhưng còn hạn chế khi chữ số biến dạng mạnh.

---

## 3.8. Triển khai dự đoán trên nét vẽ thực tế Web Demo

Phần này kiểm thử mô hình trên dữ liệu nét vẽ tự do của người dùng, còn gọi là dữ liệu ngoài phân phối MNIST. Trọng tâm không phải công nghệ Web, mà là quy trình thu nhận nét vẽ, tiền xử lý ảnh, chạy inference và trực quan hóa kết quả dự đoán.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày phần kiểm thử mô hình trên dữ liệu “wild data” do người dùng tự vẽ, chỉ tập trung vào thu nhận nét vẽ, tiền xử lý ảnh, inference và trực quan hóa kết quả.

---

### 3.8.1. Công cụ thu thập nét vẽ từ người dùng

Canvas được xem như một công cụ thu nhận dữ liệu đầu vào do người dùng tạo ra. Ảnh thu được từ vùng vẽ này là dữ liệu thô và chưa thể đưa trực tiếp vào mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Giới thiệu Canvas như một vùng thu nhận nét vẽ tự do, tạo ra ảnh đầu vào ban đầu để kiểm thử mô hình ngoài tập MNIST.

---

### 3.8.2. Khác biệt giữa ảnh vẽ thực tế và ảnh MNIST

Ảnh vẽ thực tế có thể khác MNIST về màu nền, độ dày nét, vị trí chữ số và kích thước vùng vẽ. Những khác biệt này tạo ra khoảng cách phân phối giữa dữ liệu huấn luyện và dữ liệu khi sử dụng thực tế.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích ảnh người dùng tự vẽ có thể lệch tâm, khác độ dày nét, khác màu nền, khác kích thước và chưa được chuẩn hóa như MNIST.

---

### 3.8.3. Chuyển ảnh vẽ sang grayscale

Ảnh thu được từ Canvas có thể ở dạng nhiều kênh màu, trong khi mô hình được huấn luyện với ảnh xám một kênh. Do đó, bước chuyển sang grayscale giúp đồng nhất định dạng đầu vào.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày bước chuyển ảnh thu được từ Canvas thành ảnh xám một kênh để phù hợp với định dạng dữ liệu ảnh chữ số.

---

### 3.8.4. Nghịch đảo màu về dạng nền đen chữ trắng

Dữ liệu MNIST thường biểu diễn chữ số sáng trên nền tối. Nếu ảnh người dùng vẽ có nền sáng và nét tối, cần nghịch đảo màu để đưa ảnh về dạng tương đồng với dữ liệu huấn luyện.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích bước invert màu để đưa ảnh vẽ về dạng tương đồng với MNIST, tức nền tối và nét chữ sáng.

---

### 3.8.5. Tìm bounding box vùng chứa chữ số

Ảnh vẽ thực tế thường có nhiều khoảng trống xung quanh chữ số. Bounding box giúp xác định vùng chứa nét vẽ chính để loại bỏ phần nền không cần thiết.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách xác định vùng pixel có nét vẽ để cắt bỏ khoảng trống thừa xung quanh chữ số.

---

### 3.8.6. Cắt ảnh và căn giữa chữ số

Sau khi xác định vùng chứa chữ số, ảnh cần được cắt và căn giữa trong khung mới. Bước này giúp giảm sai lệch vị trí và làm ảnh đầu vào gần hơn với cách MNIST được chuẩn hóa.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả việc crop theo bounding box rồi đưa chữ số vào giữa khung ảnh để giảm sai lệch vị trí trước khi dự đoán.

---

### 3.8.7. Resize ảnh về kích thước $28 \times 28$

Mô hình ANN đã được huấn luyện với đầu vào cố định gồm 784 pixel. Do đó, ảnh sau khi xử lý cần được resize về kích thước $28 \times 28$ trước khi flatten.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày bước resize ảnh sau khi crop/căn giữa về đúng kích thước đầu vào chuẩn của mô hình ANN.

---

### 3.8.8. Normalize và flatten thành vector 784 chiều

Sau khi ảnh đã có kích thước chuẩn, giá trị pixel cần được chuẩn hóa về khoảng $[0, 1]$. Tiếp đó, ảnh được flatten thành vector 784 chiều để phù hợp với đầu vào của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích việc chia pixel cho 255 rồi trải phẳng ảnh $28 \times 28$ thành vector 784 chiều để đưa vào hàm lan truyền tiến.

---

### 3.8.9. Chạy inference bằng trọng số đã huấn luyện

Trong giai đoạn inference, mô hình chỉ thực hiện lan truyền tiến với các tham số đã học được. Quá trình này không cập nhật trọng số và không thực hiện huấn luyện lại.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày mô hình sử dụng `W1`, `b1`, `W2`, `b2` đã lưu để dự đoán mà không huấn luyện lại.

---

### 3.8.10. Trực quan hóa ảnh trước và sau tiền xử lý

Trực quan hóa từng bước tiền xử lý giúp chứng minh rằng ảnh nét vẽ thực tế đã được đưa về gần định dạng MNIST. Đây là phần quan trọng để giải thích vì sao pipeline preprocessing ảnh hưởng mạnh đến kết quả dự đoán.

> 🛑 **[HÀNH ĐỘNG]**: Chèn chuỗi hình gồm ảnh người dùng vẽ ban đầu, ảnh grayscale, ảnh invert, ảnh crop/center và ảnh $28 \times 28$ cuối cùng.

---

### 3.8.11. Biểu đồ xác suất Softmax đầu ra

Biểu đồ xác suất Softmax giúp quan sát mô hình tự tin vào lớp nào và các lớp nào đang cạnh tranh. Với dữ liệu vẽ thực tế, biểu đồ này đặc biệt hữu ích để phân tích các trường hợp dự đoán chưa chắc chắn.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ cột 10 xác suất đầu ra để cho thấy mô hình tự tin nhất vào chữ số nào và các lớp cạnh tranh là gì.

---

### 3.8.12. Nhận xét kết quả trên nét vẽ thực tế

Kết quả trên nét vẽ thực tế cần được nhận xét một cách khách quan, bao gồm cả trường hợp đúng và sai. Phần nhận xét nên liên hệ với các phân tích trước đó về confusion matrix, flatten ảnh và tiền xử lý dữ liệu.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích một số trường hợp dự đoán đúng/sai trên nét vẽ người dùng và liên hệ với hạn chế đã thấy trong confusion matrix.

---

## 3.9. Đánh giá tổng hợp thực nghiệm

Phần đánh giá tổng hợp kết nối toàn bộ kết quả đã trình bày trong Chương 3. Nội dung cần rút ra được cấu hình phù hợp nhất, ưu điểm, hạn chế và bài học kỹ thuật từ quá trình thực nghiệm.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết toàn bộ kết quả từ baseline, so sánh siêu tham số, confusion matrix, phân tích lỗi và kiểm thử nét vẽ thực tế.

---

### 3.9.1. Cấu hình mô hình tốt nhất

Cấu hình tốt nhất cần được xác định dựa trên kết quả thực nghiệm thay vì giả định ban đầu. Việc lựa chọn cần cân bằng giữa độ chính xác, độ ổn định và chi phí tính toán.

> 🛑 **[HÀNH ĐỘNG]**: Nêu cấu hình cuối cùng được chọn, gồm số neuron tầng ẩn, learning rate, số iteration và kết quả dev accuracy/loss.

---

### 3.9.2. Ưu điểm của mô hình sau thực nghiệm

Sau khi đánh giá, cần chỉ ra các điểm mạnh mà mô hình đã thể hiện. Những ưu điểm này nên được gắn với số liệu cụ thể và các quan sát từ biểu đồ hoặc hình minh họa.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết các điểm mạnh như cài đặt đơn giản, tốc độ inference nhanh, kết quả tốt trên MNIST và có khả năng dự đoán nét vẽ sau tiền xử lý.

---

### 3.9.3. Hạn chế rút ra từ thực nghiệm

Hạn chế cần được rút ra từ kết quả thực nghiệm, không chỉ nêu chung chung. Các lỗi từ confusion matrix và nét vẽ thực tế là căn cứ quan trọng để đánh giá giới hạn của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Nêu các hạn chế như nhạy với nét vẽ lệch phân phối, dễ nhầm các chữ số hình dạng gần nhau và phụ thuộc mạnh vào tiền xử lý ảnh.

---

### 3.9.4. Bài học kỹ thuật từ quá trình thử nghiệm

Bài học kỹ thuật thể hiện năng lực phân tích và phản biện sau quá trình triển khai. Phần này cần tổng hợp các kinh nghiệm liên quan đến mô hình, dữ liệu, siêu tham số và tiền xử lý.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết bài học về lựa chọn learning rate, kích thước tầng ẩn, tầm quan trọng của confusion matrix và vai trò quyết định của preprocessing với dữ liệu thực tế.

---

# Chương 4. Kết luận và hướng phát triển

Chương cuối tổng kết các kết quả chính của đề tài và đánh giá mức độ hoàn thành mục tiêu ban đầu. Nội dung cần khách quan, không lặp lại quá nhiều chi tiết đã trình bày trong các chương trước.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết kết quả đạt được, các đóng góp chính, hạn chế và hướng cải tiến trong tương lai.

---

## 4.1. Kết luận

Phần kết luận cần khẳng định ngắn gọn những kết quả đã đạt được về mô hình, thực nghiệm và kiểm thử nét vẽ thực tế. Các nhận định nên dựa trên số liệu và phân tích đã trình bày trong Chương 3.

> 🛑 **[HÀNH ĐỘNG]**: Khẳng định mức độ hoàn thành mục tiêu của đề tài về mô hình ANN NumPy, thực nghiệm đánh giá và dự đoán nét vẽ thực tế.

---

### 4.1.1. Kết quả xây dựng ANN NumPy

Đề tài đã triển khai một mô hình ANN Fully Connected từ đầu bằng NumPy. Đây là kết quả quan trọng vì nó chứng minh nhóm hiểu được các bước tính toán cốt lõi của mạng nơ-ron.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết việc nhóm đã tự xây dựng đầy đủ các thành phần của ANN gồm forward, backward, loss, update và prediction.

---

### 4.1.2. Kết quả đánh giá thực nghiệm

Các kết quả thực nghiệm cho thấy mô hình có khả năng học và phân loại chữ số viết tay trên MNIST. Đồng thời, các công cụ phân tích như confusion matrix và biểu đồ học giúp chỉ ra rõ điểm mạnh, điểm yếu của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Tóm tắt kết quả train/dev accuracy, loss, cấu hình tốt nhất và các phát hiện chính từ confusion matrix.

---

### 4.1.3. Kết quả kiểm thử trên nét vẽ thực tế

Việc kiểm thử trên nét vẽ thực tế cho thấy mô hình có thể được sử dụng cho dữ liệu ngoài MNIST nếu có pipeline tiền xử lý phù hợp. Kết quả này giúp đề tài không chỉ dừng lại ở huấn luyện trong môi trường dữ liệu chuẩn.

> 🛑 **[HÀNH ĐỘNG]**: Tổng kết khả năng mô hình dự đoán ảnh người dùng tự vẽ sau khi qua pipeline tiền xử lý chuẩn hóa về dạng MNIST.

---

### 4.1.4. Đóng góp nổi bật của đề tài

Đóng góp của đề tài nằm ở việc kết hợp giữa tự cài đặt mô hình, thực nghiệm có hệ thống và phân tích dữ liệu ngoài phân phối. Các đóng góp này cần được trình bày rõ ràng để làm nổi bật giá trị học thuật của bài tập lớn.

> 🛑 **[HÀNH ĐỘNG]**: Nêu các đóng góp chính gồm tự cài đặt ANN, phân tích siêu tham số, phân tích lỗi chi tiết và thử nghiệm inference trên dữ liệu ngoài MNIST.

---

## 4.2. Hạn chế

Mọi mô hình học máy đều có giới hạn nhất định, đặc biệt khi áp dụng từ dữ liệu chuẩn sang dữ liệu thực tế. Phần này cần nêu hạn chế một cách khách quan và gắn với các bằng chứng thực nghiệm đã có.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày khách quan những điểm mô hình và quy trình thực nghiệm chưa giải quyết được.

---

### 4.2.1. Hạn chế trong khả năng tổng quát hóa

Mô hình được huấn luyện trên MNIST nên có thể hoạt động kém hơn khi dữ liệu đầu vào khác phân phối huấn luyện. Đây là một giới hạn quan trọng khi đưa mô hình ra kiểm thử với nét vẽ thực tế.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích mô hình có thể hoạt động kém hơn khi dữ liệu đầu vào khác nhiều so với phân phối MNIST.

---

### 4.2.2. Hạn chế khi nhận diện nét vẽ ngoài phân phối MNIST

Nét vẽ của người dùng có thể khác đáng kể so với dữ liệu MNIST về vị trí, độ dày và hình dạng. Những khác biệt này có thể làm mô hình dự đoán sai dù pipeline tiền xử lý đã được áp dụng.

> 🛑 **[HÀNH ĐỘNG]**: Nêu các trường hợp nét vẽ quá lệch tâm, quá mảnh, quá dày hoặc hình dạng không giống MNIST khiến mô hình dự đoán sai.

---

### 4.2.3. Hạn chế của quá trình Batch Gradient Descent

Batch Gradient Descent dễ hiểu và phù hợp với mục tiêu nhập môn nhưng có hạn chế về chi phí tính toán. Mỗi lần cập nhật tham số cần sử dụng toàn bộ tập huấn luyện, khiến quá trình học có thể tốn thời gian.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích Batch Gradient Descent dùng toàn bộ dữ liệu mỗi lần cập nhật nên có thể tốn thời gian và thiếu linh hoạt so với các biến thể tối ưu khác.

---

### 4.2.4. Hạn chế của tiền xử lý ảnh vẽ tay

Pipeline tiền xử lý ảnh vẽ tay có ảnh hưởng lớn đến kết quả dự đoán. Nếu bounding box, căn giữa hoặc resize không phù hợp, ảnh đầu vào cuối cùng có thể bị lệch đáng kể so với dữ liệu MNIST.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày các rủi ro như bounding box sai, căn giữa chưa tốt, resize gây méo hình hoặc invert màu không phù hợp.

---

## 4.3. Hướng phát triển

Hướng phát triển cần xuất phát từ các hạn chế đã nêu, không mở rộng lan man ra ngoài phạm vi đề tài. Các đề xuất nên tập trung vào cải thiện mô hình hiện tại, tiền xử lý ảnh và quy trình đánh giá.

> 🛑 **[HÀNH ĐỘNG]**: Đề xuất các hướng cải thiện vẫn bám sát phạm vi đề tài ANN và tiền xử lý ảnh, không mở rộng lan man sang mô hình ngoài phạm vi.

---

### 4.3.1. Tăng độ ổn định của pipeline tiền xử lý ảnh

Cải thiện preprocessing là hướng phát triển trực tiếp giúp tăng khả năng nhận diện trên nét vẽ thực tế. Các bước như crop, center, resize và normalize cần được tối ưu để giảm sai lệch phân phối.

> 🛑 **[HÀNH ĐỘNG]**: Đề xuất cải thiện crop, center, resize, normalize và chuẩn hóa độ dày nét để ảnh vẽ thực tế gần với MNIST hơn.

---

### 4.3.2. Bổ sung bộ dữ liệu kiểm thử từ nét vẽ người dùng

Một bộ dữ liệu kiểm thử từ nét vẽ thật sẽ giúp đánh giá khách quan hơn khả năng hoạt động ngoài MNIST. Dữ liệu này có thể được dùng để phân tích lỗi và cải thiện pipeline tiền xử lý.

> 🛑 **[HÀNH ĐỘNG]**: Đề xuất thu thập thêm mẫu vẽ thật từ nhiều người để đánh giá khách quan khả năng tổng quát hóa.

---

### 4.3.3. Tối ưu tốc độ dự đoán real-time

Tốc độ dự đoán là yếu tố quan trọng khi kiểm thử bằng nét vẽ người dùng. Quá trình inference và tiền xử lý cần được tối ưu để phản hồi nhanh mà vẫn giữ được chất lượng đầu vào.

> 🛑 **[HÀNH ĐỘNG]**: Đề xuất tránh tải lại trọng số nhiều lần, tối ưu phép tính ma trận và giảm chi phí tiền xử lý để dự đoán nhanh hơn.

---

### 4.3.4. Cải thiện khả năng giải thích kết quả dự đoán

Khả năng giải thích giúp người đọc và người dùng hiểu vì sao mô hình đưa ra một dự đoán nhất định. Các công cụ trực quan như xác suất Softmax, ảnh sau preprocessing và mẫu lỗi có thể hỗ trợ mục tiêu này.

> 🛑 **[HÀNH ĐỘNG]**: Đề xuất trực quan hóa xác suất Softmax, mẫu sai, trọng số đầu vào và ảnh sau tiền xử lý để người đọc hiểu vì sao mô hình dự đoán như vậy.

---

# Tài liệu tham khảo

Tài liệu tham khảo cần được trình bày thống nhất theo chuẩn trích dẫn học thuật. Các nguồn được sử dụng nên có độ tin cậy cao và liên quan trực tiếp đến MNIST, neural network, lan truyền ngược, NumPy và xử lý ảnh.

> 🛑 **[HÀNH ĐỘNG]**: Liệt kê tài liệu theo chuẩn IEEE, ưu tiên nguồn chính thống về MNIST, neural network, backpropagation, NumPy, Softmax, Cross-Entropy và xử lý ảnh cơ bản.

---

# Phụ lục

Phụ lục chứa các nội dung kỹ thuật dài hoặc chi tiết bổ trợ cho phần chính của báo cáo. Các nội dung trong phụ lục cần được liên hệ với phần thân báo cáo khi cần thiết.

> 🛑 **[HÀNH ĐỘNG]**: Đưa các nội dung kỹ thuật dài như mã nguồn, bảng kết quả đầy đủ, ảnh minh họa bổ sung và log huấn luyện.

---

## Phụ lục A. Mã nguồn huấn luyện ANN

Phụ lục này trình bày các đoạn mã nguồn quan trọng nhất phục vụ quá trình huấn luyện mô hình. Mã nguồn cần được chọn lọc, có chú thích ngắn gọn và không làm rối phần nội dung chính.

> 🛑 **[HÀNH ĐỘNG]**: Đưa các đoạn code chính của mô hình gồm đọc dữ liệu, khởi tạo tham số, forward propagation, backward propagation, update và save model.

---

## Phụ lục B. Bảng kết quả thực nghiệm đầy đủ

Phụ lục này lưu trữ các bảng kết quả chi tiết của toàn bộ thí nghiệm. Nội dung giúp người đọc kiểm chứng các nhận xét đã được rút ra trong Chương 3.

> 🛑 **[HÀNH ĐỘNG]**: Đưa bảng đầy đủ các lần thử learning rate, số neuron tầng ẩn, số iteration, loss, accuracy và thời gian huấn luyện nếu có.

---

## Phụ lục C. Confusion matrix và ảnh dự đoán sai bổ sung

Phụ lục này bổ sung các hình ảnh và ma trận lỗi không đưa hết vào phần thân báo cáo. Các dữ liệu bổ sung này hỗ trợ phân tích lỗi và làm rõ hạn chế của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Đưa thêm các confusion matrix hoặc ảnh sai chưa chèn trong Chương 3 để hỗ trợ phân tích lỗi.

---

## Phụ lục D. Minh họa pipeline tiền xử lý nét vẽ thực tế

Phụ lục này trình bày chi tiết các bước chuyển đổi ảnh vẽ thực tế về định dạng đầu vào của mô hình. Chuỗi hình minh họa cần cho thấy rõ sự thay đổi của ảnh qua từng bước xử lý.

> 🛑 **[HÀNH ĐỘNG]**: Đưa chuỗi ảnh minh họa từng bước từ ảnh vẽ gốc đến ảnh $28 \times 28$ và vector đầu vào.

---

## Phụ lục E. Kết quả kiểm thử trên nét vẽ thực tế

Phụ lục này tổng hợp các mẫu kiểm thử từ nét vẽ người dùng và kết quả dự đoán tương ứng. Bảng kiểm thử cần thể hiện cả các trường hợp đúng và sai để đánh giá khách quan.

> 🛑 **[HÀNH ĐỘNG]**: Đưa bảng gồm ảnh người dùng vẽ, ảnh sau tiền xử lý, nhãn dự đoán, xác suất Softmax cao nhất và nhận xét đúng/sai.
