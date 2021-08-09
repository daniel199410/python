public class Cliente {
	private final String Cedula;
	private final int Edad;
	private final String Nombre;

	public Cliente(String cedula, int edad, String nombre) {
		Cedula = cedula;
		Edad = edad;
		Nombre = nombre;
	}

	public String getCedula() {
		return Cedula;
	}

	public int getEdad() {
		return Edad;
	}

	public String getNombre() {
		return Nombre;
	}
}
