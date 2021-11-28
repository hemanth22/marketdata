from nsetools import Nse
from pprint import pprint
nse = Nse()
print(nse)
#q = nse.get_quote('NITINSPIN')
#pprint(q)
codelist=["NITINSPIN"]
for code in codelist:
    quote = nse.get_quote(code)
    print('Company Name:',quote["companyName"])
    print('ISIN:',quote["isinCode"])
    print('Status:',quote["css_status_desc"])
    print('Price:',quote["lastPrice"])
    print('Previous Close Price:',quote["previousClose"])
    print('Corporate Action purpose:',quote["purpose"])

fno_helper = nse.get_fno_lot_sizes()
print("========= GET FNO Lot Size ============")
pprint(fno_helper)
print("========= Top Gainers ============")
top_gainers = nse.get_top_gainers()
pprint(top_gainers)
print("========= Top Losers ============")
top_losers = nse.get_top_losers()
pprint(top_losers)
print("========= NSE Indexs ============")
listIndex = nse.get_index_list()
pprint(listIndex)