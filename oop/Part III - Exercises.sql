-- 1.
-- Viết câu lệnh truy vấn tính tổng, giá trị lớn nhất, nhỏ nhất, trung bình
-- của quantity * unit_price trong bảng order_items

-- 2.
-- Viết câu lệnh truy vấn tính tổng invoice_total, payment_total
-- và expert (invoice_total - payment_total)
-- trong bảng sql_invoicing.invoices
-- kết quả thể hiện các giá trị cho nửa đầu 2019, nửa cuối 2019,
-- và tổng cả năm 2019 (date_range (invoice_date)

-- 3.
-- Tính tổng số employee theo từng office trong CSDL sql_hr
-- Sắp xếp theo office_id

-- 4.
-- Tính tổng số đơn hàng theo từng năm trong bảng orders

-- 5.
-- Tính tổng bill cho toàn bộ hóa đơn theo order_id
-- Thông tin hiển thị bao gồm order_id, order_date,
-- num_of_product, total_bill

-- 6.
-- Trong CSDL sql_invoicing
-- Tính tổng amount trong bảng payment
-- Nhóm theo payment_id
-- Kết quả hiển thị Payment Method Name, Amount

-- 7.
-- Trong CSDL sql_invoicing
-- Tính tổng số payment và amount theo từng ngày và từng payment method
-- Kết quả hiển thị Date, Method Name, Total Payments, Total Amount
-- Sắp xếp kết quả theo ngày tăng dần

-- 8.
-- Lấy ra danh sách các khách hàng có tổng thanh toán (tổng bill các đơn hàng) > 100