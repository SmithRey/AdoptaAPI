using ApisPedido.Data;
using ApisPedido.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ApisPedido.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MascotasController : ControllerBase
    {
        private readonly AdoptaDbContext _context;

        public MascotasController(AdoptaDbContext context)
        {
            _context = context;
        }

        /// <summary>Lista todas las mascotas (evidencia Sprint 0: EF Core + Swagger).</summary>
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Mascota>>> GetMascotas()
        {
            var mascotas = await _context.Mascotas
                .AsNoTracking()
                .OrderBy(m => m.Nombre)
                .ToListAsync();

            return Ok(mascotas);
        }

        /// <summary>Lista solo mascotas disponibles para adopción.</summary>
        [HttpGet("disponibles")]
        public async Task<ActionResult<IEnumerable<Mascota>>> GetDisponibles()
        {
            var mascotas = await _context.Mascotas
                .AsNoTracking()
                .Where(m => m.Estado == "Disponible")
                .OrderBy(m => m.Nombre)
                .ToListAsync();

            return Ok(mascotas);
        }
    }
}
