import dash
from dash import html, dcc, Input, Output, State, callback

import os

print(os.getcwd())

chemin = f"{os.getcwd()}\\assets\\mp3"

# Liste uniquement les fichiers (ignore les dossiers)
mp3 = [f for f in os.listdir(chemin) if os.path.isfile(os.path.join(chemin, f))]



app = dash.Dash(__name__)
server = app.server

# ------------------------
# Exemple de données du quiz
# ------------------------


quiz_data = [
    {
        "audio": mp3[0],
        "options": ["Un néon", "Un salon de coiffure", "Quelqu'un qui fait un tatouage", "Une interférence"],
        "answer": "Un néon"
    },
    {
        "audio": mp3[1],
        "options": ["Un hérisson", "Une balançoire", "Quelqu'un qui lave une vitre","Au clair de la Lune en sifflant"],
        "answer": "Un hérisson"
    },
    {
        "audio": mp3[2],
        "options": ["Une brosse à dent", "Un bourdon", "Une tondeuse à gazon", "De la bouée tractée"],
        "answer": "Une brosse à dent"
    },
    {
        "audio": mp3[3],
        "options": ["Une poêle", "Quelqu'un qui fait pipi", "De la pluie", "Une fontaine feng shui"],
        "answer": "Une poêle"
    },
    {
        "audio": mp3[4],
        "options": ["Un pivert", "Une roue", "Un métronome", "Une montre"],
        "answer": "Une roue"
    },
    {
        "audio": mp3[5],
        "options": ["Un zozo jouant à un jeu de voiture", "Un chat"],
        "answer": "Un chat"
    },
    {
        "audio": mp3[6],
        "options": ["Une souris", "Une ampoule qui se dévisse", "Un papillon"],
        "answer": "Une souris"
    },
    {
        "audio": mp3[7],
        "options": ["Un feu d'artifice", "La mer", "Un éclair", "Un tir à la carabine"],
        "answer": "La mer"
    },
    {
        "audio": mp3[8],
        "options": ["Une hyène", "Un ado", "Un orang-outan", "Un hibou"],
        "answer": "Une hyène"
    },
    {
        "audio": mp3[9],
        "options": ["Un faisan", "Une grenouille", "Quelqu'un qui à le hoquet"],
        "answer": "Glace qui craque"
    }
]

def question(elem):

    id = int(elem['audio'].split("_")[0])

    layout = html.Div([
        html.Div([
            html.H2(f"Son N°{id} :", className='titre-son'),
            html.Audio(src=f"/assets/mp3/{elem['audio']}", controls=True)
        ], className='son'),
        dcc.RadioItems(options=elem['options'], className='radio'),
        html.Button('Valider', className='button')
    ], className='container')
    
    return layout


# ------------------------
# Layout principal
# ------------------------
app.layout = html.Div([
    html.H1("🎧 Quiz Sonore", style={"textAlign": "center"}),
    html.Div([question(elem) for elem in quiz_data]),
    dcc.Store(id="user-answers", data={})
])


if __name__ == '__main__':
    app.run_server(debug=True)