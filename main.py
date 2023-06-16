#Trabalho Projeto Integrador
#Professora: Camila Carolina Salgueiro Serrão
#Ana Luisa Esteves Oliveira;
#jennifer Rebeca;
#Tamily fernada;
#Maria Luiza Rodrigues Da silva.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from classe import *

def obter_lista_membros():
  with open("alunos_cadastrados.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    membros = []
    for linha in linhas:
      campos = linha.strip().split(",")
      nome_completo = campos[0].split(":")[1].strip()
      curso = campos[1].split(":")[1].strip()
      email = campos[2].split(":")[1].strip()
      num_matricula = campos[3].split(":")[1].strip()
      data_nascimento = campos[4].split(":")[1].strip()
      num_camisa = campos[5].split(":")[1].strip()
      membro = {
        "Nome Completo": nome_completo,
        "Curso": curso,
        "E-mail": email,
        "Número de Matrícula": num_matricula,
        "Data de Nascimento": data_nascimento,
        "Número da Camisa": num_camisa
      }
      membros.append(membro)
      capitao = {
        "Nome Completo": nome_capitao,
        "Curso": curso_capitao,
        "E-mail": email_capitao,
        "Número de Matrícula": num_matricula_capitao,
        "Data de Nascimento": data_nascimento_capitao,
        "Número da Camisa": num_camisa_capitao
      }
      membros.append(capitao)
    return membros
def cadastrar_capitao(curso_capitao, nome_capitao, email_capitao, num_matricula_capitao, data_nascimento_capitao, num_camisa_capitao):
  with open("capitao.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Curso: {curso_capitao}, Nome Completo: {nome_capitao}, E-mail: {email_capitao}, Número de Matrícula: {num_matricula_capitao}, Data de nascimento: {data_nascimento_capitao}, Número da camisa: {num_camisa_capitao}\n")
    lista_membros = obter_lista_membros()
  #Enviando email de confirmação
  email_remetente = email_capitao
  email_destinatario = "projetoum8@gmail.com"
  senha_destinatario = "cswldlepklocmidl"
  mensagem = MIMEMultipart()
  mensagem["From"] = email_remetente
  mensagem["To"] = email_destinatario
  mensagem["Subject"] = "Confirmação de Cadastro"
  texto_email = f"""
      Olá, eu sou {nome_capitao},
      E estou finalizando o meu cadastro como capitão da minha equipe!
      Segue abaixo a lista de membros inscritos na equipe:
      {"".join([f"{membro['Nome Completo']}, Curso: {membro['Curso']}, E-mail: {membro['E-mail']}, Número de Matrícula: {membro['Número de Matrícula']}, Data de Nascimento: {membro['Data de Nascimento']}, Número da Camisa: {membro['Número da Camisa']}" for membro in lista_membros])}
      E meu e-mail para caso algo não esteja de acordo:
      {email_capitao}
      Obrigado!
      Atenciosamente,
      {nome_capitao}
  """

  parte_texto = MIMEText(texto_email, "plain")
  mensagem.attach(parte_texto)
  try:
    servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    servidor_smtp.starttls()
    servidor_smtp.login(email_destinatario, senha_destinatario)
    servidor_smtp.sendmail(email_remetente,
                           email_destinatario,
                           mensagem.as_string())
    servidor_smtp.quit()
    print("Email de confirmação enviado com sucesso!")
    with open("capitao.txt", "w"):
      pass
    with open("alunos_cadastrados.txt", "w"):
      pass
  except smtplib.SMTPException as e:
    print("Ocorreu um erro ao enviar o email de confirmação:", str(e))

def exibir_cadastro():
  with open("capitao.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
      print(linha.rstrip())

def cadastrar_aluno(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno):
  with open("alunos_cadastrados.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"Nome Completo: {nome_aluno}, Curso: {curso_aluno}, E-mail: {email_aluno}, Numero de Matricula: {num_matricula_aluno}, Data de Nascimento: {data_nascimento_aluno}, Número da camisa: {num_camisa_aluno}\n")

def exibir_cadastro2():
  with open("alunos_cadastrados.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
      print(linha.rstrip())

equipes = {}
equipes = {}
Inicio = input(" > Você é o capitão da sua equipe? S/N ").capitalize()
if Inicio == "S":
  curso_capitao = input('Digite seu curso: ')
  nome_capitao = input('Digite seu Nome Completo: ')
  email_capitao = input('Digite seu e-mail: ')
  num_matricula_capitao = input('Digite seu número de matrícula: ')
  data_nascimento_capitao = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_capitao = input('Digite o número da sua camisa: ')
  capitao = CapitaoEquipe(nome_capitao, email_capitao, num_matricula_capitao, curso_capitao, data_nascimento_capitao, num_camisa_capitao)
  cadastrar_capitao(curso_capitao, nome_capitao,email_capitao, num_matricula_capitao, data_nascimento_capitao, num_camisa_capitao)
else:
  nome_aluno = input('Digite seu Nome Completo: ')
  curso_aluno = input('Digite seu curso: ')
  email_aluno = input('Digite seu e-mail: ')
  num_matricula_aluno = input('Digite seu número de matrícula: ')
  data_nascimento_aluno = input('Digite a sua data de nascimento(00/00/00): ')
  num_camisa_aluno = input('Digite o número da sua camisa: ')
  aluno = AlunoEquipe(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno,num_camisa_aluno)
  cadastrar_aluno(nome_aluno,curso_aluno, email_aluno, num_matricula_aluno, data_nascimento_aluno, num_camisa_aluno)