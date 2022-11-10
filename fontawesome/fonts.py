import requests

web = open('C:/xampp/htdocs/Futbol-Base/fontawesome/pro.min.txt', 'r')
web = web.read()

div1 = web.split('webfonts/')

cont = 1
while cont < len(div1):
    div2 = div1[cont].split(') ')
    font = div2[0]
    print(font)
    url = 'https://kit-pro.fontawesome.com/releases/v6.1.2/webfonts/'+font
    r = requests.get(url, allow_redirects=True)
    open('C:/xampp/htdocs/Futbol-Base/fontawesome/webfonts/'+font, 'wb').write(r.content)
    cont = cont + 1