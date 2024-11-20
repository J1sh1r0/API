// test/mathOperations.test.js

const { sumar, restar, multiplicar, dividir } = require('../src/mathOperations');

test('Suma de 2 + 3 es igual a 5', () => {
    expect(sumar(2, 3)).toBe(5);
});

test('Resta de 5 - 2 es igual a 3', () => {
    expect(restar(5, 2)).toBe(3);
});

test('Multiplicación de 4 * 3 es igual a 12', () => {
    expect(multiplicar(4, 3)).toBe(12);
});

test('División de 10 / 2 es igual a 5', () => {
    expect(dividir(10, 2)).toBe(5);
});

test('División por cero lanza un error', () => {
    expect(() => dividir(10, 0)).toThrow("No se puede dividir entre cero");
});
