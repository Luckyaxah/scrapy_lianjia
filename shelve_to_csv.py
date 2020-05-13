import shelve
from scrapy_lianjia.items import LianJiaZuFangItem

dbase = shelve.open('./mydbase')
columns = list(LianJiaZuFangItem.fields.keys())
output = open('mydbase.csv','w')
first_row = ','.join(columns)
output.write(first_row+'\n')

for item in dbase:
    text = map(lambda x: dbase[item].get(x) if dbase[item].get(x) else '', columns)
    text = ','.join(text)+'\n'
    output.write(text)
    
dbase.close()
output.close()