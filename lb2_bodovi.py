from flask import Flask, url_for, request, redirect, make_response

app = Flask("vjezbe")

@app.put('/putanja_put')
def index():
    return 'putanja_za_bod', 405

@app.get('/putanja_get')
def kajgod():
    samo_jako = request.args.get('samo_jako')
    return 'hocu_bodove', samo_jako

@app.get('/jos_malo_pa_gotovo')
def jos_malo():
    json = {
        "moji_bodovi": 3 
    }
    resp = make_response(json)
    return resp, 201

@app.post('/hocu_sve_bodove')
def ajmoo():
    moji_bodovi = request.json.get('svi_bodovi')
    return 'svi_bodovi', moji_bodovi

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)