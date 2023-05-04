package entidades;

import utilitarios.Ferramentas;

import java.util.ArrayList;

public class ContaCorrente
{
    private static int numDeContas = 1;

    private double saldo;
    private Correntista nome;
    private int numeroConta;
    private String senha;
    private double limiteChequeEspecial;
    private ArrayList<String> historicoTransacoes;

    //--Construtor:--
    public ContaCorrente(Correntista nome, String senha)
    {
        this.nome = nome;
        this.numeroConta = numDeContas;
        this.senha = senha;
        this.saldo = 0.0    ;
        this.limiteChequeEspecial = 1000;
        this.historicoTransacoes = new ArrayList<String>();
        numDeContas += 1;
    }

    //--Metodos:--

    //Depositar:
    public void depositar(double valor)
    {
        if(valor>0)
        {
            this.saldo += valor;
            this.historicoTransacoes.add("Deposito de R$" + valor + " realizado");
            System.out.println("Deposito de R$" + valor + " realizado");
        }else
        {
            System.out.println("Valor de depósito inválido");
        }
    }

    //Sacar:
    public void sacar(double valor)
    {
        if (this.saldo + this.limiteChequeEspecial < valor)
        {
            System.out.println("Saldo insuficiente");
        }
        else
        {
            this.saldo -= valor;
            this.historicoTransacoes.add("Saque de R$" + valor + " realizado");
            System.out.println("Saque de R$" + valor + " realizado");
        }
    }

    //Consultar saldo:
    public void consultarSaldo()
    {
        System.out.println("Saldo atual: R$"+ this.saldo);
    }

    //Extrato:
    public String extrato()
    {
        System.out.println(this.historicoTransacoes);
        System.out.println("Saldo atual: R$"+ this.saldo);

        return String.valueOf(this.historicoTransacoes);
    }

    //Transferir:
    public void transferir(ContaCorrente contaParaDeposito, double valor)
    {
        if (valor > 0 && this.getSaldo() >= valor)
        {
            setSaldo(getSaldo() - valor);
            contaParaDeposito.saldo = contaParaDeposito.getSaldo() + valor;
            this.historicoTransacoes.add("Transferencia de "+ valor + " para a conta nº"+contaParaDeposito);
            System.out.println("Transferencia de " + valor +" realizada com sucesso!");
        }
        else
        {
            System.out.println("Não Foi possivel realizar a transferencia");
        }
    }

    //--Getters e Setters--

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public String getNome() {
        return this.nome.getNome();
    }

    public void setNome(Correntista nome) {
        this.nome = nome;
    }



    public int getNumeroConta() {
        return numeroConta;
    }

    public void setNumeroConta(int numeroConta) {
        this.numeroConta = numeroConta;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public double getLimiteChequeEspecial() {
        return limiteChequeEspecial;
    }

    public void setLimiteChequeEspecial(double limiteChequeEspecial) {
        this.limiteChequeEspecial = limiteChequeEspecial;
    }

    public ArrayList<String> getHistoricoTransacoes() {
        return historicoTransacoes;
    }

    public void setHistoricoTransacoes(ArrayList<String> historicoTransacoes) {
        this.historicoTransacoes = historicoTransacoes;
    }

    public String toString()
    {
        return "\n Nome: " +this.nome.getNome()+
               "\n Conta Corrente: " +this.getNumeroConta()+
               "\n CPF: " +this.nome.getCpf()+
               "\n Email: " +this.nome.getEmail()+
               "\n Saldo: "+ Ferramentas.doubleToString(getSaldo());

    }

    public void adicionarInvestimento(Investimento investimento) {
    }
}
