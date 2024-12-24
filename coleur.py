import cv2
import os

# Fonction pour convertir une image en noir et blanc
def convert_to_black_and_white(image_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Vérifier si l'image a été chargée correctement
    if image is None:
        print(f"Erreur : Impossible de charger l'image {image_path}")
        return

    # Convertir l'image en noir et blanc (échelle de gris)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Générer le chemin de sortie dans le même dossier avec un nouveau nom
    folder, filename = os.path.split(image_path)
    name, ext = os.path.splitext(filename)
    output_path = os.path.join(folder, f"{name}_bw{ext}")

    # Sauvegarder l'image noir et blanc
    cv2.imwrite(output_path, gray_image)

    print(f"L'image noir et blanc a été sauvegardée à : {output_path}")

# Demander le chemin de l'image à l'utilisateur
image_path = input("Entrez le chemin de l'image à convertir : ")

# Appeler la fonction de conversion
convert_to_black_and_white(image_path)
