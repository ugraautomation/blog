import subprocess
from cisco_inv import *

__author__ = 'b9om'

cisco_obj = {}

cisco_obj[106] = u'Surgutskiy r-n'
cisco_obj[107] = u'g. Nizhnevartovsk'
cisco_obj[108] = u'Nizhnevartovskiy r-n'
cisco_obj[109] = u'Beloyarskiy r-n'
cisco_obj[110] = u'Berozovskiy r-n'
cisco_obj[111] = u'g. Kogalym'
cisco_obj[112] = u'g. Langepas'
cisco_obj[113] = u'g. Megion'
cisco_obj[114] = u'g. Mezhdurechensk Kondinskiy r-n'
cisco_obj[115] = u'g. Nefteyugansk'
cisco_obj[116] = u'Nefteyuganskiy r-n'
cisco_obj[117] = u'g. Nyagan'
cisco_obj[118] = u'Oktyabr\'skiy r-n'
cisco_obj[119] = u'g. Pokachi'
cisco_obj[120] = u'g. Pyt\'-Yakh'
cisco_obj[121] = u'g. Raduzhnyy'
cisco_obj[122] = u'Sovetskiy r-n'
cisco_obj[123] = u'g. Surgut'
cisco_obj[124] = u'g. Uray'
cisco_obj[125] = u'g. Yugorsk'
cisco_obj[21] = u'g. Khanty-Mansiysk'
cisco_obj[29] = u'g.Khanty-Mansiyskiy r-n'

cisco_inv = {}

cisco_inv[1] = 'router'
cisco_inv[34] = 'switch'
cisco_inv[35] = 'apc'

f_failed_adm = open('failed_adm', 'w')
ok_adm = open('ok_adm', 'w')
no_response_adm = open('no_response_adm', 'w')



for city_id, city_name in cisco_obj.items():
    for inv_id, inv_name in cisco_inv.items():
        address = "10.10.%s.%s" % (city_id,inv_id)
        res = subprocess.call(['ping', '-n', '3', address])
        if res == 0:
            print("ping to ", address,' ',city_name,' ',inv_name, " OK")
            ok_adm.write("ping to " + address + ' ' + city_name + ' ' + inv_name + " OK" + '\n' )
            if not inv_id == 35:
                try:
                    data_inv = grab_telnet(address)
                except Exception:
                    break
                ok_adm.write(data_inv)
        elif res == 2:
            print("no response from ",address,' ',city_name,' ',inv_name)
            no_response_adm.write("no response from " + address + ' ' + city_name + ' ' + inv_name + '\n')
        else:
            print("ping to ", address,' ',city_name,' ',inv_name,  " failed!")
            f_failed_adm.write("ping to " + address + ' ' + city_name + ' ' + inv_name + " failed!" + '\n')

ok_adm.close()
no_response_adm.close()
f_failed_adm.close()
