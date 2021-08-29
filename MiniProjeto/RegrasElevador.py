from experta import Rule, Fact, KnowledgeEngine, AND

class RegrasElevador(KnowledgeEngine):
    resposta = ""

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

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def andar1desejado4caminholivre(self):
        self.resposta = "Subindo para 4o andar"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def andar1desejado5caminholivre(self):
        self.resposta = "Subindo para 5o andar"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def andar1desejado6caminholivre(self):
        self.resposta = "Subindo para 6o andar"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='4')))
    def andar1desejado1caminhoatual4(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='5')))
    def andar1desejado1caminhoatual5(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='6')))
    def andar1desejado1caminhoatual6(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='2')))
    def andar1desejado2caminhoatual2(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar1desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar1desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar1desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='3')))
    def andar1desejado3caminhoatual3(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='4')))
    def andar1desejado3caminhoatual4(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='5')))
    def andar1desejado3caminhoatual5(self):
        self.resposta = "Descer para 3o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='6')))
    def andar1desejado3caminhoatual6(self):
        self.resposta = "Descer para 3o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='2')))
    def andar1desejado4caminhoatual2(self):
        self.resposta = "Subir para 4o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='3')))
    def andar1desejado4caminhoatual3(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='4')))
    def andar1desejado4caminhoatual4(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='5')))
    def andar1desejado4caminhoatual5(self):
        self.resposta = "Descer para 4o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='6')))
    def andar1desejado4caminhoatual6(self):
        self.resposta = "Descer para 4o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='2')))
    def andar1desejado5caminhoatual2(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='3')))
    def andar1desejado5caminhoatual3(self):
        self.resposta = "Subir para 5o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='4')))
    def andar1desejado5caminhoatual4(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='5')))
    def andar1desejado5caminhoatual5(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='6')))
    def andar1desejado5caminhoatual6(self):
        self.resposta = "Descer para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='2')))
    def andar1desejado6caminhoatual2(self):
        self.resposta = "Subir para 6o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='3')))
    def andar1desejado6caminhoatual3(self):
        self.resposta = "Subir para 6o andar depois"
    
    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='4')))
    def andar1desejado6caminhoatual4(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='5')))
    def andar1desejado6caminhoatual5(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='1'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='6')))
    def andar1desejado6caminhoatual6(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def atual2descer1(self):
        self.resposta = "Descendo para 1o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar2desejado1caminhoatual3(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='1')))
    def andar2desejado1caminhoatual1(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

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
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def andar2desejado3(self):
        self.resposta = "Subindo para 3o andar"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def andar2desejado4(self):
        self.resposta = "Subindo para 4o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def andar2desejado5(self):
        self.resposta = "Subindo para 5o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def andar2desejado6(self):
        self.resposta = "Subindo para 6o andar"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar2desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar2desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar2desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='4')))
    def andar2desejado1caminhoatual4(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='5')))
    def andar2desejado1caminhoatual5(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='6')))
    def andar2desejado1caminhoatual6(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='3')))
    def andar2desejado3caminhoatual3(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='4')))
    def andar2desejado3caminhoatual4(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='5')))
    def andar2desejado3caminhoatual5(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='6')))
    def andar2desejado3caminhoatual6(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='1')))
    def andar2desejado4caminhoatual1(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='3')))
    def andar2desejado4caminhoatual3(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='4')))
    def andar2desejado4caminhoatual4(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='5')))
    def andar2desejado4caminhoatual5(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='6')))
    def andar2desejado4caminhoatual6(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='1')))
    def andar2desejado5caminhoatual1(self):
        self.resposta = "Subir para 5o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='3')))
    def andar2desejado5caminhoatual3(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='4')))
    def andar2desejado5caminhoatual4(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='5')))
    def andar2desejado5caminhoatual5(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='6')))
    def andar2desejado5caminhoatual6(self):
        self.resposta = "Descer para 5o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='1')))
    def andar2desejado6caminhoatual1(self):
        self.resposta = "Subir para 6o andar depois"
    
    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='3')))
    def andar2desejado6caminhoatual3(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='4')))
    def andar2desejado6caminhoatual4(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='5')))
    def andar2desejado6caminhoatual5(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='2'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='6')))
    def andar2desejado6caminhoatual6(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

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

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def atual3desejado4livre(self):
        self.resposta = "Subindo para 4o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def atual3desejado5livre(self):
        self.resposta = "Subindo para 5o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def atual3desejado6livre(self):
        self.resposta = "Subindo para 6o andar"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar3desejado1caminhoatual2(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar3desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar3desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar3desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar3desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='1')))
    def andar3desejado1caminhoatual1(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='4')))
    def andar3desejado1caminhoatual4(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='5')))
    def andar3desejado1caminhoatual5(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='6')))
    def andar3desejado1caminhoatual6(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='2')))
    def andar3desejado2caminhoatual2(self):
        self.resposta = "Elevador ja está a caminho do andar desejado" 

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar3desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar3desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar3desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar3desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='1')))
    def andar3desejado4caminhoatual1(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='2')))
    def andar3desejado4caminhoatual2(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='4')))
    def andar3desejado4caminhoatual4(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='5')))
    def andar3desejado4caminhoatual5(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='6')))
    def andar3desejado4caminhoatual6(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='1')))
    def andar3desejado5caminhoatual1(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='2')))
    def andar3desejado5caminhoatual2(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='4')))
    def andar3desejado5caminhoatual4(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='5')))
    def andar3desejado5caminhoatual5(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='6')))
    def andar3desejado5caminhoatual6(self):
        self.resposta = "Descer para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='1')))
    def andar3desejado6caminhoatual1(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='2')))
    def andar3desejado6caminhoatual2(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='4')))
    def andar3desejado6caminhoatual4(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='5')))
    def andar3desejado6caminhoatual1(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='3'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='6')))
    def andar3desejado6caminhoatual6(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def andar4desejado4caminholivre(self):
        self.resposta = "Abrir a porta"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def andar4desejado1caminholivre(self):
        self.resposta = "Descendo para o 1o andar"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def andar4desejado2caminholivre(self):
        self.resposta = "Descendo para o 2o andar"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def andar4desejado3caminholivre(self):
        self.resposta = "Descendo para o 3o andar"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def andar4desejado5caminholivre(self):
        self.resposta = "subindo para o 5o andar"

    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def andar4desejado6caminholivre(self):
        self.resposta = "subindo para o 6o andar"    

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='1')))
    def andar4desejado1caminhoatual1(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar4desejado1caminhoatual2(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar4desejado1caminhoatual3(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='5')))
    def andar4desejado1caminhoatual5(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='6')))
    def andar4desejado1caminhoatual6(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar4desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='2')))
    def andar4desejado2caminhoatual2(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar4desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar4desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar4desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='1')))
    def andar4desejado3caminhoatual1(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='2')))
    def andar4desejado3caminhoatual2(self):
        self.resposta = "Subir para 3o andar depois"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='3')))
    def andar4desejado3caminhoatual3(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='5')))
    def andar4desejado3caminhoatual5(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='6')))
    def andar4desejado3caminhoatual6(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='1')))
    def andar4desejado5caminhoatual1(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='2')))
    def andar4desejado5caminhoatual2(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='3')))
    def andar4desejado5caminhoatual3(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='5')))
    def andar4desejado5caminhoatual5(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='6')))
    def andar4desejado5caminhoatual6(self):
        self.resposta = "Descer para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='1')))
    def andar4desejado6caminhoatual1(self):
        self.resposta = "Subir para 6o andar depois"
    
    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='2')))
    def andar4desejado6caminhoatual2(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='3')))
    def andar4desejado6caminhoatual3(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='5')))
    def andar4desejado6caminhoatual5(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='4'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='6')))
    def andar4desejado6caminhoatual6(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def andar5desejado5caminholivre(self):
        self.resposta = "Abrir a porta"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def andar5desejado1caminholivre(self):
        self.resposta = "Descendo para o 1o andar"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def andar5desejado2caminholivre(self):
        self.resposta = "Descendo para o 2o andar"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def andar5desejado3caminholivre(self):
        self.resposta = "Descendo para o 3o andar"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def andar5desejado4caminholivre(self):
        self.resposta = "Descendo para o 4o andar"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def andar5desejado6caminholivre(self):
        self.resposta = "subindo para o 6o andar"   

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='1')))
    def andar5desejado1caminhoatual1(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar5desejado1caminhoatual2(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar5desejado1caminhoatual3(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='4')))
    def andar5desejado1caminhoatual4(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='6')))
    def andar5desejado1caminhoatual6(self):
        self.resposta = "Descer para 1o andar depois"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar5desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='2')))
    def andar5desejado2caminhoatual2(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar5desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar5desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='6')))
    def andar5desejado2caminhoatual6(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='1')))
    def andar5desejado3caminhoatual1(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='2')))
    def andar5desejado3caminhoatual2(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='3')))
    def andar5desejado3caminhoatual3(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='4')))
    def andar5desejado3caminhoatual4(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='6')))
    def andar5desejado3caminhoatual6(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='1')))
    def andar5desejado4caminhoatual1(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='2')))
    def andar5desejado4caminhoatual2(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='3')))
    def andar5desejado4caminhoatual3(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='4')))
    def andar5desejado4caminhoatual4(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='6')))
    def andar5desejado4caminhoatual6(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='1')))
    def andar5desejado6caminhoatual1(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='2')))
    def andar5desejado6caminhoatual2(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='3')))
    def andar5desejado6caminhoatual3(self):
        self.resposta = "Subir para 6o andar depois"
    
    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='4')))
    def andar5desejado6caminhoatual4(self):
        self.resposta = "Subir para 6o andar depois"

    @Rule(AND(Fact(AndarAtual='5'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='6')))
    def andar5desejado6caminhoatual6(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='6'), Fact(CaminhoAtual='999')))
    def andar6desejado6caminholivre(self):
        self.resposta = "Abrir a porta"
    
    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='999')))
    def andar6desejado1caminholivre(self):
        self.resposta = "Descendo para o 1o andar"
    
    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='999')))
    def andar6desejado2caminholivre(self):
        self.resposta = "Descendo para o 2o andar"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='999')))
    def andar6desejado3caminholivre(self):
        self.resposta = "Descendo para o 3o andar"
    
    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='999')))
    def andar6desejado4caminholivre(self):
        self.resposta = "Descendo para o 4o andar"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='999')))
    def andar6desejado5caminholivre(self):
        self.resposta = "descendo para o 5o andar" 

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='1')))
    def andar6desejado1caminhoatual1(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='2')))
    def andar6desejado1caminhoatual2(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='3')))
    def andar6desejado1caminhoatual3(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='4')))
    def andar6desejado1caminhoatual4(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='1'), Fact(CaminhoAtual='5')))
    def andar6desejado1caminhoatual5(self):
        self.resposta = "Descer para 1o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='1')))
    def andar6desejado2caminhoatual1(self):
        self.resposta = "Subir para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='2')))
    def andar6desejado2caminhoatual2(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='3')))
    def andar6desejado2caminhoatual3(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='4')))
    def andar6desejado2caminhoatual4(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='2'), Fact(CaminhoAtual='5')))
    def andar6desejado2caminhoatual5(self):
        self.resposta = "Descer para 2o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='1')))
    def andar6desejado3caminhoatual1(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='2')))
    def andar6desejado3caminhoatual2(self):
        self.resposta = "Subir para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='3')))
    def andar6desejado3caminhoatual3(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='4')))
    def andar6desejado3caminhoatual4(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='3'), Fact(CaminhoAtual='5')))
    def andar6desejado3caminhoatual5(self):
        self.resposta = "Descer para 3o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='1')))
    def andar6desejado4caminhoatual1(self):
        self.resposta = "Subir para 4o andar depois"
    
    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='2')))
    def andar6desejado4caminhoatual2(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='3')))
    def andar6desejado4caminhoatual3(self):
        self.resposta = "Subir para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='4')))
    def andar6desejado4caminhoatual4(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='4'), Fact(CaminhoAtual='5')))
    def andar6desejado4caminhoatual5(self):
        self.resposta = "Descer para 4o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='1')))
    def andar6desejado5caminhoatual1(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='2')))
    def andar6desejado5caminhoatual2(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='3')))
    def andar6desejado5caminhoatual3(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='4')))
    def andar6desejado5caminhoatual4(self):
        self.resposta = "Subir para 5o andar depois"

    @Rule(AND(Fact(AndarAtual='6'), Fact(AndarDesejado='5'), Fact(CaminhoAtual='5')))
    def andar6desejado5caminhoatual5(self):
        self.resposta = "Elevador ja está a caminho do andar desejado"
    