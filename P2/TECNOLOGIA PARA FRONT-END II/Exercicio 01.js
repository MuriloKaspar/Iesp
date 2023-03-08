var i, altura, sexo, maiorAlt = 0, menorAlt = 3, mulh = 0, hom = 0, mediaMulh = 0, mediaHom = 0, contaMulh = 0, contaHom = 0;

		for(i = 1 ;i <= 5; i++) {		
			altura = parseFloat(prompt("Informe a altura["+i+"]:"));
			sexo = prompt("Informe o sexo: M ou F:").toUpperCase();
			

			if(altura > maiorAlt) { 
				maiorAlt = altura;
			} else if(altura < menorAlt) { 
				menorAlt = altura;

			} if(sexo == 'F') {
				mulh += altura;
				contaMulh++;
			} else if(sexo == 'M') {
				hom += altura;
				contaHom++;
			}
		}
		mediaMulh = mulh/contaMulh;
        mediaHom = hom/contaHom;
		alert("A maior altura é: "+maiorAlt); 
		alert("A menor altura é: "+menorAlt);
		alert("A média da altura dos homens é: "+mediaHom.toFixed(2));
		alert("O número de mulheres é: "+contaMulh);