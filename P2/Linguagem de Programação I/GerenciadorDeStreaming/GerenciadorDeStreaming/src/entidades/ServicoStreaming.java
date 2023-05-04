package entidades;

import java.util.ArrayList;
import java.util.List;

public class ServicoStreaming {
    private List<Video> listaVideos;
    private List<Usuario> listaUsuarios;
    private List<Acesso> listaAcessos;

    public ServicoStreaming() {
        this.listaVideos = new ArrayList<>();
        this.listaUsuarios = new ArrayList<>();
        this.listaAcessos = new ArrayList<>();
    }

    // getters e setters
    public List<Video> getListaVideos() {
        return listaVideos;
    }

    public void setListaVideos(List<Video> listaVideos) {
        this.listaVideos = listaVideos;
    }

    public List<Usuario> getListaUsuarios() {
        return listaUsuarios;
    }

    public void setListaUsuarios(List<Usuario> listaUsuarios) {
        this.listaUsuarios = listaUsuarios;
    }

    public List<Acesso> getListaAcessos() {
        return listaAcessos;
    }

    public void setListaAcessos(List<Acesso> listaAcessos) {
        this.listaAcessos = listaAcessos;
    }
}