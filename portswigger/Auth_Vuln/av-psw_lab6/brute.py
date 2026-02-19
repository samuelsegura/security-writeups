#!/usr/bin/env python3

# Charger les passwords
passwords = open('/Users/samuelsegura/workspace/pentest_web/pentest-auth_vuln/password.txt').read().splitlines()

usernames = []
passwords_list = []

count = 0
for password in passwords:
    count += 1
    
    # Ajouter carlos:password
    usernames.append("carlos")
    passwords_list.append(password)
    
    # Tous les 2, ajouter wiener:peter pour reset
    if count % 2 == 0:
        usernames.append("wiener")
        passwords_list.append("peter")

# Sauvegarder
with open('/Users/samuelsegura/workspace/pentest_web/pentest-auth_vuln/usernames.txt', 'w') as f:
    f.write('\n'.join(usernames))

with open('/Users/samuelsegura/workspace/pentest_web/pentest-auth_vuln/passwords_intruder.txt', 'w') as f:
    f.write('\n'.join(passwords_list))

print(f"[+] Fichiers créés avec {len(usernames)} lignes chacun")
print(f"[+] Pattern: carlos, carlos, wiener, carlos, carlos, wiener...")

