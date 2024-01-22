SELECT temperatura.id, temperatura.datum, temperatura.vrijednost
FROM temperatura
LEFT JOIN korisnik ON temperatura.id = korisnik.id
WHERE korisnik.id = '{{id_korisnika}}';


