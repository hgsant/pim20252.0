
from .reports import load_sample, gerar_relatorio, ranking_por_media
from .algorithms import merge_sort, binary_search
from c_bindings import calc_media, get_situacao

def main():
    alunos, turmas, aulas, presencas, notas = load_sample("sample_data.json")

    print(gerar_relatorio(alunos, turmas, aulas, presencas, notas))

    alunos_ordenados = merge_sort(alunos, key=lambda a: a.ra)
    alvo = alunos_ordenados[len(alunos_ordenados)//2].ra
    achado = binary_search(alunos_ordenados, alvo, key=lambda a: a.ra)
    print(f"\\nBusca binária por RA={alvo}: encontrado -> {achado.nome}")

    m = calc_media(7.0, 6.5, 5.5)
    sit = get_situacao(m, faltas=6, total_aulas=40)
    print(f"\\nC module => média={m:.2f}, situação={sit}")

    rank = ranking_por_media(alunos, notas)[:3]
    print("\\nTop 3 por média:")
    for i, (aluno, media) in enumerate(rank, start=1):
        print(f"{i}. {aluno.nome} - {media:.2f}")

if __name__ == "__main__":
    main()
