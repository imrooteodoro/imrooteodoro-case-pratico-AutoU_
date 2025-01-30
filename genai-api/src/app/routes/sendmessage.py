import os
from flask import request, render_template
from werkzeug.utils import secure_filename
from controllers.agentcontroller import AgentController
from auth.auth import connect_to_model_api

ALLOWED_EXTENSIONS = {'pdf', 'txt'}
UPLOAD_FOLDER = 'uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_to_bot(app):
    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html', prediction=None, bot_response=None)

    @app.route('/upload', methods=['POST'])
    def upload_file():
        try:
            if 'file' not in request.files:
                return render_template('index.html', prediction="Erro", bot_response="Nenhum arquivo enviado.")

            file = request.files['file']
            
            if file.filename == '':
                return render_template('index.html', prediction="Erro", bot_response="Nenhum arquivo selecionado.")

            if file and allowed_file(file.filename):
                if not os.path.exists(UPLOAD_FOLDER):
                    os.makedirs(UPLOAD_FOLDER) 

                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)

                agent_controller = AgentController()
                response, status_code = agent_controller.classify_and_respond(file_path) 
                if status_code != 200:
                    return render_template('index.html', prediction="Erro", bot_response=response["error"])

                bot_response = response.get("bot_response")
                classification = response.get("classification")
                return render_template('index.html', prediction=classification, bot_response=bot_response)
            
            return render_template('index.html', prediction="Erro", bot_response="Tipo de arquivo não suportado.")
        
        except Exception as e:
            return render_template('index.html', prediction="Erro", bot_response=f"Erro ao processar o arquivo: {str(e)}")
