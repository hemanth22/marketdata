from bselib.bse import BSE
b = BSE()
print(b)
#stocks = b.script('532698')
#data = b.quote('532698')
codelist = ['532698']
news_report = b.news('532698')
datam = b.corporate_actions('532698')
#datac = b.credit_reports('532698')
#print(data)
#print(news_report)


for code in codelist:
    quote = b.quote(code)
    print('Company Name:',quote["stockName"])
    print('Stock Price:',quote["stockPrice"])
    print('Updated On:',quote["stockPrice"])
    print('BSE Index:',quote["index"])
    print('Face Value',quote["faceValue"])
print('========= NEWS ===========')
for rp in news_report["news"]:
    print('Headline:', rp['title'])
    print('Short News:', rp['description'])
    print('News Source:', rp['source'])
    print('Report Date:', rp['publisheddate'])

print('========= corporate actions ===========')
print(datam)
print('========= board meetings ===========')
for rp in datam['board_meetings']:
    print(rp)
