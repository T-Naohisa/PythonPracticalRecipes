from urllib import parse

result = parse.urlparse("https://www.example.com.test/;parameter?q=example#hoge")
print(result)

print(result.query)
# 辞書として受け取る
print(parse.parse_qs(result.query))
# タプルとして受け取る
print(parse.parse_qsl(result.query))

print(parse.urlencode({"key1": 1, "key2": 2, "key3": "ぱいそん"}))

print(parse.urljoin("https://ja.wikipedia.org", "/wiki/Python"))
