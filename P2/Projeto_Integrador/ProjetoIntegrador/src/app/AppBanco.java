package app;

import entidades.*;
import java.util.ArrayList;
import java.util.Scanner;

public class AppBanco
{
    static Scanner input = new Scanner(System.in);
    static ArrayList<ContaCorrente> contasBancarias;

    public static void main(String[] args)
    {
        contasBancarias = new ArrayList<ContaCorrente>();
        operacoes();
    }
    public static void operacoes()
        {
            System.out.println("----------------------------------------");
            System.out.println("------Bem vindo ao Banco Integrador-----");
            System.out.println("----------------------------------------");
            System.out.println("##########-Selecione uma opção-#########");
            System.out.println("| 1 -  Criar Conta  - |");
            System.out.println("| 2 -  Depositar    - |");
            System.out.println("| 3 -  Sacar        - |");
            System.out.println("| 4 -  Transferir   - |");
            System.out.println("| 5 -  Extrato      - |");
            System.out.println("| 6 -  Listar CC    - |");
            System.out.println("| 7 -  Emprestimo   - |");
            System.out.println("| 8 -  Investimento - |");
            System.out.println("| 9 -  Sair         - |");

            int operacao = input.nextInt();

            switch(operacao)
            {
                case 1:
                    criarConta();
                    break;
                case 2:
                    depositar();
                    break;
                case 3:
                    sacar();
                    break;
                case 4:
                    transferir();
                    break;
                case 5:
                    extrato();
                    break;
                case 6:
                    listarContas();
                    break;
                case 7:
                    emprestimo();
                    break;
                case 8:
                    investimento();
                    break;
                case 9:
                    System.out.println("Obrigado por usar os serviços do Banco Integrador.");;
                    System.exit(0);
                default:
                    System.out.println("Opção inválida");;
                    operacoes();
                    break;
            }

        }

        public static void criarConta()
        {
            input.next();

            System.out.println("\nNome: ");
            String nome = input.nextLine();

            System.out.println("\n\n CPF: ");
            String cpf = input.nextLine();

            System.out.println("\n\n Email: ");
            String email = input.nextLine();

            System.out.println("\n\n Senha (6 numeros): ");
            String senha = input.next();

            Correntista correntista = new Correntista(nome,cpf,email);
            ContaCorrente conta = new ContaCorrente(correntista, senha);

            contasBancarias.add(conta);

            System.out.println("Conta Corrente criada com Sucesso!!!");
            System.out.println("\n\nTitular: "+ nome);
            System.out.println("\nCPF: "+ cpf);

            operacoes();

        }

        private static ContaCorrente acharConta(int numeroConta)
        {
            ContaCorrente conta = null;

            if(contasBancarias.size() > 0)
            {
                for(ContaCorrente i: contasBancarias)
                {
                    if (i.getNumeroConta() == numeroConta);
                    conta = i;
                }

            }
            return conta;
        }

        public static void depositar()
        {
            System.out.println("Digite o Nº da Conta para depósito: ");
            int numeroConta = input.nextInt();

            ContaCorrente conta = acharConta(numeroConta);
            if (conta != null)
            {
                System.out.println("Digite o valor a ser depositádo: ");
                Double valorDeposito = input.nextDouble();
                conta.depositar(valorDeposito);
            }
            else
            {
                System.out.println("Conta não encontrada");
            }
            operacoes();
        }

        public static void sacar()
        {
            System.out.println("Digite o Nº da Conta para saque: ");
            int numeroConta = input.nextInt();

            ContaCorrente conta = acharConta(numeroConta);
            if (conta != null)
            {
                System.out.println("Digite o valor a ser sacado: ");
                Double valorSaque = input.nextDouble();

                System.out.println("Digite a senha (6 numeros): ");
                String nSenha = input.nextLine();

                if(nSenha == conta.getSenha())
                {
                conta.sacar(valorSaque);
                }
                else
                {
                    System.out.println("Senha invalida");
                    operacoes();
                }
            }
            else
            {
                System.out.println("Conta não encontrada");
            }
            operacoes();

        }

