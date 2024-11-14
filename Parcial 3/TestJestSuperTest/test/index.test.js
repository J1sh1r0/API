const expect = require("supertest");
const url = "http://localhost:3002";

describe("Conjunto de pruebas ",()=>{ // Encapsular test dentro de la función describe()
 it('Revisar que servidor me de 200', () => { // En la función it() lo que debería hacer
 request(url)
 .get('/empleado')
 .end( function(err,res){
    expect(res.statusCode).toBe(200);
        });
    });
 });
