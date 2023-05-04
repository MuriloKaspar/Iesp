package utilitarios;

import java.text.DecimalFormat;
import java.text.NumberFormat;

public class Ferramentas

//Implementa formatação de Moeda (R$) e casas decimais aos valores numericos
{
    static NumberFormat formatarValor = new DecimalFormat("R$ #,##0.00");
    public static String doubleToString(Double valor)
    {
        return formatarValor.format(valor);
    }
}
