d = { v:v > 5 and v or None for v in range(10)}
print(d)

filtered = {f'{key=}':v for key,v in d.items() if v!=None}
print(filtered)
