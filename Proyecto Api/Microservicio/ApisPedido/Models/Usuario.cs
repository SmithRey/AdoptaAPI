namespace ApisPedido.Models
{
    public class Usuario
    {
        public int IdUsuario { get; set; }
        public string Nombre { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string? Telefono { get; set; }
        public string Ciudad { get; set; } = string.Empty;

        public Fundacion? Fundacion { get; set; }
        public ICollection<SolicitudAdopcion> Solicitudes { get; set; } = new List<SolicitudAdopcion>();
    }
}
