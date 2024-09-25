import requests
import time  # 用於動態生成 timestamp

# 591 API URL
base_url = "https://bff-house.591.com.tw/v1/web/rent/list"

# 動態生成 timestamp
timestamp = str(int(time.time() * 1000))

# https://bff-house.591.com.tw/v1/web/rent/list?regionid=8&_v_=456c1961b8&timestamp=1727226928312&kind=2&sectionid=101&order=posttime&orderType=desc
# ip = 203.69.66.146:443


# 請求頭，包含 Cookie
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": "https://rent.591.com.tw",
    "Origin": "https://rent.591.com.tw",
    "Cookie": "591_new_session=eyJpdiI6ImJzbktMalJHVTJiSmNVWUFKbFN4L3c9PSIsInZhbHVlIjoiOStDQ1VlM0ZMcm15WVByU3RtYzg0VEVsblVTSnpCTWhNeUJobHVQeXNPMHdFZjhyb0xjTWhOYUlVRGs1Ym9UNW5JUmVqekVYb0crb1NPbTk5QnYwRklseHBnaUMva1ZRUzkvVmIrQXdlNTNyeEQ5b0krS24zaFJLV3NaQTZPcHgiLCJtYWMiOiJkZDM1ZjVjZDY3OWFmNDU3N2MyNjZlNDhmNDEwODhkMDZmZWY4ZTg3MDM0YjVlNjk3ZDczMTk4OTA1ZGM1ZWEwIiwidGFnIjoiIn0%3D; T591_TOKEN=qi0m9bc17l072m4v21ld8tm2f5"
}

# region id
# 8 台中
# 4 新竹

# 設定請求參數
params = {
    "regionid": "8",
    "_v_": "456c1961b8",  # 版本號？，具體用途未知
    "timestamp": timestamp,  
    "sectionid": "101",  # 區域代碼
    "kind": "2",  # 未知
    "other": "lift",  # 其他條件
    "order": "posttime",  # 發布時間排序
    "orderType": "desc",  # 降序
    "multiNotice": "all_sex"  # 男女皆可
}

# eyJpdiI6ImJzbktMalJHVTJiSmNVWUFKbFN4L3c9PSIsInZhbHVlIjoiOStDQ1VlM0ZMcm15WVByU3RtYzg0VEVsblVTSnpCTWhNeUJobHVQeXNPMHdFZjhyb0xjTWhOYUlVRGs1Ym9UNW5JUmVqekVYb0crb1NPbTk5QnYwRklseHBnaUMva1ZRUzkvVmIrQXdlNTNyeEQ5b0krS24zaFJLV3NaQTZPcHgiLCJtYWMiOiJkZDM1ZjVjZDY3OWFmNDU3N2MyNjZlNDhmNDEwODhkMDZmZWY4ZTg3MDM0YjVlNjk3ZDczMTk4OTA1ZGM1ZWEwIiwidGFnIjoiIn0%3D


# 檢查連線狀態
# 發送 GET 請求
try:
    response = requests.get(base_url, params=params,headers=headers)
    print(base_url)
    print(response)
    
    # 檢查連線狀態
    if response.status_code == 200:
        data = response.json()  # 獲取回應的 JSON 資料
        print(data)  # 打印結果
    else:
        print(f"請求失敗，狀態碼：{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"請求發生錯誤: {e}")