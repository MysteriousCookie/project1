Projekta apraksts:

Šis projekts ir Python skripts, kas izmanto Beautiful Soup un requests bibliotēkas, lai iegūtu datus par Nike apaviem no interneta veikala. Skripts apmeklē dažādas lapas, iegūst apavu nosaukumus un cenas, filtrē saņemtos datus un saglabā tos CSV failā.

Izmantotās bibliotēkas:

Beautiful Soup: Tas ir HTML un XML analizators, kas ļauj ērti izguļt datus no web lapām.
requests: Ar šo bibliotēku tiek veikti HTTP pieprasījumi, lai iegūtu datus no mājas lapas.
time un random: Šīs bibliotēkas tiek izmantotas, lai ieviestu aizkavēšanu starp pieprasījumiem un izvairītos no pārāk lielas slodzes uz serveri.
pandas: Pandas tiek izmantots, lai izveidotu un pārvaldītu DataFrame, kurā tiek saglabāti un filtrēti dati.
re (regulārās izteiksmes): Šī bibliotēka tiek izmantota, lai no cenu virknēm izgūtu skaitliskās vērtības.

Kā izmantot programmu:

Instalēt nepieciešamās bibliotēkas: Pirms skripta palaižat, pārliecinieties, ka jums ir instalētas visas nepieciešamās bibliotēkas. To var izdarīt, izpildot komandu pip install beautifulsoup4 requests pandas.
Palaižiet skriptu: Palaidiet skriptu, lai tas apmeklētu lapas, iegūtu datus un saglabātu tos CSV failā.
Pārbaudiet rezultātus: Pēc skripta izpildes pārbaudiet radīto CSV failu (NIKE_AIR_MAX.csv), kurā ir saglabāti tikai tie apavi, kuriem nosaukums sākas ar "NIKE AIR MAX" un cena ir mazāka par 160.
