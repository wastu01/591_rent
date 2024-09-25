import requests
from bs4 import BeautifulSoup

# URL for the region you provided (台中市 西區)
url = "https://rent.housefun.com.tw/region/台中市_西區/?cid=0010&aid=117&purpid=2"

# https://rent.housefun.com.tw/region/新竹市/?cid=0006&purpid=2
# purpid 房屋類型 
# 2 獨立套房
# rpid 租金價格
# 不限 不帶參數
# RP4 1.5~2萬



# 模擬瀏覽器請求頭
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# 發送 GET 請求
response = requests.get(url, headers=headers)

# 檢查請求狀態
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 將 soup 內容保存成本機端的 HTML 文件
    with open("housefun_org.html", "w", encoding='utf-8') as file:
        file.write(soup.prettify())
    
    
    # 解析網頁內容，這裡需要根據網頁結構進行調整
    # listings = soup.find_all("div", class_="house-item")  # 假設每個租屋資料在 class="house-item" 中
    
    # for listing in listings:
    #     title = listing.find("h3").text.strip()  # 假設標題在 <h3> 標籤中
    #     price = listing.find("span", class_="price").text.strip()  # 假設價格在 class="price" 中
    #     print(f"房屋標題: {title}, 價格: {price}")
else:
    print(f"請求失敗，狀態碼：{response.status_code}")
