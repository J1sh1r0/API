const express = require('express');
const { query, validationResult } = require('express-validator'); // Importar express-validator
const app = express();

const cors = require('cors');
app.use(cors());

// Ruta GET con validación
app.get(
    '/',
    // Validar que el parámetro 'id' en la query sea un entero
    query('id').isInt().withMessage('El ID debe ser un número entero'),
    (req, res) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            // Si hay errores, devolverlos como respuesta
            return res.status(400).json({ errors: errors.array() });
        }

        // Si no hay errores, procesar la solicitud
        res.send('Server Express contestando a petición GET');
    }
);

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Server Express escuchando en el puerto 3000');
});
