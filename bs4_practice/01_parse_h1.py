from bs4 import BeautifulSoup
bsobj = BeautifulSoup("<html><body><h1>안녕하세요</h1><body></html>")
print(bsobj)

# .find()  .find_all()
h1 = bsobj.find("h1")
print(h1)
print(h1.text)
