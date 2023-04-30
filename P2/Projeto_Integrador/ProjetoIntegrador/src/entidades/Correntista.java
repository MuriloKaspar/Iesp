package entidades;

public class Correntista
{
    private static int counter = 1; //primeiro cliente terá o numero 1
    private String nome;
    private String cpf;
    private String email;


    //--Construtor--
    public Correntista(String nome, String cpf, String email)
    {
        this.nome = nome;
        this.cpf = cpf;
        this.email = email;
        counter += 1; //Cada novo cliente o contador sobe +1
    }


    //--Gets e Sets--
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


    //--Apresentação dos dados--
    public String toString()
    {
        return "\nNome: " + this.getNome() +
               "\nCPF: " + this.getCpf() +
               "\nEmail: "+ this.getEmail();
    }
}
