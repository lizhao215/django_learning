import hashlib
from jiukuaijiy.settings import BASE_DIR
import  os
def fileToObj(filename):
    with open(filename) as fr:
        return eval(fr.read())

provinces = fileToObj(os.path.join(BASE_DIR,'assets/province.json'))
citys = fileToObj(os.path.join(BASE_DIR,'assets/city.json'))
areas = fileToObj(os.path.join(BASE_DIR,'assets/area.json'))

def md(text):
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()
def get_citys_by_id(provice_id):
    return citys[provice_id]
def get_areas_by_id(city_id):
    return areas[city_id]
def get_province_by_id(provinceid):
    for item in provinces:
        if item['id']== str(provinceid):
            return item['name']
def get_area_by_id(cityid,areaid):
    for item in areas[str(cityid)]:
        if item['id']== str(areaid):
            return item['name']
def get_city_by_id(provinceid,cityid):
    for item in citys[str(provinceid)]:
        if item['id'] == str(cityid):
            return item['name']

