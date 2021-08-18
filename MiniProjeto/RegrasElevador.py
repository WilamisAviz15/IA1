from experta import Rule, Fact, KnowledgeEngine, AND

class RegrasElevador(KnowledgeEngine):
    resposta = ""

    # OK
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def andar1abrir(self):
        self.resposta = "Abrir a porta"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar1desejado1caminhoatual2(self):
        self.resposta = "Descer para o 1o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar1desejado1caminhoatual3(self):
        self.resposta = "Descer para o 1o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def atual1subir2(self):
        self.resposta = "Subindo para 2o andar"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar1desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='2')))
    def andar1desejado3caminhoatual2(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def atual1subir3(self):
        self.resposta = "Subindo para 3o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def atual2descer1(self):
        self.resposta = "Descendo para 1o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar2desejado1caminhoatual3(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar2desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar2desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='1')))
    def andar2desejado3caminhoatual1(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def atual2abrir(self):
        self.resposta = "Abrir a porta"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def andar2desejado3(self):
        self.resposta = "Subindo para 3o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def atual3descer1(self):
        self.resposta = "Descendo para 1o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def atual3descer2(self):
        self.resposta = "Descendo para 2o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def atual3abrir(self):
        self.resposta = "Abrir a porta"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='1')))
    def andar3desejado3caminhoatual1(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='2')))
    def andar3desejado3caminhoatual2(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar3desejado1caminhoatual2(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar3desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"