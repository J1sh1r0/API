const chai = require('chai');
const chaiHttp = require('chai-http');
const expect = chai.expect;
 
chai.use(chaiHttp);
 
const url = 'http://localhost:3002';
 
describe('Conjunto de pruebas', () => {
    it('Revisar que servidor me de 200', (done) => {  // Agregar `done` para manejar la asincronía
        chai.request(url)
            .get('/empleado')
            .end((err, res) => {
                expect(res).to.have.status(200);
                done();  // Llamar a `done` al final para finalizar la prueba
            });
    });
});