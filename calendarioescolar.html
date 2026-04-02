<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calendario Escolar Ultra Mejorado</title>

<style>

body{
font-family:Arial;
background:#eef1f7;
margin:0;
padding:20px;
transition:0.4s;
}

h1{text-align:center;}

#panel{
display:flex;
flex-wrap:wrap;
gap:8px;
justify-content:center;
margin-bottom:15px;
}

button{
padding:8px 14px;
border:none;
border-radius:6px;
background:#333;
color:white;
cursor:pointer;
}

button:hover{background:#555;}

.calendario{
display:grid;
grid-template-columns:repeat(7,1fr);
gap:4px;
}

.dia{
background:white;
padding:10px;
border-radius:6px;
text-align:center;
cursor:pointer;
}

.hoy{outline:3px solid blue;}
.importante{outline:3px solid gold;}
.evento{outline:3px solid purple;}

.modo-oscuro{
background:#111;
color:white;
}

.modo-oscuro .dia{
background:#333;
}

#reloj{
text-align:center;
font-size:18px;
margin-bottom:10px;
}

#temporizador{
text-align:center;
font-size:20px;
margin-top:10px;
}

</style>
</head>

<body>

<h1>Calendario Escolar Pro Max</h1>

<div id="reloj"></div>

<div id="panel">

<button onclick="crearCalendario()">Actualizar</button>
<button onclick="modoOscuro()">Modo oscuro</button>
<button onclick="agregarEvento()">Agregar evento</button>
<button onclick="marcarImportante()">Día importante</button>
<button onclick="estadisticas()">Estadísticas</button>
<button onclick="generarEventos()">Eventos aleatorios</button>
<button onclick="limpiarEventos()">Limpiar eventos</button>
<button onclick="temporizadorEstudio()">Temporizador estudio</button>
<button onclick="contadorEventos()">Contar eventos</button>
<button onclick="guardarDatos()">Guardar</button>
<button onclick="cargarDatos()">Cargar</button>
<button onclick="colorRandom()">Cambiar colores</button>

</div>

<div id="temporizador"></div>

<div id="calendario" class="calendario"></div>

<script>

let eventos={}
let importantes={}

function reloj(){

let ahora=new Date()

let h=String(ahora.getHours()).padStart(2,"0")
let m=String(ahora.getMinutes()).padStart(2,"0")
let s=String(ahora.getSeconds()).padStart(2,"0")

document.getElementById("reloj").textContent="Hora: "+h+":"+m+":"+s

}

setInterval(reloj,1000)

function crearCalendario(){

let cont=document.getElementById("calendario")
cont.innerHTML=""

let hoy=new Date()

for(let i=1;i<=365;i++){

let d=new Date()
d.setDate(i)

let div=document.createElement("div")
div.className="dia"

let clave=d.toDateString()

if(d.getDate()==hoy.getDate() && d.getMonth()==hoy.getMonth()){
div.classList.add("hoy")
}

if(eventos[clave]) div.classList.add("evento")
if(importantes[clave]) div.classList.add("importante")

div.textContent=d.getDate()

div.onclick=function(){

let texto="Fecha: "+clave

if(eventos[clave]) texto+="\nEvento: "+eventos[clave]

alert(texto)

}

cont.appendChild(div)

}

}

function modoOscuro(){
document.body.classList.toggle("modo-oscuro")
}

function agregarEvento(){

let fecha=prompt("Fecha ejemplo: Mar 10 2026")
let nombre=prompt("Evento")

if(fecha && nombre){
eventos[fecha]=nombre
crearCalendario()
}

}

function marcarImportante(){

let fecha=prompt("Fecha importante")

if(fecha){
importantes[fecha]=true
crearCalendario()
}

}

function generarEventos(){

for(let i=0;i<40;i++){

let d=new Date()
d.setDate(Math.floor(Math.random()*365))

eventos[d.toDateString()]="Evento escolar"

}

crearCalendario()

}

function limpiarEventos(){

eventos={}
importantes={}
crearCalendario()

}

function estadisticas(){

let totalEventos=Object.keys(eventos).length
let totalImportantes=Object.keys(importantes).length

alert(
"Eventos: "+totalEventos+
"\nDías importantes: "+totalImportantes
)

}

function contadorEventos(){

alert("Total eventos: "+Object.keys(eventos).length)

}

function temporizadorEstudio(){

let minutos=25

let intervalo=setInterval(function(){

minutos--

document.getElementById("temporizador").textContent=
"Tiempo de estudio: "+minutos+" min"

if(minutos<=0){

clearInterval(intervalo)
alert("Descanso!")

}

},60000)

}

function guardarDatos(){

localStorage.setItem("eventos",JSON.stringify(eventos))
localStorage.setItem("importantes",JSON.stringify(importantes))

alert("Guardado")

}

function cargarDatos(){

eventos=JSON.parse(localStorage.getItem("eventos"))||{}
importantes=JSON.parse(localStorage.getItem("importantes"))||{}

crearCalendario()

}

function colorRandom(){

let colores=["#ffb3b3","#b3ffd9","#b3d1ff","#fff0b3","#e0b3ff"]

document.body.style.background=colores[Math.floor(Math.random()*colores.length)]

}

crearCalendario()

</script>

</body>
</html>