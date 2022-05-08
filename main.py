 # -*- coding: utf-8 -*-
import random
import numpy
from change import Hexagram as Hex
from transfer import Transfer as Tra
from i_ching import IChing as IC

# 演算到这里，得出了变卦和变爻，终于完成了整个占卜。
# 此时，我们可以用两个变爻的占辞来判断吉凶，定名字；并以位置考上的那一个变爻的占辞为主。
# 参见《易经》，我们可以得到结果：“九四，由豫,大有得;勿疑,朋盍簪。”

class ReadClass():
	def __init__(self):
		self.num = 0

	def read(self):
		index = 0
		h = Hex()
		array = h.hexgram()
		print (array)
		t = Tra()
		oldHex = t.yinYangTransfer(array)
		print (oldHex)
		newHex = t.shaoTaiTransfer(array)
		print (newHex)

		for i in range (len(newHex)):
			if newHex[i] != oldHex[i]:
				index = i + 1

		print ("第 "+ str(index) +" 爻")
		i = IC()
		print (i.text(oldHex))

if __name__ == '__main__' :
	r = ReadClass()
	r.read()