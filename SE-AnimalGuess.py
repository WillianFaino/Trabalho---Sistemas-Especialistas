from experta import *
import subprocess
import sys

#função para instalar a biblioteca termcolor e possibilitar imprimir text
#colorido na saída do programa
def installTermcolor():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "termcolor"])

#função tof (true or false) para converter as respostas do usuário em valores booleanos
#correspondentes ao significado das respostas, foi utilizada essa função de conversão
#para evitar poluição do código com diversas repetições de conversões, e também para
#possibilitar que as respostas do usuário sejam mais "simples", ao invés de digitar
#True ou False, o usuário pode usar S/s ou N/n para obter os mesmos resultados, tornando
#o questionário mais intuitivo
def tof(char):
    if(char == 'S'):
        return True
    elif(char== 's'):
        return True
    else:
        return False

#variável para definir se já foi descoberto ao menos um animal com as caracteristicas informadas,
#usada para, caso nenhum animal seja encontrado, a mensagem "Animal Desconhecido" seja exibida
guessed = False


print("\n\nVocê possui a biblioteca 'Termcolor' instalada? (S/N)")
insTC = input()

if (insTC == 'N' or insTC == 'n'):
    installTermcolor()

#importa a biblioteca termcolor após o usuário confirmar que a possui ou após ser realizada a instalação
from termcolor import colored


#classe de caracteristicas dos animais que serão usadas para confeccionar as regras e posteriormente
#para adivinhar o animal
class caracts(Fact):
    pelugem = False
    penugem = False
    oviparo = False
    aereo = False
    aquatico = False
    predador = False
    denticao = False
    vertebrado = False
    respiracao_pulmonar = False
    venenoso = False
    barbatanas = False
    n_pernas = -1
    cauda = False
    domestico = False
    catsize = False
    classe_biologica = 0

    pass

