function carrinho() {

  while (continuar){

  var menu = prompt("comprar mais produtos? 1- Sim | 2- Finalizar Compra");
      if (menu.toLowerCase() == 1) {
        inserir()
        
    
  } else if (menu.toLowerCase() == 2){
      finalizar()
          
  }else{
    alert("Opçãoao inválida");

  }   
  }
  }


function inserir(){
  if (tamanho == 10){
    console.log("Carrinho cheio")
    finalizar()
  }else{
    var nome = prompt("Nome do produto :");
    var valor = prompt("Valor :");
    var valorint = parseInt(valor);
    produtos[nome]= valorint;
    tamanho++;
    carrinho()

  }
  
}


function finalizar(){
  let total = 0
  console.log("Produtos do carrinho:")
  for (const [key, value] of Object.entries(produtos)) {
  console.log(key);
  total = total + produtos[key]
}
console.log("Valor total:")
console.log(total)
console.log("Deve ser no mínimo em:")
if (total >= 100){
  var i = 0;
  while(total >=100){
    i++;
    total = total - 100
  }
  if (i == 1){
    console.log(i,"nota de 100 reais")
  }else{
    console.log(i,"notas de 100 reais")
  }
}

if (total >= 50){
  var i = 0;
  while(total >=50){
    i++;
    total = total - 50
  }
  if (i == 1){
    console.log(i,"nota de 50 reais")
  }else{
    console.log(i,"notas de 50 reais")
  }
}

if (total >= 20){
  var i = 0;
  while(total >=20){
    i++;
    total = total - 20
  }
  if (i == 1){
    console.log(i,"nota de 20 reais")
  }else{
    console.log(i,"notas de 20 reais")
  }
}

if (total >= 10){
  var i = 0;
  while(total >=10){
    i++;
    total = total - 10
  }
  if (i == 1){
    console.log(i,"nota de 10 reais")
  }else{
    console.log(i,"notas de 10 reais")
  }
}

if (total >= 5){
  var i = 0;
  while(total >=5){
    i++;
    total = total - 5
  }
  if (i == 1){
    console.log(i,"nota de 5 reais")
  }else{
    console.log(i,"notas de 5 reais")
  }
}

if (total >= 2){
  var i = 0;
  while(total >=2){
    i++;
    total = total - 2
  }
  if (i == 1){
    console.log(i,"nota de 2 reais")
  }else{
    console.log(i,"notas de 2 reais")
  }
}

if (total >= 1){
  var i = 0;
  while(total >=1){
    i++;
    total = total - 1
  }
  if (i == 1){
    console.log(i,"nota de 1 real")
  }else{
    console.log(i,"notas de 1 real")
  }
}
return continuar = false

}

let continuar = true;
var tamanho = 0;
produtos = {};
inserir()







