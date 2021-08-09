package reto2;

public class MotoAcuatica {
	private final String Identificador;
	private final String Modelo;
	private final String Marca;

	public MotoAcuatica(String identificador, String modelo, String marca) {
		Identificador = identificador;
		Modelo = modelo;
		Marca = marca;
	}

	public String getIdentificador() {
		return Identificador;
	}

	public String getModelo() {
		return Modelo;
	}

	public String getMarca() {
		return Marca;
	}
}
