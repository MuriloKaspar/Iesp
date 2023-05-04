package aplicacao;

import entidades.*;

import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Usuario usuario = new Usuario();

        Scanner input = new Scanner(System.in);

        int opcao;

        do {
            System.out.println("BEM VINDO AO PIRATAFLIX");
            System.out.println("====== Menu ======");
            System.out.println("1. Criar conta");
            System.out.println("2. Acessar conta");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");

            opcao = input.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Opção escolhida: Criar conta");
                    usuario.criarConta();// Chamar método para criar conta
                    break;
                case 2:
                    System.out.println("Opção escolhida: Acessar conta");
                    usuario.login();// Chamar método para acessar conta

                    System.out.print("Digite a classificação indicativa do vídeo que deseja assistir: ");
                    String classificacao = input.next();

                    System.out.print("Digite a sua idade: ");
                    int idadeUsuario = input.nextInt();

                    boolean temPermissao = ValidadorClassificacao.validarClassificacao(classificacao, idadeUsuario);

                    if (temPermissao) {
                        System.out.println("Usuário tem permissão para assistir ao vídeo.");
                    } else {
                        System.out.println("Usuário não tem permissão para assistir ao vídeo.");
                    }

                    break;
                case 3:
                    System.out.println("Opção escolhida: Sair");
                    break;
                default:
                    System.out.println("Opção inválida");
                    break;
            }
        } while (opcao != 3);

        input.close();
    }
}