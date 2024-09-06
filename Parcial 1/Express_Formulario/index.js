const express = require('express');
const  cors  = require ('cors');
const multer = require('multer');
const bodyParser = require('body-parser');
require('body-parser-xml')(bodyParser);

const app = express();
const upload = multer()

app.use(cors());                                //Middleware de Terceros
app.use(express.json());                        //Middleware Incorporado en Express
app.use(express.text());                        //Middleware para Texto
app.use(express.urlencoded({extended:true}));   //Middleware para parsear un formulario URL en Code
app.use(upload.none())                          //Middleware para pasea un for data     
app.use(bodyParser.xml());                      //Parseador de XML

app.post('/clientes/',(req,res)=>{
    console.log(req.body);
    res.json({mensaje: 'Server Express contestando a peticion post'})
})

app.listen(3000,()=>{
    console.log('Server Express Escuchando en puerto 3000')
})
