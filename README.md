# Classificador de emails (NLP and GenAI)

Um classificador de e-mails inteligente desenvolvido para uma empresa fictícia do setor financeiro, utilizando Natural Language Processing (NLP) e Generative AI (GenAI).

## Treinamento do Modelo

O modelo de classificação foi desenvolvido utilizando o BERTimbau, uma versão do BERT treinada para o português brasileiro. O processo de treinamento foi realizado no Google Colab, e você pode encontrar o notebook completo no diretório `notebook`, assim como o dataset em `notebook/mocked_dataset`.

O modelo treinado está disponível publicamente no Hugging Face:
- [imrooteodoro/email_classifier](https://huggingface.co/imrooteodoro/email_classifier)

## Pré-requisitos

- Docker
- Docker Compose
- Git

## Instalação

### 1. Clone o Repositório

```bash
git clone https://github.com/imrooteodoro/imrooteodoro-case-pratico-AutoU_.git
cd imrooteodoro-case-pratico-AutoU_
```

### 2. Instalação do Docker e Docker Compose

#### Linux (Ubuntu/Debian)

1. Instale o Docker:
```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
```

2. Instale o Docker Compose:
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

3. Verifique as instalações:
```bash
docker --version
docker-compose --version
```

#### Windows

1. Instale o Docker Desktop:
   - Faça o download do [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop)
   - Execute o instalador e siga as instruções
   - Reinicie o computador quando solicitado

2. Verifique a instalação:
```bash
docker --version
docker-compose --version
```

## Configuração

### Variáveis de Ambiente

1. No diretório `model-api/src`:
   - Configure o modelo do Hugging Face:
   ```
   MODEL_PATH="<repositorio do modelo no Hugging Face>"
   ```

2. No diretório `genai-api/src`, configure o arquivo `.env` com:
   - `API_KEY`: Sua chave API do [Gemini](https://aistudio.google.com/app/apikey?hl=pt-br)
   - `API_URL`: URL gerada pela model-api após sua inicialização

## Execução

1. No diretório `model-api/src`, execute:
```bash
docker-compose up
```

Este comando iniciará todos os serviços necessários para o funcionamento do classificador de e-mails.

## Arquitetura

O projeto segue uma arquitetura distribuída, conforme ilustrado abaixo:

![Arquitetura do Projeto](assets/arqu.svg)

## Suporte

Para questões e suporte, abra uma issue no repositório do GitHub.
