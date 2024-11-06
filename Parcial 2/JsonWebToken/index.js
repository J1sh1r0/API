const express = require('express');
const jwt = require('jsonwebtoken'); // Importamos jsonwebtoken
const app = express();
const PORT = 3000;

// Clave secreta para firmar el JWT (debe ser segura y almacenarse en un entorno seguro, como variables de entorno)
const SECRET_KEY = 'tu_secreta_clave';

// Middleware para verificar el token
function verificarToken(req, res, next) {
    const token = req.headers['authorization'];

    if (!token) {
        return res.status(403).json({ mensaje: 'Token no proporcionado.' });
    }

    // Verifica y decodifica el token
    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) {
            return res.status(401).json({ mensaje: 'Token no válido.' });
        }

        req.usuario = decoded; // Guardamos la información del usuario en la petición
        next();
    });
}

// Ruta pública para obtener un token
app.post('/login', (req, res) => {
    // Aquí autenticas al usuario con sus credenciales
    const usuario = { id: 1, nombre: 'Dominic' }; // Ejemplo de usuario autenticado

    // Genera el token con un tiempo de expiración de 1 hora
    const token = jwt.sign(usuario, SECRET_KEY, { expiresIn: '1h' });

    res.json({ token });
});

// Ruta protegida que requiere un token válido
app.get('/recurso-protegido', verificarToken, (req, res) => {
    res.json({
        mensaje: 'Accediste a un recurso protegido.',
        usuario: req.usuario
    });
});

// Inicia el servidor
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
