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

Chương này trình bày các khái niệm và công thức nền tảng liên quan đến bài toán nhận diện chữ số viết tay bằng ANN. Nội dung cần bảo đảm mối liên hệ rõ ràng giữa lý thuyết toán học, thuật toán và mã nguồn triển khai bằng NumPy.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày nền tảng toán học và thuật toán cần thiết để hiểu mô hình ANN Fully Connected dùng cho nhận diện chữ số viết tay.

---

## 2.1. Bài toán phân loại ảnh chữ số viết tay

Bài toán nhận diện chữ số viết tay có thể được mô hình hóa như một bài toán phân loại ảnh đa lớp. Mỗi ảnh đầu vào cần được ánh xạ đến một nhãn chữ số duy nhất trong tập các lớp cho trước.

> 🛑 **[HÀNH ĐỘNG]**: Định nghĩa bài toán đầu vào là ảnh chữ số và đầu ra là một trong 10 lớp dự đoán.

---

### 2.1.1. Đầu vào của bài toán

Đầu vào của mô hình là ảnh chữ số viết tay đã được chuẩn hóa về kích thước cố định. Trong đề tài này, mỗi ảnh được biểu diễn dưới dạng một ma trận pixel có kích thước $28 \times 28$.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày ảnh đầu vào là ảnh xám kích thước $28 \times 28$, sau đó được biểu diễn thành vector 784 chiều.

---

### 2.1.2. Đầu ra của bài toán

Đầu ra của mô hình là xác suất tương ứng với từng lớp chữ số. Lớp có xác suất lớn nhất được chọn làm kết quả dự đoán cuối cùng.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích đầu ra là phân phối xác suất trên 10 lớp chữ số từ 0 đến 9.

---

### 2.1.3. Đặc điểm của phân loại đa lớp

Bài toán phân loại chữ số viết tay thuộc nhóm phân loại đa lớp, trong đó mỗi mẫu chỉ có một nhãn đúng. Điều này yêu cầu mô hình tạo ra một phân phối xác suất hợp lệ trên toàn bộ các lớp.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích đây là bài toán multi-class classification, mỗi mẫu chỉ thuộc một nhãn đúng duy nhất.

---

## 2.2. Dữ liệu MNIST và tiền xử lý

MNIST là bộ dữ liệu phổ biến trong các bài toán nhập môn về nhận diện chữ số viết tay. Để phù hợp với mô hình ANN Fully Connected, dữ liệu cần được chuẩn hóa và biến đổi trước khi đưa vào huấn luyện.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày đặc điểm dữ liệu MNIST và các bước tiền xử lý cần thiết trước khi huấn luyện ANN.

---

### 2.2.1. Cấu trúc ảnh $28 \times 28$

Mỗi ảnh MNIST là ảnh xám có kích thước cố định, trong đó mỗi pixel biểu diễn mức cường độ sáng. Cấu trúc này giúp việc chuyển đổi dữ liệu sang vector đầu vào của ANN trở nên trực tiếp.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả mỗi ảnh có 784 pixel, mỗi pixel biểu diễn cường độ sáng trong ảnh chữ số viết tay.

---

### 2.2.2. Flatten ảnh thành vector 784 chiều

Mạng Fully Connected nhận đầu vào dưới dạng vector thay vì ma trận hai chiều. Vì vậy, ảnh $28 \times 28$ cần được trải phẳng thành vector có 784 phần tử.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích cách trải phẳng ma trận ảnh $28 \times 28$ thành vector một chiều để phù hợp với mạng Fully Connected.

---

### 2.2.3. Normalize pixel

Chuẩn hóa pixel giúp đưa các giá trị đầu vào về cùng một thang đo, từ đó hỗ trợ quá trình tối ưu ổn định hơn. Đây là bước tiền xử lý quan trọng trước khi huấn luyện mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày việc chia giá trị pixel cho 255 để đưa dữ liệu về khoảng $[0, 1]$, giúp mô hình học ổn định hơn.

---

### 2.2.4. One-hot encoding nhãn

Nhãn chữ số ban đầu thường ở dạng số nguyên từ 0 đến 9. Khi tính hàm mất mát Cross-Entropy, các nhãn này cần được chuyển thành vector one-hot tương ứng.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích cách chuyển nhãn số nguyên thành vector 10 chiều để tính Cross-Entropy Loss.

---

## 2.3. Mô hình ANN Fully Connected

