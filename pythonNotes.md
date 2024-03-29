# *****************Python Notlarım*****************
# NUMPY FRAMEWORK
- Herhangi birşey import ederken import dosya_adi as dosya_kısaltmasi olarak kısaltma ataması yapmak mümkün
- Numpy kullanılma sebebi matlabtaki gibi vektör oluşturma, matrix oluşturmada kullanılır.
##  Array(kelime anlamı olarak MATRİS anlamına gelir)
- np.array ile matris oluşturuluyor
### .reshape() _bir matrisi geçici olarak yeniden düzenler_
- array.reshape(x,y)x satırında y sütünü kada matris oluşturmuş oluyoruz
### .ndim _matrisin kaç boyutlu olduğunu öğrenmemize yarar_
- array.ndim ile kaç boyutlu olduğunu öğrenebiliriz.
- array.dtype.name ile integer mı string mi onu öğrnebilirim.
### .size _matrisin boyutunu öğrenebilirim_
- array.size ile boyutunu öğrenebilirim. 
### .zeros() _içine girdiğimiz matris boyutuna bağlı kalarak 0 ların olduğu matris üretir_
- np.zeros(x,y)x e ylik bir matris oluşturur. append metodu memory i çok yorduğu için tecih edilir.
- Zeros a ekleme yapmak için zeros_değişkeninin_adı[x,y]=z xnci satır ynci sütunu değişkeni z olsun demiş oluruz.
- Zerosdaki eklemelerde indeksteki mantıkla aynı 0 ncı satır 0 ncı sütun indeks demek.
### .ones() _içine girdiğimiz matris boyutuna bağlı kalarak 1 lerden oluşan matris üretir_
- np.ones(x,y) zerosla aynı mantık 1 lerden oluşan bir matris yaratır.
### .empty() _içine giridğimiz ölçülerde boş matris üretir_
- np.empty(x,y) zeros ones ile yaptıklarımızın aynısı sadece boş bir matriks yaratır.
### .arange() 
- np.arange(x,y,z) x den y e kadar olan sayıları z atlayarak yaz demektir. 
### _Dipnot_: _Pythonda yukarıdaki gibi yazıldığında x i dahil eder fakat son sayı y i dahil etmez_
- np.linspace(x,y,z)x den y e kadar olan sayıları z kadar türetir en son y i de dahil eder.
## Numpy Operatörleri
- np.sin(x) içerisine girilen değerin sinusunu alır.
- np.random.random(x,y)5 e 5 lik 0 ile 1 arasında sayı oluşturur.
### .sum(),.max(),.min() _değerler içerisinden max min bulma veya değerlerin toplamını bulmada kullanılır_
- array.sum() tüm değerlerin toplamı
- array.max() oluşturulan sayılardaki maximum değer
- array.min() oluşturulan sayılardaki minimum değer.
- **axis=0** olursa sütunları alır 1 olursa satırları alır.
- array.sum(axis=0) matristeki sütunları toplar
- array.sum(axis=1) matristeki satırları toplar
### .sqrt() _içerisine girilen değikenin karekökünü almada kullanılır_
- np.sqrt(a) a nın karekökünü almada kullanılır.
### .square() _içiresine atılan değerin karesini alır_
- np.square(a) a nın karesini almada kullanılır
### .T ve .dot() _birlikte kullanıldığında bir matrisin transpozunu alır_
- array.dot(digerArray.T) T transpoz yani matrisi tersine çevirir 3 e 2 ise 2 e 3 yapar.
- Transpoz çarpımı hatırlamazsan google a yaz
## Indexing and Slicing
- Herhangi bir arrayde indeksleri 0 dan 3 ekadar olacak şekilde örneğin yazdırmak istiyorsam array[0:3] dersem 0 dan 3 e kadar olan sayıları 3 dahil olmadan yazdırır.
- Bir arrayı tersine çevirme array[::-1]
### Matrisler arasından seçim yapma
- array[:,1] iki nokta  satırların hepsini al virgülden sonraki 1 de 1nci indeksteki sütunu al demiş oluyorum 
- array[x,y] x satır y sütun anlamına gelir eğerki son satırı almak istiyorsak x yerine -1 yazarız eğer ki tüm satırları almak istiyorsak : kullanırız.
## Shape Manip.
- Matrislerde düz liste olarak yazmaya yarar.
### .ravel() _tek bir vektör haline getirir_
- array.ravel() tek bir vektör haline getirir.
### Matrisleri tekrar design etmek
- a.reshape(x,y) x ve y kaça kaçlık matrise döndürmek istediğimizi girmiş oluruz.
- 3 lü matriste transpozunu almak için array.T
- **resize reshape den farkı ne?**
- reshape geçici olarak değiştirirken resize matrisin yapısını değiştirip kaydeder.
- array.resize(x,y)
## Stacking Arrays
- Bir array ile diğper bir arrayi birleştirmeye yarar.
- Dikine birleştirmek istiyorsak np.vstack((arrayismi,arrayismi))
- Yatay birleştirmek için np.hstack((arrayinismi,arrayinismi))
## Arrayı Listeye Dönüştürme(Conver and Copy)
- Liste şeklinden veri beklendiği durumlarda yapılır.
-  Birtane array oluşturup farklı işlemler yapmamız gereken durumlarda ihtiyaç duyuyoruz örneğin ilgili arraydeki herhangi bir rakamı değiştirmek gibi. 
- copyyapmakistenilendegiskenismi.copy() kopyalarsam sadece o değişken değişir memorydeki değişmez
# PANDAS FRAMEWORK
- Data frame için oluşturulmuş kütüphanelerdir.
- Hızlı ve etkili dataframes
- Dosyalar arasında geçişleri kolay.
- Missing data lara çözüm üretmede avantajlı.
- reshape ile datayı daha verimli kullanabiliriz.
- slicing ve indexing kolay.
- time series data analizinde yardımcı.(zamanla gelen data)
- Her şeyden önemlisi hız açısından optimize bir kütüphane.
- Kısaltması dünya üzerinde pd olarak kullanırlar yada direkt pandas. olarak kullanılır.
## Tanımlanmış bir sözlükğü excel tablosuna çevirme
- Excel tablosu şeklinde göstermek için kullanılır.
- yeni_degisken_isim=pandas.DataFrame(ilgili_dictionary_ismi)
## .head()
- Önden göz gezdirme için kullanılır.
- Head içerisinde herhangi bir değer girilmezse defaulttaki değer baz alınır içine girilen rakama göre de veri çekilebilir.
- İlgili datadaki ilk 5 taneyi bana ver anlamına gelir.
- Kullanım şekli;
- head=cagırmakIstenilenDegiskenIsmi.head()
- Çağırmak istediğimiz datanın isminin sonuna .head() getirerek kullanabiliriz.
## .tail()
- Sondaki 5 i göstermemize yarar.
- Tail içerisinde herhangi bir değer girilmezse defaulttaki değer(5) baz alınır içine girilen rakama göre de veri çekilebilir.
- tail=cagırmakIstenilenDegiskenIsmi.tail()
## Pandas Basic Methods
- dataframeismiumns dataframe ataması yaptığımız sütunları gösterir
- dataframeismi() dataframe in bilgilerini özet geçer sütun sayısı tip(numpy mı pandas mı)
### .dtypes parametresi
- dataframeisimi.dtypes her column type ını yazdırır
### .describe() methodu
- dataframeismi.describe() sadece nümerik özelliklerini alır
## Pandas Indexing and Slicing
- dataframeismi["sütun basligi"] sadece ilgili sütundaki bilgileri alır. ve indexleride hep alır pandasta. 
- Veri çekmenin başka yoluda dataframeİsmi.sütunbasligi
- dataframeismi["yeni eklenecek sütun basliginin ismi "]=[sütunobje1,sütunobje2,sütunobje3] gibi dataframe e ekleme yapılmaktadır.
### .loc() methodu 
- Sütunlarda gezinme/seçme işlemi yapmak için aynı numpyda kine benzer; dataframe.loc[satir,"sütunbasligi"]
- Eğer ki satirdan sadece 3 tane veriye ihtiyacım varsa; dataframe.loc[:3,"sütunbasligi"]
- Belirli başlık  aralığını yazdırmak istersem; dataframe.loc[:3,"sütunbasligi":"DİGERsütunbasligi"]
- Başlık aralığınız yazdırmanın diğer yöntemi; dataframeismi.loc[:3,["sütunbasligi","DİĞERsütunbasligi"]]
- Pandastaki gibi tersten yazdırmak istersem; dataframeismi.loc[::-1,:]
- Name dahil olmak üzere 0ncı column dan istediğimiz yere kadar yazdırmak isterse; dataframeismi.loc[:,:"sütunbasligi"] üstunbasligi dahil olmak üzere yazdırır.
- loc LOCATİON anlamına gelir
### .iloc() methodu
- iloc integer LOCATİON anlamına gelir.
- İlla ismiyle çağırmak zorunda değiliz şöyle de yapılabilir; dataframeismi.iloc[:,indexDegeri] indexDegeri 0 1 2 diye sayılmaktadır.
### .linspace()
- Belirli bir eşit aralıkta sayıları döndürür 
- Matris tanımlarken kullanılır.
- Matlabdaki gibidir işlevi
### .hstack()
- Dizileri yatay olarak sırasıyla yığınlar(horizantal)
## Filtering Pandas Data Frame _datayı filtreleme_
- dataframeismi.sütunbasligi > kontrol edilecek değer dersek bool cinsinden dataframe in içindeki değerleri verdiğimiz değere göre gösterir.
- 2 ayrı koşulu birleştirmek istersek dataframeismi[filtrelenmişDeğişken1,filtrelenmişDeğişken2]
- Direkt olarak kontrol sağlanmak istenirse; print(dataframeismi[dataframeismi.sütunbasligi> kontrol sağlanacak değer])
## Pandas List Comprehension
### .mean() _ortalama bulma fonksiyonu_
- Ortalama bulma; dataframeismi.sütunbasligi.mean() ile o sütuna ait ortalama bulunabilir.
### .lower() methodu _büyük harfleri küçük harflere çevirme_
- Her bir columnda gezinip büyük harfleri küçük harflere çevirmek için; dataframeismi.columns=[each.lower() for each in dataframeismi.columns]
### .slipt() _başlıklardaki boşlukları belirleme_
- Başlıklar arasındaki boşlukları belirlemede  için kullanılır.
- Kullanım şekli dataframeismi.columns=[each.slipt()[0]+"_" each.slipt()[1] if(len(each.slipt())>1) else each for each in dataframeismi.columns]
##  Concatenating Data _Ayrı dataları birleştirme_
### .drop()
- ilgili dataframeden başlık çıkarmaya yarar 
-  dataframeismi.drop(dataframeismi.index[x]) ilgili indexi çıkarırken kullanılır 
- dataframeismi.drop(["yeni eklenmiş başlık"],axis=1,inplace= True)
- inplace yeni değeri alır dataframeismi ne dahil eder. 
### pdconcat() _iki ayrı datayı birleştirmede kullanılır_
_Vertical Birleştirme_
- data1=dataframeismi.head() dataframedeki baştaki 5 değerş alır
- data=2dataframeismi.tail() dataframede sondaki 5 değeri alır
- pd.concat([data1,data2],axis=0)
_Horizantal Birleştirme_
-data_h_concat=pd.concat([maas,age],axis=1)
- axis in 1 oluşu dikey olarak ekler
## Transforming Data _Data değerlerinde düzenleme yapma_
- dataframeismi["yeni_baslik"]=[each*2  for each in dataframeismi.gezinmekistenenbaslikadi] başlık içindeki tüm değerleri gezer 2 ile çarpıp yeni başlığa ekler.
### .apply() _dataframe deki değeri değiştirip yeni başlığa atamada kullanılır_
- _Adım1_:def ile bir fonksiyon oluşturulur.
- _Adım2_: dataframeismi["yeni-baslik"]=dataframeismi.degistirilecekbaslik.apply(fonksiyon_ismi)
# Yapay Zeka OOP
- 
## Classes 
- 


