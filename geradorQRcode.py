import  pyqrcode
import png

url = input('Insira a Url que ai ser transformada em QRcode: \n')

nomearquivo= input('Insira o nome do arquivo que o  Qrcode será salvo: \n')

print('Sua URL é:  \n'+ url)

pyqrcode.create(url).png(f'{nomearquivo}.png', scale=8)

print('Seu Qrcode foi gerado com sucesso !')