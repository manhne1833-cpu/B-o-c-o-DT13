# 🌪️ Phân Tích Dữ Liệu Bão Ảnh Hưởng Đến Việt Nam Và Miền Trung

> **Báo cáo cuối kỳ môn Lập trình Python — Khoa Toán-Tin, Trường Đại học Sư phạm Đà Nẵng**

## 👥 Thông tin nhóm (Team Members)

**Nhóm: 10** — **Giảng viên hướng dẫn:** Nguyễn Hoàng Hải

| STT | Họ và Tên | MSSV | Nhiệm vụ | % đóng góp |
|---|---|---|---|---|
| 1 | Phan Nhật Hoàng | 3120225057 | Làm code, Phân tích thống kê và biểu đồ | 22% |
| 2 | Trần Quốc Trung | 3120225167 | Thu thập và tiền xử lý dữ liệu, trực quan hóa dữ liệu | 18% |
| 3 | Nguyễn Tấn Mạnh | 3120225088 | Hỗ trợ code, Phân tích thống kê và biểu đồ | 17% |
| 4 | Nguyễn Võ Xuân Phúc | 3120225119 | Làm báo cáo | 17% |
| 5 | Trương Quang Thứ | 3120225147 | Trình bày báo cáo | 13% |
| 6 | Trương Chí Cường | 3120225021 | Trình bày báo cáo | 13% |

## 📝 Giới thiệu dự án (Description)

Việt Nam, đặc biệt là khu vực miền Trung, thường xuyên chịu ảnh hưởng của bão và áp thấp nhiệt đới hình thành trên Tây Bắc Thái Bình Dương và Biển Đông. Dự án xây dựng một chương trình Python phân tích dữ liệu bão lịch sử (**best-track**) từ bộ dữ liệu **NOAA IBTrACS** nhằm nhận biết quy luật hoạt động của bão: tần suất theo năm/tháng, cường độ, mùa bão, quỹ đạo di chuyển và mức độ ảnh hưởng đến Việt Nam trong giai đoạn khoảng 1975–2025.

Quy trình xử lý: **Dữ liệu thô → Đọc dữ liệu → Làm sạch → Lọc khu vực Việt Nam → Chuẩn hóa → Phân tích thống kê → Trực quan hóa → Xuất kết quả.**

---

## ✨ Các chức năng chính (Features)

- [x] Tải và đọc dữ liệu best-track bão từ tệp CSV IBTrACS (lưu vực Tây Bắc Thái Bình Dương).
- [x] Làm sạch dữ liệu: chuyển đổi kiểu dữ liệu (thời gian, tọa độ, gió, áp suất), loại bỏ bản ghi thiếu/không hợp lệ và trùng lặp.
- [x] Lọc các cơn bão có khả năng ảnh hưởng đến Việt Nam bằng điều kiện không gian (hộp tọa độ Biển Đông/Việt Nam).
- [x] Chuẩn hóa đơn vị tốc độ gió (knot → km/h) và áp suất trung tâm (hPa/mb).
- [x] Thống kê tần suất bão theo năm và theo tháng (riêng cho khu vực miền Trung 10.8°N–20.0°N).
- [x] Phân tích cường độ bão qua tốc độ gió cực đại và áp suất trung tâm thấp nhất.
- [x] Phân tích tương quan giữa vận tốc gió và áp suất tâm bão.
- [x] Phân loại và so sánh tỷ lệ các cấp bão (thang Beaufort) ảnh hưởng đến vùng duyên hải.
- [x] Trực quan hóa dữ liệu bằng biểu đồ đường, cột, histogram/KDE, scatter và pie chart.
- [x] Kiến trúc hướng đối tượng (OOP) với các lớp `StormDataLoader` (tải & tiền xử lý) và `StormAnalyzer` (phân tích thống kê).

---

## 💻 Công nghệ & Thư viện sử dụng (Technologies)

