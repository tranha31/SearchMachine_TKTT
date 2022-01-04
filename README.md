# SearchMachine_TKTT

*Cài đặt Scrapy:

pip install scrapy

(Bạn có thể tiến hành crawl lại data bằng cách tạo project scrapy và chạy các spider trong folder search_information/search_information)

*Mở folder search_information, chạy file convert.py thu được file data.txt
Đổi định dạng thành data.json để chuyển dữ liệu về dạng chuẩn để thêm vào Elasticsearch

*Cài đặt Elasticsearch và Elasticsearch-Analysis-Vietnamese tại đây

Youtube: https://www.youtube.com/watch?v=aAuW_wV81Xk
Link GitHub: https://github.com/viiiprock/es-vietnamese-docker

*Sau khi cài đặt xong Elasticsearch: Tạo index search_machine, và put data nhận được từ file convert.py lên index.

*Cài đặt server php và thư viện elasticsearch trên php:

- Cài đặt PHP: https://www.sitepoint.com/how-to-install-php-on-windows/
- Cài đặt elasticsearch php: https://packagist.org/packages/elasticsearch/elasticsearch

-------------------------
Sau khi cài đặt đầy đủ, để chạy hệ thống:
B1: Chạy docker elasticsearch và kibana.
    Truy cập: localhost:9200 để đăng nhập Elasticsearh.
    Truy cập: localhost:5601 để đăng nhập Kibana.
B2: Mở folder search_machine 
    Chạy server php: php -S localhost:8888
B3: Truy cập vào link: http://localhost:8888/index.php