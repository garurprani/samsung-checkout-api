import requests
import json
import uuid

url = "https://www.samsung.com/in/api/v4/shopping-carts/06458284-459d-4856-9663-cca51b28a34a/billing-info"

# Generate a new client request ID for each request
client_request_id = f"pwa_common_{str(uuid.uuid4())}"


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

# Replace this payload with the actual JSON body you want to send in the POST request
payload = {
    "address_save": False,
    "billing_email_domain": "SONICSERVER.ONLINE",
    "business_name": "SONIC KOMMERCE LLP",
    "city": "New Delhi",
    "country": "IN",
    "displayText": "SONIC KOMMERCE LLP, 94/1,2ND FLOOR,, Wazirpur Industrial Area,New Delhi, 110052",
    "email": "SAM_YASHWANTTT12987@SONICSERVER.ONLINE",
    "first_name": "SONIC",
    "gstin": "07AEPFS1223N1ZN",
    "is_primary_address": False,
    "last_name": "KOMMERCE LLP",
    "line_1": "94/1,2ND FLOOR,",
    "line_2": "Wazirpur Industrial Area,New Delhi",
    "needGst": True,
    "phone": "8287944260",
    "postal_code": "110052",
    "same_as_shipping": False,
    "shipping_address_save": False,
    "state": "Delhi"
}





try:
    response = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))
    
    if response.status_code == 200:
        response_json = response.json()
        
        print("\n" + "="*50)
        print("✅ BILLING INFORMATION UPDATED SUCCESSFULLY")
        print("="*50)
        
        # ===== BILLING INFO =====
        billing = response_json.get('billing_info', {})
        print("\n🧾 BILLING DETAILS:")
        print(f"• Name: {billing.get('first_name', '')} {billing.get('last_name', '')}")
        print(f"• Business: {billing.get('business_name', '')}")
        print(f"• Email: {billing.get('email', '')}")
        print(f"• Phone: {billing.get('phone', '')}")
        print(f"• GSTIN: {billing.get('gstin', '')}")
        print(f"• Address: {billing.get('line_1', '')}, {billing.get('line_2', '')}")
        print(f"• City: {billing.get('city', '')}, {billing.get('state', '')} - {billing.get('postal_code', '')}")
        # print(f"• Display Text: {billing.get('displayText', '')}")  # Uncomment if needed
        
        # ===== CART SUMMARY =====
        cost = response_json.get('cost', {})
        print("\n💰 ORDER SUMMARY:")
        print(f"• Subtotal: ₹{cost.get('subtotal', 0):,.2f}")
        print(f"• Discount: ₹{cost.get('discount', {}).get('amount', 0):,.2f}")
        print(f"• Tax: ₹{cost.get('tax', 0):,.2f}")
        print(f"• Shipping: ₹{cost.get('shipping', 0):,.2f}")
        print(f"• Total: ₹{cost.get('total', 0):,.2f}")
        # print(f"• Service Charge: ₹{cost.get('service_charge', {}).get('cancellation_return_fee', 0):,.2f}")  # Uncomment if needed
        
        # ===== PRODUCT DETAILS =====
        line_items = response_json.get('line_items', {})
        for item_id, item in line_items.items():
            if item.get('attributes', {}).get('product_type') == 'Physical':
                print("\n📦 PRODUCT DETAILS:")
                attrs = item.get('attributes', {})
                print(f"• Name: {attrs.get('display_name', '')}")
                print(f"• Model: {attrs.get('model_name', '')} ({attrs.get('model_code', '')})")
                print(f"• SKU: {item.get('sku_id', '')}")
                
                # Print options (color, storage, memory)
                for opt in attrs.get('options', []):
                    if opt.get('type_name') in ['colour', 'storage', 'memory']:
                        print(f"• {opt['type_name'].title()}: {opt['value']}")
                
                print(f"• Quantity: {item.get('quantity', 1)}")
                print(f"• Price: ₹{item.get('line_item_cost', {}).get('sale_price', 0):,.2f}")
                print(f"• Status: {item.get('inventory_status', {}).get('custom_stock_message', '')}")
                # print(f"• Image: {attrs.get('image_url', '')}")  # Uncomment if needed
        
        # ===== SHIPPING INFO =====
        shipping = response_json.get('shipping_info', {})
        print("\n🚚 SHIPPING DETAILS:")
        print(f"• Name: {shipping.get('first_name', '')} {shipping.get('last_name', '')}")
        print(f"• Address: {shipping.get('line_1', '')}, {shipping.get('line_2', '')}")
        print(f"• City: {shipping.get('city', '')}, {shipping.get('state', '')} - {shipping.get('postal_code', '')}")
        print(f"• Phone: {shipping.get('phone', '')}")
        print(f"• Email: {shipping.get('email', '')}")
        # print(f"• Landmark: {shipping.get('landmark', '')}")  # Uncomment if needed
        
        # ===== SYSTEM INFO =====
        print("\n⚙️ SYSTEM INFO:")
        print(f"• Cart ID: {response_json.get('cart_id', '')}")
        print(f"• User ID: {response_json.get('user_info', {}).get('user_id', '')}")
        print(f"• Status: {response_json.get('status', '')}")
        # print(f"• Device: {response_json.get('user_info', {}).get('device_attributes', {}).get('browser', '')}")  # Uncomment if needed
        
        print("\n" + "="*50)
        
    else:
        print(f"\n❌ ERROR: {response.status_code}")
        print(response.text)

except Exception as e:
    print(f"\n⚠️ EXCEPTION: {str(e)}")