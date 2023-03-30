function multiDois() {
    if (arguments.length === 0) {
      console.log("É obrigatório informar pelo menos um valor.");
      return;
    }
    
    for (let i = 0; i < arguments.length; i++) {
      const valor = arguments[i];
      if (typeof valor !== 'number') {
        console.log(`O valor ${valor} não é um número e será ignorado.`);
        continue;
      }
      console.log(valor * 2);
    }
  }
  
  multiDois(7,8,10);