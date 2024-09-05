const express = require('express');
const  cors  = require ('cors'); 
const app = express();

app.use(cors());                //Middleware de Terceros
app.use(express.json());        //Middleware Incorporado en Express
app.use(express.text());        //Middleware para Texto

app.get('/clientes/:id',cors(),(req,res)=>{
    console.log(req.params);
    res.json({mensaje: 'Server Express contestando a peticion get'})
})
app.post('/clientes/',(req,res)=>{
    console.log(req.query);
    res.json({mensaje: 'Server Express contestando a peticion post'})
})
app.put('/clientes/',(req,res)=>{
    console.log(req.body);
    res.json({mensaje: 'Server Express contestando a peticion post'})
})
app.listen(3000,()=>{
    console.log('Server Express Escuchando en puerto 3000')
})


