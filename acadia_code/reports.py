
import json
from typing import List, Dict
from .data_models import Aluno, Turma, Aula, Presenca, Nota
from .algorithms import merge_sort, binary_search, build_index

def load_sample(path: str = "sample_data.json"):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    alunos = [Aluno(**a) for a in data["alunos"]]
    turmas = [Turma(**t) for t in data["turmas"]]
    aulas  = [Aula(**a) for a in data["aulas"]]
    presencas = [Presenca(**p) for p in data["presencas"]]
    notas = [Nota(**n) for n in data["notas"]]
    return alunos, turmas, aulas, presencas, notas

def media_notas_por_aluno(notas: List[Nota]) -> Dict[int, float]:
    medias = {}
    for n in notas:
        medias[n.aluno_id] = (n.n1 + n.n2 + n.n3) / 3.0
    return medias

def aulas_por_aluno_map(aulas: List[Aula], turmas: List[Turma]) -> Dict[int, List[int]]:
    aulas_turma = {}
    for a in aulas:
        aulas_turma.setdefault(a.turma_id, []).append(a.id)
    mapa = {}
    for t in turmas:
        for aluno_id in t.alunos:
            mapa.setdefault(aluno_id, []).extend(aulas_turma.get(t.id, []))
    return mapa

def frequencia_por_aluno(presencas: List[Presenca], aulas_por_aluno: Dict[int, List[int]]) -> Dict[int, float]:
    freq = {}
    # Para cada aluno, calcula % de presenças
    for aluno_id, aulas in aulas_por_aluno.items():
        if not aulas:
            freq[aluno_id] = 1.0
            continue
        pres = sum(1 for a in aulas if any((p.aula_id == a and p.aluno_id == aluno_id and p.status == 'P') for p in presencas))
        freq[aluno_id] = pres / len(aulas)
    return freq

def ranking_por_media(alunos: List[Aluno], notas: List[Nota]):
    medias = media_notas_por_aluno(notas)
    return sorted([(a, medias.get(a.id, 0.0)) for a in alunos], key=lambda x: x[1], reverse=True)

def gerar_relatorio(alunos, turmas, aulas, presencas, notas):
    idx_ra = build_index(alunos, key=lambda a: a.ra)  # exemplo de índice
    alunos_ord_por_ra = merge_sort(alunos, key=lambda a: a.ra)

    aulas_map = aulas_por_aluno_map(aulas, turmas)
    freq = frequencia_por_aluno(presencas, aulas_map)
    medias = media_notas_por_aluno(notas)

    linhas = []
    linhas.append("RELATÓRIO ACADÊMICO (Notas e Frequência)")
    linhas.append("="*60)
    for a in merge_sort(alunos, key=lambda x: x.nome):
        linhas.append(f"Aluno: {a.nome} (RA: {a.ra})")
        linhas.append(f" - Média: {medias.get(a.id, 0.0):.2f}")
        linhas.append(f" - Frequência: {100*freq.get(a.id, 1.0):.1f}%")
        linhas.append("-"*40)
    return "\\n".join(linhas)
