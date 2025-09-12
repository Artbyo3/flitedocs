# 🔧 Configuración de Variables de Entorno

## Archivo .env (Desarrollo Local)

Crea un archivo `.env` en la raíz del proyecto con:

```env
# Flask Configuration
SECRET_KEY=tu-clave-secreta-aqui-cambiar-en-produccion
FLASK_ENV=development

# Database (si necesitas en el futuro)
# DATABASE_URL=sqlite:///flitedocs.db
```

## Variables de Entorno en Vercel

En el dashboard de Vercel, configura:

- `SECRET_KEY` - Tu clave secreta de producción
- `FLASK_ENV` - Establecer como 'production'

## Generar SECRET_KEY

Para generar una SECRET_KEY segura:

```python
import secrets
print(secrets.token_hex(32))
```

## Seguridad

- ✅ El archivo `.env` está en `.gitignore`
- ✅ No se sube a GitHub
- ✅ Las variables de Vercel están encriptadas
- ❌ Nunca commites el archivo `.env`
