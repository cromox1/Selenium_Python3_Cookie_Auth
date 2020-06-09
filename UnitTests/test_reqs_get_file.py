from requests import get as urlget
from time import sleep

tmpfilename = 'tmptest1234.pdf'
pdffileurl = 'https://pixitmedia.com/wp-content/uploads/2020/02/PixStor-Overview-1219-final.pdf'

req = urlget(pdffileurl, allow_redirects=True, stream=True)

file1 = open(tmpfilename, "wb")
file1.write(req.content)

sleep(15)
file1.close()