# tmpfilename = 'PixStor-Overview-1219-final.pdf'
tmpfilename = 'tmptest2345.pdf'

import fleep
file1 = open(tmpfilename, "rb")
baca = fleep.get(file1.read(128))
print('TYPE = ' + str(baca.type))
print('EXTN = ' + str(baca.extension))
print('MIME = ' + str(baca.mime))
file1.close()