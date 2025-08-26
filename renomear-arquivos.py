import os
import sys

def renomear_arquivos(diretorio, nome_base):
    for i, arquivo in enumerate(os.listdir(diretorio), start=1):
        caminho_antigo = os.path.join(diretorio, arquivo)

        if not os.path.isfile(caminho_antigo):
            continue

        _, extensao = os.path.splitext(arquivo)
        novo_nome = f"{nome_base}{i}{extensao}"
        caminho_novo = os.path.join(diretorio, novo_nome)

        os.rename(caminho_antigo, caminho_novo)
        print(f"{arquivo} -> {novo_nome}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python arquivo.py <diretorio-alvo> <nome-base>")
        sys.exit(1)

    diretorio = sys.argv[1]
    nome_base = sys.argv[2]

    if not os.path.isdir(diretorio):
        print("Erro: diretório não encontrado.")
        sys.exit(1)

    renomear_arquivos(diretorio, nome_base)

