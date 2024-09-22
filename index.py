# 591 API URL
base_url = "https://bff-house.591.com.tw/v1/web/rent/list"

# regionid
# 8 台中
# 4 新竹



params = {
    "regionid": "8",  # 縣市
    "_v_": "456c1961b8",  # 未知
    "timestamp": "1726972183153",  # 時間
    "sectionid": "101",  # 區 鎮 鄉
    "kind": "2",  # 房屋類型
    "other": "lift",  # 其他條件
    "order": "posttime",  # 排序方式
    "orderType": "desc",  # 排序類型
    "multiNotice": "all_sex"  # 男女都可
}

import requests

response = requests.get(base_url, params=params)

# 檢查連線狀態

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"請求失敗，狀態碼：{response.status_code}")