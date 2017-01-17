import wikipedia

f = open('cab.txt', 'r')
interest = f.readlines()

book = xlwt.Workbook()
sheet1 = book.add_sheet('Links of Cabinet')
x=0

for name in interest:
    pg = wikipedia.page(name)
    lnk=pg.links
    sheet1.write(0,x,name)
    y=1
    for n in links:
        sheet1.write(y,x,lnk)
    x+=1

book.save('linkedup.xls')
