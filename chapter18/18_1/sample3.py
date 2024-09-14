import secrets
from urllib import parse

reset_token = secrets.token_urlsafe()
url = "https://example.com/?reset=" + reset_token
print(url)

url_parse = parse.urlparse(url)
qs = parse.parse_qs(url_parse.query)
print(qs)

print(secrets.compare_digest(reset_token, qs["reset"][0]))
