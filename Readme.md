## Projeto TechFlow - disciplina DevOps!

## 🚀 TechFlow Pipeline

Pipeline completo de CI/CD com Python, Pytest, Docker e GitHub Actions.

---

## 📌 Visão Geral

Este projeto demonstra um fluxo completo de DevOps com:

- Testes automatizados (unitários e integração)
- Cobertura de código (mínimo 80%)
- Build de imagem Docker
- Push para Docker Hub
- Release automática via GitHub Actions

---

## 🧱 Tecnologias

- Python 3.11
- Pytest
- Pytest-Cov
- Docker
- GitHub Actions

---

## 📁 Estrutura do Projeto

  src/
├── calculator.py
├── database.py
└── init.py

tests/
├── test_calculator.py
└── test_integration.py

.github/workflows/
└── ci-cd.yml
|__ ci.yml
|__ cd.yml


---

## ⚙️ CI/CD Pipeline

O pipeline executa automaticamente:

1. Instala dependências
2. Executa testes
3. Gera cobertura de código
4. Valida mínimo de 80%
5. Build da imagem Docker
6. Push para Docker Hub
7. Release automática (tags)

---

## 🧪 Rodando os testes

```bash
pip install -r requirements.txt
pytest tests/ --cov=src --cov-report=term-missing

🐳 Docker

Build:
docker build -t meu-pipeline .

Run:
docker run --rm seu-usuario/meu-pipeline:latest

📦 Versionamento

git tag v1.0.0
git push origin v1.0.0


🔐 Secrets necessários

DOCKER_HUB_USERNAME
DOCKER_HUB_TOKEN




