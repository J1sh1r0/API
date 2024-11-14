let chai = require('chai');
let chaiHttp = require('chai-http');
const expect = require('chai').expect;

chai.use(chaiHttp);
const url = 'http://localhost:3002';


describe('Conjunto de pruebas ',()=>{ // Encapsular test dentro de la función describe()
 it('Revisar que servidor me de 200', (done) => { // En la función it() lo que debería hacer
 chai.request(url)
 .get('/empleado')
 .end( function(err,res){
        expect(res).to.have.status(200);
        done();
    });
 });
 });