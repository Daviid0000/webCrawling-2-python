import requests
from bs4 import BeautifulSoup
import wget
# from os import mkdir
from os import mkdir
import pprint

url = "https://www.netflix.com/ar/"



try:
  def funcionPeticion():
    response = requests.get(url)
    print("¡La petición fue un exito!")
    mkdir("Imágenes")
    soup = BeautifulSoup(response.text, 'html.parser')

    img = soup.find_all('img')

    for imagen in img:
      urlImagen = imagen.get('src')
      print(f"url de imagen: {urlImagen}")

      # descargaImagen = wget.download(urlImagen)
      # print(f"Imagen descargada: {descargaImagen}")

    # pprint.pprint(f"imagen: {img}")
  funcionPeticion()

except requests.exceptions.RequestException:
  print("La petición falló")