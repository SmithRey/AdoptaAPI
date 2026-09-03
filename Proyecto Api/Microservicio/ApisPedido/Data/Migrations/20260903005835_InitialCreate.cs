using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ApisPedido.Data.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "USUARIO",
                columns: table => new
                {
                    Id_Usuario = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Nombre = table.Column<string>(type: "nvarchar(150)", maxLength: 150, nullable: false),
                    Email = table.Column<string>(type: "nvarchar(255)", maxLength: 255, nullable: false),
                    Telefono = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: true),
                    Ciudad = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_USUARIO", x => x.Id_Usuario);
                });

            migrationBuilder.CreateTable(
                name: "FUNDACION",
                columns: table => new
                {
                    Id_Fundacion = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Id_Usuario = table.Column<int>(type: "int", nullable: false),
                    Nombre = table.Column<string>(type: "nvarchar(200)", maxLength: 200, nullable: false),
                    Descripcion = table.Column<string>(type: "nvarchar(max)", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_FUNDACION", x => x.Id_Fundacion);
                    table.ForeignKey(
                        name: "FK_FUNDACION_USUARIO_Id_Usuario",
                        column: x => x.Id_Usuario,
                        principalTable: "USUARIO",
                        principalColumn: "Id_Usuario",
                        onDelete: ReferentialAction.Restrict);
                });

            migrationBuilder.CreateTable(
                name: "MASCOTA",
                columns: table => new
                {
                    Id_Mascota = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Id_Fundacion = table.Column<int>(type: "int", nullable: false),
                    Nombre = table.Column<string>(type: "nvarchar(150)", maxLength: 150, nullable: false),
                    Especie = table.Column<string>(type: "nvarchar(50)", maxLength: 50, nullable: false),
                    Edad = table.Column<int>(type: "int", nullable: false),
                    Tamano = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false),
                    Ciudad = table.Column<string>(type: "nvarchar(100)", maxLength: 100, nullable: false),
                    Descripcion = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    Estado = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false),
                    FechaRegistro = table.Column<DateTime>(type: "datetime2", nullable: false, defaultValueSql: "SYSUTCDATETIME()")
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_MASCOTA", x => x.Id_Mascota);
                    table.CheckConstraint("CK_MASCOTA_Edad", "[Edad] >= 0 AND [Edad] <= 50");
                    table.CheckConstraint("CK_MASCOTA_Estado", "[Estado] IN ('Disponible','EnProceso','Adoptada','Retirada')");
                    table.CheckConstraint("CK_MASCOTA_Tamano", "[Tamano] IN ('Pequeno','Mediano','Grande')");
                    table.ForeignKey(
                        name: "FK_MASCOTA_FUNDACION_Id_Fundacion",
                        column: x => x.Id_Fundacion,
                        principalTable: "FUNDACION",
                        principalColumn: "Id_Fundacion",
                        onDelete: ReferentialAction.Restrict);
                });

            migrationBuilder.CreateTable(
                name: "SOLICITUD_ADOPCION",
                columns: table => new
                {
                    Id_Solicitud = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Id_Mascota = table.Column<int>(type: "int", nullable: false),
                    Id_Usuario = table.Column<int>(type: "int", nullable: false),
                    Estado = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false),
                    Mensaje = table.Column<string>(type: "nvarchar(max)", nullable: true),
                    FechaSolicitud = table.Column<DateTime>(type: "datetime2", nullable: false, defaultValueSql: "SYSUTCDATETIME()")
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_SOLICITUD_ADOPCION", x => x.Id_Solicitud);
                    table.CheckConstraint("CK_SOLICITUD_Estado", "[Estado] IN ('Pendiente','EnRevision','Aprobada','Rechazada','Completada')");
                    table.ForeignKey(
                        name: "FK_SOLICITUD_ADOPCION_MASCOTA_Id_Mascota",
                        column: x => x.Id_Mascota,
                        principalTable: "MASCOTA",
                        principalColumn: "Id_Mascota",
                        onDelete: ReferentialAction.Restrict);
                    table.ForeignKey(
                        name: "FK_SOLICITUD_ADOPCION_USUARIO_Id_Usuario",
                        column: x => x.Id_Usuario,
                        principalTable: "USUARIO",
                        principalColumn: "Id_Usuario",
                        onDelete: ReferentialAction.Restrict);
                });

            migrationBuilder.CreateIndex(
                name: "IX_FUNDACION_Id_Usuario",
                table: "FUNDACION",
                column: "Id_Usuario",
                unique: true);

            migrationBuilder.CreateIndex(
                name: "IX_MASCOTA_Id_Fundacion",
                table: "MASCOTA",
                column: "Id_Fundacion");

            migrationBuilder.CreateIndex(
                name: "IX_SOLICITUD_ADOPCION_Id_Mascota",
                table: "SOLICITUD_ADOPCION",
                column: "Id_Mascota");

            migrationBuilder.CreateIndex(
                name: "IX_SOLICITUD_ADOPCION_Id_Usuario",
                table: "SOLICITUD_ADOPCION",
                column: "Id_Usuario");

            migrationBuilder.CreateIndex(
                name: "IX_USUARIO_Email",
                table: "USUARIO",
                column: "Email",
                unique: true);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "SOLICITUD_ADOPCION");

            migrationBuilder.DropTable(
                name: "MASCOTA");

            migrationBuilder.DropTable(
                name: "FUNDACION");

            migrationBuilder.DropTable(
                name: "USUARIO");
        }
    }
}