# Bitişi
## _While_
- for döngülerinde yapcaklarımız while döngüsünde de yapabiliriz.Sadece bazı noktalarda for döngüleri daha avantajlı oluyor
```python
		i=0
		while(i<10)
		    print("i nin degeri: {}".format(i))
		    i +=1
```
- İsmi 3 kere yazdırma
```python
		a=0
		while(a<=3)
			print("yarkoZe35")
			a+=1
```
 
- for da yaptığımız okumaları while ile de yapabiliriz
```python
		liste=[1,2,3,4,5]
		index=0
		while(index<len(liste))
			print("Hangi index:{},Liste:{}".format(index,liste[index]))
			index +=1
```
## _Mantıksal Bağlaçlar_
- _**and operatörü**_:Satır bitene kadar inceler false çıktığı an false yazar false değilse true değer döndürür

- _**or operatörü**_: bütün işlemlerin sonucu false ise false döndürür aksi takdirde hep true döndürür.

- _**not operatörü**_: bir işlemin sonucunu true ise false, false ise true yapar


## _For_

-for elemanlar üzerinde gezinmemize yarar

-for eleman in liste dediğimiz zaman eleman gezineceğimiz değişkendeki her elemena eşit olmuş oluyor
```python
	liste=[1,2,3,4,5]
	for i in liste:
	    print("Eleman",eleman)
	#her elemanı alt alta yazdırmış oluyoruz liste bitene kadar çalışmış oluyor.


```
```python
	toplam=0
	liste=[1,2,3,4,5]
	for eleman in liste:
	    toplam=toplam+eleman
	    print("Toplamları:",toplam)#her döngüde toplamları yazar
	print("Toplamları:",toplam)#döngü bitince toplamlarını yazar

```
```python
	 liste=[(1,2),(3,4),(35,20)]
	#iç içe for yaparakta yazılabilir.
	for i,j in liste
	    print("Sayılarınız i:{} j:{}".format(i,j))
```




