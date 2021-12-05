from bsedata.bse import BSE
import requests
#b = BSE()
#print(b)
b = BSE(update_codes = True)
codelist=["532698","500477","543396"]
#q = b.getQuote('532698')
for code in codelist:
    quote = b.getQuote(code)
    print('Company Name:',quote["companyName"])
    print('Stock Price:',quote["currentValue"])
    print('Updated On:',quote["updatedOn"])
    print('BSE Group:',quote["group"])
    print('Face Value',quote["faceValue"])
    print('industry',quote["industry"])
    print('Previous Close stock price:',quote["previousClose"])
    print('Market Cap Full:',quote["marketCapFull"])
    print('Market Cap Free Float:',quote["marketCapFreeFloat"])
    print('Total Traded Value:',quote["totalTradedValue"])
