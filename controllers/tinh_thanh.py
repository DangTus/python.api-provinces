import json


def get_tinh_thanh(code: int = None, codename: str = None, phone_code: int = None):
    # Đọc file
    with open('data/provinces.json', encoding='utf-8') as f:
        data = json.load(f)

    result = []

    # Kiểm tra xem có đối số truyền vào hay không
    if code != None or codename != None or phone_code != None:
        # Có ít nhất 1 đối số truyền vào
        for item in data:
            check = True

            if code != None:
                check = check and code == item['code']

            if codename != None:
                check = check and codename == item['codename']

            if phone_code != None:
                check = check and phone_code == item['phone_code']

            # Kiểm tra xem các đối số truyền vào có giống với dữ liệu không
            if check:
                item.pop('districts')
                return item
            
        # Kiểm tra result có trống hay không. Nếu không -> return một đoạn json báo truyền dữ liệu sai

    else:
        # Không có đối số truyền vào -> Hiển thị tất cả Tỉnh/Thành
        for item in data:
            item.pop('districts')
            result.append(item)

        return result
