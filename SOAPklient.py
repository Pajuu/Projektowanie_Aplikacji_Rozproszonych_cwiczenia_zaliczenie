import requests

url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CountryFlag xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>PL</sCountryISOCode>
    </CountryFlag>
  </soap:Body>
</soap:Envelope>"""

headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=xml)

print("Flaga polski:\n", response.text)

url2 = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

xml2 = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <ListOfLanguagesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
    </ListOfLanguagesByName>
  </soap:Body>
</soap:Envelope>"""

response = requests.request("POST", url2, headers=headers, data=xml2)
print("Lista języków:\n", response.text)