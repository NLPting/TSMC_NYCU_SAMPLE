# TSMC_NCTU_SAMPLE 期末專題，範例程式碼

## 程式使用情境
### 1. 用程式去呼叫Google網頁伺服器，然後將顯示出來的URL，抓出來。 (支援換頁及限縮搜尋時間)
### 2. 對我們要的URL，進行萃取，取得文字內容。
### 3. 將文字內容，進行word count計算。
### 4. 將word count結果儲存到Excel，以利分析之使用。

## Local PC 測試，主程式 crawler_sample.py檔案
### 1. 請先安裝Python環境
### 2. pip install requirements.txt
### 3. 執行crawler_sample.py
### 4. 產出Excel 檔案，以做分析。

## 範例程式碼，詳細解析請參考如下:
### 事前準備
### 1. pip install notebook
### 2. 在CMD下，jupyter notebook
### 3. 打開crawler_sample.ipynb，開始瀏覽執行步驟。

### 解說
### 1. 在Google上輸入關鍵字，然後將顯示出來的URL，抓出來。 (支援換頁及限縮收尋時間)
#### 使用google_search 這支Function
- 參數使用 timeline : 搜尋時間 => 參數可以參考qdr:h (past hour), qdr:d (past day),qdr:w (past week),qdr:m (past month),qdr:y (past year)
- 參數使用 page : 換頁
```
def google_search(self,query,timeline='',page='0'):
    url = self.url + query + '&tbs={timeline}&start={page}'.format(timeline=timeline,page=page)
    print('[Check][URL] URL : {url}'.format(url=url))
    response = self.get_source(self.url + query)
    return self.parse_googleResults(response)
```
    
####  這邊用到get_source及parse_googleResults，兩支Function，為了解析Google Search網路資源，並將URL/標題/內文，找出來。
```
def get_source(self,url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
def parse_googleResults(self,response):
        css_identifier_result = "tF2Cxc"
        css_identifier_title = "h3"
        css_identifier_link = "yuRUbf"
        css_identifier_text = "VwiC3b"
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.findAll("div", {"class": css_identifier_result})
        output = []
        for result in results:
            item = {
                'title': result.find(css_identifier_title).get_text(),
                'link': result.find("div", {"class": css_identifier_link}).find(href=True)['href'],
                'text': result.find("div", {"class": css_identifier_text}).get_text()
            }
            output.append(item)
        return output ```
       
### 2. 對我們要的URL，進行萃取，取得文字內容。
- 使用get_source 這支Function，取得網路資源後，
- 使用html_parser 這支Function，將網路資源進行解析。
- 使用html_getText 這支Function，將我要的區塊p tag的文字取出來。
```
def get_source(self,url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
def html_parser(self,htmlText):
    soup = BeautifulSoup(htmlText, 'html.parser')
    return soup
def html_getText(self,soup):
    orignal_text = ''
    for el in soup.find_all('p'):
        orignal_text += ''.join(el.find_all(text=True))
    return orignal_text```
    
### 3. 將文字內容，進行word count計算
#### 使用word_count function，將一篇文章內容，進行各文字的count個數
```
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
def word_count(self, text):
        counts = dict()
        stop_words = set(stopwords.words('english'))
        words = word_tokenize(text)
        #words = text.replace(',','').split()
        for word in words:
            if word not in stop_words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
        return counts
```
        
### 4. 將聲量結果儲存到Excel
#### 使用get_wordcount_json function濾掉不要的word count dict, 取自己要的(whitelist)
#### 同時利用jsonarray_toexcel function將結果，落地於Excel，以做聲量分析
```
def get_wordcount_json(self,whitelist , dict_data):
        data_array = []
        for i in whitelist:
            json_data = {
                'Date' : 'Week1',
                'Company' : i , 
                'Count' : dict_data[i]
            }
            data_array.append(json_data)
        return data_array
def jsonarray_toexcel(self,data_array):
    df = pd.DataFrame(data=data_array)
    df.to_excel('result.xlsx' , index=False)
    return
```







