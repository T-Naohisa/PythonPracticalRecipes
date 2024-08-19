from urllib import parse

result = parse.urlparse("https://www.example.com.test/;parameter?q=example#hoge")
print(result)
