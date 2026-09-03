namespace ApisPedido.Models
{
    public class SolicitudAdopcion
    {
        public int IdSolicitud { get; set; }
        public int IdMascota { get; set; }
        public int IdUsuario { get; set; }
        public string Estado { get; set; } = "Pendiente";
        public string? Mensaje { get; set; }
        public DateTime FechaSolicitud { get; set; }

        public Mascota Mascota { get; set; } = null!;
        public Usuario Usuario { get; set; } = null!;
    }
}
