def luas_persegi_panjang(panjang,lebar) :
    return panjang * lebar

def luas_lingkaran(jari2) :
    return 3.14 * (jari2**2)

def luas_cube(sisi) :
    return (sisi*2)*6

def celcius_to_fahrenheit(celcius) :
    return ((9/5)*celcius)+32

def reamur_to_kelvin(reamur):
    return ((5/4)*reamur)+273

print(luas_persegi_panjang(10,5))
print(luas_lingkaran(2))
print(luas_cube(2))
print(celcius_to_fahrenheit(10))
print(reamur_to_kelvin(4))