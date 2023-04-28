package entidades;

import java.util.List;

public class Serie extends Video {
    private int temporada;
    private int episodios;

    public Serie(String titulo, String diretor, List<String> elenco, String genero, String sinopse, int ano, int classificacaoIndicativa, int temporada, int episodios) {
        super(titulo, diretor, elenco, genero, sinopse, ano, classificacaoIndicativa);
        this.temporada = temporada;
        this.episodios = episodios;
    }

    public int getTemporada() {
        return temporada;
    }

    public void setTemporada(int temporada) {
        this.temporada = temporada;
    }

    public int getEpisodios() {
        return episodios;
    }

    public void setEpisodios(int episodios) {
        this.episodios = episodios;
    }

    public String toString() {
        return "Série: " + super.getTitulo() + " - Temporada: " + this.temporada + " - Episódios: " + this.episodios;
    }
}