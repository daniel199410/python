import org.junit.Test;

import java.util.Calendar;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;

public class Reto3 {
	@Test
	public void shouldGetJuan() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("15536614", 14, "Juanito");
		Cliente cliente2 = new Cliente("35214", 43, "Juan");
		Cliente cliente3 = new Cliente("121344", 23, "Carlos");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.JULY);
		calendar.set(Calendar.DAY_OF_MONTH, 31);
		Alquiler alquiler = new Alquiler(23, cliente, motoAcuatica, calendar.getTime(), 2);
		Alquiler alquiler2 = new Alquiler(24, cliente2, motoAcuatica, calendar.getTime(), 2);
		Alquiler alquiler3 = new Alquiler(24, cliente3, motoAcuatica, calendar.getTime(), 4);
		Alquiler[] alquileres = {alquiler, alquiler2, alquiler3};
		assertEquals(cliente2, Alquiler.DescuentoClient(alquileres));
	}

	@Test
	public void shouldGetNull() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("15536614", 14, "Juanito");
		Cliente cliente2 = new Cliente("35214", 16, "Juan");
		Cliente cliente3 = new Cliente("121344", 17, "Carlos");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.AUGUST);
		calendar.set(Calendar.DAY_OF_MONTH, 1);
		Alquiler alquiler = new Alquiler(23, cliente, motoAcuatica, calendar.getTime(), 4);
		Alquiler alquiler2 = new Alquiler(24, cliente2, motoAcuatica, calendar.getTime(), 4);
		calendar.set(Calendar.DAY_OF_MONTH, 31);
		Alquiler alquiler3 = new Alquiler(24, cliente3, motoAcuatica, calendar.getTime(), 4);
		Alquiler[] alquileres = {alquiler, alquiler2, alquiler3};
		assertNull(Alquiler.DescuentoClient(alquileres));
	}

	@Test
	public void shouldGetFelipe() {
		MotoAcuatica motoAcuatica = new MotoAcuatica("LDA432", "RXT", "Sea-Doo");
		Cliente cliente = new Cliente("15536614", 18, "Alexander");
		Cliente cliente2 = new Cliente("35214", 26, "Aaron");
		Cliente cliente3 = new Cliente("121344", 32, "Felipe");
		Calendar calendar = Calendar.getInstance();
		calendar.set(Calendar.YEAR, 2021);
		calendar.set(Calendar.MONTH, Calendar.AUGUST);
		calendar.set(Calendar.DAY_OF_MONTH, 2);
		Alquiler alquiler = new Alquiler(23, cliente, motoAcuatica, calendar.getTime(), 5);
		Alquiler alquiler2 = new Alquiler(24, cliente2, motoAcuatica, calendar.getTime(), 4);
		Alquiler alquiler3 = new Alquiler(24, cliente3, motoAcuatica, calendar.getTime(), 1);
		Alquiler[] alquileres = {alquiler, alquiler2, alquiler3};
		assertEquals(cliente3, Alquiler.DescuentoClient(alquileres));
	}
}
