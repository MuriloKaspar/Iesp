package entidades;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Acesso
{
    private Usuario usuario;
    private String titulo;
    private LocalDateTime dataHora;

    public Acesso(Usuario usuario, String titulo)
    {
        this.usuario = usuario;
        this.titulo = titulo;
        this.dataHora = LocalDateTime.now();
    }



    public Usuario getUsuario(){
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public LocalDateTime getDataHora(){
        return dataHora;
    }

    public void setDataHora(LocalDateTime dataHora) {
        this.dataHora = dataHora;
    }

    @Override
    public String toString()
    {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        return "Usuário: " + usuario.getNome() + " - Título: " + titulo.getBytes() +
                " - Data de acesso: " + dataHora.format(formatter);
    }
}
