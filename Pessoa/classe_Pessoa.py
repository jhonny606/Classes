class Pessoa:
    def __init__(self):
        self.nome = None
        self.sexo = None
        self.cor_olhos = None
        self.pai = None
        self.mae = None

    def set_nome(self, nome):
        self.nome = nome

    def set_sexo(self, sexo):
        sexo = sexo.upper()
        if sexo in 'MF':
            self.sexo = sexo
        else:
            print('O sexo deve ser "M" ou "F"')
    
    def set_cor_olhos(self, cor_olhos):
        cor_olhos = cor_olhos.upper()
        if cor_olhos in 'CVA':
            self.cor_olhos = cor_olhos
        else:
            print('Cor dos olhos deve ser "C", "V" ou "A"')
    def set_pai(self, pai):
        self.pai = pai

    def set_mae(self, mae):
        self.mae = mae

    def gera_pessoa(self):
        if self.sexo == 'F':
            print('Prosseguindo')
        else:
            print('Método disponível somente para sexo feminino')
    
    def imprime_dados(self):
        print(f'''
{self.nome}
{self.get_sexo_extenso()}
{self.get_cor_olhos_extenso()}
{self.pai}
{self.mae}''')

#Métodos GET:
    def get_nome(self):
        return self.nome
    
    def get_sexo(self):
        return self.sexo

    def get_sexo_extenso(self):
        if self.sexo == 'F':
            return 'Feminino'
        elif self.sexo == 'M':
            return 'Masculino'
        else:
            return 'Indefinido'
    
    def get_cor_olhos_extenso(self):
        if self.cor_olhos == 'C':
            return 'Castanhos'
        elif self.cor_olhos == 'V':
            return 'Verdes'
        elif self.cor_olhos == 'A':
            return 'Azuis'
        else:
            return 'Indefinido'

nome = input('Nome: ')
sexo = input('Sexo: ')
cor_olhos = input('Cor dos olhos: ')
pai = input('Nome pai: ')
mae = input('Nome mae: ')

p = Pessoa()
p.set_nome(nome)
p.set_sexo(sexo)
p.set_cor_olhos(cor_olhos)
p.set_pai(pai)
p.set_mae(mae)
p.gera_pessoa()
p.imprime_dados()