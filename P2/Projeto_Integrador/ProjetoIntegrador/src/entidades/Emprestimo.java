package entidades;

public class Emprestimo
{
    private double valorEmprestimo;
    private int quantParcelas;
    private double taxaJuros;
    private double valorParcela;


    // Construtor da classe Empréstimo:

    public Emprestimo(double valorEmprestimo, int quantParcelas)
    {
        this.valorEmprestimo = valorEmprestimo;
        this.quantParcelas = quantParcelas;

        if (quantParcelas <= 12) {
            this.taxaJuros = 0.025; // 2.5% ao mês
        } else {
            this.taxaJuros = 0.03; // 3% ao mês
        }

        this.valorParcela = calcularValorParcela();
    }

    // Metodos da Classe Emprestimo:

    //Calcular o valor da parcela
    private double calcularValorParcela()
    {
        double valorParcela = (valorEmprestimo * taxaJuros * quantParcelas) / quantParcelas;
        return valorParcela;
    }

    public void imprimirInformacoes()
    {
        System.out.println("Valor do empréstimo: R$" + valorEmprestimo);
        System.out.println("Prazo de pagamento: " + quantParcelas + " meses");
        System.out.println("Taxa de juros: " + taxaJuros + "% ao mes");
        System.out.println("Valor da parcela: R$" + valorParcela);
    }

    //gets e sets:

    public double getValorEmprestimo() {
        return valorEmprestimo;
    }

    public void setValorEmprestimo(double valorEmprestimo) {
        this.valorEmprestimo = valorEmprestimo;
    }

    public int getQuantParcelas() {
        return quantParcelas;
    }

    public void setQuantParcelas(int quantParcelas) {
        this.quantParcelas = quantParcelas;
    }

    public double getTaxaJuros() {
        return taxaJuros;
    }

    public void setTaxaJuros(double taxaJuros) {
        this.taxaJuros = taxaJuros;
    }

    public double getValorParcela() {
        return valorParcela;
    }

    public void setValorParcela(double valorParcela) {
        this.valorParcela = valorParcela;
    }
}