        public static void transferir()
        {
            System.out.println("Digite o Nº da Conta Remetente: ");
            int contaRemetente = input.nextInt();

            ContaCorrente conta = acharConta(contaRemetente);
            if (conta != null)
            {
                System.out.println("Digite o Nº da Conta Destino: ");
                int contaDestino = input.nextInt();

                ContaCorrente conta2 = acharConta(contaDestino);
                if  (conta2 != null)
                {
                    System.out.println("Digite o valor a ser Trasferido: ");
                    Double valorTransf = input.nextDouble();

                    System.out.println("Digite a senha (6 numeros): ");
                    String nSenha = input.nextLine();

                    if(nSenha == conta.getSenha())
                    {
                        conta.transferir(conta2,valorTransf);
                    }
                    else
                    {
                        System.out.println("Senha invalida");
                    }
                }
                else
                {
                    System.out.println("Conta destino não encontrada");
                }

            }
            else
            {
                System.out.println("Conta remetente não encontrada");
            }
            operacoes();
        }

        public static void extrato()
        {
            System.out.println("Digite o Nº da Conta para obter o Extrato");
            int contaExtrato = input.nextInt();

            ContaCorrente conta = acharConta(contaExtrato);
            if (conta != null)
            {
                System.out.println(conta.extrato());
            }
        }

        public static void listarContas()
        {
            if(contasBancarias.size() > 0)
            {
                for(ContaCorrente conta : contasBancarias)
                {
                    System.out.println(conta);
                }
            }
            else
            {
                System.out.println("Ainda não há contas cadastradas");
            }
            operacoes();
        }

        public static void emprestimo()
        {
            menuEmprestimo();
        }
            public static void menuEmprestimo()
        {
        System.out.println("Deseja:");
        System.out.println("1 - Simular emprestimo");
        System.out.println("2 - Fazer emprestimo");
        System.out.println("3 - Voltar ao menu inicial");

        int menu = input.nextInt();
        switch (menu)
        {
            case 1:
                simularEmprestimo();
                break;
            case 2:
                fazerEmprestimo();
                break;
            case 3:
                operacoes();
            default:
                System.out.println("Opção inválida");;
                menuEmprestimo();
                break;
        }


    }
    public static void simularEmprestimo()
    {
        System.out.println("Deseja fazer uma simulação de emprestimo?");
        System.out.println("Digite o valor do emprestimo: ");
        double valorEmprestimo = input.nextDouble();
        System.out.println("Digite a quantidade de parcelas: ");
        int parcelas = input.nextInt();

        Emprestimo emprestimo = new Emprestimo(valorEmprestimo,parcelas);

        emprestimo.imprimirInformacoes();
    }
    public static void fazerEmprestimo()
    {
        System.out.println("Deseja fazer um emprestimo?");
        System.out.println("Digite o Nº da Conta Corrente: ");
        int numeroConta = input.nextInt();

        ContaCorrente conta = acharConta(numeroConta);
        if (conta != null)
        {
            System.out.println("Digite o valor do emprestimo: ");
            double valorEmprestimo = input.nextDouble();

            System.out.println("Digite a quantidade de parcelas: ");
            int parcelas = input.nextInt();

            Emprestimo emprestimo = new Emprestimo(valorEmprestimo,parcelas);

            System.out.println("Digite a senha (6 numeros): ");
            String nSenha = input.nextLine();

            if(nSenha == conta.getSenha())
            {
                conta.depositar(valorEmprestimo);
                System.out.println("Emprestimo de "+ valorEmprestimo + " aprovado!");
            }
            else
            {
                System.out.println("Senha invalida");
            }

        }
        else
        {
            System.out.println("Conta não encontrada");
        }
        operacoes();
    }

        public static void investimento() {

            System.out.println("----------------------------------------");
            System.out.println("------------Investimento----------------");
            System.out.println("----------------------------------------");

            System.out.println("Digite o número da conta corrente:");
            int numConta = input.nextInt();

            ContaCorrente conta = acharConta(numConta);
            if (conta == null) {
                System.out.println("Conta não encontrada.");
                operacoes();
            }

            System.out.println("Digite o tipo de investimento:");
            String tipoInvestimento = input.next();

            System.out.println("Digite o valor a ser aplicado:");
            double valorAplicado = input.nextDouble();

            System.out.println("Digite a taxa de juros:");
            double taxaJuros = input.nextDouble();

            System.out.println("Digite o prazo de vencimento em dias:");
            int prazoVencimento = input.nextInt();

            Investimento investimento = new Investimento(tipoInvestimento, valorAplicado, taxaJuros, prazoVencimento);

            conta.adicionarInvestimento(investimento);

            System.out.println("Investimento adicionado com sucesso.");
            operacoes();
        }

}
