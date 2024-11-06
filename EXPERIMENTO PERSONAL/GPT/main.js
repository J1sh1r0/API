// Cargar dependencias
const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
require('dotenv').config();

// Crear instancia de Express
const app = express();

// Middleware
app.use(bodyParser.json());

// Crear conexión con MySQL
const db = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME,
    port: process.env.DB_PORT
});

// Conectar a MySQL
db.connect((err) => {
    if (err) {
        console.error('Error al conectar a MySQL:', err);
        return;
    }
    console.log('Conectado a la base de datos MySQL.');
});

// Ruta inicial
app.get('/', (req, res) => {
    res.send('API para gestionar usuarios y pagos');
});

// Obtener todos los usuarios
app.get('/usuarios', (req, res) => {
    const query = 'SELECT * FROM usuarios';
    db.query(query, (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// Crear un nuevo usuario
app.post('/usuarios', (req, res) => {
    const { nombre, edad, genero, fecha_asignacion, telefono, direccion } = req.body;
    const query = 'INSERT INTO usuarios (nombre, edad, genero, fecha_asignacion, telefono, direccion) VALUES (?, ?, ?, ?, ?, ?)';
    db.query(query, [nombre, edad, genero, fecha_asignacion, telefono, direccion], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Usuario creado con éxito', id: results.insertId });
    });
});

// Actualizar un usuario
app.put('/usuarios/:id', (req, res) => {
    const { id } = req.params;
    const { nombre, edad, genero, telefono, direccion } = req.body;
    const query = 'UPDATE usuarios SET nombre = ?, edad = ?, genero = ?, telefono = ?, direccion = ? WHERE id_usuario = ?';
    db.query(query, [nombre, edad, genero, telefono, direccion, id], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Usuario actualizado con éxito' });
    });
});

// Eliminar un usuario
app.delete('/usuarios/:id', (req, res) => {
    const { id } = req.params;
    const query = 'DELETE FROM usuarios WHERE id_usuario = ?';
    db.query(query, [id], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Usuario eliminado con éxito' });
    });
});

// Obtener pagos de un usuario
app.get('/usuarios/:id/pagos', (req, res) => {
    const { id } = req.params;
    const query = 'SELECT * FROM pagos WHERE id_usuario = ?';
    db.query(query, [id], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json(results);
    });
});

// Registrar un pago
app.post('/pagos', (req, res) => {
    const { id_usuario, monto, fecha_acordada, fecha_pago, regargo, estado_pago } = req.body;
    const query = 'INSERT INTO pagos (id_usuario, monto, fecha_acordada, fecha_pago, regargo, estado_pago) VALUES (?, ?, ?, ?, ?, ?)';
    db.query(query, [id_usuario, monto, fecha_acordada, fecha_pago, regargo, estado_pago], (err, results) => {
        if (err) {
            return res.status(500).send(err);
        }
        res.json({ message: 'Pago registrado con éxito', id: results.insertId });
    });
});

// Configuración del puerto y arranque del servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor ejecutándose en el puerto ${PORT}`);
});
