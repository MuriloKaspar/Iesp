package entidades;

import java.util.ArrayList;
import java.util.Scanner;

public class Usuario
{
    private ArrayList<Usuario> contas = new ArrayList<Usuario>();
    private String nome;
    private String email;
    private String senha;
    private ArrayList<String> favoritos;

    //--Construtor:--


    public Usuario() {
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.favoritos = new ArrayList<>();
    }


    //--Metodos:--
    public void criarConta() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o nome do titular da conta:");
        this.nome = scanner.nextLine();

        System.out.println("Digite o email titular da conta:");
        this.email = scanner.nextLine();

        System.out.println("Digite a senha:");
        this.senha = scanner.nextLine();

        Usuario conta = new Usuario();
        contas.add(conta);

        System.out.println("Conta criada com sucesso!");
    }

    public void login() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite seu email:");
        String emailDigitado = scanner.nextLine();

        System.out.println("Digite sua senha:");
        String senhaDigitada = scanner.nextLine();

        for (Usuario conta : contas) {
            if (conta.getEmail().equals(emailDigitado) && conta.getSenha().equals(senhaDigitada)) {
                System.out.println("Login realizado com sucesso!");
                return;
            }
        }

        System.out.println("Email ou senha incorretos.");
    }

    //--gets e setts:--
    public ArrayList<Usuario> getContas() {
        return contas;
    }

    public void setContas(ArrayList<Usuario> contas) {
        this.contas = contas;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public ArrayList<String> getFavoritos() {
        return favoritos;
    }

    public void setFavoritos(ArrayList<String> favoritos) {
        this.favoritos = favoritos;
    }
}