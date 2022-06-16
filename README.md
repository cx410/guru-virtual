# Guru Virtual with Flask and JavaScript
![Guru Virtual](https://i.ibb.co/ZNY7C2g/image-2022-06-16-19-50-36.png)
Penerapan guru virtual ditujukan untuk mengatasi masalah keterpisahan ruang dan waktu antara siswa dan pengajar melalui media komputer. Siswa dapat memperoleh bahan belajar yang sudah dirancang dalam paket-paket pembelajaran yang tersedia dalam guru virtual.

Dalam projek akhir ini kami menggunakan refrensi chatbot di repositori [ini](https://github.com/python-engineer/pytorch-chatbot) menggunakan Flask dan JavaScript.

Dalam projek ini bisa menggunakan 2 opsi deployment:
- Deploy with Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

Nama Kelompok
- Rama Abimanyu                 (19101054)
- Novitasari Nur Ainis Setiani  (19101040)
- Sabda Yagra Ahessa            (19101037)
- Aie Devi Nurainie             (19101062)

## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/cx410/guru-virtual.git
$ cd guru-virtual
$ python -m venv venv
$ venv\Scripts\activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modifikasi `intents.json` untuk mendapatkan pertanyaan dan jawaban yang berbeda

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```
Untuk menjalankan dalam bentuk website, gunakan command berikut.
```
$ (venv) python app.py
```

## Credits:
This repo was used for the frontend code:
https://github.com/hitchcliff/front-end-chatjs
