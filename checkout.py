import requests
import uuid

url = "https://www.samsung.com/in/api/v4/shopping-carts/shipping-info"


# Generate a new client request ID for each request
client_request_id = f"pwa_common_{str(uuid.uuid4())}"

# Headers from the request
headers = {
    "authority": "www.samsung.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
    "origin": "https://www.samsung.com",
    "referer": "https://www.samsung.com/in/web/cart?addItem%5B%5D=SM-M356BLBB%2C1&postal_code=110052",
    "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "x-client-request-id": client_request_id,
    "x-ecom-app-id": "pwa",
    "x-ecom-jwt": "ZXlKaGJHY2lPaUpTVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpZMmhsYldGZmRtVnljMmx2YmlJNklqRXVNQ0lzSW1WNGNDSTZNVGMwTnpZMk5UY3lNQzR3TlN3aWJXRjRYMlY0Y0dseWVTSTZNVGMwTnpRd09ETXlNQzR3TlN3aWRtVnljMmx2YmlJNklqRXVNQ0lzSW1OcGNHaGxjaUk2SWxVeVJuTmtSMVpyV0RFNU1WbFZkWEUyTVdWSWIzaERaMmRwTnpGTlpsQjRPWHBVWkVkbVlXcERTbGRZZWpaVUwwVXpNRmxJU0hoMmFEVm1aRUl4VURWUFEzZDNRVUZTUkhaTFZuY3hTbGxMV1ZScVFUSmtXSGRXZWpsVGFIcEVMMnRxYmxVdlRubGtOMUJrVFhWamNWbE5abUoxUVZCTWRWQmxhMU5IVERFMFVFdHFXbmh4ZVc5elptazJkVTFsVlc1a056UjRjVVozY25JdmJFbHhNelJyUVd4T1ZWQlRVMGMwTDJGVVdFTm9ZbnBxVEhGMk5VeGljU3RFYlhndmJtcEdaakZWVUVSU2VEaE9NVGxLWXl0VVpEbDZNWGwxUjNOWE0wOHZjbGs1Ylc5UlJWWXlTMHBKZVV0SmQzcHJWVU5ZWTNWdVNFOVBNRXRST0ROU05reDJZekEzZWtNMlYwczBTbTlZVEhsVFYwMVlWbmRHU2taclVXWmtOMWxsVlZwdlYzRkVNVnBOYml0eFIzSlFTMnhZYWxWbloxZGliR1ZoT0Uxck9DdFJlWEZ4ZDFwTE0zQk5kbFZ3V21GWk9VbGpkU3NyZW5wa00ydGlhVW94VGtWQ2VHTldWbVJUVjFOcmFXNVlTMnRJYWs0cmNuUllabFY0ZEd0U2REUmphVkE1YlZOMmIzZHZkM3BPUmsxU1NGRlZTemhPTnpacFlXcDVlbGRyU1U5RVpHSkRlVGxWU1ZsQ1FsbElTVVJsWVVSV1pFSjJRWEZNV2xodU5sRm1NbGhVZVZsWGFraFVSa2czYmtWWEt6aFBVV05UWjJoU2VIaG1lRmxQUnpRMFJtcEhkR0Y1U1ROek9XaGFOM0pMZEdsWU9IWjNibUk1VHk5dWJFUmFNbGxOUm5SWlRsbEZTMDVpZVdSWmJtNXhUVU5WTjFsNlVIQXpTWGh3UW1WeU0ybHpRWGhYWjBSNlYzcDZjM2hYWlhCUldtRTRlVlpKYzBodmFtcHNibmRVWTNwSFFuQkJZa2RCY3psalRXRjRURGhVUVdRNVJEZG5aak5GTUdKRk9IbHdOMUJUVEVSM2RGbGhjMmhvVkZOdGNtcG9aMVZEZGpKMlYxRldWRlZrWlZGWWRsSTJWM2hMVERsd1MyWmxVWEpDYW5JclkxYzNielphUzI0MVRDOVZValpwT0hWaU5URkRNVzlRYTJsWGIySlVNelYzT0RWdWIySjJZWGgzUzFoSGNsWTVOamx0ZGpaMVEwcHVhbmhHZUN0TE1IbHJWMkZwYlhGbFNHMTVaV3RVTkRReE1XRlBjM2R6TjNsa2NWcFZNbEJKU2toeE1YSjZMM2RCTkRkM2EwdHBTVUY0VkdSRVFubGxWbTUyUjA5a1JEQTBOMGw0VTBWSFUyWmtLMHRSZHpNMGNGa3ljbXhpU0VSQlUwOVNjRkl5ZVU1QmFXWnFWa3NyV0dFMVRFWWlMQ0pwWVhRaU9qRTNORGMwTURZMU1qQjkuckxwN0J6UW9wbmotenFMQ0YybmM1eGVmbS1KV0JrT2NIbjd0cTV0NGg2WU1QZEtXRy1DRzN5clVJekJJUTJZcG9kSWtQLXF1U0VkVUFrTkxPemgtVEstTXNERFpDMV9LenAyVkxyNlFxbGNMR0pHTTVQTGxSNHBPX3IzTVVWc09FV0ZlWkFoVS1RZnh0dGpMMG0tbUYyR3RUbFBfcXZlbTJiaDFjZTgtNGdN"
}