Mô hình ANN Fully Connected là kiến trúc mạng nơ-ron trong đó các neuron giữa hai tầng liên tiếp được kết nối đầy đủ. Kiến trúc này phù hợp để minh họa các khái niệm nền tảng như trọng số, bias, lan truyền tiến và lan truyền ngược.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cấu trúc mạng nơ-ron nhiều lớp dùng trong đề tài.

---

### 2.3.1. Kiến trúc $784 \rightarrow 128 \rightarrow 10$

Kiến trúc của mô hình gồm tầng đầu vào 784 chiều, một tầng ẩn 128 neuron và tầng đầu ra 10 neuron. Tầng đầu ra tương ứng với 10 lớp chữ số cần phân loại.

> 🛑 **[HÀNH ĐỘNG]**: Chèn sơ đồ kiến trúc gồm input layer 784 neuron, hidden layer 128 neuron và output layer 10 neuron.

---

### 2.3.2. Vai trò của trọng số và bias

Trọng số và bias là các tham số học được trong quá trình huấn luyện. Chúng quyết định cách mô hình biến đổi dữ liệu đầu vào qua từng tầng để tạo ra dự đoán.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích trọng số học mức ảnh hưởng của đặc trưng đầu vào, còn bias điều chỉnh ngưỡng kích hoạt của neuron.

---

### 2.3.3. Bảng kích thước các ma trận trong mô hình

Việc xác định đúng kích thước các ma trận giúp bảo đảm tính nhất quán giữa công thức toán học và mã nguồn NumPy. Bảng kích thước cũng giúp người đọc kiểm tra được từng bước tính toán trong mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng kích thước `X`, `Y`, `W1`, `b1`, `Z1`, `A1`, `W2`, `b2`, `Z2`, `A2` để liên hệ công thức với code.

---

## 2.4. Lan truyền tiến

Lan truyền tiến là quá trình đưa dữ liệu đầu vào đi qua các tầng của mạng để tạo ra xác suất dự đoán. Đây là bước mô hình thực hiện suy luận trước khi tính sai số.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày quá trình mô hình biến đổi dữ liệu đầu vào thành xác suất dự đoán.

---

### 2.4.1. Tính toán tầng ẩn

Ở tầng ẩn, dữ liệu đầu vào được nhân với ma trận trọng số và cộng với bias. Kết quả tuyến tính này sau đó được đưa qua hàm kích hoạt để tạo biểu diễn phi tuyến.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức `Z1 = W1X + b1` và giải thích ý nghĩa của phép biến đổi tuyến tính đầu tiên.

---

### 2.4.2. Hàm kích hoạt ReLU

ReLU là hàm kích hoạt đơn giản nhưng hiệu quả, giúp mô hình học được các quan hệ phi tuyến. Hàm này giữ nguyên các giá trị dương và đưa các giá trị âm về 0.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức $ReLU(z) = max(0, z)$ và vai trò đưa tính phi tuyến vào mô hình.

---

### 2.4.3. Tính toán tầng đầu ra

Tầng đầu ra biến đổi biểu diễn của tầng ẩn thành các giá trị logits cho từng lớp chữ số. Các logits này chưa phải xác suất và cần được đưa qua Softmax.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức `Z2 = W2A1 + b2` để tạo logits cho 10 lớp chữ số.

---

### 2.4.4. Softmax và xác suất dự đoán

Softmax chuyển đổi logits thành phân phối xác suất trên các lớp đầu ra. Nhãn dự đoán được xác định bằng lớp có xác suất lớn nhất.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích Softmax biến logits thành xác suất và nhãn dự đoán được lấy bằng `argmax`.

---

## 2.5. Hàm mất mát và lan truyền ngược

Sau khi mô hình tạo ra dự đoán, cần đo sai số giữa kết quả dự đoán và nhãn thật. Lan truyền ngược sử dụng sai số này để tính gradient và cập nhật các tham số của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách mô hình đo sai số và tính gradient để cập nhật trọng số.

---

### 2.5.1. Cross-Entropy Loss

Cross-Entropy Loss là hàm mất mát thường dùng cho bài toán phân loại đa lớp. Hàm này phạt mạnh các dự đoán có xác suất thấp đối với nhãn đúng.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức loss cho phân loại đa lớp và giải thích loss càng nhỏ thì dự đoán càng gần nhãn thật.

---

### 2.5.2. Gradient tại tầng đầu ra

