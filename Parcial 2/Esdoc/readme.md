# Módulo de Operaciones Matemáticas - `mathOperations`

Este proyecto es un módulo de JavaScript que proporciona funciones para realizar operaciones matemáticas básicas como sumar, restar, multiplicar y dividir. El código está documentado utilizando JSDoc para generar documentación detallada automáticamente.

## Contenido del Módulo

El módulo incluye las siguientes funciones:

- **sumar(a, b)**: Suma dos números.
- **restar(a, b)**: Resta dos números.
- **multiplicar(a, b)**: Multiplica dos números.
- **dividir(a, b)**: Divide dos números. Si el divisor es 0, lanza un error.

## Instalación

Este módulo no requiere instalación. Simplemente importa las funciones que necesites en tu archivo JavaScript.

### Ejemplo de Uso

```javascript
// Importa las funciones del módulo mathOperations
import { sumar, restar, multiplicar, dividir } from './mathOperations.js';

// Uso de las funciones
console.log("Suma: ", sumar(5, 3)); // Suma: 8
console.log("Resta: ", restar(5, 3)); // Resta: 2
console.log("Multiplicación: ", multiplicar(5, 3)); // Multiplicación: 15

// Manejo de errores en la división
try {
    console.log("División: ", dividir(10, 2)); // División: 5
    console.log("División: ", dividir(10, 0)); // Error
} catch (error) {
    console.error(error.message); // El denominador no puede ser 0.
}
