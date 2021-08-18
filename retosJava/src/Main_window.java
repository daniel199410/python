import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Date;

public class Main_window {
	private Cliente cliente;
	private MotoAcuatica motoAcuatica;
	private Alquiler[] alquileres;

	private JPanel panel;
	private JTextField cedulaTextField;
	private JTextField nombreTextFields;
	private JTextField edadTextField;
	private JButton botonCrearInstanciaButton;
	private JButton botonSiguienteVistaButton;
	private JTextField identificadorTextField;
	private JTextField modeloTextField;
	private JTextField marcaTextField;
	private JButton botonCrearInstanciaMotoButton;
	private JButton botonSiguienteVistaMotoButton;
	private JPanel panelMoto;
	private JPanel panelCliente;
	private JPanel vistaAlquileres;
	private JTextField tamanoArregloTextField;
	private JButton botonInstanciarArregloButton;
	private JTextField idAlquilerTextField;
	private JTextField fechaAlquilerTextField;
	private JTextField horaAlquilerTextField;
	private JTextField indiceAlquilerTextField;
	private JButton botonCrearInstanciaAlquilerButton;
	private JTextField textField1;
	private JButton botónConsultarButton;
	private JLabel idAlquilerLabel;
	private JLabel motoAcuaticaLabel;
	private JLabel fechaLabel;
	private JLabel horasAlquilerLabel;
	private JLabel clienteLabel;
	private JButton irAVistaClientesButton;
	private JButton irAVistaMotosButton;
	private JButton irSiguienteVistaButton;
	private JPanel vistaAdmin;
	private JTextField fechaInicialTextField;
	private JTextField fechaFinalTextField;
	private JButton botónConsultarButton1;
	private JLabel ventasAcumuladasLabel;

	public Main_window() {
		botonCrearInstanciaButton.addActionListener(e -> {
			String cedula = cedulaTextField.getText();
			int edad = Integer.parseInt(edadTextField.getText());
			String nombre = nombreTextFields.getText();
			cliente = new Cliente(cedula, edad, nombre);
		});
		botonSiguienteVistaButton.addActionListener(e -> {
			panelMoto.setVisible(true);
			panelCliente.setVisible(false);
		});
		botonCrearInstanciaMotoButton.addActionListener(e -> {
			motoAcuatica = new MotoAcuatica(identificadorTextField.getText(), modeloTextField.getText(), marcaTextField.getText());
		});
		botonSiguienteVistaMotoButton.addActionListener(e -> {
			panelMoto.setVisible(false);
			vistaAlquileres.setVisible(true);
		});
		botonInstanciarArregloButton.addActionListener(e -> {
			int longitud = Integer.parseInt(tamanoArregloTextField.getText());
			alquileres = new Alquiler[longitud];
		});
		botonCrearInstanciaAlquilerButton.addActionListener(e -> {
			int id = Integer.parseInt(idAlquilerTextField.getText());
			int horas = Integer.parseInt(horaAlquilerTextField.getText());
			alquileres[Integer.parseInt(indiceAlquilerTextField.getText())] = new Alquiler(id, cliente, motoAcuatica, horas);
		});
		botónConsultarButton.addActionListener(e -> {
			Alquiler alquiler = alquileres[Integer.parseInt(indiceAlquilerTextField.getText())];
			idAlquilerLabel.setText(String.format("Id: %d", alquiler.getId()));
			clienteLabel.setText(String.format("Cliente: %s", alquiler.getCliente().getNombre()));
			motoAcuaticaLabel.setText(String.format("Moto: %s", alquiler.getMoto().getIdentificador()));
			fechaLabel.setText(String.format("Fecha %tF", alquiler.getFecha()));
			horasAlquilerLabel.setText(String.format("HorasAlquiler: %d", alquiler.getHorasAlquiler()));
		});
		irAVistaClientesButton.addActionListener(e -> {
			vistaAlquileres.setVisible(false);
			panelCliente.setVisible(true);
		});
		irAVistaMotosButton.addActionListener(e -> {
			vistaAlquileres.setVisible(false);
			panelMoto.setVisible(true);
		});
		irSiguienteVistaButton.addActionListener(e -> {
			vistaAlquileres.setVisible(false);
			vistaAdmin.setVisible(true);
		});
	}

	public static void main(String[] args) {
		JFrame jFrame = new JFrame("Frame");
		jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		jFrame.setContentPane(new Main_window().panel);
		jFrame.pack();
		jFrame.setVisible(true);
	}
}
