//Resposta item 1
var pessoa = {
    nome: "João",
    idade: 35,
    profissao: "Engenheiro",
    endereco: {
      logradouro: "Rua Arlindo Nogueira",
      bairro: "Centro",
      cidade: "Teresina",
      cep: "64000-290"
    }
  };

//Resposta item 2
function imprimirPessoa (pessoa) {
  console.log("Nome:"+ pessoa.nome+"Idade:"+ pessoa.idade+"Profissão:"+ pessoa.profissao+"Logradouro:"+ pessoa.endereco.logradouro+"Bairro:"+ pessoa.endereco.bairro+"Cidade:"+ pessoa.endereco.cidade+"CEP:"+ pessoa.endereco.cep);
}