import json


def get_quan_huyen(tt_code: int, tt_codename: str = None, tt_phonecode: int = None):
    # Mở file JSON và đọc dữ liệu
    with open('data/provinces-2.json', encoding='utf-8') as f:
        provinces = json.load(f)

    # Khởi tạo biến kết quả
    result = {
        'status': 'error',
        'msg': '',
        'data': []
    }

    # Lặp qua các tỉnh/thành phố
    for province in provinces:
        # Kiểm tra xem tỉnh/thành phố có mã code khớp với tham số đầu vào
        # Nếu có, kiểm tra tiếp các tham số tùy chọn (tt_codename, tt_phonecode)
        # Nếu các tham số đều khớp, gán danh sách quận/huyện của tỉnh/thành phố cho biến result['data'] và dừng vòng lặp
        if tt_code == province['code'] and (tt_codename is None or tt_codename == province['codename']) and (tt_phonecode is None or tt_phonecode == province['phone_code']):
            result['data'] = province['districts']
            break

    # Kiểm tra kết quả
    # Nếu danh sách quận/huyện có ít nhất 1 phần tử, đặt status = 'success'
    # Loại bỏ thuộc tính 'wards' trong mỗi phần tử danh sách quận/huyện
    # Nếu danh sách quận/huyện rỗng, đặt msg = 'No data found'
    if result['data']:
        result['status'] = 'success'

        for district in result['data']:
            district.pop('wards')
    else:
        result['msg'] = 'No data found'

    # Trả về kết quả
    return result
