import pdfplumber

class TextExtractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_text(self):
        if self.file_path.lower().endswith(".pdf"):
            return self.extract_text_from_pdf(self.file_path)
        elif self.file_path.lower().endswith(".txt"):
            return self.extract_text_from_txt(self.file_path)
        else:
            raise ValueError("Tipo de arquivo não suportado")

    def extract_text_from_pdf(self, pdf_path):
        try:
            text = ""
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text.strip() if text else "Nenhum texto extraído do PDF"
        except Exception as e:
            raise RuntimeError(f"Erro ao processar o PDF: {e}")

    def extract_text_from_txt(self, txt_path):
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except Exception as e:
            raise RuntimeError(f"Erro ao processar o arquivo TXT: {e}")
