import numpy as np
import matplotlib.pyplot as plt

#L = 32
sims = 1000
maxSize = 10

tmovil = np.zeros(maxSize-1)
tfijo = np.zeros(maxSize-1)


def move(dado,x,y):
	if dado == 0:
		x += 1
	elif dado == 1:
		x -= 1
	elif dado == 2:
		y += 1
	else:
		y -= 1
	return x, y

def handleGoingOffLimits(x,y):
    #celeste a-b
    if y==2*L:
        x += 2*L
        y = L-1

        return x, y

    if ( y==L and (x >= 2*L) ):
        x -= 2*L
        y = 2*L-1

        return x, y

    #limon a-b
    if y== -L-1:
        x += 2*L
        y = 0

        return x, y

    if( y==-1 and (x >= 2*L) ):
        x -= 2*L
        y = -L

        return x, y

    #negro a-b
    if x== 3*L:
        x = -L

        return x, y

    if x== -L -1:
        x = 3 * L -1

        return x, y

    #verde a-b
    if (x==-1 and (L <= y)):
        x = -y+ L-1
        y = L-1

        return x, y

    if ( y== L and (x<= -1)):
        x = 0
        y = L -1 -x

        return x, y

    #marron a-b
    if (x== L and (y >=L) ):
        x = y
        y = L-1

        return x, y

    if( y==L and (L <= x) and (x <=2*L-1)):
        x = L -1
        y = x

        return x, y

    #purpura a-b
    if ( y== -1 and ( x <=-1) ):
        x = 0
        y = x

        return x, y

    if ( x==-1 and (y<=-1) ):
        x = y
        y = 0

        return x, y

    #rosa a-b
    if( x==L and ( y <=-1) ):
        x = -y + L -1
        y = 0

        return x, y

    if(y == -1 and (L <= x) and ( x <= 2*L -1) ):
        x = L -1
        y = -x + L -1

        return x, y

    return x, y

for L in range(1,maxSize):
	numStepsBiMovement = np.zeros(sims)
	numStepsSingleMove = np.zeros(sims)
	for i in range(sims):
		x1 = 0
		y1 = 0
		x2 = 3*L-1
		y2 = L-1
		print(i)
		while True:
			dado1 = np.random.randint(4)
			x1, y1 = move(dado1,x1,y1)

			x1, y1 = handleGoingOffLimits(x1,y1)

			if x1 == x2 and y1 == y2:
				break

			dado2 = np.random.randint(4)
			x2, y2 = move(dado2,x2,y2)

			x2, y2 = handleGoingOffLimits(x2,y2)

			numStepsBiMovement[i] += 1

			if x1 == x2 and y1 == y2:
				break

	for i in range(sims):
		x1 = 0
		y1 = 0
		xf = 3*L-1
		yf = L-1
		print(i)
		while True:
			dado = np.random.randint(4)
			x1, y1 = move(dado,x1,y1)

			x1, y1 = handleGoingOffLimits(x1,y1)

			numStepsSingleMove[i] += 1

			if x1 == xf and y1 == yf:
				break

	print("Size:",L)

	tmovil[L-1] = np.mean(numStepsBiMovement)
	tfijo[L-1] = np.mean(numStepsSingleMove)

ratio = tmovil / tfijo

print(tmovil)
print(tfijo)
print(ratio)

plt.figure()
plt.plot(ratio)
plt.grid()
plt.show()

##
##pos = plt.figure()
##ax = pos.gca()
##ax.axis("equal")
##ax.set_xticks(np.arange(-L, 3*L-1, 1))
##ax.set_yticks(np.arange(0, L-1, 1))
##plt.grid()
##plt.show()


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