function parOuImpar(numero) {
    if (numero < 0) {
      console.log("É obrigatório informar um número maior ou igual a zero.");
    } else if (numero % 2 == 0) {
      console.log(`O número ${numero} é par.`);
    } else {
      console.log(`O número ${numero} é ímpar.`);
    }
}
parOuImpar(-1);