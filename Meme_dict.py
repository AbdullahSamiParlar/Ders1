print("Meme_dict'e hoşgeldin!")
meme_dict = {
            "MEME":"İngilizce bir kelime. Şaka unsuru olan herşey",
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NOOB":"Acemi",
            "PRO":"Profesyonal",
            "EZ":"Kazanınca dalga geç",
            "KIDDO":"Tabiri caizse velet",

            
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Sözlükte bulunamadı")
