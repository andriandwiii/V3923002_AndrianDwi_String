#!/usr/bin/env python
# coding: utf-8

# In[ ]:


nama_lengkap = input ("Masukan Nama Anda : ")

#menghitung jumlah huruf dari nama lengkap
jumlah_huruf = len(nama_lengkap.replace(" ", ""))

#menghitung jumlah huruf vokal dari nama lengkap
huruf_vokal = "aiueoAIUEO"
jumlah_vokal = len({char for char in nama_lengkap if char in huruf_vokal})

#menghitung jumlah huruf konsonan dari nama lengkap
jumlah_konsonan = jumlah_huruf - jumlah_vokal

print("jumlah vokal dari nama lengkap Anda adalah:",jumlah_huruf)
print("jumlah huruf vokal dari nama lengkap Anda adalah:",jumlah_vokal)
print("jumlah huruf konsonan dari nama lengkap Anda adalah:",jumlah_konsonan)

