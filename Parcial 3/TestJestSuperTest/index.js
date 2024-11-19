const express = require('express');
const cors = require('cors');
const app = express();
 
app.use(cors()); // Middleware de terceros
 
app.get('/empleado', (req, res) => {
    res.json({ mensaje: 'Server Express contestando a petición get' });
});
 
module.exports = app; // Exporta la instancia de app