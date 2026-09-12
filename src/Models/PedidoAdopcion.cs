namespace AdoptaAPI.Models
{
    /// <summary>Pedido de adopción: un usuario solicita una mascota.</summary>
    public class PedidoAdopcion
    {
        public int IdMascota { get; set; }
        public int IdUsuario { get; set; }
        public string? Mensaje { get; set; }
    }
}
