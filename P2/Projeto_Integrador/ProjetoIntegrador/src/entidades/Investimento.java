package entidades;

import java.util.ArrayList;

public class Investimento {

    private String tipoInvestimento;
    private double valorAplicado;
    private double taxaJuros;
    private int prazoVencimento;
    private ArrayList<Double> historicoInvestimentos;

    public Investimento(String tipoInvestimento, double valorAplicado, double taxaJuros, int prazoVencimento) {
        this.tipoInvestimento = tipoInvestimento;
        this.valorAplicado = valorAplicado;
        this.taxaJuros = taxaJuros;
        this.prazoVencimento = prazoVencimento;
        this.historicoInvestimentos = new ArrayList<>();
    }

    public double consultarRentabilidade() {
        double juros = this.valorAplicado * this.taxaJuros;
        return this.valorAplicado + juros;
    }

    public boolean resgatarInvestimento() {
        if (this.valorAplicado > 0) {
            this.historicoInvestimentos.add(-1 * this.valorAplicado);
            this.valorAplicado = 0;
            return true;
        }
        return false;
    }

    public boolean adicionarInvestimento(double valorInvestimento) {
        if (valorInvestimento > 0) {
            this.historicoInvestimentos.add(valorInvestimento);
            this.valorAplicado += valorInvestimento;
            return true;
        }
        return false;
    }

    public String getTipoInvestimento() {
        return tipoInvestimento;
    }

    public double getValorAplicado() {
        return valorAplicado;
    }

    public double getTaxaJuros() {
        return taxaJuros;
    }

    public int getPrazoVencimento() {
        return prazoVencimento;
    }

    public ArrayList<Double> getHistoricoInvestimentos() {
        return historicoInvestimentos;
    }
}
