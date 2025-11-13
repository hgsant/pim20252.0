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
