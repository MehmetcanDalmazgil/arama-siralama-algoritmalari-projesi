
def lineer_arama(dizi, sayi):
   islem = 0
   for i in range(len(dizi)):
      islem = islem + 1
      if dizi[i] == sayi:
         islem = islem + 1
         return i,islem
   return -1,islem

def binary_arama(dizi, alt, ust, sayi,islem):
   if ust >= alt:
      islem = islem + 1
      orta = (ust + alt) // 2
      if dizi[orta] == sayi: 
         islem = islem + 1
         return orta,islem
      elif dizi[orta] > sayi:
         islem = islem + 1
         return binary_arama(dizi, alt, ust - 1, sayi,islem)
      else:
         islem = islem + 1
         return binary_arama(dizi, orta + 1, ust, sayi,islem)
   else:
      islem = islem + 1
      return -1,islem
   
def insertion_sort(dizi,islem):

   for i in range(1, len(dizi)):
      key = dizi[i]
      islem = islem + 1
      j = i - 1
      islem = islem + 1
      while j >= 0 and key < dizi[j]:
         dizi[j + 1] = dizi[j]
         j -= 1
         islem = islem + 1
      dizi[j + 1] = key
      islem = islem + 1
   islem = islem + 1
   return islem 

   
def merge_sort(dizi, sol_index, sag_index,islem):
   if sol_index >= sag_index:
      islem = islem + 1
      return islem

   orta = (sol_index + sag_index)//2
   islem = islem + 1
   islem = merge_sort(dizi, sol_index, orta,islem)
   islem = merge_sort(dizi, orta + 1, sag_index,islem)
   islem = merge(dizi, sol_index, sag_index, orta,islem)

   islem = islem + 1
   return islem

def merge(dizi, sol_index, sag_index, orta,islem):
   
   sol_gecici = dizi[sol_index:orta + 1]
   sag_gecici = dizi[orta+1:sag_index+1]
   sol_gecici_index = 0
   sag_gecici_index = 0
   sort_index = sol_index
   islem = islem + 5

   while sol_gecici_index < len(sol_gecici) and sag_gecici_index < len(sag_gecici):

      if sol_gecici[sol_gecici_index] <= sag_gecici[sag_gecici_index]:
         dizi[sort_index] = sol_gecici[sol_gecici_index]
         sol_gecici_index = sol_gecici_index + 1
         islem = islem + 2

      else:
         dizi[sort_index] = sag_gecici[sag_gecici_index]
         sag_gecici_index = sag_gecici_index + 1
         islem = islem + 2

      sort_index = sort_index + 1
      islem = islem + 1

   while sol_gecici_index < len(sol_gecici):
      dizi[sort_index] = sol_gecici[sol_gecici_index]
      sol_gecici_index = sol_gecici_index + 1
      sort_index = sort_index + 1
      islem = islem + 3

   while sag_gecici_index < len(sag_gecici):
      dizi[sort_index] = sag_gecici[sag_gecici_index]
      sag_gecici_index = sag_gecici_index + 1
      sort_index = sort_index + 1
      islem = islem + 3
   islem = islem + 1
   return islem 


def heapify(dizi, n, i,islem):
   en_buyuk = i
   sol = 2 * i + 1
   sag = 2 * i + 2
   islem = islem + 3

   if sol < n and dizi[en_buyuk] < dizi[sol]:
      en_buyuk = sol
      islem = islem + 1

   if sag < n and dizi[en_buyuk] < dizi[sag]:
      en_buyuk = sag
      islem = islem + 1

   if en_buyuk != i:
      dizi[i], dizi[en_buyuk] = dizi[en_buyuk], dizi[i]
      islem = islem + 1
      islem = heapify(dizi, n, en_buyuk,islem)
   
   islem = islem + 1
   return islem

