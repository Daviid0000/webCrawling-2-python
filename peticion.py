import requests
from bs4 import BeautifulSoup
import wget
from os import mkdir

url = "https://www.netflix.com/ar/"
ruta = "./carpeta"


try:
  def funcionPeticion():
    response = requests.get(url)
    print("¡La petición fue un exito!")
    
    try:
      mkdir(ruta)
      soup = BeautifulSoup(response.text, 'html.parser')

      img = soup.find_all('img')
      if img:
        try:
          for imagen in img:
            urlImagen = imagen.get('src')
            print(f"url de imagen: {urlImagen}")

            wget.download(urlImagen, ruta)
        except requests.exceptions.ConnectionError:
          pass

      else:
        print("Proceso detenido: imagen no encontrada")
    except FileExistsError:
      print("Proceso detenido: La carpeta ya existe")

  funcionPeticion()

except requests.exceptions.ConnectionError:
  print("Proceso detenido: Fallo en la  conexión")
except requests.exceptions.HTTPError:
  print("Error en la solicitud HTTP")