| Thành phần | Chi tiết |
|---|---|
| Ngôn ngữ | Python 3.10+ |
| Xử lý dữ liệu | `pandas`, `numpy` |
| Trực quan hóa | `matplotlib`, `seaborn` |
| Trực quan hóa tương tác | `plotly`, `folium` |
| Xử lý không gian địa lý | `geopandas`, `shapely` |
| Phân tích thống kê / xu hướng | `scikit-learn` hoặc `scipy` |

---

## 📂 Cấu trúc thư mục dự án (Project Structure)

```
📦 Nhom_10/
┣ 📂data/            # Dữ liệu thô và dữ liệu đã xử lý (ibtracs.WP.list.v04r00.csv)
┣ 📂src/              # Các tệp mã nguồn (StormDataLoader, StormAnalyzer, ...)
┣ 📂outputs/          # Biểu đồ, bảng CSV và bản đồ HTML xuất ra
┣ 📜main.py           # Điểm khởi chạy chương trình
┣ 📜requirements.txt  # Danh sách thư viện cần cài đặt
┗ 📜README.md         # Tài liệu mô tả dự án và hướng dẫn chạy chương trình
```

---

## 🚀 Hướng dẫn cài đặt và chạy (Installation)

### 1️⃣ Cài đặt môi trường

- Đảm bảo máy tính đã cài đặt **Python 3.10** trở lên.

### 2️⃣ Cài đặt thư viện

Mở Terminal tại thư mục dự án và chạy lệnh sau để cài đặt các thư viện phụ thuộc:

```
pip install pandas numpy matplotlib plotly folium
pip install geopandas shapely   # tùy chọn, cho phân tích không gian nâng cao
```

### 3️⃣ Chuẩn bị dữ liệu

- Tải tệp dữ liệu **NOAA IBTrACS** (định dạng CSV, lưu vực Tây Bắc Thái Bình Dương) và đặt vào thư mục `data/`.
- Cập nhật đường dẫn dữ liệu trong chương trình nếu cần.

### 4️⃣ Chạy chương trình

```
python main.py
```

- Kết quả (bảng số liệu, biểu đồ, bản đồ) sẽ được lưu vào thư mục `outputs/`.

---

## 📊 Các câu hỏi phân tích & kết quả trực quan hóa

| # | Câu hỏi phân tích | Phương pháp | Loại biểu đồ |
|---|---|---|---|
| 1 | Tần suất bão theo năm (1975–2025) thay đổi như thế nào? | Groupby theo `Year`, đếm số `SID` duy nhất | Line Chart + Linear Trendline |
| 2 | Tháng nào là tháng cao điểm của mùa bão tại miền Trung? | Phân vùng miền Trung (10.8°N–20.0°N), đếm số bão theo tháng | Bar Chart |
| 3 | Sự phân bố cường độ bão (áp suất tâm bão) biến đổi ra sao? | Trích xuất `USA_PRES` nhỏ nhất của từng cơn bão | Histogram & KDE Plot |
| 4 | Tương quan giữa vận tốc gió và áp suất tâm bão như thế nào? | So sánh `USA_WIND` và `USA_PRES` | Scatter Plot |
| 5 | Tỷ lệ các cấp bão ảnh hưởng đến các vùng duyên hải? | Phân loại theo thang Beaufort, tính tỷ lệ % | Pie / Donut Chart |

**Một số nhận xét chính:**
- Trung bình mỗi năm có khoảng 4–8 cơn bão/áp thấp nhiệt đới ảnh hưởng đến Biển Đông và Việt Nam, có năm lên tới 10–12 cơn.
- Mùa bão tại miền Trung đạt cao điểm vào **tháng 9 và tháng 10**, sau đó dịch chuyển dần xuống phía Nam vào tháng 11–12.
- Phần lớn các cơn bão có áp suất trung tâm trong khoảng 970–995 hPa; các trường hợp dưới 940 hPa tương ứng với siêu bão.
- Áp suất tâm bão và tốc độ gió cực đại có tương quan nghịch chặt chẽ.
- Nhóm bão cấp 8–11 chiếm tỷ lệ cao nhất về số lượng, nhưng siêu bão (chỉ ~5–10% số vụ) gây ra phần lớn thiệt hại.

