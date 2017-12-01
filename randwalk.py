import numpy as np
import matplotlib.pyplot as plt

L = 16

sims = 1000
tmovil = np.zeros(L//2)
tfijo = np.zeros(L//2)


for j  in range(L//2):
	count = np.zeros(sims)
	countfijo = np.zeros(sims)
	for i in range(sims):
		x1 = j
		y1 = j
		x2 = L-j
		y2 = L-j

		print(i)
		#while x1 != x2 and y1 != y2:
		while True:
			dado1 = np.random.randint(4)
			if dado1 == 0:
				x1 += 1
			elif dado1 == 1:
				x1 -= 1
			elif dado1 == 2:
				y1 += 1
			else:
				y1 -= 1

			if x1 == -1:
				x1 = 1
			if x1 == L + 1:
				x1 = L - 1
			if y1 == -1:
				y1 = 1
			if y1 == L + 1:
				y1 = L - 1

			if x1 == x2 and y1 == y2:
				break

			dado2 = np.random.randint(4)
			if dado2 == 0:
				x2 += 1
			elif dado2 == 1:
				x2 -= 1
			elif dado2 == 2:
				y2 += 1
			else:
				y2 -= 1

			if x2 == -1:
				x2 = 1
			if x2 == L + 1:
				x2 = L - 1
			if y2 == -1:
				y2 = 1
			if y2 == L + 1:
				y2 = L - 1

			if x1 == x2 and y1 == y2:
				break

			count[i] += 1

	for i in range(sims):
		x1 = j
		y1 = j
		xf = L-j
		yf = L-j

		print(i)
		#while x1 != x2 and y1 != y2:
		while True:
			dado = np.random.randint(4)
			if dado == 0:
				x1 += 1
			if dado == 1:
				x1 -= 1
			if dado == 2:
				y1 += 1
			if dado == 3:
				y1 -= 1

			if x1 == -1:
				x1 = 1
			if x1 == L + 1:
				x1 = L - 1
			if y1 == -1:
				y1 = 1
			if y1 == L + 1:
				y1 = L -1

			countfijo[i] += 1
			if x1 == xf and y1 == yf:
				break
	print("--->",j)

	tmovil[j] = np.mean(count)
	tfijo[j] = np.mean(countfijo)

ratio = tmovil / tfijo

print(tmovil)
print(tfijo)
print(ratio)

plt.figure()
plt.plot(ratio)
plt.grid()
plt.show()

"""
	plt.figure()
	plt.subplot(211)
	plt.hist(count, 100)
	plt.xlim((0,2500))
	plt.subplot(212)
	plt.hist(countfijo, 100)
	plt.xlim((0,2500))
	plt.show()
"""