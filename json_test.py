import json

obj = [1,
       2,
       {5: "1"}
       ]
# convert to str
s = json.dumps(obj)
print(s, type(s))

# convert to object
o = json.loads(s)
print(o, type(o))

