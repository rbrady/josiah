import lxml.html
import requests


def main():
    news = requests.get("http://new.google.com")
    page = lxml.html.fromstring(news.text)
    for title in page.xpath("//span[@class='title']"):
        print(title.text)


if __name__=="__main__":
    main()
