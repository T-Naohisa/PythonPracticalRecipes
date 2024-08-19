import json

data = [
    {"id": 123, "entities": {"url": "python.org", "hashtags": ["#python", "#pythonjp"]}}
]
# json文字列をエンコードする jsonにする
print(json.dumps(data, indent=2))


data2 = '[{"id": 123, "entities": {"url": "python.org", "hashtags": ["#python", "#pythonjp"]}}]'
# json文字列をデコードする pythonの型に変更する
print(json.loads(data2))
