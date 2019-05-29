r, g, b = 0, 0, 0

r = 0 if r <= 0 else 255 if r >= 255 else r
g = 0 if g <= 0 else 255 if g >= 255 else g
b = 0 if b <= 0 else 255 if b >= 255 else b

result = hex(r)[-2:] + hex(g)[-2:] + hex(b)[-2:]

print(result.upper())

print(hex(0))
