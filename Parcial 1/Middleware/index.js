const express = require('express');
const  cors  = require ('cors'); 
const app = express();
app.use(cors());                //Middleware de Terceros
app.use((req,res,next)=>{       //Middleware de Aplicacion
    console.log(new Date());
    next();
})
app.use(express.json());        //Middleware Incorporado en Express

app.get('/',cors(),(req,res)=>{
    res.json({mensaje: 'Server Express contestando a peticion get'})
})
app.post('/',(req,res)=>{
    res.json({mensaje: 'Server Express contestando a peticion post'})
})
app.listen(3000,()=>{
    console.log('Server Express Escuchando en puerto 3000')
})

app.use(function(err, req, res, next) {             //Middleware de Manejo de Error
    res.status(500).send('Algo no a ido bien!')
});
