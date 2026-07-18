from api.api import app

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 INICIANDO SISTEMA DE TRADING INSTITUCIONAL 🚀")
    print("=" * 50)
    # CORREGIDO: Actualizado el enlace al puerto 5001
    print("🌐 Servidor web activo en: http://127.0.0.1:5001")
    print("💡 Presiona CTRL+C para detener el bot en cualquier momento.")
    print("=" * 50)
    
    # CORREGIDO: Cambiado de 5000 a 5001
    app.run(debug=True, port=5001)