def heap_sort(dizi,islem):
   uzunluk = len(dizi)
   islem = islem + 1

   for i in range(uzunluk // 2 - 1, -1, -1):
      islem = islem + 1
      islem = heapify(dizi, uzunluk, i,islem)

   for j in range(uzunluk - 1, 0, -1):
      dizi[j], dizi[0] = dizi[0], dizi[j]
      islem = islem + 2
      islem = heapify(dizi, j, 0,islem)
   
   islem = islem + 1
   return islem


def bolumleme(dizi, dusuk, yuksek,islem):
   i = (dusuk -1)
   pivot = dizi[yuksek]
   islem = islem + 2

   for j in range(dusuk, yuksek):
      islem = islem + 1
      if dizi[j] <= pivot:
         i = i+ 1
         dizi[i], dizi[j] = dizi[j], dizi[i]
         islem = islem + 2

   dizi[i + 1], dizi[yuksek] = dizi[yuksek], dizi[i + 1]
   islem = islem + 3
   return (i + 1),islem

def quick_sort(dizi, dusuk, yuksek,islem):

   if len(dizi) == 1:
      islem = islem + 1
      return islem

   if dusuk < yuksek:
      pi,islem = bolumleme(dizi, dusuk, yuksek,islem)
      islem = quick_sort(dizi, dusuk, pi - 1,islem)
      islem = quick_sort(dizi, pi + 1, yuksek,islem)
   
   return islem 


def counting_sort(dizi, max_sayi):
   islem = 0
   sayac = [0] * (max_sayi + 1)
   islem = islem + 1
   for i in dizi:
      sayac[i] += 1
      islem = islem + 1

   index = 0
   islem = islem + 1
   for i in range(len(sayac)):
      while 0 < sayac[i]:
         dizi[index] = i
         index += 1
         sayac[i] -= 1
         islem = islem + 3
   
   return islem 


def bucket_sort(dizi):
   islem = 0
   max_sayi = max(dizi)
   boyut = max_sayi / len(dizi)
   bucket_list = []
   islem = islem + 3
   for x in range(len(dizi)):
      bucket_list.append([])
      islem = islem + 1

   for i in range(len(dizi)):
      j = int(dizi[i] / boyut)
      islem = islem + 1
      if j != len(dizi):
         bucket_list[j].append(dizi[i])
         islem = islem + 1
      else:
         bucket_list[len(dizi) - 1].append(dizi[i])
         islem = islem + 1

   for z in range(len(dizi)):
      islem = islem + 1
      insertion_sort(bucket_list[z],islem)
      
   sonuc_list = []
   islem = islem + 3
   for x in range(len(dizi)):
      sonuc_list = sonuc_list + bucket_list[x]
      islem = islem + 3
   
   islem = islem + 1
   return sonuc_list,islem
   

def radix_sort(dizi):
   islem = 0
   mod=10
   islem = islem + 1
   def key_factory(digit, mod):
      def key(dizi, index):
         return ((dizi[index] // (mod ** digit)) % mod)
      return key

   max_sayi = max(dizi)
   exp = 0
   islem = islem + 2
   while mod ** exp <= max_sayi:
      dizi,islem = counting_sort_radix(dizi, mod - 1, key_factory(exp, mod),islem)
      exp = exp + 1
      islem = islem + 4

   return dizi,islem

def counting_sort_radix(dizi, max_sayi, key,islem):

   c = [0] * (max_sayi + 1)
   islem = islem + 1
   for i in range(len(dizi)):
      c[key(dizi, i)] = c[key(dizi, i)] + 1
      islem = islem + 1

   c[0] = c[0] - 1
   islem = islem + 1
   for i in range(1, max_sayi + 1):
      c[i] = c[i] + c[i - 1]
      islem = islem + 1

   sonuc = [None] * len(dizi)
   islem = islem + 1
   for i in range(len(dizi) - 1, -1, -1):
      sonuc[c[key(dizi, i)]] = dizi[i]
      c[key(dizi, i)] = c[key(dizi, i)] - 1
      islem = islem + 2

   islem = islem + 1
   return sonuc,islem