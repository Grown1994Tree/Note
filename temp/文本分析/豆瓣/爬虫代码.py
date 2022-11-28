import ssl
import bs4
import re
import requests
import csv
import codecs
import time

class DouBanSpider:
    def __init__(self):
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        self.headers = {"User-Agent": self.userAgent}
    
    # 拿到豆瓣图书的分类标签
    def getBookCategories(self):
        try:
            url = "https://book.douban.com/tag/?view=type&icn=index-sorttags-all"
            response = requests.get(url, headers=self.headers)
            content = response.text
            return content
        except:
            print("error")
            return None
    
    # 找到每个标签的内容
    def getCategroiesContent(self):
        content = self.getBookCategories()
        if not content:
            print("页面抓取失败...")
            return None
        soup = bs4.BeautifulSoup(content, 'lxml')
        categroyMatch = re.compile(r"^/tag/*")
        categroies = []
        for category in soup.find_all("a", {"href": categroyMatch}):
            if category:
                categroies.append(category.string)
        return categroies
    
    # 拿到每个标签的链接
    def getCategoryLink(self):
        categories = self.getCategroiesContent()
        categoryLinks = []
        for item in categories:
            link = "https://book.douban.com/tag/" + str(item)
            categoryLinks.append(link)
        return categoryLinks
    
    # 爬取书目信息
    def getBookInfo(self, categroyLinks):
        self.setCsvTitle()
        categroies = categroyLinks
        try:
            for link in categroies:
                print("正在爬取：" + link)
                bookList = []
                response = requests.get(link, headers=self.headers)
                soup = bs4.BeautifulSoup(response.text, 'lxml')
                bookCategroy = soup.h1.string
                for book in soup.find_all("li", {"class": "subject-item"}):
                    bookSoup = bs4.BeautifulSoup(str(book), 'lxml')
                    bookTitle = bookSoup.h2.a["title"]
                    bookAuthor = bookSoup.find("div", {"class": "pub"})
                    bookComment = bookSoup.find("span", {"class": "pl"})
                    bookContent = bookSoup.li.p
                    if bookTitle and bookAuthor and bookComment and bookContent:
                        bookList.append([bookTitle.strip(),bookCategroy.strip() , bookAuthor.string.strip(),bookComment.string.strip(), bookContent.string.strip()])
                    
                self.saveBookInfo(bookList)
                time.sleep(3)

            print("爬取结束...")
        
        except:
            print("error")
            return None
        
    # 保存表头
    def setCsvTitle(self):
        csvFile = codecs.open("data/data.csv", "a", "utf_8_sig")
        try:
            writer = csv.writer(csvFile)
            writer.writerow(["title", "tag", "info", "comments", "content"])
        finally:
            csvFile.close()
    
    # 保存书本信息
    def saveBookInfo(self, bookList):
        bookList = bookList
        csvFile = codecs.open("data/data.csv", "a", "utf_8_sig")
        try:
            writer = csv.writer(csvFile)
            for book in bookList:
                writer.writerow(book)
        finally:
            csvFile.close()
    
    # 启动
    def start(self):
        categoryLink = self.getCategoryLink()
        self.getBookInfo(categoryLink)


douBanSpider = DouBanSpider()
douBanSpider.start()
