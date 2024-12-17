from ..app import app
import requests
from flask import render_template

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id):
    base_url = "https://www.wikidata.org/wiki/Special:EntityData" # FIXME à mettre ailleurs ?
    response = requests.get(f"{base_url}/{id}.json")
    # Création des 3 objets appelés dans le template HTML grâce à Jinja
    status_code = response.status_code
    content = response.headers.get("Content-Type")
    check_type = type(response.json())
    json = response.json()
    return render_template("pages/display_wikidata_content.html", id=id, status_code = status_code, content=content, json=json, check_type=check_type)