---

## 🧩 Kiến trúc chương trình (Program Design)

Chương trình được tổ chức theo hướng đối tượng (OOP) với hai lớp chính:

- **`StormDataLoader`**: tải dữ liệu IBTrACS, lọc lưu vực Tây Bắc Thái Bình Dương, chuyển đổi kiểu dữ liệu và lọc các bản ghi thuộc vùng ảnh hưởng Việt Nam.
- **`StormAnalyzer`**: thống kê số lượng bão theo năm/tháng, tính xu hướng cường độ (gió cực đại, áp suất tối thiểu) theo từng cơn bão và theo năm.

**Các hàm chính:**

| Hàm | Chức năng |
|---|---|
| `load_data(path)` | Đọc dữ liệu CSV |
| `clean_data(df)` | Làm sạch và chuyển kiểu dữ liệu |
| `filter_vietnam(df)` | Lọc vùng có khả năng ảnh hưởng Việt Nam |
| `prepare_storm_level(df)` | Tạo dữ liệu tổng hợp theo cơn bão |
| `count_by_year(df)` | Thống kê theo năm |
| `count_by_month(df)` | Thống kê theo tháng |
| `analyze_intensity(df)` | Tính các chỉ số cường độ |
| `plot_tracks(df)` | Vẽ quỹ đạo bão |
| `plot_landfall_points(df)` | Vẽ điểm tiếp cận/đổ bộ |
| `create_interactive_map(df)` | Tạo bản đồ Folium/Plotly |

---

## 📋 Tóm tắt quy trình dự án

```
📥 Đọc dữ liệu IBTrACS (CSV)
   ↓
🧹 Làm sạch & chuẩn hóa (thời gian, tọa độ, gió, áp suất)
   ↓
🗺️ Lọc khu vực ảnh hưởng Việt Nam / miền Trung
   ↓
📊 Thống kê theo năm, tháng, cường độ
   ↓
📈 Trực quan hóa (line, bar, histogram, scatter, pie, bản đồ quỹ đạo)
```

---

## ⚠️ Hạn chế

- Chất lượng và mức độ đầy đủ của dữ liệu có thể khác nhau giữa các giai đoạn.
- Định nghĩa "ảnh hưởng đến Việt Nam" dựa trên điều kiện không gian đơn giản (hộp tọa độ), chưa dùng ranh giới hành chính/bờ biển chính xác.
- IBTrACS không phải lúc nào cũng cung cấp trực tiếp điểm đổ bộ chính xác.
- Phân tích xu hướng trong mẫu thời gian hữu hạn không đủ để kết luận chắc chắn về biến đổi khí hậu.

## 🔭 Hướng phát triển

- Xây dựng bản đồ tương tác bằng Folium/Plotly; dashboard bằng Streamlit.
- Dùng GeoPandas/Shapely để xác định điểm giao với đường bờ biển chính xác hơn.
- Tích hợp dữ liệu **EM-DAT** (thiệt hại thiên tai) và **ENSO** (El Niño/La Niña).
- Áp dụng học máy để phân loại mức độ rủi ro hoặc dự báo thống kê.
- Tự động tạo báo cáo PDF/Word từ kết quả phân tích.

---

## 📌 Ghi chú

- **Học phần:** Lập trình Python
- **Nhóm:** 10
- **Giảng viên hướng dẫn:** Nguyễn Hoàng Hải
- **Khoa:** Toán – Tin, Trường Đại học Sư phạm – Đại học Đà Nẵng
- **Nguồn dữ liệu chính:** NOAA IBTrACS (International Best Track Archive for Climate Stewardship)