#mecanismo de conhecimento onde as regras são definidas, será instanciada e executada, recebendo por parametro
#um objeto do tipo "caracts" possuindo os atributos que o usuário informou, e então irá exibir o(s) resultado(s)
#apropriado(s) de acordo com a entrada
class SE_AnimalGuess(KnowledgeEngine):
    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def anta(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Anta", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=True, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def ariranha(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Ariranha", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=False, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def boto_cor_de_rosa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Boto-Cor-De_Rosa", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def bugio(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Bugio", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=True, classe_biologica=1),salience=1)
    def cachorro_vinagre(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Cachorro-Vinagre", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=True, catsize=False, classe_biologica=1),salience=1)
    def chimpanze(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Chimpanze", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=True, classe_biologica=1),salience=1)
    def gato_maracaja(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Gato-Maracaja", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=True),salience=1)
    def jaguatirica(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jaguatirica", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def lobo_guara(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Lobo-Guara", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=True, classe_biologica=1),salience=1)
    def macaco_aranha(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Macaco-Aranha", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def macaco_barrigudo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Macaco-Barrigudo", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=True, catsize=True, classe_biologica=1),salience=1)
    def mico_leao_dourado(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Mico-Leao-Dourado", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def mono_carvoeiro(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Mono-Carvoeiro", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def onca_pintada(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Onca-Pintada", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=True, catsize=False, classe_biologica=1),salience=1)
    def orangotango(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Orangotango", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=True,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=True, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def peixe_boi(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Peixe-Boi", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=True, classe_biologica=1),salience=1)
    def queixada(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Queixada", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def tamandua_bandeira(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Tamandua-Bandeira", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=False, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=1),salience=1)
    def urso_de_oculos(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Urso-De-Oculos", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def aguia_cinzenta(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Aguia-Cinzenta", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def aracari_banana(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Aracari-Banana", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def arara_azul(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Arara-Azul", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def arara_caninde(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Arara-Caninde", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=True, catsize=True, classe_biologica=2),salience=1)
    def chaua(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Chaua", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=False,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def ema(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Ema", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def gaviao_pombo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Gaviao-Pombo", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def guara(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Guara", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def harpia(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Harpia", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def jacurutu(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jacurutu", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def jacutinga(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jacutinga", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def jandaia_amarela(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jandaia-Amarela", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=False,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def macuco(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Macuco", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def murucututu(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Murucututu", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def mutum(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Mutum", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=True, catsize=True, classe_biologica=2),salience=1)
    def papagaio_da_cara_roxa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Papagaio-Da-Cara-Roxa", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def pato_de_crista(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Pato-De-Crista", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def pavo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Pavo", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=True, classe_biologica=2),salience=1)
    def tucano_de_bico_preto(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Tucano-De-Bico-Preto", "green"))

    @Rule(caracts(pelugem=False, penugem=True, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=2, cauda=True,
                  domestico=False, catsize=False, classe_biologica=2),salience=1)
    def urubu_rei(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Urubu-Rei", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def cobra_cipo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Cobra-Cipo", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=True, catsize=True, classe_biologica=3),salience=1)
    def jabuti(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jabuti", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def jacare_coroa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jacare-Coroa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def jararaca_ilhoa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jararaca-Ilhoa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def jiboia(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Jiboia", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def sucuri(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Sucuri", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=True, catsize=False, classe_biologica=3),salience=1)
    def tracaja(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Tracaja", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=3),salience=1)
    def urutu_cruzeiro(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Urutu-Cruzeiro", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=True, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=4),salience=1)
    def baiacu(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Baiacu", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=True, catsize=False, classe_biologica=4),salience=1)
    def cascudinho_de_caverna(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Cascudinho-De-Caverna", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=True, catsize=False, classe_biologica=4),salience=1)
    def lambari(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Lambari", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=4),salience=1)
    def matrinxa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Matrinxa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=4),salience=1)
    def pirarucu(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Pirarucu", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=True, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=True, classe_biologica=4),salience=1)
    def raia_chita(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Raia-Chita", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=False, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=4),salience=1)
    def tambaqui(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Tambaqui", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=False,
                  venenoso=True, barbatanas=True, n_pernas=0, cauda=True,
                  domestico=False, catsize=False, classe_biologica=4),salience=1)
    def tubarao_raposa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Tubarao-Raposa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=5),salience=1)
    def perereca_de_alcatrazes(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Perereca-De-Alcatrazes", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=5),salience=1)
    def ra_flecha_azul(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Ra-Flecha-Azul", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=True, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=5),salience=1)
    def ra_pimenta(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Ra-Pimenta", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=False, denticao=False, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=True, catsize=False, classe_biologica=5),salience=1)
    def sapo_barriga_de_fogo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Sapo-Barriga-De-Fogo", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=False, classe_biologica=5),salience=1)
    def sapo_cururu(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Sapo-Cururu", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=True,
                  predador=True, denticao=True, vertebrado=True, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=4, cauda=False,
                  domestico=False, catsize=True, classe_biologica=5),salience=1)
    def sapo_de_chifre(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Sapo-De-Chifre", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=6),salience=1)
    def abelha(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Abelha", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=6),salience=1)
    def joaninha(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Joaninha", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=6),salience=1)
    def mariposa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Mariposa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=True, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=6),salience=1)
    def pirilampo(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Pirilampo", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=True, aquatico=False,
                  predador=True, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=6),salience=1)
    def vespa(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Vespa", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=7),salience=1)
    def bicho_pau(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Bicho-Pau", "green"))

    @Rule(caracts(pelugem=False, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=False, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=False, barbatanas=False, n_pernas=0, cauda=False,
                  domestico=False, catsize=False, classe_biologica=7),salience=1)
    def caracol_da_mata_atlantica(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Caracol-Da-Mata-Atlantica", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=8, cauda=False,
                  domestico=False, catsize=False, classe_biologica=7),salience=1)
    def caranguejeira(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Caranguejeira", "green"))

    @Rule(caracts(pelugem=True, penugem=False, oviparo=True, aereo=False, aquatico=False,
                  predador=True, denticao=False, vertebrado=False, respiracao_pulmonar=True,
                  venenoso=True, barbatanas=False, n_pernas=6, cauda=False,
                  domestico=False, catsize=False, classe_biologica=7),salience=1)
    def sauva_limao(self):
        global guessed
        guessed=True
        print(colored("\n\nO animal provavelmente eh: Sauva-Limao", "green"))

    #regra com prioridade baixa, será executada após todas as outras terem sido verificadas, serve para exibir
    #uma mensagem apropriada caso nenhum animal tenha sido relacionado aos dados de entrada
    @Rule(caracts(),salience=0)
    def desconhecido(self):
        if(guessed == False):
            print(colored("\n\nAnimal Desconhecido", "magenta"))
        pass




#instanciação do mecanismo de conhecimento e preparação do mesmo para a execução (reset)
se = SE_AnimalGuess()
se.reset()

#nome do programa e autor
print("Sistema Especialista Descobridor de Animais")
print("Autor: Willian Cavaller Faino")



print("\n\nInicio do questionario para descobrir o animal\n\n")
print(colored("Reponda apenas com as opções fornecidas nos enunciados das perguntas", "red", attrs=['underline']))


#inicio do questionario
print('O animal possui pelugem? (S/N)')
pel = input()
pel = tof(pel)

print('\n\n\nO animal possui penugem? (S/N)')
pen = input()
pen = tof(pen)

print('\n\n\nO animal eh oviparo? (S/N)')
ovi = input()
ovi = tof(ovi)

print('\n\n\nO animal eh aereo? (S/N)')
aer = input()
aer = tof(aer)

print('\n\n\nO animal eh aquatico? (S/N)')
aqu = input()
aqu = tof(aqu)

print('\n\n\nO animal eh um predador? (S/N)')
pre = input()
pre = tof(pre)

print('\n\n\nO animal possui denticao? (S/N)')
den = input()
den = tof(den)

print('\n\n\nO animal eh vertebrado? (S/N)')
ver = input()
ver = tof(ver)

print('\n\n\nO animal possui respiração pulmonar? (S/N)')
rep = input()
rep = tof(rep)

print('\n\n\nO animal eh venenoso? (S/N)')
ven = input()
ven = tof(ven)

print('\n\n\nO animal possui barbatanas? (S/N)')
bar = input()
bar = tof(bar)

print('\n\n\nQuantas pernas o animal possui? (0, 2, 4, 6 ,8)')
npe = int(input())

print('\n\n\nO animal possui cauda? (S/N)')
cau = input()
cau = tof(cau)

print('\n\n\nO animal eh domestico? (S/N)')
dom = input()
dom = tof(dom)

print('\n\n\nO animal tem o tamanho proximo ao de um gato domestico? (S/N)')
cat = input()
cat = tof(cat)

print('\n\n\nQual a classe biologica do animal? (1-mamifero, 2-ave, 3-reptil, 4-peixe, 5-anfibio, '
      '6-inseto, 7-artropode ou molusco)')
cla = int(input())

#adiciona um objeto com os atributos informados pelo usuário à lista de fatos do mecanismo
#de conhecimento
se.declare(caracts(pelugem=pel, penugem=pen, oviparo=ovi, aereo=aer, aquatico=aqu, predador=pre,
                   denticao=den, vertebrado=ver, respiracao_pulmonar=rep, venenoso=ven, barbatanas=bar,
                   n_pernas=npe, cauda=cau, domestico=dom, catsize=cat, classe_biologica=cla))

#executa o mecanismo com os dados informados pelo usuário
se.run()
