import pyshorteners
url = input('enter the url:')

def shortenur1(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))
    shortenurl(url)