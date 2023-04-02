import requests

headers = {"X-API-Key": "5ebcb2ed4d4fd3d565a3d4ae028c0242c5e583d8"}
link = "https://alerts.com.ua/api/states/{city_id}"

vin_id = requests.get("https://alerts.com.ua/api/states/1", headers=headers)
luck_id = requests.get("https://alerts.com.ua/api/states/2", headers=headers)
dnpr_id = requests.get("https://alerts.com.ua/api/states/3", headers=headers)
don_id = requests.get("https://alerts.com.ua/api/states/4", headers=headers)
zhut_id = requests.get("https://alerts.com.ua/api/states/5", headers=headers)
zak_id = requests.get("https://alerts.com.ua/api/states/6", headers=headers)
zap_id = requests.get("https://alerts.com.ua/api/states/7", headers=headers)
ivano_id = requests.get("https://alerts.com.ua/api/states/8", headers=headers)
kyiv_id = requests.get("https://alerts.com.ua/api/states/9", headers=headers)
crop_id = requests.get("https://alerts.com.ua/api/states/10", headers=headers)
lug_id = requests.get("https://alerts.com.ua/api/states/11", headers=headers)
lviv_id = requests.get("https://alerts.com.ua/api/states/12", headers=headers)
muk_id = requests.get("https://alerts.com.ua/api/states/13", headers=headers)
odes_id = requests.get("https://alerts.com.ua/api/states/14", headers=headers)
plt_id = requests.get("https://alerts.com.ua/api/states/15", headers=headers)
rivn_id = requests.get("https://alerts.com.ua/api/states/16", headers=headers)
sum_id = requests.get("https://alerts.com.ua/api/states/17", headers=headers)
ter_id = requests.get("https://alerts.com.ua/api/states/18", headers=headers)
hrk_id = requests.get("https://alerts.com.ua/api/states/19", headers=headers)
hrsn_id = requests.get("https://alerts.com.ua/api/states/20", headers=headers)
hml_id = requests.get("https://alerts.com.ua/api/states/21", headers=headers)
crk_id = requests.get("https://alerts.com.ua/api/states/22", headers=headers)
crg_id = requests.get("https://alerts.com.ua/api/states/23", headers=headers)
chern_id = requests.get("https://alerts.com.ua/api/states/24", headers=headers)

if "false" in vin_id.text:
    print("Тривога в Вінницькій обл. відсутня.")
else:
    print("Повітряна тривога в Вінницькій обл.")
if "false" in luck_id.text:
    print("Тривога в Волинській обл. відсутня.")
else:
    print("Повітряна тривога в Волинській обл.")
if "false" in dnpr_id.text:
    print("Тривога в Дніпропетровській обл. відсутня.")
else:
    print("Повітряна тривога в Дніпропетровській обл.")
if "false" in don_id.text:
    print("Тривога в Донецькій обл. відсутня.")
else:
    print("Повітряна тревога в Донецькій обл.")
if "false" in zhut_id.text:
    print("Тривога в Житомирській обл. відсутня.")
else:
    print("Повітряна тривога в Житомирській обл.")
if "false" in zak_id.text:
    print("Тривога в Закарпатській обл. відсутня.")
else:
    print("Повітряна тривога в Закарпатській обл.")
if "false" in zap_id.text:
    print("Тривога в Запорізькій обл. відсутня.")
else:
    print("Повітряна тривога в Запорізькій обл.")
if "false" in ivano_id.text:
    print("Тривога в Івано-Франківській обл. відсутня.")
else:
    print("Повітряна тривога в івано-Франківській обл.")
if "false" in kyiv_id.text:
    print("Тривога в Київській обл. відсутня.")
else:
    print("Повітряна тревога в Києвській обл.")
if "false" in crop_id.text:
    print("Тривога в Кропивницькій обл. відсутня.")
else:
    print("Повітряна тривога в Кропивницькій обл.")
if "false" in lug_id.text:
    print("Тривога в Луганській обл. відсутня.")
else:
    print("Повітряна тривога в Луганській обл.")
if "false" in lviv_id.text:
    print("Тривога в Львівській обл. відсутня.")
else:
    print("Повітряна тривога в Львівській обл.")
if "false" in muk_id.text:
    print("Тривога в Миколаївській обл. відсутня.")
else:
    print("Повітряна тривога в Миколаївській обл.")
if "false" in odes_id.text:
    print("Тривога в Одеській обл. відсутня.")
