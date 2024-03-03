# Autor: Arthur Berti Petersen Scholze
# Data de Criação: 14/02/2024
# Versão Atual: v2.5
# Linguagem: Python versão 3.12
# 
# Eu passei muito tempo desenvolvendo esse humilde código que por sinal 
# ainda não está acabado pois pretendo colocar muitas funções a mais mas 
# já vou publicar essa versão pois estou muito orgulhoso do meu trabalho
# e queria compartilhar com todos vocês.
# 
# Espero que gostem! :)

import json
import os
from colorama import Fore, Style

class Disciplina:
    def __init__(self, nome, semestre):
        self.nome = nome
        self.semestre = semestre

class Aluno:
    def __init__(self, rm, nome, nota):
        self.rm = rm
        self.nome = nome
        self.nota = nota
        self.disciplinas = []

# Função para obter as notas de um único aluno
def obter_notas_aluno():
    rm = input("RM do aluno: ")
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    incluir_disciplina_semestre = input("Deseja incluir disciplinas e semestres? (S/N): ").lower()

    aluno = Aluno(rm, nome, nota)
    aluno.disciplinas = []

    if incluir_disciplina_semestre == 's':
        while True:
            disciplina_nome = input("Nome da disciplina (ou digite 'fim' para encerrar): ")
            if disciplina_nome.lower() == 'fim':
                break
            semestre = input("Semestre da disciplina: ")
            disciplina = Disciplina(disciplina_nome, semestre)
            aluno.disciplinas.append(disciplina)

    return [aluno]

# Função para adicionar um único aluno ao arquivo JSON
def adicionar_aluno(alunos):
    novo_aluno = obter_notas_aluno()
    alunos.extend(novo_aluno)
    print("Aluno(s) adicionado(s).")

# Função para adicionar vários alunos ao arquivo JSON
def adicionar_alunos(alunos):
    quantidade_alunos = int(input("Digite a quantidade de alunos a serem adicionados: "))
    novos_alunos = []

    for _ in range(quantidade_alunos):
        novo_aluno = obter_notas_aluno()
        novos_alunos.extend(novo_aluno)

    alunos.extend(novos_alunos)
    print(f"{quantidade_alunos} aluno(s) adicionado(s).")

# Função para exibir as notas dos alunos
def exibir_notas(alunos):
    print("\nLista de notas:")
    for aluno in alunos:
        print(f"RM {aluno.rm} - {aluno.nome} - Disciplinas: {[disciplina.nome for disciplina in aluno.disciplinas]} - Nota: {aluno.nota}")

# Função para calcular estatísticas das notas
def calcular_estatísticas(alunos):
    notas = [aluno.nota for aluno in alunos]
    soma_das_notas = sum(notas)
    
    if len(notas) > 0:
        media_das_notas = soma_das_notas / len(notas)
        media_formatada = "{:.2f}".format(media_das_notas)  # Formata a média com duas casas decimais
    else:
        media_formatada = "0.00"  # Se não houver notas, define a média como 0.00
    
    maior_nota = max(notas)
    menor_nota = min(notas)

    estatísticas = (
        "\nEstatísticas:\n"
        f" - Média das notas: {media_formatada}\n"
        f" - Maior nota: {maior_nota}\n"
        f" - Menor nota: {menor_nota}\n"
    )
    
    print(estatísticas)

# Função para classificar os alunos por faixa de notas
def classificar_alunos(alunos):
    faixas = {'A': [], 'B': [], 'C': [], 'D': []}

    for aluno in alunos:
        nota = aluno.nota
        if nota >= 9.0:
            faixas['A'].append(aluno)
        elif 7.0 <= nota < 9.0:
            faixas['B'].append(aluno)
        elif 5.0 <= nota < 7.0:
            faixas['C'].append(aluno)
        else:
            faixas['D'].append(aluno)

    classificação = "\nClassificação dos alunos:\n"
    for faixa, alunos_na_faixa in faixas.items():
        classificação += f" - Faixa {faixa}: {len(alunos_na_faixa)} alunos\n"

    return classificação