Gradient tại tầng đầu ra thể hiện sai lệch giữa phân phối xác suất dự đoán và nhãn thật dạng one-hot. Với kết hợp Softmax và Cross-Entropy, công thức gradient được rút gọn thuận tiện cho cài đặt.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức `dZ2 = A2 - Y` và ý nghĩa đây là sai lệch giữa xác suất dự đoán và nhãn one-hot.

---

### 2.5.3. Gradient tại tầng ẩn

Sai số từ tầng đầu ra được truyền ngược về tầng ẩn thông qua ma trận trọng số. Đạo hàm ReLU được sử dụng để xác định những neuron nào có đóng góp vào gradient.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách sai số được lan truyền ngược qua `W2` và nhân với đạo hàm ReLU để tính gradient tầng ẩn.

---

### 2.5.4. Cập nhật tham số bằng Batch Gradient Descent

Batch Gradient Descent cập nhật tham số dựa trên gradient tính từ toàn bộ tập huấn luyện. Cách tiếp cận này đơn giản, dễ hiểu và phù hợp với mục tiêu tự cài đặt mô hình từ đầu.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày công thức cập nhật `W := W - αdW`, `b := b - αdb` trên toàn bộ tập huấn luyện.

---

## 2.6. Phương pháp đánh giá

Đánh giá mô hình cần kết hợp giữa chỉ số tổng quát và phân tích chi tiết theo từng lớp. Các phương pháp đánh giá trong phần này giúp xác định không chỉ mô hình đúng bao nhiêu, mà còn sai ở đâu và vì sao.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày các chỉ số và công cụ dùng để đánh giá mô hình trong thực nghiệm.

---

### 2.6.1. Train accuracy và dev accuracy

Train accuracy phản ánh mức độ mô hình học được từ tập huấn luyện, trong khi dev accuracy phản ánh khả năng tổng quát hóa. So sánh hai chỉ số này giúp nhận diện hiện tượng học chưa đủ hoặc quá khớp.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích train accuracy đo khả năng học trên tập huấn luyện, còn dev accuracy đo khả năng tổng quát hóa.

---

### 2.6.2. Train loss và dev loss

Loss cho biết mức độ sai lệch của phân phối dự đoán so với nhãn thật. Việc theo dõi train loss và dev loss theo thời gian giúp đánh giá quá trình hội tụ của mô hình.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày ý nghĩa của loss trên train/dev trong việc quan sát quá trình hội tụ và dấu hiệu overfitting.

---

### 2.6.3. Confusion matrix

Confusion matrix là công cụ trực quan để quan sát mô hình nhầm lẫn giữa các lớp như thế nào. Ma trận này đặc biệt hữu ích trong bài toán chữ số viết tay vì một số cặp chữ số có hình dạng gần nhau.

> 🛑 **[HÀNH ĐỘNG]**: Giải thích confusion matrix cho biết mô hình dự đoán đúng/sai từng lớp và giúp phát hiện các cặp chữ số dễ nhầm.

---

### 2.6.4. Phân tích mẫu dự đoán sai

Phân tích mẫu dự đoán sai giúp bổ sung góc nhìn định tính cho các chỉ số định lượng. Những mẫu sai tiêu biểu có thể chỉ ra hạn chế của dữ liệu, mô hình hoặc bước tiền xử lý.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách chọn một số ảnh sai tiêu biểu, so sánh nhãn thật, nhãn dự đoán và đặc điểm nét viết gây nhầm lẫn.

---

# Chương 3. Thực nghiệm và đánh giá kết quả

Chương này là phần trọng tâm của báo cáo, trình bày quá trình triển khai, huấn luyện, đánh giá và phân tích mô hình. Nội dung cần có số liệu thực nghiệm, biểu đồ, bảng so sánh và nhận xét cụ thể.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày toàn bộ quá trình triển khai ANN bằng NumPy, huấn luyện, so sánh siêu tham số, phân tích lỗi và kiểm thử trên nét vẽ thực tế.

---

## 3.1. Thiết kế thực nghiệm

Thiết kế thực nghiệm xác định cách dữ liệu được xử lý, mô hình được huấn luyện và kết quả được đánh giá. Phần này cần mô tả rõ các điều kiện thực nghiệm để bảo đảm kết quả có thể được kiểm chứng lại.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả môi trường, dữ liệu, quy trình huấn luyện và cách đánh giá mô hình.

---

### 3.1.1. Môi trường chạy

