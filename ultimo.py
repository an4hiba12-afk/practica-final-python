from urllib import request[cite: 1]
from urllib.error import URLError[cite: 1]

lpo = ["coño", "bobo", "culiao", "pinche", "estupido", "estupida"][cite: 1]


def verificar_web(url):[cite: 1]
    try:[cite: 1]
        f = request.urlopen(url)[cite: 1]
    except URLError:[cite: 1]
        return "¡La url " + url + " no existe!"[cite: 1]
    else:[cite: 1]
        aux = f.read()[cite: 1]
        contenido = aux.split()[cite: 1]
        palabras_encontradas = [][cite: 1]
        cantidad_po = 0[cite: 1]
        for l in lpo:[cite: 1]
            for con in contenido:[cite: 1]
                if l in con.decode():[cite: 1]
                    palabras_encontradas.append(l)[cite: 1]

        return palabras_encontradas[cite: 1]


url = "https://es.wiktionary.org/wiki/Wikcionario:Insultos_regionales"[cite: 1]
print("\n-------------------------------------\n")[cite: 1]
print("\nInforme de sitio:")[cite: 1]
print(verificar_web(url))[cite: 1]