#String - str metinsel ifadeleri tutar 
strTüründeDegiskenIsmı = "str türünde bir metinsel veri"
print(strTüründeDegiskenIsmı)

#Sayısal veri tipi = int, float, complex
#int -- tam sayılı veriler tutar
tamSayi = 10
#float -- ondalıklı sayıları tutar 
ondalikliSayi = 10.5
# complex -- complex veri tipi, bir gerçek sayı ve bir sanal sayıyı içeren karmaşık sayılar için kullanılır
a = complex(3,4)
print(a.real)
print(a.imag)

#Sequence veri tipleri - list, tuple, range
#list -- birden fazla verileri tutar bu veriler str, int, float..vs gibi olabilir
benimListem = [5, 6, 6.6, "Metinsel bir eleman", True, False, complex(3,9)]
print(benimListem[0]) #programlama dilleri saymaya 0'dan başladığı içinn listemin sıfırıncı yani 5'i ekrana yazdıracaktır

#tuple - list gibi çalışır tek farkı elemanları değiştirelemez.

benimListemTuple = (5, 6, 6.6, "Metinsel bir eleman", True, False, complex(3,9))
##benimListemTuple[0] = 10 #hata verecektir çünkü tuple listesi değiştirelemez

#range - belirli aralıktaki sayıları oluşturmak için kullanılır
sayiListesi = list(range(10))
print(sayiListesi)
#eğer başlangıç değeri verilirse ordan başlar
sayiListesi = list(range(2,10))
print(sayiListesi)


