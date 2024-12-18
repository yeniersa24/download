from flask import Flask, request, send_file, render_template
import yt_dlp
import os

app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para procesar la descarga
@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    try:
        # Opciones para descargar el video
        options = {'outtmpl': 'downloads/%(title)s.%(ext)s'}
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>"

# Crear la carpeta de descargas si no existe
if not os.path.exists('downloads'):
    os.makedirs('downloads')

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
