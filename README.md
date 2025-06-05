# OppoMind CRM Assistant

Este projeto tem como objetivo criar um **assistente inteligente para CRM** que recebe mensagens via **WhatsApp**, transcreve áudios usando o **Whisper**, interpreta intenções com **Rasa**, e responde ao usuário por meio de uma **API Flask**.

---

## Visão Geral

O projeto está dividido em três partes principais, cada uma com seu ambiente virtual (`venv`) isolado para evitar conflitos de dependência:

- `whisperenv`: Transcrição de áudio com [OpenAI Whisper](https://github.com/openai/whisper)
- `rasaenv`: Interpretação de intenções com [Rasa](https://rasa.com)
- `apienv`: API REST com [Flask](https://flask.palletsprojects.com) que orquestra tudo

---

## Requisitos

- Python `3.10.11` (recomendado)
- Git
- pip
- venv (ambientes isolados)

---

## Estrutura de Pastas

```
OppoMind/
├── apienv/                   # Ambiente virtual da API Flask
│   ├── venv/
│   └── requirements.txt
├── rasaenv/                  # Ambiente virtual do Rasa
│   ├── venv/
│   └── requirements.txt
├── whisperenv/               # Ambiente virtual do Whisper
│   ├── venv/
│   └── requirements.txt
├── resources/                # Recursos externos (audios e simulação de banco)
│   ├── audios/               # Arquivos de áudio para transcrição
│   │   └── audio_test1.m4a
│   └── context/              # JSONs simulando banco de oportunidades do CRM
│       └── oportunidades.json
├── src/                      # Código-fonte principal
│   ├── agent/                # Projeto Rasa completo
│   │   ├── .rasa/
│   │   ├── actions/
│   │   ├── data/
│   │   ├── models/
│   │   ├── tests/
│   │   ├── config.yml
│   │   ├── credentials.yml
│   │   ├── domain.yml
│   │   └── endpoints.yml
│   ├── api/                  # Código da API Flask
│   │   ├── routes.py
│   │   └── __init__.py
│   ├── transcriber.py        # Transcrição de áudio com Whisper
│   └── main.py               # Orquestrador central (opcional)
├── .gitignore
└── README.md
```

---

## Instalação (passo a passo)

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/OppoMind.git
cd OppoMind
```

### 2. Criar ambientes virtuais e instalar dependências

#### Whisper

```bash
cd whisperenv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

#### Rasa

```bash
cd rasaenv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

#### API Flask

```bash
cd apienv
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

---

## Como executar o projeto

Abra **3 terminais separados**, um para cada componente:

### Terminal 1 — Rasa

```bash
cd rasaenv
venv\Scripts\activate
cd ../src/agent
rasa train           # Se ainda não treinou o modelo
rasa run --enable-api
```

### Terminal 2 — Whisper

```bash
cd whisperenv
venv\Scripts\activate
python ../src/transcriber.py
```

### Terminal 3 — API Flask

```bash
cd apienv
venv\Scripts\activate
cd ../src/api
flask run --host=0.0.0.0
```

---

## Fluxo da Integração

```plaintext
Usuário envia áudio (WhatsApp) → API Flask → Whisper (transcrição) → Rasa (interpretação) → API responde
```

Você pode simular uma mensagem para o Rasa com:

```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
     -H "Content-Type: application/json" \
     -d '{"sender": "usuario1", "message": "quero agendar uma visita"}'
```

---

## Base de Conhecimento Simulada

A pasta `resources/context/oportunidades.json` funciona como um "banco de dados fake", onde ficam:

```json
[
  {
    "id": "OPP123",
    "cliente": "João Silva",
    "comentario": "Agendar visita para o dia 10"
  },
  {
    "id": "OPP456",
    "cliente": "Maria Souza",
    "comentario": "Reagendar demonstração"
  }
]
```

Esses dados podem ser buscados pela API com base em nome ou ID.

---

## Observações Técnicas

- Toda dependência crítica está isolada por `venv`, evitando conflitos entre pacotes como `numpy`, `numba` e `tensorflow`.
- A pasta `resources/audios/` pode receber arquivos `*.m4a` ou `*.wav` que serão processados.
- A API pode ser facilmente estendida com mais rotas em `src/api/routes.py`.

---

## Autor

Desenvolvido com amor por Felipe Jovino dos Santos