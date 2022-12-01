import zeep 

wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

client = zeep.Client(wsdl=wsdl_url)

country_code = "BR"

result = client.service.CapitalCity(
	sCountryISOCode=country_code
)

print(f"Mostrando a capital de(a) {country_code} é {result}")