else:
    print("Повітряна тривога в Одеській обл.")
if "false" in plt_id.text:
    print("Тривога в Полтавській обл. відсутня.")
else:
    print("Повітряна тривога в Полтавській обл.")
if "false" in rivn_id.text:
    print("Тривога в Рівненській обл. відсутня.")
else:
    print("Повітряна тривога в Рівненській обл.")
if "false" in sum_id.text:
    print("Тривога в Сумській обл. відсутня.")
else:
    print("Повітряна тривога в Сумській обл.")
if "false" in ter_id.text:
    print("Тривога в Тернопільській обл. відсутня.")
else:
    print("Повітряна тривога в Тернопільській обл.")
if "false" in hrk_id.text:
    print("Тривога в Харківській обл. відсутня.")
else:
    print("Повітряна тривога в Харковській обл.")
if "false" in hrsn_id.text:
    print("Тривога в Херсонській обл. відсутня.")
else:
    print("Повітряна тривога в Херсонській обл.")
if "false" in hml_id.text:
    print("Тривога в Хмельницькій обл. відсутня.")
else:
    print("Повітряна тривога в Хмельницькій обл.")
if "false" in crk_id.text:
    print("Тривога в Черкаській обл. відсутня.")
else:
    print("Повітряна тривога в Черкаській обл.")
if "false" in chern_id.text:
    print("Тривога в Чернівецькій обл. відсутня.")
else:
    print("Повітряна тривога в Чернівецькій обл.")
if "false" in crg_id.text:
    print("Тривога в Чернігівській обл. відсутня.")
else:
    print("Повітряна тривога в Черніговській обл.")

