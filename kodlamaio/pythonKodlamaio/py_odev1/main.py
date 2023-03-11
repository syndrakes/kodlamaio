### Stringler = metinsel ifadeler
stringIfade = 'sometext' 

### Sayılar = int , float , complex 

theInt = 10 #tamsayı
theFloat = 10.01 #ondalıklı sayı
theComplex = 10j #complex

### Diziler = tuple, list, set, dict, bytes, range

theTuple = ("bir", "iki", "üç") 
# içindeki veriler 'sıralı ve tanımlandıktan sonra değiştirilemez' + tekrar eden veriler olabilir

theList = ["bir", "iki", "üç"]
# içindeki veriler 'sıralı ve tanımlandıktan sonra değiştirilebilir' + tekrar eden veriler olabilir

theDict = {
  "bir": 1,
  "iki": 2,
  "üç":  3
}

# js'deki object literal. 'sıralıdır, değiştirilebilir ve tekrar eden veriler barındırmaz'

theSet = {"bir", "iki", "üç"} 

# içindeki veriler 'sırasız ve tanımlandıktan sonra değiştirilemez' + tekrar eden veriler barındırmaz
# değiştirilemezler fakat içindeki verileri silebilir veya başka veriler ekleyebiliriz

theBytes = b('hello')
# sadece ASCII karakterleri yer alır. başında b harfi ile yazılır. 0-255 arası integer alabilir

for i in range(5): # theRange
    print(i)
# bir döngü tipi. verilen sayıya ulaşana kadar 0'dan birer artırarak verilen sayının bir eksiğine kadar gider.

### Boolean 

theBool = True

# True ya da False değeri alır

#None 

theNone = None


#
##
###
####
######
#######
######
####
###
##
#

 #Courses kısmındaki kursların (içerikleriyle birlikte) hepsi bir değişkene atanmış dizi ve bu dizi döngü kullanılarak içerikleriyle birlikte ayrı bir kısım/parça/link olarak HTML'e konmuş. 
 # Profil kısmındaki her bilgi bizim kayıt olduğumuzda doldurulacak olan değişkenler.



#
##
###
####
######
#######
######
####
###
##
#

# bitir ve devam et butonu :
# 
#  if homeworkDoneButtonClicked === true : 
#     homework = true
#     progress++
#     showNext()

# course'lara enrolling : 
#
#  if courseEnroll === true :
#     try:
#       courseEnrolledPeople.append(user.id, user.name, user.surname)
#       showSuccessMessage()
#     except:
#       showErrorMessage('Bir hata meydana geldi.' + err)