# Cookies from the request (simplified - you may need to include more or get fresh ones)
cookies = {
    "deliveryPincode": "110052",
    "device_type": "pc",
    "country_codes": "in",
    "cookie_country": "in",
    "s_ecom_scid": "d6a12606-20d1-4642-b3c5-dff1843aaabf",
    "s_ecom_sc_cnt": "0",
    "ecom_vi2_IND": "OWVjN2Y1NGQtNzhjZi00MTY2LTk2YzEtNTIzYTdhYWYxZTZi",
    "ecom_session_id2_IND": "ZmY1MTYyYTAtOGRiMi00MmU1LTg5OTYtMzExNGNhYTNiMTk0",
    "jwt_IND": "ZXlKaGJHY2lPaUpTVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnpZMmhsYldGZmRtVnljMmx2YmlJNklqRXVNQ0lzSW1WNGNDSTZNVGMwTnpZMk5UY3lNQzR3TlN3aWJXRjRYMlY0Y0dseWVTSTZNVGMwTnpRd09ETXlNQzR3TlN3aWRtVnljMmx2YmlJNklqRXVNQ0lzSW1OcGNHaGxjaUk2SWxVeVJuTmtSMVpyV0RFNU1WbFZkWEUyTVdWSWIzaERaMmRwTnpGTlpsQjRPWHBVWkVkbVlXcERTbGRZZWpaVUwwVXpNRmxJU0hoMmFEVm1aRUl4VURWUFEzZDNRVUZTUkhaTFZuY3hTbGxMV1ZScVFUSmtXSGRXZWpsVGFIcEVMMnRxYmxVdlRubGtOMUJrVFhWamNWbE5abUoxUVZCTWRWQmxhMU5IVERFMFVFdHFXbmh4ZVc5elptazJkVTFsVlc1a056UjRjVVozY25JdmJFbHhNelJyUVd4T1ZWQlRVMGMwTDJGVVdFTm9ZbnBxVEhGMk5VeGljU3RFYlhndmJtcEdaakZWVUVSU2VEaE9NVGxLWXl0VVpEbDZNWGwxUjNOWE0wOHZjbGs1Ylc5UlJWWXlTMHBKZVV0SmQzcHJWVU5ZWTNWdVNFOVBNRXRST0ROU05reDJZekEzZWtNMlYwczBTbTlZVEhsVFYwMVlWbmRHU2taclVXWmtOMWxsVlZwdlYzRkVNVnBOYml0eFIzSlFTMnhZYWxWbloxZGliR1ZoT0Uxck9DdFJlWEZ4ZDFwTE0zQk5kbFZ3V21GWk9VbGpkU3NyZW5wa00ydGlhVW94VGtWQ2VHTldWbVJUVjFOcmFXNVlTMnRJYWs0cmNuUllabFY0ZEd0U2REUmphVkE1YlZOMmIzZHZkM3BPUmsxU1NGRlZTemhPTnpacFlXcDVlbGRyU1U5RVpHSkRlVGxWU1ZsQ1FsbElTVVJsWVVSV1pFSjJRWEZNV2xodU5sRm1NbGhVZVZsWGFraFVSa2czYmtWWEt6aFBVV05UWjJoU2VIaG1lRmxQUnpRMFJtcEhkR0Y1U1ROek9XaGFOM0pMZEdsWU9IWjNibUk1VHk5dWJFUmFNbGxOUm5SWlRsbEZTMDVpZVdSWmJtNXhUVU5WTjFsNlVIQXpTWGh3UW1WeU0ybHpRWGhYWjBSNlYzcDZjM2hYWlhCUldtRTRlVlpKYzBodmFtcHNibmRVWTNwSFFuQkJZa2RCY3psalRXRjRURGhVUVdRNVJEZG5aak5GTUdKRk9IbHdOMUJUVEVSM2RGbGhjMmhvVkZOdGNtcG9aMVZEZGpKMlYxRldWRlZrWlZGWWRsSTJWM2hMVERsd1MyWmxVWEpDYW5JclkxYzNielphUzI0MVRDOVZValpwT0hWaU5URkRNVzlRYTJsWGIySlVNelYzT0RWdWIySjJZWGgzUzFoSGNsWTVOamx0ZGpaMVEwcHVhbmhHZUN0TE1IbHJWMkZwYlhGbFNHMTVaV3RVTkRReE1XRlBjM2R6TjNsa2NWcFZNbEJKU2toeE1YSjZMM2RCTkRkM2EwdHBTVUY0VkdSRVFubGxWbTUyUjA5a1JEQTBOMGw0VTBWSFUyWmtLMHRSZHpNMGNGa3ljbXhpU0VSQlUwOVNjRkl5ZVU1QmFXWnFWa3NyV0dFMVRFWWlMQ0pwWVhRaU9qRTNORGMwTURZMU1qQjkuckxwN0J6UW9wbmotenFMQ0YybmM1eGVmbS1KV0JrT2NIbjd0cTV0NGg2WU1QZEtXRy1DRzN5clVJekJJUTJZcG9kSWtQLXF1U0VkVUFrTkxPemgtVEstTXNERFpDMV9LenAyVkxyNlFxbGNMR0pHTTVQTGxSNHBPX3IzTVVWc09FV0ZlWkFoVS1RZnh0dGpMMG0tbUYyR3RUbFBfcXZlbTJiaDFjZTgtNGdN",
    # Add other important cookies as needed
}

