names = [("name", "Kalob"), ("occupation", "Coder")]
d = {}
for key, value in names:
    d[key] = value
print(d)

d = {key: value for key, value in names}
print(d)

d = dict(names)
print(d)
