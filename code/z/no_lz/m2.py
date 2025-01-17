import numpy as np
from te.m import m
from tensorflow.keras.layers import Input, Dense, Dropout, dot
from tensorflow.keras.models import Model
from tensorflow.keras import regularizers

class m2(m):
	fn = "m"
	dd = "/ex/z/no_lz"

	def md(self):
		self.x_n = 274
		self.y_n = 204
		self.g_n = 85
		x = Input((self.x_n,), name="x")
		y = Input((self.y_n,), name="y")
		g = Input((self.g_n, self.y_n), name="g")

		# x
		d = Dense(int(self.y_n*1), activation='relu', kernel_regularizer=regularizers.l2(0.01))
		self.x2 = Dropout(0.2)(d(x))

		# y0
		d2 = Dense(int(self.y_n*1), activation='relu', kernel_regularizer=regularizers.l2(0.01))
		self.y2 = Dropout(0.2)(d2(y))
		self.g2 = Dropout(0.2)(d2(g))

		c = dot([self.y2, self.x2], axes=-1, normalize=True)
		self.m = Model(inputs=[x, y, g], outputs=c)
		self.m.compile(loss=self.ls(), optimizer='sgd', metrics=[self.ls()])


def te_sc2(m, x, g):
	sc = []
	tmp = np.zeros((len(g.v), m.g_n,m.y_n))
	for v in x.c2:
		x_ = np.tile(v, (len(g.v),1))
		sc.append(m.m.predict([x_, g.c2, tmp]).flatten())
	return np.array(sc), g.ei
