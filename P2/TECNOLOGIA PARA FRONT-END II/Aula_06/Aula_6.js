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
  console.log("Nome:", pessoa.nome);
  console.log("Idade:", pessoa.idade);
  console.log("Profissão:", pessoa.profissao);
  console.log("Endereço:");
  console.log("Logradouro:", pessoa.endereco.logradouro);
  console.log("Bairro:", pessoa.endereco.bairro);
  console.log("Cidade:", pessoa.endereco.cidade);
  console.log("CEP:", pessoa.endereco.cep);
}
imprimirPessoa(pessoa);