function somar(numero1, numero2){
    var total = numero1+numero2;
    return total;
}

var resultado = somar (2,5);
console.log(resultado);

var multiplicar = function(n1,n2){
    return (n1*n2);
}

multiplicar(2,6);

//usando "hoisting" a declaração da função é "enviada" para o topo no pre-processamento
//function somar(numero1,numero2){
//    var total = numero1+numero2;
//    return total;
//}