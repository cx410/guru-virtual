#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[2]:


engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""

with mic as source:
  print("Silahkan mulai berbicara")
  rekaman = engine.listen(source)
  print("Waktu habis")

  try:
    hasil = engine.recognize_google(rekaman, language = "id-ID")
    print(hasil)
  except engine.unknowValueError:
    print("Maaf tidak terdeteksi, silahkan cobalagi")
  except Exception as e:
    print(e)


# In[ ]:





# In[ ]:




