import json


def get_phuong_xa(tt_code: int, qh_code: int, tt_codename: str = None, tt_phonecode: int = None, qh_codename: str = None):
    # Mở file JSON và đọc dữ liệu
    with open('data/provinces-3.json', encoding='utf-8') as f:
        provinces = json.load(f)

    # Khởi tạo biến kết quả
    result = {
        'status': 'error',
        'msg': '',
        'data': []
    }

    # Lặp qua các tỉnh/thành phố
    for province in provinces:
        # Kiểm tra nếu mã tỉnh/thành phố phù hợp và có thể truy xuất đến codename và phone_code (nếu có)
        if tt_code == province['code'] and (tt_codename is None or tt_codename == province['codename']) and (tt_phonecode is None or tt_phonecode == province['phone_code']):
            # Lấy danh sách quận/huyện của tỉnh/thành phố hiện tại
            districts = province['districts']

            # Lặp qua danh sách quận/huyện trong districts
            for district in districts:
                # Kiểm tra nếu mã quận/huyện phù hợp và có thể truy xuất đến codename (nếu có)
                if qh_code == district['code'] and (qh_codename is None or qh_codename == district['codename']):
                    # Lưu danh sách phường/xã của quận/huyện phù hợp vào kết quả trả về
                    result['data'] = district['wards']
                    break

    # Nếu có dữ liệu phường/xã thì trả về kết quả thành công, ngược lại trả về thông báo lỗi
    if result['data']:
        result['status'] = 'success'
    else:
        result['msg'] = 'No data found'

    # Trả về kết quả
    return result
