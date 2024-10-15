/**
 * Módulo de operaciones matemáticas
 * @module mathOperations
 */

/**
 * Suma dos números.
 * @param {number} a - El primer número.
 * @param {number} b - El segundo número.
 * @returns {number} El resultado de la suma.
 */
export function sumar(a, b) {
    return a + b;
}

/**
 * Resta dos números.
 * @param {number} a - El primer número.
 * @param {number} b - El segundo número.
 * @returns {number} El resultado de la resta.
 */
export function restar(a, b) {
    return a - b;
}

/**
 * Multiplica dos números.
 * @param {number} a - El primer número.
 * @param {number} b - El segundo número.
 * @returns {number} El resultado de la multiplicación.
 */
export function multiplicar(a, b) {
    return a * b;
}

/**
 * Divide dos números.
 * @param {number} a - El numerador.
 * @param {number} b - El denominador.
 * @returns {number} El resultado de la división.
 * @throws {Error} Si el denominador es 0.
 */
export function dividir(a, b) {
    if (b === 0) {
        throw new Error('El denominador no puede ser 0.');
    }
    return a / b;
}

