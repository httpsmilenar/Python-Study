#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import playsound as ps

url = r"C:\Users\PC\Documents\Study\Python Study\audio.mpeg"
ps.playsound(url)
try:
    ps("/audio.mpeg")
    print("rodou")
except:
    print("num rodou")