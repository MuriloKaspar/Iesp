package entidades;

import java.util.ArrayList;
import java.util.List;

public class Playlist {
    private String nome;
    private List<Video> listaDeReproducao;

    public Playlist(String nome) {
        this.nome = nome;
        this.listaDeReproducao = new ArrayList<>();
    }

    public void adicionarVideo(Video video) {
        listaDeReproducao.add(video);
    }

    public void removerVideo(int index) {
        listaDeReproducao.remove(index);
    }

    public void reproduzir() {
        if (listaDeReproducao.isEmpty()) {
            System.out.println("A lista de reprodução está vazia!");
        } else {
            for (Video video : listaDeReproducao) {
                System.out.println("Reproduzindo: " + video.getTitulo());
            }
        }
    }
}