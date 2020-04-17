import requests
import re
import random
url = "http://earn500.fun/m_data.php"
s = """SumonKabirNazmulArafatAkbarSajjadSohailKosikBibaJarifM
irjaRabeyaSlmanSabiqRubiyaNusratNahidHasanSirazamnMuniraswanS
omanjanBigyaniAnikhAriteshPrJahanaraKanizMirjaHasnaInzamaulSh
arminTaziaAfrinShornaSabrinaTaimurRizwanIpshitaTasnimSnehaNazi
nMaksudaSultanaNilimaawarParvikPuspanshuDebtanuSochinSowmikDi
ptarsikaNoinaSriyamiAtyamajaKoushukiSomdeeptiSairatiRiptyRipt
aFarbinPrajuktiDirghayeeRakibSakibNomanAbduSanjidaRafikKarimJub
airAhmedBillasSamiyaNondiniPutkiSumaiyaSahbeaKdhadkKDhjadkfOdia
hdkKdhakdfhLOdiajdfkLdkahdkKdhakdfjLkdfhakdfjLidfjakdfTlaksdjfi
oQewauflskWTonuzaMayshaBushraHannahIsratjdflaskEduraoRweifjaTlks
dFarinAbdullahAhmedDurjoyAbdulYuraIslamoiUwejflRokyNusratIaskdf
jwOeiursiPldjflaAskdSrthawDeiofjDaliyaAfhanSamhaSamantaTamalSkdFhaslKjdf"""
nmb = ['3','5','6','7','8','9']
occs = ['Student','Teacher','Nothing','ছাত্র','বেকার',]
names = re.sub( r"([A-Z])", r" \1", s).split()
for _ in range(len(names)):
    nm = '01'+str(nmb[random.randint(0,5)])+str(random.randint(00000000,99999999))
    email = names[_].lower()+'@gmail.com'
    ps = names[_]+nm[4:]
    ocs = occs[random.randint(0,2)]
    requests.post(url,allow_redirects=False,data={
        "user": names[_],
        "email": email,
        "phone":nm,
        "pass":ps,
        "occupation":ocs
    })
    print(f'Seding name={names[_]}, email={email}, phone={nm} password={ps}, occupation={ocs}')