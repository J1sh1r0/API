const express = require('express');
const path = require('path');
const pug = require('pug');
const app = express();
const cors = require('cors');

app.use(cors());
app.set('view engine', 'pug');
app.set('view', path.join(__dirname, 'views'));

app.get('/',(req,res)=> {
    console.log(req.query.nombre);
    let opciones={nombre:req.query.nombre};
    res.render('mivista', opciones);
});

app.listen(3000, () => {
    console.log('Server Express escuchando en el puerto 3000');
});
