using System.Net.Http.Json;
using ApisPedido.Models;
using Microsoft.AspNetCore.Mvc;

namespace ApisPedido.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PedidoController : ControllerBase
    {
        private readonly HttpClient _httpClient;
        private readonly IConfiguration _config;

        public PedidoController(HttpClient httpClient, IConfiguration config)
        {
            _httpClient = httpClient;
            _config = config;
        }

        [HttpPost]
        public async Task<IActionResult> CrearPedido([FromBody] Pedido pedido)
        {
            // Validación básica
            if (pedido == null || string.IsNullOrEmpty(pedido.Producto))
            {
                return BadRequest("El pedido no es válido");
            }

            decimal precioFinal;

            // Leer configuración
            bool usarMicroservicio = _config.GetValue<bool>("UsarMicroservicio");

            if (usarMicroservicio)
            {
                try
                {
                    var url = _config.GetValue<string>("UrlMicroservicio");
                    var response = await _httpClient.PostAsJsonAsync(url, pedido);

                    if (!response.IsSuccessStatusCode)
                    {
                        return StatusCode((int)response.StatusCode, "Error en microservicio");
                    }

                    precioFinal = await response.Content.ReadFromJsonAsync<decimal>();
                }
                catch (Exception)
                {
                    // Fallback si falla el microservicio
                    precioFinal = CalcularLocal(pedido);
                }
            }
            else
            {
                // Lógica local (sin microservicio)
                precioFinal = CalcularLocal(pedido);
            }

            return Ok(new
            {
                pedido.Producto,
                pedido.Precio,
                PrecioFinal = precioFinal,
                Modo = usarMicroservicio ? "Microservicio" : "Local"
            });
        }

        // Método reutilizable para cálculo local
        private decimal CalcularLocal(Pedido pedido)
        {
            decimal descuento = 0;
            if (pedido.Precio > 100)
                descuento = pedido.Precio * 0.1m;
            return pedido.Precio - descuento;
        }
    }

    public class Pedido
    {
        public string Producto { get; set; }
        public decimal Precio { get; set; }
    }
}