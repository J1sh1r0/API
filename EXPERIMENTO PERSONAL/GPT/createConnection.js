require('dotenv').config();
const mysql = require('mysql2/promise');

async function createConnection() {
  return await mysql.createConnection({
    host: process.env.DB_HOST || 'localhost',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || '', // Coloca tu contraseña en el archivo .env
    database: process.env.DB_DATABASE || 'gestion_usuarios_pagos',
    port: process.env.DB_PORT || 3306
  });
}

module.exports = createConnection;
