import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.assertEquals;

public class Reto4 {
    @Test
    public void shouldGet1() {
        int[] edades = {44, 57, 33, 42, 24, 23, 45, 18, 86, 32, 25, 20, 19};
        List<Cliente> clienteList = new ArrayList<>();
        Alquiler[] alquileres = new Alquiler[edades.length];
        MotoAcuatica motoAcuatica = new MotoAcuatica("", "", "");
        for(int i = 0; i < edades.length; i++) {
            alquileres[i] = new Alquiler(i, new Cliente("123", edades[i], "Nombre"), motoAcuatica, i);
        }
        assertEquals(1, Alquiler.ObtenerPublicoObjetivo(alquileres));
    }
}
