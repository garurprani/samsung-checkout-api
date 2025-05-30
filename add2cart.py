import requests
import json
import uuid

# Ask user for the SKU to add
sku = input("Enter the SKU to add to cart: ").strip()
quantity= input("Enter the Quantity: ")

# URL for the cart API
url = "https://www.samsung.com/in/api/v4/shopping-carts/"

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

# Payload data with postal code
payload = {
    "line_items": [
        {
            "sku_id": sku,
            "quantity": quantity
        }
    ],
    "postal_code": "110052",
}

try:
    response = requests.post(url, headers=headers, cookies=cookies, json=payload)
    
    if response.status_code == 200:
        cart_data = response.json()
        line_item = next(iter(cart_data['line_items'].values()))  # Get first item
        
        # ===== PRODUCT DETAILS =====
        attributes = line_item['attributes']
        options = attributes['options']
        
        # Extract specific options
        color = next((opt['value'] for opt in options if opt['type_name'] == 'colour'), 'N/A')
        storage = next((opt['value'] for opt in options if opt['type_name'] == 'storage'), 'N/A')
        memory = next((opt['value'] for opt in options if opt['type_name'] == 'memory'), 'N/A')
        
        print("\n" + "="*40)
        print("🛒 PRODUCT ADDED TO CART SUCCESSFULLY")
        print("="*40)
        
        print("\n📱 PRODUCT DETAILS:")
        print(f"• Name: {attributes['display_name']}")
        print(f"• Model: {attributes['model_name']} ({attributes['model_code']})")
        print(f"• SKU: {line_item['sku_id']}")
        print(f"• Color: {color}")
        print(f"• Storage: {storage}")
        print(f"• Memory: {memory}")
        # print(f"• Image: {attributes['image_url']}")  # Uncomment if needed
        # print(f"• Product Page: https://www.samsung.com{attributes['product_details_page_url']}")  # Uncomment if needed
        
        # ===== CART SUMMARY =====
        cost = cart_data['cost']
        print("\n💰 CART SUMMARY:")
        print(f"• Cart ID: {cart_data['cart_id']}")
        print(f"• Subtotal: ₹{cost['subtotal']:,.2f}")
        print(f"• Tax: ₹{cost['tax']:,.2f}")
        print(f"• Shipping: ₹{cost['shipping']:,.2f}")
        print(f"• Total: ₹{cost['total']:,.2f}")
        # print(f"• Discount: ₹{cost['discount']['amount']:,.2f}")  # Uncomment if needed
        
        # ===== USER & DELIVERY INFO =====
        user_info = cart_data['user_info']
        print("\n👤 USER & DELIVERY INFO:")
        print(f"• User ID: {user_info['user_id']}")
        print(f"• Delivery PIN: {payload['postal_code']}")
        print(f"• Status: {line_item['inventory_status']['custom_stock_message']}")
        print(f"• Referral Codes: {', '.join(cart_data['referral_codes']) or 'None'}")  # Uncomment if needed
        # print(f"• Device: {user_info['device_attributes']['os']} {user_info['device_attributes']['browser']}")  # Uncomment if needed
        
        # ===== TAX DETAILS (COMMENTED OUT) =====
        """
        print("\n🧾 TAX DETAILS:")
        for tax_group, taxes in cart_data['tax_groups'].items():
            for tax in taxes:
                print(f"• {tax['name'].title()}: {tax['value']}%")
        """
        
        print("\n" + "="*40)
        
    else:
        print(f"\n❌ FAILED TO ADD PRODUCT (Status {response.status_code})")
        print("Response:", response.text)

except Exception as e:
    print(f"\n⚠️ AN ERROR OCCURRED: {str(e)}")