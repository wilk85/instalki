from urllib.request import urlopen
from os.path import basename
import os

# funkcja ta pobiera pliki z wskazanych adresów url, oraz nadaje im nazwę wyciągniętą z url

tinyurl = 'http://tinywall.pados.hu/ccount/click.php?id=3'
freecomm = 'https://freecommander.com/downloads/FreeCommanderXE-32-public_setup.zip'
firefox = 'https://download.mozilla.org/?product=firefox-stub&os=win&lang=pl'
chrome ='https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7BAA48962C-663A-13DD-16AD-F0EDD6584A0A%7D%26lang%3Dpl%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Ddefaultbrowser/update2/installers/ChromeSetup.exe'
tt = 'https://binaries.openttd.org/releases/1.8.0/openttd-1.8.0-windows-win64.exe'

# pobieram pliki wraz z ich rozszerzeniami
def splitter(url):
    # ścieżka do pulpitu
    desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    response = urlopen(url)
    # pobiera pełną ścieżkę razem z rozszerzeniem
    basename = response.url
    splitext = basename.split('/')
    # wydzielam nazwę pliku do ścieżki zapisu splitext[-1]

    file = response.read()
    response.close()
    f2 = open(desktop + '/' + splitext[-1], 'wb')
    print('pobrano' +' '+ splitext[-1])
    f2.write(file)
    f2.close()

splitter(tinyurl)
splitter(freecomm)
splitter(firefox)
splitter(chrome)
splitter(tt)