Môi trường chạy ảnh hưởng đến tốc độ huấn luyện và khả năng tái lập kết quả. Cần ghi rõ các công cụ, thư viện và cấu hình cơ bản được sử dụng trong quá trình thực nghiệm.

> 🛑 **[HÀNH ĐỘNG]**: Nêu ngôn ngữ Python, các thư viện NumPy, Pandas, Matplotlib và cấu hình máy nếu cần.

---

### 3.1.2. Cách chia tập train/dev/test demo

Việc chia dữ liệu cần được mô tả chính xác để tránh nhầm lẫn giữa đánh giá có nhãn và minh họa dự đoán không nhãn. Tập dev được dùng để đánh giá trong khi các ảnh demo có thể dùng để trực quan hóa kết quả.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách chia dữ liệu có nhãn thành train/dev và làm rõ test demo chỉ dùng để trực quan hóa nếu không có nhãn.

---

### 3.1.3. Quy trình huấn luyện

Quy trình huấn luyện gồm các bước lặp lại nhằm tối ưu tham số của mô hình. Mỗi vòng lặp cần thực hiện lan truyền tiến, tính loss, lan truyền ngược và cập nhật trọng số.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả vòng lặp huấn luyện gồm forward propagation, tính loss, backward propagation và update tham số.

---

### 3.1.4. Quy trình đánh giá

Quy trình đánh giá giúp đo chất lượng mô hình sau hoặc trong quá trình huấn luyện. Các chỉ số định lượng cần đi kèm với phân tích lỗi để đưa ra nhận xét có cơ sở.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách tính loss, accuracy, confusion matrix và chọn mẫu sai để phân tích.

---

## 3.2. Cấu hình mô hình cơ sở

Mô hình cơ sở đóng vai trò baseline để so sánh với các cấu hình thực nghiệm khác. Cấu hình này cần được mô tả rõ về kiến trúc, learning rate, số iteration và cách khởi tạo tham số.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cấu hình ban đầu được dùng làm baseline cho các thí nghiệm tiếp theo.

---

### 3.2.1. Kiến trúc $784 \rightarrow 128 \rightarrow 10$

Kiến trúc baseline sử dụng một tầng ẩn để cân bằng giữa độ đơn giản và khả năng học phi tuyến. Đây là cấu trúc chính được sử dụng xuyên suốt trong quá trình thực nghiệm.

> 🛑 **[HÀNH ĐỘNG]**: Mô tả mô hình baseline gồm 784 đầu vào, 128 neuron tầng ẩn và 10 đầu ra.

---

### 3.2.2. Learning rate mặc định

Learning rate quyết định độ lớn bước cập nhật tham số trong mỗi iteration. Giá trị mặc định cần được chọn hợp lý để mô hình có thể hội tụ mà không dao động quá mạnh.

> 🛑 **[HÀNH ĐỘNG]**: Nêu giá trị learning rate ban đầu và lý do chọn làm điểm xuất phát thực nghiệm.

---

### 3.2.3. Số iteration mặc định

Số iteration quyết định số lần mô hình cập nhật tham số trong quá trình huấn luyện. Việc chọn số iteration cần đủ lớn để mô hình học được nhưng không quá lớn gây lãng phí thời gian.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày số vòng lặp huấn luyện baseline và cách ghi log theo các mốc iteration.

---

### 3.2.4. Phương pháp khởi tạo trọng số

Khởi tạo trọng số ảnh hưởng trực tiếp đến quá trình hội tụ của mạng nơ-ron. Cần mô tả cách khởi tạo được sử dụng và nêu nhận xét về vai trò của nó trong thực nghiệm.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày cách khởi tạo `W1`, `b1`, `W2`, `b2` và nhận xét ảnh hưởng của khởi tạo đến quá trình học.

---

## 3.3. Kết quả mô hình cơ sở

Kết quả mô hình cơ sở cung cấp cái nhìn ban đầu về khả năng học của ANN trước khi thay đổi các siêu tham số. Các kết quả cần được trình bày bằng bảng và biểu đồ để dễ phân tích.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày kết quả định lượng đầu tiên của mô hình baseline.

---

### 3.3.1. Bảng loss và accuracy theo iteration

Bảng kết quả theo iteration giúp theo dõi sự thay đổi của loss và accuracy trong quá trình huấn luyện. Đây là căn cứ quan trọng để nhận xét mô hình có đang hội tụ hay không.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng gồm các mốc iteration và các giá trị train loss, dev loss, train accuracy, dev accuracy.

