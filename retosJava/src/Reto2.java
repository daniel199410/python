import org.junit.Test;

import java.util.Calendar;
import java.util.Date;

import static org.junit.Assert.assertEquals;

public class Reto2 {
	@Test
	public void shouldGet30000() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("100513551", 18, "Carlos");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.JULY);
		calendar.set(Calendar.DAY_OF_MONTH, 18);
		Alquiler alquiler = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 1);
		assertEquals(30000, alquiler.CalcularCosto());
	}

	@Test
	public void shouldGet0() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("10009931", 14, "Charlie");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.JULY);
		calendar.set(Calendar.DAY_OF_MONTH, 18);
		Alquiler alquiler = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 1);
		assertEquals(0, alquiler.CalcularCosto());
	}

	@Test
	public void shouldGet450000() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica2 = new MotoAcuatica("PDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica3 = new MotoAcuatica("ZDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica4 = new MotoAcuatica("DDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("100513551", 18, "Carlos");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.JULY);
		calendar.set(Calendar.DAY_OF_MONTH, 18);
		Alquiler alquiler = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 1);
		Alquiler alquiler2 = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 2);
		calendar.set(Calendar.DAY_OF_MONTH, 19);
		Alquiler alquiler3 = new Alquiler(1, cliente, motoAcuatica2, calendar.getTime(), 4);
		calendar.set(Calendar.DAY_OF_MONTH, 14);
		Alquiler alquiler4 = new Alquiler(1, cliente, motoAcuatica3, calendar.getTime(), 3);
		calendar.set(Calendar.DAY_OF_MONTH, 26);
		Alquiler alquiler5 = new Alquiler(1, cliente, motoAcuatica4, calendar.getTime(), 4);
		Alquiler[] alquileres = new Alquiler[5];
		alquileres[0] = alquiler;
		alquileres[1] = alquiler2;
		alquileres[2] = alquiler3;
		alquileres[3] = alquiler4;
		alquileres[4] = alquiler5;

		calendar.set(Calendar.DAY_OF_MONTH, 16);
		Date min = calendar.getTime();
		calendar.set(Calendar.DAY_OF_MONTH, 20);
		Date max = calendar.getTime();

		assertEquals(450000, Alquiler.VentasPorDias(alquileres, min, max));
	}

	@Test
	public void shouldGet540000() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica2 = new MotoAcuatica("PDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica3 = new MotoAcuatica("ZDA432", "RXT", "Sea-Doo");
		MotoAcuatica motoAcuatica4 = new MotoAcuatica("DDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("100513551", 18, "Carlos");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.JULY);
		calendar.set(Calendar.DAY_OF_MONTH, 18);
		Alquiler alquiler = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 1);
		Alquiler alquiler2 = new Alquiler(1, cliente, motoAcuatica, calendar.getTime(), 2);
		calendar.set(Calendar.DAY_OF_MONTH, 19);
		Alquiler alquiler3 = new Alquiler(1, cliente, motoAcuatica2, calendar.getTime(), 4);
		calendar.set(Calendar.DAY_OF_MONTH, 14);
		Alquiler alquiler4 = new Alquiler(1, cliente, motoAcuatica3, calendar.getTime(), 3);
		calendar.set(Calendar.DAY_OF_MONTH, 26);
		Alquiler alquiler5 = new Alquiler(1, cliente, motoAcuatica4, calendar.getTime(), 4);
		Alquiler[] alquileres = new Alquiler[5];
		alquileres[0] = alquiler;
		alquileres[1] = alquiler2;
		alquileres[2] = alquiler3;
		alquileres[3] = alquiler4;
		alquileres[4] = alquiler5;

		calendar.set(Calendar.DAY_OF_MONTH, 19);
		Date min = calendar.getTime();
		calendar.set(Calendar.DAY_OF_MONTH, 26);
		Date max = calendar.getTime();

		assertEquals(540000, Alquiler.VentasPorDias(alquileres, min, max));
	}
}
