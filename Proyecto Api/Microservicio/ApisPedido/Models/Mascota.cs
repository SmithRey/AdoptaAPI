namespace ApisPedido.Models
{
    public class Mascota
    {
        public int IdMascota { get; set; }
        public int IdFundacion { get; set; }
        public string Nombre { get; set; } = string.Empty;
        public string Especie { get; set; } = string.Empty;
        public int Edad { get; set; }
        public string Tamano { get; set; } = string.Empty;
        public string Ciudad { get; set; } = string.Empty;
        public string? Descripcion { get; set; }
        public string Estado { get; set; } = "Disponible";
        public DateTime FechaRegistro { get; set; }

        public Fundacion Fundacion { get; set; } = null!;
        public ICollection<SolicitudAdopcion> Solicitudes { get; set; } = new List<SolicitudAdopcion>();
    }
}
