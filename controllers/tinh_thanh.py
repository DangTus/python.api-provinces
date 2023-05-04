import json


def get_tinh_thanh():
    # Mở file JSON và đọc dữ liệu
    with open('data/provinces-1.json', encoding='utf-8') as f:
        data = json.load(f)

    # Khởi tạo biến kết quả
    result = {
        'status': 'success',
        'msg': '',
        'data': []
    }

    # Lặp qua danh sách các tỉnh/thành phố và loại bỏ thông tin về các quận/huyện
    for item in data:
        item.pop('districts')
        result['data'].append(item)

    # Trả về kết quả
    return result
