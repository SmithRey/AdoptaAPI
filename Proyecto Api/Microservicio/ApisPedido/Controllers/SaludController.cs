using Microsoft.AspNetCore.Mvc;

namespace ApisPedido.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class SaludController : ControllerBase
    {
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new
            {
                estado = "ok",
                proyecto = "AdoptaAPI",
                sprint = "Sprint 0",
                stack = new[] { ".NET 8", "EF Core", "Swagger" }
            });
        }
    }
}
