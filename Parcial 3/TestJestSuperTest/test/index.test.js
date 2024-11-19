const request = require("supertest");
const app = require("../index"); // Importa la instancia de la app
 
describe("Conjunto de pruebas", () => {
    it("Revisar que servidor me de 200", (done) => { // Usa done para manejar la asincronía
        request(app)
            .get("/empleado")
            .end((err, res) => {
                expect(res.statusCode).toBe(200);
                done(); // Llama a done al final para indicar que la prueba ha terminado
            });
    });
});