# Função para corrigir notas dos alunos
def corrigir_notas(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja corrigir: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            nova_nota = float(input(f"Digite a nova nota para o RM {rm_aluno}: "))
            aluno.nota = nova_nota
            print(f"Nota corrigida para o RM {rm_aluno}")
    exportar_notas_para_json(alunos)

# Função para adicionar aluno ao arquivo JSON
def adicionar_aluno_json(alunos):
    novo_aluno = obter_notas_aluno()
    alunos.extend(novo_aluno)
    print("Aluno(s) adicionado(s) ao arquivo JSON.")
    exportar_notas_para_json(alunos)

# Função para adicionar vários alunos ao arquivo JSON
def adicionar_alunos_json(alunos):
    quantidade_alunos = int(input("Digite a quantidade de alunos a serem adicionados: "))
    novos_alunos = []
# 
    for _ in range(quantidade_alunos):
        novo_aluno = obter_notas_aluno()
        novos_alunos.extend(novo_aluno)

    alunos.extend(novos_alunos)
    print(f"{quantidade_alunos} aluno(s) adicionado(s) ao arquivo JSON.")
    exportar_notas_para_json(alunos)

# Função para remover um aluno pelo RM
def remover_aluno(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja remover: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            alunos.remove(aluno)
            print(f"Aluno com RM {rm_aluno} removido.")
            exportar_notas_para_json(alunos)
            return
    print(f"Aluno com RM {rm_aluno} não encontrado.")

# Função para visualizar disciplinas de um aluno específico
def visualizar_disciplinas_aluno(aluno):
    print(f"\nDisciplinas e Semestres associados ao aluno {aluno.nome} (RM: {aluno.rm}):")
    if aluno.disciplinas:
        for disciplina in aluno.disciplinas:
            print(f" - Disciplina: {disciplina.nome}, Semestre: {disciplina.semestre}")
    else:
        print("Nenhuma disciplina associada.")

# Função para visualizar disciplinas de todos os alunos
def visualizar_disciplinas_todos_alunos(alunos):
    for aluno in alunos:
        print(f"\nDisciplinas e Semestres associados ao aluno {aluno.nome} (RM: {aluno.rm}):")
        if aluno.disciplinas:
            for disciplina in aluno.disciplinas:
                print(f" - Disciplina: {disciplina.nome}, Semestre: {disciplina.semestre}")
        else:
            print("Nenhuma disciplina associada para o aluno.")

# Função para calcular média ponderada considerando pesos das disciplinas
def calcular_media_ponderada(alunos):
    total_notas_ponderadas = 0
    total_pesos = 0

    for aluno in alunos:
        for disciplina in aluno.disciplinas:
            peso = float(input(f"Informe o peso para a disciplina {disciplina.nome} no semestre {disciplina.semestre}: "))
            total_notas_ponderadas += aluno.nota * peso
            total_pesos += peso

    if total_pesos > 0:
        media_ponderada = total_notas_ponderadas / total_pesos
        print("\nMédia Ponderada das Notas considerando pesos das disciplinas:", media_ponderada)
    else:
        print("\nNão foi possível calcular a Média Ponderada. Certifique-se de fornecer pesos para as disciplinas.")

# Função para exportar as notas dos alunos para um arquivo JSON
def exportar_notas_para_json(alunos):
    nome_arquivo = "main20.json"
    try:
        with open(nome_arquivo, 'w') as arquivo:
            dados = {
                "alunos": [
                    {
                        "rm": aluno.rm,
                        "nome": aluno.nome,
                        "nota": aluno.nota,
                        "disciplinas": [
                            {"nome": disciplina.nome, "semestre": disciplina.semestre}
                            for disciplina in aluno.disciplinas
                        ]
                    }
                    for aluno in alunos
                ]
            }
            json.dump(dados, arquivo, indent=4)

        print(f"Dados exportados para o arquivo {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao exportar dados para o arquivo {nome_arquivo}: {str(e)}")

# Função para ler dados de um arquivo JSON e inicializar a lista de alunos
def ler_dados_json(nome_arquivo):
    
    alunos = []

    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)

        for aluno_data in dados.get("alunos", []):
            aluno = Aluno(aluno_data["rm"], aluno_data["nome"], aluno_data["nota"])
            aluno.disciplinas = [
                Disciplina(disciplina["nome"], disciplina["semestre"])
                for disciplina in aluno_data.get("disciplinas", [])
            ]
            alunos.append(aluno)

        dados_carregados = f"{Fore.BLUE}Dados carregados.{Style.RESET_ALL} Total de {Fore.YELLOW}{len(alunos)}{Style.RESET_ALL} alunos."
        print(dados_carregados)

    except Exception as e:
        print(f"Erro ao carregar dados do arquivo {nome_arquivo}: {str(e)}")

    return alunos

# Função para calcular a média das notas dos alunos que cursaram uma determinada disciplina
def calcular_media_disciplina(alunos, disciplina_nome):
    notas = [aluno.nota for aluno in alunos if disciplina_nome in [disciplina.nome for disciplina in aluno.disciplinas]]
    if notas:
        media = sum(notas) / len(notas)
        media_formatada = "{:.2f}".format(media)  # Formata a média com duas casas decimais
        print(f"\nMédia das notas dos alunos que cursaram {disciplina_nome}: {media_formatada}")
    else:
        print("\nNenhum aluno cadastrado cursando a disciplina especificada.")

# Função para calcular a média das notas dos alunos que cursaram uma determinada disciplina em um determinado semestre
def calcular_media_disciplina_semestre(alunos, disciplina_nome, semestre):
    notas = [aluno.nota for aluno in alunos if disciplina_nome in [disciplina.nome for disciplina in aluno.disciplinas] and semestre in [disciplina.semestre for disciplina in aluno.disciplinas]]
    if notas:
        media = sum(notas) / len(notas)
        media_formatada = f"{media:.2f}"
        print(f"\nMédia das notas dos alunos que cursaram {disciplina_nome} no semestre {semestre}: {media_formatada}")
    else:
        print("\nNenhum aluno cadastrado cursando a disciplina especificada no semestre especificado.")

# Função para buscar aluno por RM
def buscar_aluno_por_rm(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja buscar: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            print(f"Aluno encontrado: RM {rm_aluno} - {aluno.nome} - Nota: {aluno.nota}")
            return
    print(f"Aluno com RM {rm_aluno} não encontrado.")

# Função para buscar aluno por nome
def buscar_aluno_por_nome(alunos):
    nome_aluno = input("Informe o nome do aluno que deseja buscar: ")
    encontrados = [aluno for aluno in alunos if nome_aluno.lower() in aluno.nome.lower()]
    if encontrados:
        print("Alunos encontrados:")
        for aluno in encontrados:
            print(f"RM {aluno.rm} - {aluno.nome} - Nota: {aluno.nota}")
    else:
        print(f"Nenhum aluno com o nome {nome_aluno} encontrado.")

# Função para listar todos os alunos
def listar_todos_alunos(alunos):
    print("\nLista de todos os alunos:")
    for aluno in alunos:
        print(f"RM {aluno.rm} - {aluno.nome} - Nota: {aluno.nota}")

# Função para atualizar nota do aluno
def atualizar_nota_aluno(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja atualizar a nota: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            nova_nota = float(input(f"Digite a nova nota para o RM {rm_aluno}: "))
            aluno.nota = nova_nota
            print(f"Nota atualizada para o RM {rm_aluno}")
            exportar_notas_para_json(alunos)
            return
    print(f"Aluno com RM {rm_aluno} não encontrado.")

# Função para remover disciplina de um aluno
def remover_disciplina(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja remover disciplina: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            disciplina_nome = input("Informe o nome da disciplina a ser removida: ")
            for disciplina in aluno.disciplinas:
                if disciplina.nome == disciplina_nome:
                    aluno.disciplinas.remove(disciplina)
                    print(f"Disciplina {disciplina_nome} removida para o RM {rm_aluno}.")
                    exportar_notas_para_json(alunos)
                    return
            print(f"Disciplina {disciplina_nome} não encontrada para o RM {rm_aluno}.")
            return
    print(f"Aluno com RM {rm_aluno} não encontrado.")

# Função para adicionar disciplina para um aluno
def adicionar_disciplina(alunos):
    rm_aluno = input("Informe o RM do aluno que deseja adicionar disciplina: ")
    for aluno in alunos:
        if aluno.rm == rm_aluno:
            disciplina_nome = input("Informe o nome da disciplina a ser adicionada: ")
            semestre = input("Informe o semestre da disciplina: ")
            nova_disciplina = Disciplina(disciplina_nome, semestre)
            aluno.disciplinas.append(nova_disciplina)
            print(f"Disciplina {disciplina_nome} adicionada para o RM {rm_aluno}.")
            exportar_notas_para_json(alunos)
            return
    print(f"Aluno com RM {rm_aluno} não encontrado.")

# Função para calcular média por faixa etária
def calcular_media_faixa_etária(alunos):
    faixas_etárias = {'<18': [], '18-21': [], '22-25': [], '26-30': [], '30+': []}

    for aluno in alunos:
        idade = int(input(f"Informe a idade do aluno {aluno.nome} (RM: {aluno.rm}): "))
        if idade < 18:
            faixas_etárias['<18'].append(aluno)
        elif 18 <= idade <= 21:
            faixas_etárias['18-21'].append(aluno)
        elif 22 <= idade <= 25:
            faixas_etárias['22-25'].append(aluno)
        elif 26 <= idade <= 30:
            faixas_etárias['26-30'].append(aluno)
        else:
            faixas_etárias['30+'].append(aluno)

    for faixa, alunos_na_faixa in faixas_etárias.items():
        if alunos_na_faixa:
            notas = [aluno.nota for aluno in alunos_na_faixa]
            media = sum(notas) / len(notas)
            print(f"Média da faixa etária {faixa}: {media:.2f}")
        else:
            print(f"Nenhum aluno na faixa etária {faixa}.")

# Função para calcular média das notas de todos os alunos
def calcular_media_geral(alunos):
    notas = [aluno.nota for aluno in alunos]
    if notas:
        media_geral = sum(notas) / len(notas)
        print(f"\nMédia geral das notas: {media_geral}")
    else:
        print("\nNenhum aluno cadastrado.")

# Limpa o terminal antes de mostrar o menu
if os.name == 'posix':  # Sistema baseado em Unix (Linux, macOS)
                os.system("clear") 
elif os.name == 'nt':  # Sistema Windows
                os.system("cls")

# Função principal
def main():
    nome_arquivo = "main20.json"

    if nome_arquivo:
        alunos = ler_dados_json(nome_arquivo)
    else:
     op_subcategoria = ""  # Inicialize op_subcategoria fora do loop

    while True:
        print(Fore.CYAN + ".___  .                           _, ._,  _, " + Style.RESET_ALL)
        print(Fore.CYAN + "[__  _|. . _. _. _. _. _         '_) (_  |.| " + Style.RESET_ALL)
        print(Fore.CYAN + "[___(_](_|(_.(_](_.(_](_)        ._) (_) |_| " + Style.RESET_ALL)

        print("\n" + Fore.YELLOW + "Menu de Opções:" + Style.RESET_ALL)
        print("\n" + Fore.CYAN + "1." + Style.RESET_ALL + Fore.CYAN + " Exibir notas dos alunos" + Style.RESET_ALL)
        print("\n" + Fore.GREEN + "2." + Style.RESET_ALL + Fore.GREEN + " Operações com notas:" + Style.RESET_ALL)
        print(Fore.GREEN + "   1." + Style.RESET_ALL + Fore.GREEN + " Calcular estatísticas" + Style.RESET_ALL)
        print(Fore.GREEN + "   2." + Style.RESET_ALL + Fore.GREEN + " Classificar alunos por faixa de notas" + Style.RESET_ALL)
        print(Fore.GREEN + "   3." + Style.RESET_ALL + Fore.GREEN + " Corrigir notas" + Style.RESET_ALL)
        print(Fore.GREEN + "   4." + Style.RESET_ALL + Fore.GREEN + " Calcular média ponderada das notas" + Style.RESET_ALL)
        print("\n" + Fore.BLUE + "3." + Style.RESET_ALL + Fore.BLUE + " Operações com alunos:" + Style.RESET_ALL)
        print(Fore.BLUE + "   1." + Style.RESET_ALL + Fore.BLUE + " Adicionar aluno" + Style.RESET_ALL)
        print(Fore.BLUE + "   2." + Style.RESET_ALL + Fore.BLUE + " Adicionar vários alunos" + Style.RESET_ALL)
        print(Fore.BLUE + "   3." + Style.RESET_ALL + Fore.BLUE + " Remover aluno" + Style.RESET_ALL)
        print(Fore.BLUE + "   4." + Style.RESET_ALL + Fore.BLUE + " Buscar aluno por RM" + Style.RESET_ALL)
        print(Fore.BLUE + "   5." + Style.RESET_ALL + Fore.BLUE + " Buscar aluno por nome" + Style.RESET_ALL)
        print(Fore.BLUE + "   6." + Style.RESET_ALL + Fore.BLUE + " Listar todos os alunos" + Style.RESET_ALL)
        print(Fore.BLUE + "   7." + Style.RESET_ALL + Fore.BLUE + " Atualizar nota do aluno" + Style.RESET_ALL)
        print(Fore.BLUE + "   8." + Style.RESET_ALL + Fore.BLUE + " Calcular média das notas de todos os alunos" + Style.RESET_ALL)
        print("\n" + Fore.MAGENTA + "4." + Style.RESET_ALL + Fore.MAGENTA + " Operações com disciplinas:" + Style.RESET_ALL)
        print(Fore.MAGENTA + "   1." + Style.RESET_ALL + Fore.MAGENTA + " Calcular média das notas de uma disciplina" + Style.RESET_ALL)
        print(Fore.MAGENTA + "   2." + Style.RESET_ALL + Fore.MAGENTA + " Calcular média das notas de uma disciplina em um determinado semestre" + Style.RESET_ALL)
        print("\n" + Fore.YELLOW + "5." + Style.RESET_ALL + Fore.YELLOW + "Operações Adicionais" + Style.RESET_ALL)
        print(Fore.YELLOW + "   1." + Style.RESET_ALL + Fore.YELLOW + " Remover disciplina de um aluno" + Style.RESET_ALL)
        print(Fore.YELLOW + "   2." + Style.RESET_ALL + Fore.YELLOW + " Adicionar disciplina para um aluno" + Style.RESET_ALL)
        print(Fore.YELLOW + "   3." + Style.RESET_ALL + Fore.YELLOW + " Visualizar disciplinas de um aluno" + Style.RESET_ALL)
        print(Fore.YELLOW + "   4." + Style.RESET_ALL + Fore.YELLOW + " Visualizar a disciplina de todos os alunos" + Style.RESET_ALL)
        print(Fore.YELLOW + "   5." + Style.RESET_ALL + Fore.YELLOW + " Calcular média por faixa etária" + Style.RESET_ALL)
        print("\n" + Fore.CYAN + "6" + Style.RESET_ALL + Fore.CYAN + " Exportar notas para json" + Style.RESET_ALL)
        print("\n" + Fore.RED + "0." + Style.RESET_ALL + Fore.RED + " Sair" + Style.RESET_ALL)

        opção = input("\nEscolha uma opção (0-6): ")

        if opção == '0':
            if os.name == 'posix':  # Sistema baseado em Unix (Linux, macOS)
                os.system("clear") 
            elif os.name == 'nt':  # Sistema Windows
                os.system("cls")
            break
        elif opção == '1':
            exibir_notas(alunos)
        elif opção == '2':
            op_subcategoria = input("Escolha uma subcategoria (1-6): ").lower()
            if op_subcategoria == '1':
                print(calcular_estatísticas(alunos))
            elif op_subcategoria == '2':
                print(classificar_alunos(alunos))
            elif op_subcategoria == '3':
                corrigir_notas(alunos)
            elif op_subcategoria == '4':
                calcular_media_ponderada(alunos)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif opção == '3':
            op_subcategoria = input("Escolha uma subcategoria (1-8): ").lower()
            if op_subcategoria == '1':
                adicionar_aluno_json(alunos)
            elif op_subcategoria == '2':
                adicionar_alunos_json(alunos)
            elif op_subcategoria == '3':
                remover_aluno(alunos)
            elif op_subcategoria == '4':
                buscar_aluno_por_rm(alunos)
            elif op_subcategoria == '5':
                buscar_aluno_por_nome(alunos)
            elif op_subcategoria == '6':
                listar_todos_alunos(alunos)
            elif op_subcategoria == '7':
                atualizar_nota_aluno(alunos)
            elif op_subcategoria == '8':
                calcular_media_geral(alunos)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif opção == '4':
            op_subcategoria = input("Escolha uma subcategoria (1-2): ").lower()
            if op_subcategoria == '1':
                disciplina_nome = input("Informe o nome da disciplina: ")
                calcular_media_disciplina(alunos, disciplina_nome)
            elif op_subcategoria == '2':
                disciplina_nome = input("Informe o nome da disciplina: ")
                semestre = input("Informe o semestre da disciplina: ")
                calcular_media_disciplina_semestre(alunos, disciplina_nome, semestre)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif opção == '5':
            op_subcategoria = input("Escolha uma subcategoria (1-5): ").lower()
            if op_subcategoria == '1':
                remover_disciplina(alunos)
            elif op_subcategoria == '2':
                adicionar_disciplina(alunos)
            elif op_subcategoria == '3':
                visualizar_disciplinas_aluno(alunos)
            elif op_subcategoria == '4':
                visualizar_disciplinas_todos_alunos(alunos)
            elif op_subcategoria == '5':
                calcular_media_faixa_etária(alunos)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        elif opção == '6':
             exportar_notas_para_json(alunos)

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
