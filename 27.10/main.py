import requests
import xmltodict
from xml.dom.minidom import parse, parseString
import xml.dom.minidom

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
			<soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
				 <soap:Body>
                    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
                        <sCountryISOCode>BR</sCountryISOCode>
                    </CapitalCity>
                </soap:Body>
			</soap:Envelope>"""
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=payload)
dict_response = xmltodict.parse(response.text)
print(dict_response['soap:Envelope']['soap:Body']['m:CapitalCityResponse']['m:CapitalCityResult'])


DOMTree =  parseString(response.text)
collection = DOMTree.documentElement
capitalCityResult = collection.getElementsByTagName("m:CapitalCityResult")
print("CapitalCityResult: %s" % capitalCityResult[0].childNodes[0].data)
