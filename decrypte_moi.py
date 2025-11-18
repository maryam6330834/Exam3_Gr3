import hashlib
#Référence Notes de cours cryptographie
#Réferences exercices cryptographie
messages_gr3 = {
    "pseudo" : "DebugWoman",
    "messages" : ["Rendez vous au point 8 à midi", "Plan B activer en cas de problème", "Le code maître est 2345"],
    "cryptes" : ["Uhqghc yrxv dx srlqw 1 à plgl", "Sodq E dfwlyhu hq fdv gh sureoèph", "Oh frgh pdîwuh hvw 4567"]
}

def decrypte(message):
    alphabet = " abcdefghijklmnopqrstuvwxyz" and "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
    resultat = ""
    for c in message :
        if c in alphabet :
            cesar_inverser = hashlib.sha256(alphabet.encode()).hexdigest()
            resultat += hashlib.sha256(alphabet.encode()).hexdigest()
        elif alphabet.upper():
            cesar_inverser = hashlib.sha256(alphabet.encode()).hexdigest()

    return resultat

message = messages_gr3
code = decrypte(message )
print(code)