function multiArray(array) {
    if (array.length == 0) {
      console.log("É obrigatório informar um array com valores numéricos válidos!");
      return [];
    }
    
    console.log("Valores do Array: ", array);
  
    const novoArray = array.map((valor) => {
      const novoValor = valor * 2;
      return novoValor;
    });
  
    console.log("Novos valores do Array: ", novoArray);
    return novoArray;
  }

const arrayInic = [1, 2, 3, 4, 5];
const novoArray = multiArray(arrayInic);