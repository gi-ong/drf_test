import requests

# TOKEN = '4b919686ba42b1ff8dd6ba61b8fda03f709d0dfd'
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLC"
    "J1c2VybmFtZSI6InRlc3RlcjIiLCJleHAiOjE2Nzg2MzQ5MjEsImVtY"
    "WlsIjoiIn0.schpu48pLHzTWpWIaq9LFA191axIP1bpOOfLCrC620w"
)



headers = {
    # 'Authorization' : f'Token {TOKEN}', # Token 인증
    'Authorization' : f'JWT {JWT_TOKEN}', # JWT 인증
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())