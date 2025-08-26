from PIL import Image
import sys
import os

def crop_transparencia(img_path):
    img = Image.open(img_path)
    img = img.convert("RGBA")

    bbox = img.getbbox()
    if bbox:
        cropped = img.crop(bbox)
        cropped.save(img_path, "PNG")
        print(f"Imagem cortada salva em: {img_path}")
    else:
        print("Nada para recortar: a imagem está totalmente transparente.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python crop.py <imagem.png>")
        sys.exit(1)

    img_path = sys.argv[1]

    if not os.path.isfile(img_path):
        print("Erro: arquivo não encontrado.")
        sys.exit(1)

    crop_transparencia(img_path)
