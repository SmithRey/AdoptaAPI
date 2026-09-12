using AdoptaAPI.Data;
using AdoptaAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace AdoptaAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PedidoController : ControllerBase
    {
        private readonly AdoptaDbContext _context;

        public PedidoController(AdoptaDbContext context)
        {
            _context = context;
        }

        /// <summary>Crea una solicitud de adopción (pedido) para una mascota.</summary>
        [HttpPost]
        public async Task<ActionResult<SolicitudAdopcion>> CrearPedido([FromBody] PedidoAdopcion pedido)
        {
            if (pedido.IdMascota <= 0 || pedido.IdUsuario <= 0)
            {
                return BadRequest("Debe indicar IdMascota e IdUsuario.");
            }

            var mascota = await _context.Mascotas.FindAsync(pedido.IdMascota);
            if (mascota is null)
            {
                return NotFound($"No existe la mascota {pedido.IdMascota}.");
            }

            if (mascota.Estado is "Adoptada" or "Retirada")
            {
                return BadRequest($"La mascota no está disponible para adopción (estado: {mascota.Estado}).");
            }

            var usuarioExiste = await _context.Usuarios.AnyAsync(u => u.IdUsuario == pedido.IdUsuario);
            if (!usuarioExiste)
            {
                return NotFound($"No existe el usuario {pedido.IdUsuario}.");
            }

            var solicitud = new SolicitudAdopcion
            {
                IdMascota = pedido.IdMascota,
                IdUsuario = pedido.IdUsuario,
                Mensaje = pedido.Mensaje,
                Estado = "Pendiente",
                FechaSolicitud = DateTime.UtcNow
            };

            _context.SolicitudesAdopcion.Add(solicitud);

            if (mascota.Estado == "Disponible")
            {
                mascota.Estado = "EnProceso";
            }

            await _context.SaveChangesAsync();

            solicitud.Mascota = null!;
            solicitud.Usuario = null!;

            return Created($"/api/Pedido/{solicitud.IdSolicitud}", solicitud);
        }
    }
}
