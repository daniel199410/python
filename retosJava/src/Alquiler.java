import java.util.Date;

public class Alquiler {
	private final int Id;
	private final Cliente Cliente;
	private final MotoAcuatica Moto;
	private final Date Fecha;
	private final int HorasAlquiler;

	public Alquiler(int id, Cliente cliente, MotoAcuatica moto, int horasAlquiler) {
		Id = id;
		Cliente = cliente;
		Moto = moto;
		HorasAlquiler = horasAlquiler;
		this.Fecha = new Date();
	}

	public Alquiler(int id, Cliente cliente, MotoAcuatica moto, Date fecha, int horasAlquiler) {
		Id = id;
		Cliente = cliente;
		Moto = moto;
		Fecha = fecha;
		HorasAlquiler = horasAlquiler;
	}

	public int getId() {
		return Id;
	}

	public Cliente getCliente() {
		return Cliente;
	}

	public MotoAcuatica getMoto() {
		return Moto;
	}

	public Date getFecha() {
		return Fecha;
	}

	public int getHorasAlquiler() {
		return HorasAlquiler;
	}

	public int CalcularCosto() {
		if(this.Cliente.getEdad() < 18) {
			return 0;
		}
		return switch (this.Moto.getIdentificador().charAt(0)) {
			case 'L' -> 30000 * this.HorasAlquiler;
			case 'D' -> 45000 * this.HorasAlquiler;
			case 'P' -> 90000 * this.HorasAlquiler;
			default -> 50000 * this.HorasAlquiler;
		};
	}

	public static int VentasPorRangoDias(Alquiler[] alquileres, Date min, Date max) {
		int count = 0;
		for (Alquiler alquiler : alquileres) {
			if (alquiler.Fecha.compareTo(min) >= 0 && alquiler.getFecha().compareTo(max) <= 0) {
				count += alquiler.CalcularCosto();
			}
		}
		return count;
	}

	public static Cliente DescuentoCliente(Alquiler[] alquileres) {
		Alquiler menor = null;
		for(Alquiler alquiler: alquileres) {
			if(alquiler.Cliente.getEdad() >= 18 && (menor == null || alquiler.HorasAlquiler < menor.HorasAlquiler)) {
				menor = alquiler;
			}
		}
		if(menor != null) {
			return menor.Cliente;
		}
		return null;
	}
}