## _İf Elif Else blokları_


```python
	a==2
	if(3<a):
		print("sonuc yanlis {}".format(a))
	elif(3>a):
		print("sonucunuz dogru{}".format(a))
	else:
		print("farklı deger veriniz")

```
## Class
- Constructor:
```python
	class calisan:
		def __init(self,isim,soyisim,email,maas):
			self.isim=isim
			self.soyisim=soyisim
			self.maas=maas+"$"
			self.email=isim+soyisim+"@gmail.com"
			

```
- Classlara Variable tanımlama:
```python
	class calisan:
		zam_orani=1.8
		counter=0
		def __init(self,isim,soyisim,email,maas):
			self.isim=isim
			self.soyisim=soyisim
			self.maas=maas+"$"
			self.email=isim+soyisim+"@gmail.com"
			Calisan.counter= calisan.counter+1
			#self ile tanımlama yapamam çünkü classımda eklenen eleman sayısını 1 arttırmam lazım
		def zamOraniself):
			self.maas=self.maas+self.maas*self.zam_orani
			
calisanOguz=calisan("Muhammed oğuzhan","Çiftçi",5000)
print("ilk maas: {}".format(calisanOguz.maas))
calisanOguz.zamOrani()
print("ilk maas: {}".format(calisanOguz.maas))
```
- Class example
```python
	class calisan:
		zam_orani=1.8
		counter=0
		def __init(self,isim,soyisim,email,maas):
			self.isim=isim
			self.soyisim=soyisim
			self.maas=maas+"$"
			self.email=isim+soyisim+"@gmail.com"
			Calisan.counter= calisan.counter+1
			#self ile tanımlama yapamam çünkü classımda eklenen eleman sayısını 1 arttırmam lazım
		def zamOraniself):
			self.maas=self.maas+self.maas*self.zam_orani
			
calisanOguz=calisan("Muhammed oğuzhan","Çiftçi",5000)
calisanYarko=calisan("Yavuz yarkın","Okular",5000)
calisanEmir=calisan("Emirhan","Özen",5000),
####listelere ekleyebilir miyiz sorusunun cevabı
liste[calisan1,calisan2,calisan3]
maxi_maas=-1
index=-1
for each in liste:
	if(each.maas>maxi_maas):
		maxi_maas=each.maas
		index= each
print(maxi_maas
print(liste[index.



```



