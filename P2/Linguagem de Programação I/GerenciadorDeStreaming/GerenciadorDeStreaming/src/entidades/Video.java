package entidades;

import java.util.List;

public class Video //título, diretor, elenco, gênero, sinopse, ano de lançamento e classificação indicativa.
{
    private String titulo;
    private String diretor;
    private List<String> elenco;
    private String genero;
    private String sinopse;
    private int ano;
    private int classificacaoInd;

    public Video (String titulo, String diretor, List<String> elenco, String genero, String sinopse, int ano, int classificacaoInd)
    {
        this.titulo = titulo;
        this.diretor = diretor;
        this.elenco = elenco;
        this.genero = genero;
        this.sinopse = sinopse;
        this.ano = ano;
        this.classificacaoInd = classificacaoInd;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDiretor() {
        return diretor;
    }

    public void setDiretor(String diretor) {
        this.diretor = diretor;
    }

    public List<String> getElenco() {
        return elenco;
    }

    public void setElenco(List<String> elenco) {
        this.elenco = elenco;
    }

    public String getGenero() {
        return genero;
    }

    public void setGenero(String genero) {
        this.genero = genero;
    }

    public String getSinopse() {
        return sinopse;
    }

    public void setSinopse(String sinopse) {
        this.sinopse = sinopse;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public int getClassificacaoInd() {
        return classificacaoInd;
    }

    public void setClassificacaoInd(int classificacaoInd) {
        this.classificacaoInd = classificacaoInd;
    }
}