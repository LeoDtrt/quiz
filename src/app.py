from dash import Dash, html, dcc, Input, Output, State, callback, ALL
from dash.exceptions import PreventUpdate

app = Dash(__name__)
server = app.server

# ------------------------
# Exemple de données du quiz
# ------------------------


quiz_data = [
    {
        "audio": '01_neon.mp3',
        "options": ["Un néon", "Un salon de coiffure", "Quelqu'un qui fait un tatouage", "Une interférence"],
        "answer": "Un néon"
    },
    {
        "audio": '02_cri_herisson.mp3',
        "options": ["Un hérisson", "Une balançoire", "Quelqu'un qui lave une vitre","Au clair de la Lune en sifflant"],
        "answer": "Un hérisson"
    },
    {
        "audio": '03_brosse_a_dent_electrique.mp3',
        "options": ["Une brosse à dent", "Un bourdon", "Une tondeuse à gazon", "De la bouée tractée"],
        "answer": "Une brosse à dent"
    },
    {
        "audio": '04_bruit_de_friture_a_la_poele.mp3',
        "options": ["Une poêle", "Quelqu'un qui fait pipi", "De la pluie", "Une fontaine feng shui"],
        "answer": "Une poêle"
    },
    {
        "audio": '05_roue_velo.mp3',
        "options": ["Un pivert", "Une roue", "Un métronome", "Une montre"],
        "answer": "Une roue"
    },
    {
        "audio": '06_chat_chafouin.mp3',
        "options": ["Un zozo jouant à un jeu de voiture", "Un chat"],
        "answer": "Un chat"
    },
    {
        "audio": '07_bruit_de_souris.mp3',
        "options": ["Une souris", "Une ampoule qui se dévisse", "Un papillon"],
        "answer": "Une souris"
    },
    {
        "audio": '08_vague_galet_etretat.mp3',
        "options": ["Un feu d'artifice", "La mer", "Un éclair", "Un tir à la carabine"],
        "answer": "La mer"
    },
    {
        "audio": '09_hyene_qui_rigole.mp3',
        "options": ["Une hyène", "Un ado", "Un orang-outan", "Un hibou"],
        "answer": "Une hyène"
    },
    {
        "audio": '10_faisan.mp3',
        "options": ["Un faisan", "Une grenouille", "Quelqu'un qui à le hoquet"],
        "answer": "Glace qui craque"
    }
]

def question(elem):

    id = int(elem['audio'].split("_")[0])

    layout = html.Div([
        html.H2(f"Son N°{id} :", className='title-son'),
        html.Audio(src=f"/assets/mp3/{elem['audio']}", controls=True, className='son'),
        dcc.RadioItems(
            id={'index':id,'type':'radio'}, 
            options=elem['options'],
            labelStyle={
                'display': 'flex',
                'alignItems': 'flex-start',
                'gap': '8px',
                'margin': '5px 0'
            },
            inputStyle={'marginRight': '8px'},
            className='radio'
        )
    ], className='container')
    
    return layout


# ------------------------
# Layout principal
# ------------------------
app.layout = html.Div([
    html.H1("🎧 Quiz Sonore", style={"textAlign": "center"}),
    html.Div([question(elem) for elem in quiz_data]),
    html.Button('Valider', id='btn-valide', className='button'),
    html.Div(id='resultats', children='lala', className='container'),
    dcc.Store(id="user-answers", data={})
])



@callback(
    Output('resultats','children',allow_duplicate=True),
    Input('btn-valide','n_clicks'),
    State({'index':ALL,'type':'radio'}, 'value'),
    prevent_initial_call=True
)
def update(btn, values):
    if btn is None:
        raise PreventUpdate
    else:
        print(values)
        reponses = [v for v in values if v is not None]
        resultats = ''
        if len(reponses)>0:
            resultats = ', '.join(reponses)
            print(resultats)
        return resultats



if __name__ == '__main__':
    app.run_server(debug=True)