const express = require('express');
const fs = require('fs'); // Importar el módulo fs
const path = require('path'); // Importar el módulo path
const { query, validationResult } = require('express-validator'); // Importar express-validator
const https = require('https'); // Importar https para crear el servidor HTTPS
const cors = require('cors');
const app = express();

// Configurar las opciones de HTTPS con las llaves SSL
const options = {
    key: fs.readFileSync(path.join(__dirname, 'ssl/key.pem')), // Leer la llave privada
    cert: fs.readFileSync(path.join(__dirname, 'ssl/cert.pem')) // Leer el certificado
};

app.use(cors());

// Ruta GET con validación de query
app.get(
    '/',
    query('id').isInt().withMessage('El ID debe ser un número entero'), // Validar que el parámetro 'id' en la query sea un entero
    (req, res) => {
        const errors = validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(400).json({ errors: errors.array() }); // Si hay errores, devolverlos como respuesta
        }
        res.send('Servidor Express contestando a petición GET'); // Si no hay errores, procesar la solicitud
    }
);

// Crear el servidor HTTPS y escuchar en el puerto 3000
https.createServer(options, app).listen(3000, () => {
    console.log("Servidor Express escuchando en el puerto 3000 con HTTPS");
});
