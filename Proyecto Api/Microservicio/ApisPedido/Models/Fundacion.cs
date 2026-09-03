namespace ApisPedido.Models
{
    public class Fundacion
    {
        public int IdFundacion { get; set; }
        public int IdUsuario { get; set; }
        public string Nombre { get; set; } = string.Empty;
        public string? Descripcion { get; set; }

        public Usuario Usuario { get; set; } = null!;
        public ICollection<Mascota> Mascotas { get; set; } = new List<Mascota>();
    }
}