maps_list = {
    "1": "https://www.google.com/maps/d/u/0/viewer?mid=1ODeqZzyrD--SR_Kk2QikzzbaplYFIKsq&hl=en_US&ll={latt}%2C{long}&z=17",
    "2": "https://www.google.com/maps/d/u/0/embed?mid=1Umceq4F24ME3kVcHRLhfZ_8IqJAge8Y&ehbc=2E312F&ll={latt}%2C{long}&z=17",
    "3": "https://www.google.com/maps/d/u/0/viewer?mid=1VT7MBpAXCVfa3_ToOzlovSpW5RRO3lWZ&ll={latt}%2C{long}&z=17",
    "4": "https://www.google.com/maps/d/u/0/viewer?mid=1ayYGeIEBnSOPTg6W9pZvi2_o_YXDFqGT&hl=en_US&ll={latt}%2C{long}&z=17",
    "5": "https://www.google.com/maps/d/u/0/viewer?mid=1LrlMgVSGzLfilD0UyZe7e5eplztrzIWG&ll={latt}%2C{long}&z=17",
    "6": "https://www.google.com/maps/d/u/0/viewer?mid=1gHojIW_Zjs_qPe4Aqr_W3OPAjY2t69ym&hl=en_US&ll={latt}%2C{long}&z=17",
    "7": "https://ukryttya.zp.gov.ua/?fbclid=IwAR189tJBdZToFCfnb1wWWQiPQCDWIsnoj-nc7OSk_xQIUKLcVCl9L0C06n4",
    "8": "https://www.google.com/maps/d/u/0/viewer?fbclid=IwAR3FGxT4fJgstzugZw1KtmJj2oTmOWXBbiLHaw_OFhXsSxT7iBYtmVqQhDM&mid=1ikN1D3nl3Pqmdzhl2pmimebPSiwopDE&ll={latt}%2C{long}&z=17",
    "9": "https://www.google.com/maps/d/u/0/viewer?mid=1nv3QreO1QS5_AmRRNLHXu7u99sKJ6JRR&ll={latt}%2C{long}&z=17",
    "10": "https://www.google.com/maps/d/u/0/viewer?mid=1Qyxbt-UOgTpGFBuyiCsOrTe3ounflaE_&fbclid=IwAR3urY_8ThpGFCIk0cxgQOxswR_6LIH7f-mhnoV90JzjOIC7NCn5PQUXF4Y&ll={latt}%2C{long}&z=17",
    "11": "https://www.google.com/maps/d/u/0/viewer?mid=1x-b6-vkSBG0bDk9rVIxnJs7kY-Kt4J7Z&hl=ru&ll=48.69639692217959%2C{long}&z=17",
    "12": "https://www.google.com/maps/d/u/0/viewer?mid=1UDpNf1BkhkvocpOXh8yluxdSRBnP3jRT&hl=en_US&ll={latt}%2C{long}&z=17",
    "13": "https://www.google.com/maps/d/u/0/viewer?mid=1DD_gnR2xEeidXqh0UF4tmPvVzlX1OdzQ&hl=ru&ll=46.94075430633404%2C{long}&z=17",
    "14": "https://www.google.com/maps/d/u/0/viewer?mid=1f7Nswyb-hXG0wkFDhyGYFbrANok&hl=ru&fbclid=IwAR3WQENPPGYdz60vu2FC6JHx0JhEI9DRrH_eVYGv8K_rhnIKFAHdBRUHWp4&ll={latt}%2C{long}&z=17",
    "15": "https://www.google.com/maps/d/u/0/viewer?mid=10wBVAAKCTHdPXYODiUbhjTTrJoY&amp%3Bll={latt}%2C{long}&amp%3Bz=12&ll={latt}%2C{long}&z=17",
    "16": "https://www.google.com/maps/d/u/0/viewer?mid=137hE80p26hMRz3AVkSR9RJRrt77Jbvo&ll=50.60140202940377%2C{long}&z=17",
    "17": "https://www.google.com/maps/d/u/0/viewer?mid=12U9NWrsOmGKyf6zGQvdY2br4USc7OeFx&hl=ru&ll={latt}%2C{long}&z=17",
    "18": "https://giscid.maps.arcgis.com/apps/View/index.html?appid=cf66288d0b34497ba8530415606f6a5e&fbclid=IwAR1vvpzbAydauiYTqIPHAk477khuXRQL1LcdB7dnxUqi_VN4Hx1vmjusWXo",
    "19": "https://www.google.com/maps/d/u/0/viewer?mid=16g3PB0LSZYAsrrAuiXZuxEBVaN0&ll={latt}%2C{long}&z=17",
    "20": "https://www.google.com/maps/d/u/0/viewer?mid=1UvMNOVrvfUsrbXMOocTsq__NToM&ll={latt}%2C{long}&z=17",
    "21": "https://www.google.com/maps/d/u/0/viewer?mid=15NSLcOIYzWeSf46DD_Sd8iJJcKM&hl=en_US&ll={latt}%2C{long}&z=17",
    "22": "https://www.google.com/maps/d/u/0/viewer?mid=1pVsKVOq2Uq3Z_UlcjZxffA7mejMyeac&hl=en_US&ll={latt}%2C{long}&z=17",
    "23": "https://www.google.com/maps/d/u/0/viewer?mid=1oYvZrZg3VwPbRWtabOPfaMyI6Bk&hl=en_US&ll={latt}%2C{long}&z=17",
    "24": "https://www.google.com/maps/d/u/0/viewer?hl=ru&mid=1VJ4yH6VbKhqRP6Z1W3DB7vKhpXM&ll={latt}%2C{long}&z=17",
}

city_list = {"1": "Вінницьку",
             "2": "Волинську",
             "3": "Дніпропетровську",
             "4": "Донецьку",
             "5": "Житомирську",
             "6": "Закарпатьську",
             "7": "Запорізьку",
             "8": "Івано-Франківську",
             "9": "Київську",
             "10": "Кропивницьку",
             "11": "Луганську",
             "12": "Львівську",
             "13": "Миколаївську",
             "14": "Одеську",
             "15": "Полтавську",
             "16": "Рівненську",
             "17": "Сумську",
             "18": "Тернопільську",
             "19": "Харківську",
             "20": "Херсонську",
             "21": "Хмельницьку",
             "22": "Черкаську",
             "23": "Чернівецьку",
             "24": "Чернігівську",
             }

city_list_alert = {"1": "Вінницькій",
                   "2": "Волинській",
                   "3": "Дніпропетровській",
                   "4": "Донецькій",
                   "5": "Житомирській",
                   "6": "Закарпатьській",
                   "7": "Запорізькій",
                   "8": "Івано-Франківській",
                   "9": "Київській",
                   "10": "Кропивницькій",
                   "11": "Луганській",
                   "12": "Львівській",
                   "13": "Миколаївській",
                   "14": "Одеській",
                   "15": "Полтавській",
                   "16": "Рівненській",
                   "17": "Сумській",
                   "18": "Тернопільській",
                   "19": "Харківській",
                   "20": "Херсонській",
                   "21": "Хмельницькій",
                   "22": "Черкаській",
                   "23": "Чернівецькій",
                   "24": "Чернігівській",
                   }
