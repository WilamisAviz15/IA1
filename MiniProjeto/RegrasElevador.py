from experta import Rule, Fact, KnowledgeEngine, AND

class RegrasElevador(KnowledgeEngine):
    resposta = ""

    # OK
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1')))
    def atual1abrir(self):
        self.resposta = "Abrir a porta"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2')))
    def atual1subir2(self):
        self.resposta = "Subindo para 2o andar"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3')))
    def atual1subir3(self):
        self.resposta = "Subindo para 3o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1')))
    def atual2descer1(self):
        self.resposta = "Descendo para 1o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2')))
    def atual2abrir(self):
        self.resposta = "Abrir a porta"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3')))
    def atual2subir(self):
        self.resposta = "Subindo para 3o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1')))
    def atual3descer1(self):
        self.resposta = "Descendo para 1o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2')))
    def atual3descer2(self):
        self.resposta = "Descendo para 2o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='3')))
    def atual3abrir(self):
        self.resposta = "Abrir a porta"