## Listeler(list)
- Listelerin alt parametrelerini öğrenmek için dir(liste) diyerek alt parametrelerini öğrenebiliriz neler barındığına dair.
- list.append() listeye eleman eklemek için kullanılır.
- list.reverse() listeyi sondan başa sıralar.
- list.remove() içine atılan değeri ilgili listeden kaldırır.


```python
	listenin_ismi[x:y]
	x indeksinden y indeksine kadar olan sayıları almamıza yarar.

```
## Try-except
### syntax error
- Yazım hataları imla hataları gibi düşünebiliriz.
### parantez syntax hataları
- parantezi unutmaya bağlı hatalarda syntax hatası verebilir
### typeError
- eğer ki bir string ve bir integer değeri toplama durumlarında dönüşüm yapmazsak bu hatayı alırız.
### ZeroDivisionError
- paydanın sıfır olduğu durumlar örnektir.
## Demet(tuple)
- Listelerin standrt parantez kullanılarak yazım şeklidir.
- t.count(): içine girilen değerden kaçtane olduğunu gösterir


## _Dict_
```python
	 #sözlüklerde okuma nasıl yapılır
	#tırnak içindekiler anahtar-keys
	#diğer tarafı values olarak geçer
	sözlük={"oğuz":16,"yarkın":35,"emirhan":10,"sude":10}
```

