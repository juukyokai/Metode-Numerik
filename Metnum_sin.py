#!/bin/python
from math import sin

e= 2.7182818284
rumus = "sin x"
def f(x):
  y = sin(x)
  return y
def trapezoid(h,n,pos):
	hasil = 0
	for i in range(0,n):
		hasil = hasil + (h/2 * (f(pos[i]) + f(pos[i+1])))
		print("f(",i,") : ",f(pos[i])," f(",i+1,") : ",f(pos[i+1]))
	return hasil
if __name__ == '__main__':
	#Input batas bawah dan atas
	a = float(input("Masukkan batas atas area  : "))
	b = float(input("Masukkan batas bawah area : "))
	#Input berapa jumlah bagi
	n = int(input("masukkan jumlah pembagi area hitung : "))

	#memproses posisi x1 hingga xn
	pos = []
	temp = a
	h = (b - a)/n
	print("delta x : ",h)
	for i in range(0,n+1):
		pos.append(temp)
		temp = temp + h

	#hasil hitung
	print("hasil hitung dengan rumus : ",rumus," memiliki area : ",trapezoid(h,n,pos))

