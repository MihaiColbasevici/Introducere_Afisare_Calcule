tot = int(input("Dați suma în lei. \t \t"))
unit = tot % 10
zeci = (tot // 10) % 10
sute = (tot // 100) % 10
mii = tot // 1000

nr_mii = mii

if (sute >= 5):
    nr_5sute = sute // 5
elif (sute < 5):
    nr_5sute = 0
sute = sute - nr_5sute*5
if (sute >= 2):
    nr_2sute = sute // 2
elif (sute < 2):
    nr_2sute = 0
sute = sute - nr_2sute*2
if (sute >= 1):
    nr_1suta = sute
elif (sute == 0):
    nr_1suta = 0

if (zeci >= 5):
    nr_5zeci = zeci // 5
elif (zeci < 5):
    nr_5zeci = 0
zeci = zeci - nr_5zeci*5
if (zeci >= 2):
    nr_2zeci = zeci //2
elif (zeci < 2):
    nr_2zeci = 0
zeci = zeci - nr_2zeci*2
if (zeci >= 1):
    nr_zece = zeci
elif (zeci == 0):
    nr_zece = 0

if (unit >= 5):
    nr_5unit = unit // 5
elif (unit < 5):
    nr_5unit = 0
unit = unit - nr_5unit*5
if (unit >= 2):
    nr_2unit = unit // 2
elif (unit < 2):
    nr_2unit = 0
unit = unit - nr_2unit*2
if (unit >= 1):
    nr_unit = unit
elif (unit == 0):
    nr_unit = 0

print("Veți avea nevoie de: ")
if (nr_mii != 0):
    print(nr_mii, "bancnotă/e de 1000 de lei;")
if (nr_5sute != 0):
    print(nr_5sute, "bancnotă/e de 500 de lei;")
if (nr_2sute != 0):
    print(nr_2sute, "bancnotă/e de 200 de lei;")
if (nr_1suta != 0):
    print(nr_1suta, "bancnotă/e de 100 de lei;")
if (nr_5zeci != 0):
    print(nr_5zeci, "bancnotă/e de 50 de lei;")
if (nr_2zeci != 0):
    print(nr_2zeci, "bancnotă/e de 20 de lei;")
if (nr_zece != 0):
    print(nr_zece, "bancnotă/e de 10 lei;")
if (nr_5unit != 0):
    print(nr_5unit, "bancnotă/e de 5 lei;")
if (nr_2unit != 0):
    print(nr_2unit, "bancnotă/e metalică/e de 2 lei;")
if (nr_unit != 0):
    print(nr_unit, "bancnotă/e de 1 leu.")