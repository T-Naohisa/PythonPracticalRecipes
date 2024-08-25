from urllib import request

# with request.urlopen("https://httpbin.org/get") as f:
#    res = f.read()[:92]
#    print(res)

data = "key1=value1&key2=value2"
res = request.urlopen("https://httpbin.org/post", data=data.encode())
print(res.status)