## _Parametre,Metod ve Operatörler_
### range() parametresi
- istediğimiz oranları  belirterek sayı dizisi oluşturu range kelime olarak aralık anlamına gelir.
```python
	    range(0,20)
	    print(*range(0,20))
	#sayılarım 0 dan 20 e 2 atlayarak gitsin demiş oluyorum
	    print(*range(0,20,2))
	#20 den sıfıra kadar 1 atlayarak git demiş oluyorum
	    print(*range(20,0,-1))
	#1den 100 e kadar olan sayıları range ve for kullanarak yazdırma
	    for i in range(1,101):
		print(i)
	#binom mantığıyla yıldız bastırma
	    for i in range(1,10):
		print("*"* i)
```

### .format() parametresi
```python
	toplam=0
	liste=[1,2,3,4,5]
	for eleman in liste:
	    toplam=toplam+eleman
	    print("Toplamları:{} Elemanlar:{}" .format(toplam,eleman))
	    #her döngüde toplamları yazar
```
### break ve continue ifadeleri
- _**break**_: döngü herhangi bir zamanda break ifadesiyle karşılaşınca durduruluyor.Sadece bulunduğu döngüyü sonlandırır.
```python
	i=0
	while(i<10):
	if(i ==5):
	 break
	 print("i:",i)
	 i +=1
```
```python
	liste=[1,2,3,4,5,6,7,8,9]
	for i in liste:
		if(i ==3):
			break
	#i=3 olunca for döngüsü biter
	print(i)
```
- _**continue**_ : Break e kıyasla daha az kullanılır. Etki alanı daha az olduğu için. Dngü herhangi bir yerde continue ile karşılaşırsa döngünün başına döner.
```python
	liste=list(range(0,10))
	for i in liste:
		if (i ==3 or i==5):
			continue
		print("i:",i)
		#3 ve 5 değerlerini görünce döngünün başına gider geriye kalan tüm değerleri bastırır.
```
- _**lambda function**_ : fonksiyonları oluştururken kullandığımız parametreleri kısaltmaya yarar.Program daha akıcı kodlanabilir.
```python
	 def hesapla(x):
           	cikti=x*x
        	return x
	hesapla= lambda x:x*x
	print(hesapla(3))
```

### Kalan bulma operatörü
- x%y
### in operatörü
- **in operatörü**: bir değerin başka birdeğer içerisinde var olup olmadığını kontrol etmemize yarar.
	```python
	"a" in "merhaba"
	#true veya false değer döndürür.
	```
## _Basit Örnekler_
### Bir sayının tek mi çift mi olduğunu bulma
```python
	liste=[34,17,23,68]
	for eleman in liste
	    if(eleman % 2 ==0)
		print("Sayınız({}) çift bir sayıdır.".format(eleman))
	    else:
		print("Sayınız({})çift bir sayı değildir.".format(eleman))
		break
```


























