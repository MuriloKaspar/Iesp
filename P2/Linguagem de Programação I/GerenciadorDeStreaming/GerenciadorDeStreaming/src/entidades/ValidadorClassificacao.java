package entidades;

public class ValidadorClassificacao {

    public static boolean validarClassificacao(String classificacao, int idadeUsuario) {
        if (classificacao.equalsIgnoreCase("Livre")) {
            return true;
        } else if (classificacao.equalsIgnoreCase("10 anos") && idadeUsuario >= 10) {
            return true;
        } else if (classificacao.equalsIgnoreCase("12 anos") && idadeUsuario >= 12) {
            return true;
        } else if (classificacao.equalsIgnoreCase("14 anos") && idadeUsuario >= 14) {
            return true;
        } else if (classificacao.equalsIgnoreCase("16 anos") && idadeUsuario >= 16) {
            return true;
        } else if (classificacao.equalsIgnoreCase("18 anos") && idadeUsuario >= 18) {
            return true;
        } else {
            return false;
        }
    }

}