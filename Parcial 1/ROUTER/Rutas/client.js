// Rutas/clientes.js
const express = require('express');
const mysql = require('mysql2/promise');

const router = express.Router(); // Declara el Router

// Crea la conexión a la base de datos
// const connection = mysql.createConnection({
//     host: 'localhost',
//     user: 'root',
//     password: '',  // Coloca tu contraseña aquí si es necesario
//     database: 'biblioteca',  // Cambia el nombre de la base de datos si es necesario
// });

// Ruta para obtener todos los usuarios
router.get('/', async (req, res) => {
  let sentenciaSql = 'SELECT * FROM usuarios';
  const [rows, fields] = await connection.execute(sentenciaSql);
  res.json(rows);
});

// Ruta para obtener un usuario por ID
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',  // Coloca tu contraseña aquí si es necesario
    database: 'biblioteca',  // Cambia el nombre de la base de datos si es necesario
});
  const [rows, fields] = await connection.execute('SELECT * FROM usuarios WHERE Id_Usuario = ?', [id]);

  if (rows.length === 0) {
    res.json({ registros: 'No se encontró Usuario' });

  } else {
    res.json(rows);
  }

});

// Ruta POST para agregar un nuevo usuario
router.post('/', async (req, res) => {
  const { nombre, apellido_paterno, apellido_materno, correo, usuario, contrasena, rol } = req.body;
  try {
    const [result] = await connection.execute(
      'INSERT INTO clientes (nombre, apellido_paterno, apellido_materno, correo, usuario, contrasena, rol) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [nombre, apellido_paterno, apellido_materno || null, correo, usuario, contrasena, rol]
    );
    res.json({ mensaje: 'Cliente agregado exitosamente', idCliente: result.insertId });
  } catch (error) {
    res.status(500).json({ error: 'Error al agregar el Usuario' });
  }
});

// Exporta el router para usarlo en index.js
module.exports.router = router;

