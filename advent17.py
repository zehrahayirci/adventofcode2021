def invtri(x):
	return int((x * 2)**0.5)

def search(xmin, xmax, ymin, ymax, v0xmin):
	total = 0
	yhi   = 0

	for v0x in range(v0xmin, xmax + 1):
		for v0y in range(ymin, -ymin):
			x, y   = 0, 0
			vx, vy = v0x, v0y

			while x <= xmax and y >= ymin:
				if x >= xmin and y <= ymax:
					total += 1
					break

				x, y = (x + vx, y + vy)
				vy -= 1

				if vx > 0:
					vx -= 1

				if y > yhi:
					yhi = y

	return yhi, total

yhi, total = search(241,273,-97,-63,invtri(241))
print(yhi,total)
