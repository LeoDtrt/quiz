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
        "answer": "Un faisan"
    }
]

def question(elem):

    id = get_id(elem)

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

def get_id(elem):
    return int(elem['audio'].split("_")[0])

def space():
    return html.Span('...', style={'color':'white'})

def img(status, gif=False, w=30):
    if gif:
        extension = 'gif'
    else:
        extension = 'png'
    return html.Img(src=f'/assets/img/{status}.{extension}', style={'width': f'{w}px', 'height':f'{w}px'})


def build_resultat(elem, value):
    
    id = get_id(elem)
    
    res = html.Li([img('nok'), html.Span([f'Son N°{id} : La bonne réponse était {elem['answer']}'], className='reponse')], className='li-custom')
    num = 0
    if value is not None:
        if value == elem['answer']:
            res = html.Li([img('ok'), html.Span([f'Son N°{id} : {elem['answer']}'], className='reponse'), img('firework', gif=True)], className='li-custom')
            num = 1
    return res, num


# ------------------------
# Layout principal
# ------------------------
app.layout = html.Div([
    html.H1("🎧 Quiz Sonore", style={"textAlign": "center"}),
    html.Div([question(elem) for elem in quiz_data]),
    html.Button('Valider', id='btn-valide', className='button'),
    html.Div(id='resultats', className='container', style={'display':'none'})
])



@callback(
    Output('resultats','children', allow_duplicate=True),
    Output('resultats','style', allow_duplicate=True),
    Input('btn-valide','n_clicks'),
    State({'index':ALL,'type':'radio'}, 'value'),
    prevent_initial_call=True
)
def update(btn, values):
    if btn is None:
        raise PreventUpdate
    else:
        n = len(quiz_data)
        reponses = []
        score = 0
        for i in range(n):
            res, num = build_resultat(quiz_data[i], values[i])
            reponses.append(res)
            score += num
        

        if score > 7:
            img_score = img('firework', w=45)
        elif score > 4:
            img_score = img('strong', w=45)
        else:
            img_score = img('broke', w=50)            
        layout = html.Div([
            html.Div([html.H2(f"Résultats : {score}/10"), space(), img_score], style={'display':'flex'}),
            html.Ul(reponses, className='liste-custom')
        ])
        style = {'display':'block'}
        return layout, style



if __name__ == '__main__':
    app.run_server(debug=True)