---

### 3.3.2. Biểu đồ train/dev loss

Biểu đồ loss giúp trực quan hóa xu hướng giảm sai số trong quá trình học. Sự khác biệt giữa train loss và dev loss cũng có thể cho thấy dấu hiệu overfitting hoặc underfitting.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ đường thể hiện loss giảm theo thời gian và nhận xét tốc độ hội tụ.

---

### 3.3.3. Biểu đồ train/dev accuracy

Biểu đồ accuracy giúp quan sát mức cải thiện khả năng phân loại của mô hình theo thời gian. Việc so sánh train accuracy và dev accuracy giúp đánh giá khả năng tổng quát hóa.

> 🛑 **[HÀNH ĐỘNG]**: Chèn biểu đồ accuracy để so sánh khả năng học trên train và khả năng tổng quát hóa trên dev.

---

### 3.3.4. Nhận xét về tốc độ hội tụ

Tốc độ hội tụ phản ánh mức độ hiệu quả của cấu hình huấn luyện ban đầu. Phần nhận xét cần dựa trên số liệu và biểu đồ đã trình bày, không đưa ra kết luận cảm tính.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích mô hình học nhanh hay chậm, có dao động hay không và loss/accuracy có ổn định về cuối quá trình học không.

---

## 3.4. So sánh siêu tham số

So sánh siêu tham số giúp đánh giá ảnh hưởng của các lựa chọn cấu hình đến chất lượng mô hình. Phần này cần giữ các điều kiện thí nghiệm nhất quán để kết quả so sánh có ý nghĩa.

> 🛑 **[HÀNH ĐỘNG]**: Trình bày các thí nghiệm thay đổi learning rate và số neuron tầng ẩn để tìm cấu hình phù hợp.

---

### 3.4.1. Ảnh hưởng của learning rate

Learning rate là một trong những siêu tham số quan trọng nhất của Gradient Descent. Giá trị quá nhỏ có thể khiến mô hình học chậm, trong khi giá trị quá lớn có thể làm quá trình tối ưu dao động hoặc không hội tụ.

> 🛑 **[HÀNH ĐỘNG]**: So sánh các learning rate như 0.01, 0.05, 0.1, 0.2 trên cùng kiến trúc và cùng số iteration.

---

### 3.4.2. Ảnh hưởng của số neuron tầng ẩn

Số neuron tầng ẩn quyết định năng lực biểu diễn của mô hình. Tầng ẩn quá nhỏ có thể không học đủ đặc trưng, trong khi tầng ẩn quá lớn có thể làm tăng chi phí tính toán.

> 🛑 **[HÀNH ĐỘNG]**: So sánh các cấu hình hidden layer như 64, 128, 256 neuron để đánh giá năng lực biểu diễn và chi phí tính toán.

---

### 3.4.3. Ảnh hưởng của số iteration

Số iteration ảnh hưởng đến mức độ mô hình được tối ưu sau quá trình huấn luyện. Khi tăng số iteration, mô hình có thể cải thiện đến một ngưỡng nhất định trước khi kết quả bắt đầu bão hòa.

> 🛑 **[HÀNH ĐỘNG]**: Phân tích mô hình cải thiện đến mức nào khi tăng số iteration và xác định khi nào kết quả bắt đầu bão hòa.

---

### 3.4.4. So sánh các cấu hình thực nghiệm

Bảng so sánh các cấu hình giúp tổng hợp toàn bộ kết quả thực nghiệm một cách rõ ràng. Các giá trị cần được trình bày nhất quán để thuận tiện cho việc lựa chọn mô hình cuối cùng.

> 🛑 **[HÀNH ĐỘNG]**: Chèn bảng tổng hợp nhiều cấu hình gồm learning rate, số neuron, số iteration, train/dev accuracy, train/dev loss và thời gian huấn luyện nếu có.

---

### 3.4.5. Lựa chọn cấu hình cuối cùng

Cấu hình cuối cùng cần được chọn dựa trên kết quả thực nghiệm, không chỉ dựa trên accuracy cao nhất. Cần cân nhắc thêm độ ổn định, chi phí tính toán và mức độ phù hợp với mục tiêu nhập môn.

> 🛑 **[HÀNH ĐỘNG]**: Kết luận cấu hình được chọn dựa trên cân bằng giữa độ chính xác, độ ổn định, thời gian huấn luyện và độ đơn giản của mô hình.

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