from ..app import app
import requests
from flask import render_template


# Index
@app.route("/")
def index():
    return "Ajouter '/retrieve_wikidata/<string:id>' au chemin pour récupérer des items Wikidata au format JSON"

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id: int):
    """ Requête le site wikidata.org et récupère le code HTTP, de type de contenu de la ressource ainsi que le contenu JSON s'il existe. 

    Args:
        id: identifiant unique Wikidata de la ressource

    Returns:
        render_template(): fonction permettant de passer des variables construites dans la route à un templates HTML
    """
    base_url = "https://www.wikidata.org/wiki/Special:EntityData"  # À externaliser ?
    json = None  # Initialisation de la variable json pour éviter les UnboundLocalError dans le cas ou l'identifiant renseigné est invalide.

    try:
        response = requests.get(f"{base_url}/{id}.json")
        status_code = response.status_code  # Récupération du code HTTP
        content = response.headers.get("Content-Type")  # Récupération du Content-Type

        if status_code == 200 and content.startswith("application/json") == True:
            json = response.json()  # Si la requête est réussie et qu'il s'agit bien de contenu au format JSON, on transforme la variable en objet python JSON (dict) 

    except Exception as e:
        print(f"Erreur lors de la récupération des données : {e}") 

    # Passage des variables valides vers le template HTML
    return render_template(
        "pages/display_wikidata_content.html",
        id=id,
        status_code=status_code,
        content=content,
        json=json
    )