# Example request setup (replace with your own)
response = requests.get(url, headers=headers, cookies=cookies)
print("Status code:", response.status_code)
print("Response:")

response_json = response.json()

for i, item in enumerate(response_json, 1):
    print(f"\n📦 Entry {i}:")
    print(f"• id: {item['id']}")
    print(f"• created_date: {item['created_date']}")
   #print(f"• modified_date: {item['modified_date']}")
    # print(f"• address_overridden: {item['address_overridden']}")  # Uncomment if needed
    # print(f"• address_save: {item['address_save']}")  # Uncomment if needed
    print(f"• city: {item['city']}")
    print(f"• country: {item['country']}")
    print(f"• email: {item['email']}")
    print(f"• first_name: {item['first_name']}")
    # print(f"• is_primary_address: {item['is_primary_address']}")  # Uncomment if needed
   #print(f"• label: {item['label']}")
   #print(f"• last_name: {item['last_name']}")
   #print(f"• line_1: {item['line_1']}")
    # print(f"• line_2: {item['line_2']}")  # Uncomment if needed
    print(f"• phone: {item['phone']}")
    print(f"• postal_code: {item['postal_code']}")
    # print(f"• shipping_address_save: {item['shipping_address_save']}")  # Uncomment if needed
    print(f"• state: {item['state']}")
    print(f"• type: {item['type']}")
    # print(f"• is_locked_address: {item['is_locked_address']}")  # Uncomment if needed
    print("-" * 30)