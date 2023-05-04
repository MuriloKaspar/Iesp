package entidades;

import java.util.List;

public class Filme extends Video {

    public Filme(String titulo, String diretor, List<String> elenco, String genero, String sinopse, int ano, int classificacaoIndicativa) {

        super(titulo, diretor, elenco, genero, sinopse, ano, classificacaoIndicativa);

    }
}