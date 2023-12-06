from flask import Flask, url_for, redirect, request, make_response, render_template, session

app = Flask("Prva flask aplikacija")



app.secret_key = '_5#y2L"F4Q8z-n-xec]/'

@app.get('/pocetna_stranica')
def pocetna_stranica():
    response = render_template('pocetna_stranica.html')
    return response, 200

@app.post('/korisnicki_unos')
def korisnicki_unos():
    text = request.form.get('text')
    password = request.form.get('password')
    email = request.form.get('email')

    return f"{text} + {password} + {email}"

@app.post('/temperatura')
def rect():
    temp = request.json.get('temperatura')
    if temp is not None:
        global temperatura
        temperatura.append(temp)
        return 'Uspješno ste upisali', 201
    else:
        return 'Niste upisali ispravan ključ', 404

     

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)