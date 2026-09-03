using System.Text.Json.Serialization;
using ApisPedido.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers().AddJsonOptions(options =>
{
    options.JsonSerializerOptions.ReferenceHandler = ReferenceHandler.IgnoreCycles;
});
builder.Services.AddHttpClient();
builder.Services.AddTransient(sp => sp.GetRequiredService<IHttpClientFactory>().CreateClient());
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "AdoptaAPI",
        Version = "v1",
        Description = "API de adopción de mascotas. Sprint 0: .NET 8, EF Core y Swagger."
    });
});

builder.Services.AddDbContext<AdoptaDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("AdoptaAPI")));

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "AdoptaAPI v1");
        options.DocumentTitle = "AdoptaAPI";
    });
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
