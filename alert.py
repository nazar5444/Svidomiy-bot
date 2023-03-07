import requests

headers = {"X-API-Key": "5ebcb2ed4d4fd3d565a3d4ae028c0242c5e583d8"}
link = "https://alerts.com.ua/api/states/{city_id}"

vin_id = requests.get("https://alerts.com.ua/api/states/1", headers=headers)
luck_id = requests.get("https://alerts.com.ua/api/states/2", headers=headers)
dnpr_id = requests.get("https://alerts.com.ua/api/states/3", headers=headers)
don_id = requests.get("https://alerts.com.ua/api/states/4", headers=headers)
zhut_id = requests.get("https://alerts.com.ua/api/states/5", headers=headers)
zak_id = requests.get("https://alerts.com.ua/api/states/6", headers=headers)
kyiv_id = requests.get("https://alerts.com.ua/api/states/9", headers=headers)
lviv_id = requests.get("https://alerts.com.ua/api/states/12", headers=headers)
odes_id = requests.get("https://alerts.com.ua/api/states/14", headers=headers)
plt_id = requests.get("https://alerts.com.ua/api/states/15", headers=headers)
sum_id = requests.get("https://alerts.com.ua/api/states/17", headers=headers)
hrk_id = requests.get("https://alerts.com.ua/api/states/19", headers=headers)
hrsn_id = requests.get("https://alerts.com.ua/api/states/20", headers=headers)
hml_id = requests.get("https://alerts.com.ua/api/states/21", headers=headers)
crk_id = requests.get("https://alerts.com.ua/api/states/22", headers=headers)
crg_id = requests.get("https://alerts.com.ua/api/states/23", headers=headers)

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
if "false" in kyiv_id.text:
    print("Тривога в Київській обл. відсутня.")
else:
    print("Повітряна тревога в Києвській обл.")
if "false" in lviv_id.text:
    print("Тривога в Львівській обл. відсутня.")
else:
    print("Повітряна тривога в Львівській обл.")
if "false" in odes_id.text:
    print("Тривога в Одеській обл. відсутня.")
else:
    print("Повітряна тривога в Одеській обл.")
if "false" in plt_id.text:
    print("Тривога в Полтавській обл. відсутня.")
else:
    print("Повітряна тривога в Полтавській обл.")
if "false" in sum_id.text:
    print("Тривога в Сумській обл. відсутня.")
else:
    print("Повітряна тривога в Сумській обл.")
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
if "false" in crg_id.text:
    print("Тривога в Чернігівській обл. відсутня.")
else:
    print("Повітряна тривога в Черніговській обл.")

TOKEN = "5636715243:AAGoPgmHYLVPiUAEsLe5xQigPN8vCVQNQs8"

maps_list = {
    "1": "https://www.google.com/maps/d/u/0/viewer?mid=1ODeqZzyrD--SR_Kk2QikzzbaplYFIKsq&hl=en_US&ll={latt}%2C{long}&z=17",
    "2": "https://www.google.com/maps/d/u/0/embed?mid=1Umceq4F24ME3kVcHRLhfZ_8IqJAge8Y&ehbc=2E312F&ll={latt}%2C{long}&z=17",
    "3": "https://www.google.com/maps/d/u/0/viewer?mid=1VT7MBpAXCVfa3_ToOzlovSpW5RRO3lWZ&ll={latt}%2C{long}&z=17",
    "4": "https://www.google.com/maps/d/u/0/viewer?mid=1ayYGeIEBnSOPTg6W9pZvi2_o_YXDFqGT&hl=en_US&ll={latt}%2C{long}&z=17",
    "5": "https://www.google.com/maps/d/u/0/viewer?mid=1LrlMgVSGzLfilD0UyZe7e5eplztrzIWG&ll={latt}%2C{long}&z=17",
    "6": "https://www.google.com/maps/d/u/0/viewer?mid=1gHojIW_Zjs_qPe4Aqr_W3OPAjY2t69ym&hl=en_US&ll={latt}%2C{long}&z=17",
    "9": "https://www.google.com/maps/d/u/0/viewer?mid=1nv3QreO1QS5_AmRRNLHXu7u99sKJ6JRR&ll={latt}%2C{long}&z=17",
    "12": "https://www.google.com/maps/d/u/0/viewer?mid=1UDpNf1BkhkvocpOXh8yluxdSRBnP3jRT&hl=en_US&ll={latt}%2C{long}&z=17",
    "14": "https://www.google.com/maps/d/u/0/viewer?mid=1f7Nswyb-hXG0wkFDhyGYFbrANok&hl=ru&fbclid=IwAR3WQENPPGYdz60vu2FC6JHx0JhEI9DRrH_eVYGv8K_rhnIKFAHdBRUHWp4&ll={latt}%2C{long}&z=17",
    "15": "https://www.google.com/maps/d/u/0/viewer?mid=10wBVAAKCTHdPXYODiUbhjTTrJoY&amp%3Bll={latt}%2C{long}&amp%3Bz=12&ll={latt}%2C{long}&z=17",
    "17": "https://www.google.com/maps/d/u/0/viewer?mid=12U9NWrsOmGKyf6zGQvdY2br4USc7OeFx&hl=ru&ll={latt}%2C{long}&z=17",
    "19": "https://www.google.com/maps/d/u/0/viewer?mid=16g3PB0LSZYAsrrAuiXZuxEBVaN0&ll={latt}%2C{long}&z=17",
    "20": "https://www.google.com/maps/d/u/0/viewer?mid=1UvMNOVrvfUsrbXMOocTsq__NToM&ll={latt}%2C{long}&z=17  ",
    "21": "https://www.google.com/maps/d/u/0/viewer?mid=15NSLcOIYzWeSf46DD_Sd8iJJcKM&hl=en_US&ll={latt}%2C{long}&z=17",
    "22": "https://www.google.com/maps/d/u/0/viewer?mid=1pVsKVOq2Uq3Z_UlcjZxffA7mejMyeac&hl=en_US&ll={latt}%2C{long}&z=17",
    "23": "https://www.google.com/maps/d/u/0/viewer?hl=ru&mid=1VJ4yH6VbKhqRP6Z1W3DB7vKhpXM&ll={latt}%2C{long}&z=17"
}

city_list = {"1": "Вінницьку",
             "2": "Волинську",
             "3": "Дніпропетровську",
             "4": "Донецьку",
             "5": "Житомирську",
             "6": "Закарпатьська",
             "9": "Київську",
             "12": "Львівську",
             "14": "Одеську",
             "15": "Полтавську",
             "17": "Сумську",
             "19": "Харківську",
             "20": "Херсонську",
             "21": "Хмельницьку",
             "22": "Черкаську",
             "23": "Чернігівську"
             }
