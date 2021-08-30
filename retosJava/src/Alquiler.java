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
		switch (this.Moto.getIdentificador().charAt(0)) {
			case 'L': return  30000 * this.HorasAlquiler;
			case 'D': return 45000 * this.HorasAlquiler;
			case 'P': return 90000 * this.HorasAlquiler;
			default: return 50000 * this.HorasAlquiler;
		}
	}

	public static int VentasPorDias(Alquiler[] alquileres, Date min, Date max) {
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

    public static int ObtenerPublicoObjetivo(Alquiler[] alquileres) {
        int[] publicoObjetivo = {0, 0, 0, 0};
        for(Alquiler alquiler: alquileres) {
            if(alquiler.Cliente.getEdad() >= 18 && alquiler.Cliente.getEdad() <= 30) {
                publicoObjetivo[0] += 1;
            }
            if(alquiler.Cliente.getEdad() >= 31 && alquiler.Cliente.getEdad() <= 45) {
                publicoObjetivo[1] += 1;
            }
            if(alquiler.Cliente.getEdad() >= 46 && alquiler.Cliente.getEdad() <= 60) {
                publicoObjetivo[2] += 1;
            }
            if(alquiler.Cliente.getEdad() >= 61) {
                publicoObjetivo[3] += 1;
            }
        }
        int menor = 1;
        for(int i = 1; i < publicoObjetivo.length; i++) {
            if (publicoObjetivo[i] > publicoObjetivo[i - 1]) {
                menor = i + 1;
            }
        }
        return menor;
    }
}
