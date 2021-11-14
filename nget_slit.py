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
