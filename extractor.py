import requests
import json
from datetime import datetime

URL = "https://api.golemio.cz/v2/municipallibraries/5"

def fetch_libraries():
    response = requests.get(URL, headers={"Content-Type": "application/json"})
    print(response)
    libraries = response.json().get("data", [])

    extracted = []
    for lib in libraries:
        extracted.append({
            "library_id": lib.get("id"),
            "name": lib.get("name"),
            "street": lib.get("address", {}).get("street"),
            "postcode": lib.get("address", {}).get("postalCode"),
            "city": lib.get("address", {}).get("city"),
            "district": lib.get("address", {}).get("district"),
            "country": lib.get("address", {}).get("country"),
            "latitude": lib.get("location", {}).get("latitude"),
            "longitude": lib.get("location", {}).get("longitude"),
            "opening_time": lib.get("opening_hours", {}).get("opening_hours")
        })

    filename = f"urban_libraries_{datetime.utcnow().strftime('%Y-%m-%d')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(extracted, f, indent=2)

    print(f"Extracted {len(extracted)} records into {filename}")

if __name__ == "__main__":
    fetch_libraries()
