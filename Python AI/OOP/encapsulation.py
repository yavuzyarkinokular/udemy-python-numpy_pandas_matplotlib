# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 06:38:41 2021

@author: yarki
"""
#tanım olarak variable ve methodlara erişimi kısıtlamak demektir.
#---------------------kodda bir hata var bankAccount()takes no arguments
class bankAccount(object):
    def __init(self,money,name,adress):
        #buradaki variable lar global olduğu için erişilebiliyor
        #iki tane alt çizgi koyduğumuz an private olmuş oluyor
        self.__money=money
        self.name=name 
        self.adress=adress


personEge=bankAccount(5000,"Ege Bağçıvan","Narlıdere")
personYarko=bankAccount(4820,"Yavuz Yarkın Okular","Balçova")
personErdem=bankAccount(2324,"Erdem Çankaya","Balçova")      
#erdemin parasını aldı benim parama ekledi
personYarko.money=personYarko.money +personErdem.money
print(personYarko.money)
#private yapınca erişmek istediğimizde AttributeError hatası verir değil değiştirmek görüntülemekte yapılamaz
personYarko.__money #private yaptıktan sonra bu şekilde çağırabiliyoruz içerdeki methodu