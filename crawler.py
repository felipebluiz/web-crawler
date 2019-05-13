import urllib.request

content = urllib.request.urlopen("https://www.climatempo.com.br/previsao-do-tempo/cidade/424/carapicuiba-sp").read()
content = str(content)

find = 'id="tempMax0">'
position = int(content.index(find) + len(find))
max = content[position : position  + 2]

find = 'id="tempMin0">'
position = int(content.index(find) + len(find))
min = content[position : position  + 2]

print("Temp. Máxima: " + max)
print("Temp. Mínima: " + min)
