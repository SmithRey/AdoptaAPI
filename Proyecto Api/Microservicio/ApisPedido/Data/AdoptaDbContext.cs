using ApisPedido.Models;
using Microsoft.EntityFrameworkCore;

namespace ApisPedido.Data
{
    public class AdoptaDbContext : DbContext
    {
        public AdoptaDbContext(DbContextOptions<AdoptaDbContext> options) : base(options)
        {
        }

        public DbSet<Usuario> Usuarios => Set<Usuario>();
        public DbSet<Fundacion> Fundaciones => Set<Fundacion>();
        public DbSet<Mascota> Mascotas => Set<Mascota>();
        public DbSet<SolicitudAdopcion> SolicitudesAdopcion => Set<SolicitudAdopcion>();

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Usuario>(entity =>
            {
                entity.ToTable("USUARIO");
                entity.HasKey(e => e.IdUsuario);
                entity.Property(e => e.IdUsuario).HasColumnName("Id_Usuario");
                entity.Property(e => e.Nombre).HasMaxLength(150).IsRequired();
                entity.Property(e => e.Email).HasMaxLength(255).IsRequired();
                entity.Property(e => e.Telefono).HasMaxLength(20);
                entity.Property(e => e.Ciudad).HasMaxLength(100).IsRequired();
                entity.HasIndex(e => e.Email).IsUnique();
            });

            modelBuilder.Entity<Fundacion>(entity =>
            {
                entity.ToTable("FUNDACION");
                entity.HasKey(e => e.IdFundacion);
                entity.Property(e => e.IdFundacion).HasColumnName("Id_Fundacion");
                entity.Property(e => e.IdUsuario).HasColumnName("Id_Usuario");
                entity.Property(e => e.Nombre).HasMaxLength(200).IsRequired();
                entity.HasIndex(e => e.IdUsuario).IsUnique();
                entity.HasOne(e => e.Usuario)
                    .WithOne(u => u.Fundacion)
                    .HasForeignKey<Fundacion>(e => e.IdUsuario)
                    .OnDelete(DeleteBehavior.Restrict);
            });

            modelBuilder.Entity<Mascota>(entity =>
            {
                entity.ToTable("MASCOTA");
                entity.HasKey(e => e.IdMascota);
                entity.Property(e => e.IdMascota).HasColumnName("Id_Mascota");
                entity.Property(e => e.IdFundacion).HasColumnName("Id_Fundacion");
                entity.Property(e => e.Nombre).HasMaxLength(150).IsRequired();
                entity.Property(e => e.Especie).HasMaxLength(50).IsRequired();
                entity.Property(e => e.Tamano).HasMaxLength(20).IsRequired();
                entity.Property(e => e.Ciudad).HasMaxLength(100).IsRequired();
                entity.Property(e => e.Estado).HasMaxLength(20).IsRequired();
                entity.Property(e => e.FechaRegistro)
                    .HasColumnType("datetime2")
                    .HasDefaultValueSql("SYSUTCDATETIME()");
                entity.ToTable(t =>
                {
                    t.HasCheckConstraint("CK_MASCOTA_Edad", "[Edad] >= 0 AND [Edad] <= 50");
                    t.HasCheckConstraint("CK_MASCOTA_Estado", "[Estado] IN ('Disponible','EnProceso','Adoptada','Retirada')");
                    t.HasCheckConstraint("CK_MASCOTA_Tamano", "[Tamano] IN ('Pequeno','Mediano','Grande')");
                });
                entity.HasOne(e => e.Fundacion)
                    .WithMany(f => f.Mascotas)
                    .HasForeignKey(e => e.IdFundacion)
                    .OnDelete(DeleteBehavior.Restrict);
            });

            modelBuilder.Entity<SolicitudAdopcion>(entity =>
            {
                entity.ToTable("SOLICITUD_ADOPCION");
                entity.HasKey(e => e.IdSolicitud);
                entity.Property(e => e.IdSolicitud).HasColumnName("Id_Solicitud");
                entity.Property(e => e.IdMascota).HasColumnName("Id_Mascota");
                entity.Property(e => e.IdUsuario).HasColumnName("Id_Usuario");
                entity.Property(e => e.Estado).HasMaxLength(20).IsRequired();
                entity.Property(e => e.FechaSolicitud)
                    .HasColumnType("datetime2")
                    .HasDefaultValueSql("SYSUTCDATETIME()");
                entity.ToTable(t =>
                    t.HasCheckConstraint("CK_SOLICITUD_Estado",
                        "[Estado] IN ('Pendiente','EnRevision','Aprobada','Rechazada','Completada')"));
                entity.HasOne(e => e.Mascota)
                    .WithMany(m => m.Solicitudes)
                    .HasForeignKey(e => e.IdMascota)
                    .OnDelete(DeleteBehavior.Restrict);
                entity.HasOne(e => e.Usuario)
                    .WithMany(u => u.Solicitudes)
                    .HasForeignKey(e => e.IdUsuario)
                    .OnDelete(DeleteBehavior.Restrict);
            });
        }
    }
}
