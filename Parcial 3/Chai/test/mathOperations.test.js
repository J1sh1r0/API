import * as chai from 'chai';
import test from 'node:test';
import * as areas from "../src/areas.js";

test("Si le mando un 2 debe de dar 4", ()=>{
    let res = areas.areaCuadrado(2);
    chai.assert.equal(res,4);    
    chai.assert.typeOf(res, 'number'); 
})

test("Si le mando un 2 debe de dar 4", ()=>{
    let res = areas.areaCuadrado(2);
    chai.expect(res).to.be.a('number')
})