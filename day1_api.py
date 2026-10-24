import requests

url = "https://api.restcountries.com/countries/v5?q=kenya"
headers = {"Authorization": "Bearer rc_live_67ddb75cea1c44fd95aad2d14d39c525"}

response = requests.get(url, headers=headers)

print("Status code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    
    # Navigate into the correct structure
    country = data["data"]["objects"][0]

    name = country["names"]["common"]
    capital = country["capitals"][0]["name"]
    population = country["population"]
    currency = country["currencies"][0]["code"]

    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency}")
else:
    print("Request failed. Status:", response.status_code)
    print("Response:", response.text)
