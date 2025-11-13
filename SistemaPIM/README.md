# AcadIA – Algoritmos (Python) + Módulo Crítico (C)

Este pacote demonstra **algoritmos e estruturas de dados em Python** (busca, ordenação e relatórios) e um **módulo crítico em C estruturado** para cálculos de desempenho e validação de frequência, conforme o PIM.

## Estrutura
```
acadia_code/
  data_models.py         # dataclasses (Aluno, Turma, Aula, Nota, Presenca)
  algorithms.py          # ordenação (merge sort), busca binária, indexação
  reports.py             # geração de relatórios (médias, presença, ranking)
  c_module.c             # C: média, situação, normalização de nota
  c_bindings.py          # Python: ctypes para chamar o módulo C
  demo.py                # executa exemplos (chama C se compilado)
  test_algorithms.py     # testes simples
  sample_data.json       # dados fictícios para demonstração
  build.sh               # (Linux/Mac) compila o C para .so
  build.bat              # (Windows) compila o C para .dll
  README.md
```

## Como executar
1) **Opcional:** Compile o módulo em C  
- Linux/Mac: `bash build.sh`  
- Windows (MinGW/MSVC): `build.bat`

2) **Rodar a demonstração:** `python demo.py`

3) **Testes:** `python test_algorithms.py`
# 🧠 Sistema AcadIA – Sistema Acadêmico Inteligente

Este projeto faz parte do **PIM UNIP 2025** e foi desenvolvido em **Python** com integração em **C**.  
O sistema tem como objetivo automatizar o controle acadêmico de alunos, realizando **cálculo de médias, verificação de frequência, classificação automática e geração de relatórios**.

---

## 🚀 Funcionalidades Principais
- 📊 Cálculo automático de médias e frequências.
- 🧮 Ordenação e busca com algoritmos (Merge Sort e Binary Search).
- 🔍 Busca rápida de alunos pelo número de matrícula (RA).
- 🧠 Integração com módulo em C para cálculo de médias.
- 🧾 Geração de relatório completo com ranking dos melhores alunos.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.14**
- **Linguagem C (módulo externo integrado)**
- **Bibliotecas padrão do Python**
- **VS Code / GitHub Desktop**

---

## ⚙️ Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/hgsantTraducao/Sistema.PIM.2025.git
