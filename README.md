## MINI PROJETO IA1 - CRIAÇÃO DE UM SISTEMA ESPECIALISTA PARA MANIPULAÇÃO DE UM ELEVADOR

Este projeto tem o objetivo da criação de um Um sistema baseado em conhecimento para controlar
um elevador em um prédio de 6 andares. Foi feito durante a disciplina Inteligência Artificial 1 do período 2020.2 no Instituto da Computação - IC, na Universidade Federal de Alagoas - UFAL.

Professor da disciplina:
* Evandro Barros           - Professor Adjunto              - evandro@ic.ufal.br

Participantes:
* Élisson Souza            - Engenharia de Computação       - efs2@ic.ufal.br
* Wilamis Micael           - Engenharia de Computação       - wmaa@ic.ufal.br

## Base de regras de decisão
| Regras | Condições      |                         |                                 | Saída                                        |
|--------|----------------|-------------------------|---------------------------------|----------------------------------------------|
|        | Andar desejado | Andar atual do elevador | andar o elevador está a caminho |                                              |
| R1     | 1              | 1                       | 999                             | Abrir a porta                                |
| R2     | 2              | 1                       | 999                             | Subir para 2o andar                          |
| R3     | 3              | 1                       | 999                             | Subir para 3o andar                          |
| R4     | 4              | 1                       | 999                             | Subir para 4o andar                          |
| R5     | 5              | 1                       | 999                             | Subir para 5o andar                          |
| R6     | 6              | 1                       | 999                             | Subir para 6o andar                          |
| R7     | 1              | 1                       | 2                               | Descer para 1o andar depois                  |
| R8     | 1              | 1                       | 3                               | Descer para 1o andar depois                  |
| R9     | 1              | 1                       | 4                               | Descer para 1o andar depois                  |
| R10    | 1              | 1                       | 5                               | Descer para 1o andar depois                  |
| R11    | 1              | 1                       | 6                               | Descer para 1o andar depois                  |
| R12    | 2              | 1                       | 2                               | Elevador já está a caminho do andar desejado |
| R13    | 2              | 1                       | 3                               | Descer para 2o andar depois                  |
| R14    | 2              | 1                       | 4                               | Descer para 2o andar depois                  |
| R15    | 2              | 1                       | 5                               | Descer para 2o andar depois                  |
| R16    | 2              | 1                       | 6                               | Descer para 2o andar depois                  |
| R17    | 3              | 1                       | 2                               | Subir para 3o andar depois                   |
| R18    | 3              | 1                       | 3                               | Elevador já está a caminho do andar desejado |
| R19    | 3              | 1                       | 4                               | Descer para 3o andar depois                  |
| R20    | 3              | 1                       | 5                               | Descer para 3o andar depois                  |
| R21    | 3              | 1                       | 6                               | Descer para 3o andar depois                  |
| R22    | 4              | 1                       | 2                               | Subir para 4o andar depois                   |
| R23    | 4              | 1                       | 3                               | Subir para 4o andar depois                   |
| R24    | 4              | 1                       | 4                               | Elevador já está a caminho do andar desejado |
| R25    | 4              | 1                       | 5                               | Descer para 4o andar depois                  |
| R26    | 4              | 1                       | 6                               | Descer para 4o andar depois                  |
| R27    | 5              | 1                       | 2                               | Subir para 5o andar depois                   |
| R28    | 5              | 1                       | 3                               | Subir para 5o andar depois                   |
| R29    | 5              | 1                       | 4                               | Subir para 5o andar depois                   |
| R30    | 5              | 1                       | 5                               | Elevador já está a caminho do andar desejado |
| R31    | 5              | 1                       | 6                               | Descer para 5o andar depois                  |
| R32    | 6              | 1                       | 2                               | Subir para 6o andar depois                   |
| R33    | 6              | 1                       | 3                               | Subir para 6o andar depois                   |
| R34    | 6              | 1                       | 4                               | Subir para 6o andar depois                   |
| R35    | 6              | 1                       | 5                               | Subir para 6o andar depois                   |
| R36    | 6              | 1                       | 6                               | Elevador já está a caminho do andar desejado |
| R37    | 1              | 2                       | 999                             | Descer para 1o andar                         |
| R38    | 2              | 2                       | 999                             | Abrir a porta                                |
| R39    | 3              | 2                       | 999                             | Subir para 3o andar                          |
| R40    | 4              | 2                       | 999                             | Subir para 4o andar                          |
| R41    | 5              | 2                       | 999                             | Subir para 5o andar                          |
| R42    | 6              | 2                       | 999                             | Subir para 6o andar                          |
| R43    | 1              | 2                       | 1                               | Elevador já está a caminho do andar desejado |
| R44    | 1              | 2                       | 3                               | Descer para 1o andar depois                  |
| R45    | 1              | 2                       | 4                               | Descer para 1o andar depois                  |
| R46    | 1              | 2                       | 5                               | Descer para 1o andar depois                  |
| R47    | 1              | 2                       | 6                               | Descer para 1o andar depois                  |
| R48    | 2              | 2                       | 1                               | Subir para 2o andar depois                   |
| R49    | 2              | 2                       | 3                               | Descer para 2o andar depois                  |
| R50    | 2              | 2                       | 4                               | Descer para 2o andar depois                  |
| R51    | 2              | 2                       | 5                               | Descer para 2o andar depois                  |
| R52    | 2              | 2                       | 6                               | Descer para 2o andar depois                  |
| R53    | 3              | 2                       | 1                               | Subir para 3o andar depois                   |
| R54    | 3              | 2                       | 3                               | Elevador já está a caminho do andar desejado |
| R55    | 3              | 2                       | 4                               | Descer para 3o andar depois                  |
| R56    | 3              | 2                       | 5                               | Descer para 3o andar depois                  |
| R57    | 3              | 2                       | 6                               | Descer para 3o andar depois                  |
| R58    | 4              | 2                       | 1                               | Subir para 4o andar depois                   |
| R59    | 4              | 2                       | 3                               | Subir para 4o andar depois                   |
| R60    | 4              | 2                       | 4                               | Elevador já está a caminho do andar desejado |
| R61    | 4              | 2                       | 5                               | Descer para 4o andar depois                  |
| R62    | 4              | 2                       | 6                               | Descer para 4o andar depois                  |
| R63    | 5              | 2                       | 1                               | Subir para 5o andar depois                   |
| R64    | 5              | 2                       | 3                               | Subir para 5o andar depois                   |
| R65    | 5              | 2                       | 4                               | Subir para 5o andar depois                   |
| R66    | 5              | 2                       | 5                               | Elevador já está a caminho do andar desejado |
| R67    | 5              | 2                       | 6                               | Descer para 5o andar depois                  |
| R68    | 6              | 2                       | 1                               | Subir para 6o andar depois                   |
| R69    | 6              | 2                       | 3                               | Subir para 6o andar depois                   |
| R70    | 6              | 2                       | 4                               | Subir para 6o andar depois                   |
| R71    | 6              | 2                       | 5                               | Subir para 6o andar depois                   |
| R72    | 6              | 2                       | 6                               | Elevador já está a caminho do andar desejado |
| R73    | 1              | 3                       | 999                             | Descer para 1o andar                         |
| R74    | 2              | 3                       | 999                             | Descer para 2o andar                         |
| R75    | 3              | 3                       | 999                             | Abrir a porta                                |
| R76    | 4              | 3                       | 999                             | Subir para 4o andar                          |
| R77    | 5              | 3                       | 999                             | Subir para 5o andar                          |
| R78    | 6              | 3                       | 999                             | Subir para 6o andar                          |
| R79    | 1              | 3                       | 1                               | Elevador já está a caminho do andar desejado |
| R80    | 1              | 3                       | 2                               | Descer para 1o andar depois                  |
| R81    | 1              | 3                       | 4                               | Descer para 1o andar depois                  |
| R82    | 1              | 3                       | 5                               | Descer para 1o andar depois                  |
| R83    | 1              | 3                       | 6                               | Descer para 1o andar depois                  |
| R84    | 2              | 3                       | 1                               | Subir para 2o andar depois                   |
| R85    | 2              | 3                       | 2                               | Elevador já está a caminho do andar desejado |
| R86    | 2              | 3                       | 4                               | Descer para 2o andar depois                  |
| R87    | 2              | 3                       | 5                               | Descer para 2o andar depois                  |
| R88    | 2              | 3                       | 6                               | Descer para 2o andar depois                  |
| R89    | 4              | 3                       | 1                               | Subir para 4o andar depois                   |
| R90    | 4              | 3                       | 2                               | Subir para 4o andar depois                   |
| R91    | 4              | 3                       | 4                               | Elevador já está a caminho do andar desejado |
| R92    | 4              | 3                       | 5                               | Descer para 4o andar depois                  |
| R93    | 4              | 3                       | 6                               | Descer para 4o andar depois                  |
| R94    | 5              | 3                       | 1                               | Subir para 5o andar depois                   |
| R95    | 5              | 3                       | 2                               | Subir para 5o andar depois                   |
| R96    | 5              | 3                       | 4                               | Subir para 5o andar depois                   |
| R97    | 5              | 3                       | 5                               | Elevador já está a caminho do andar desejado |
| R98    | 5              | 3                       | 6                               | Descer para 5o andar depois                  |
| R99    | 6              | 3                       | 1                               | Subir para 6o andar depois                   |
| R100   | 6              | 3                       | 2                               | Subir para 6o andar depois                   |
| R101   | 6              | 3                       | 4                               | Subir para 6o andar depois                   |
| R102   | 6              | 3                       | 5                               | Subir para 6o andar depois                   |
| R103   | 6              | 3                       | 6                               | Elevador já está a caminho do andar desejado |
| R104   | 1              | 4                       | 999                             | Descer para 1o andar                         |
| R105   | 2              | 4                       | 999                             | Descer para 2o andar                         |
| R106   | 3              | 4                       | 999                             | Descer para 3o andar                         |
| R107   | 4              | 4                       | 999                             | Abrir a porta                                |
| R108   | 5              | 4                       | 999                             | Subir para 5o andar                          |
| R109   | 6              | 4                       | 999                             | Subir para 6o andar                          |
| R110   | 1              | 4                       | 1                               | Elevador já está a caminho do andar desejado |
| R111   | 1              | 4                       | 2                               | Descer para 1o andar depois                  |
| R112   | 1              | 4                       | 3                               | Descer para 1o andar depois                  |
| R113   | 1              | 4                       | 5                               | Descer para 1o andar depois                  |
| R114   | 1              | 4                       | 6                               | Descer para 1o andar depois                  |
| R115   | 2              | 4                       | 1                               | Subir para 2o andar depois                   |
| R116   | 2              | 4                       | 2                               | Elevador já está a caminho do andar desejado |
| R117   | 2              | 4                       | 3                               | Descer para 2o andar depois                  |
| R118   | 2              | 4                       | 5                               | Descer para 2o andar depois                  |
| R119   | 2              | 4                       | 6                               | Descer para 2o andar depois                  |
| R120   | 3              | 4                       | 1                               | Subir para 3o andar depois                   |
| R121   | 3              | 4                       | 2                               | Subir para 3o andar depois                   |
| R122   | 3              | 4                       | 3                               | Elevador já está a caminho do andar desejado |
| R123   | 3              | 4                       | 5                               | Descer para 3o andar depois                  |
| R124   | 3              | 4                       | 6                               | Descer para 3o andar depois                  |
| R125   | 5              | 4                       | 1                               | Subir para 5o andar depois                   |
| R126   | 5              | 4                       | 2                               | Subir para 5o andar depois                   |
| R127   | 5              | 4                       | 3                               | Subir para 5o andar depois                   |
| R128   | 5              | 4                       | 5                               | Elevador já está a caminho do andar desejado |
| R129   | 5              | 4                       | 6                               | Descer para 5o andar depois                  |
| R130   | 6              | 4                       | 1                               | Subir para 6o andar depois                   |
| R131   | 6              | 4                       | 2                               | Subir para 6o andar depois                   |
| R132   | 6              | 4                       | 3                               | Subir para 6o andar depois                   |
| R133   | 6              | 4                       | 5                               | Subir para 6o andar depois                   |
| R134   | 6              | 4                       | 6                               | Elevador já está a caminho do andar desejado |
| R135   | 1              | 5                       | 999                             | Descer para 1o andar                         |
| R136   | 2              | 5                       | 999                             | Descer para 2o andar                         |
| R137   | 3              | 5                       | 999                             | Descer para 3o andar                         |
| R138   | 4              | 5                       | 999                             | Descer para 4o andar                         |
| R139   | 5              | 5                       | 999                             | Abrir a porta                                |
| R140   | 6              | 5                       | 999                             | Subir para 6o andar                          |
| R141   | 1              | 5                       | 1                               | Elevador já está a caminho do andar desejado |
| R142   | 1              | 5                       | 2                               | Descer para 1o andar depois                  |
| R143   | 1              | 5                       | 3                               | Descer para 1o andar depois                  |
| R144   | 1              | 5                       | 4                               | Descer para 1o andar depois                  |
| R145   | 1              | 5                       | 6                               | Descer para 1o andar depois                  |
| R146   | 2              | 5                       | 1                               | Subir para 2o andar depois                   |
| R147   | 2              | 5                       | 2                               | Elevador já está a caminho do andar desejado |
| R148   | 2              | 5                       | 3                               | Descer para 2o andar depois                  |
| R149   | 2              | 5                       | 4                               | Descer para 2o andar depois                  |
| R150   | 2              | 5                       | 6                               | Descer para 2o andar depois                  |
| R151   | 3              | 5                       | 1                               | Subir para 3o andar depois                   |
| R152   | 3              | 5                       | 2                               | Subir para 3o andar depois                   |
| R153   | 3              | 5                       | 3                               | Elevador já está a caminho do andar desejado |
| R154   | 3              | 5                       | 4                               | Descer para 3o andar depois                  |
| R155   | 3              | 5                       | 6                               | Descer para 3o andar depois                  |
| R156   | 4              | 5                       | 1                               | Subir para 4o andar depois                   |
| R157   | 4              | 5                       | 2                               | Subir para 4o andar depois                   |
| R158   | 4              | 5                       | 3                               | Subir para 4o andar depois                   |
| R159   | 4              | 5                       | 4                               | Elevador já está a caminho do andar desejado |
| R160   | 4              | 5                       | 6                               | Descer para 4o andar depois                  |
| R161   | 6              | 5                       | 1                               | Subir para 6o andar depois                   |
| R162   | 6              | 5                       | 2                               | Subir para 6o andar depois                   |
| R163   | 6              | 5                       | 3                               | Subir para 6o andar depois                   |
| R164   | 6              | 5                       | 4                               | Subir para 6o andar depois                   |
| R165   | 6              | 5                       | 6                               | Elevador já está a caminho do andar desejado |
| R166   | 1              | 6                       | 999                             | Descer para 1o andar                         |
| R167   | 2              | 6                       | 999                             | Descer para 2o andar                         |
| R168   | 3              | 6                       | 999                             | Descer para 3o andar                         |
| R169   | 4              | 6                       | 999                             | Descer para 4o andar                         |
| R170   | 5              | 6                       | 999                             | Descer para 5o andar                         |
| R171   | 6              | 6                       | 999                             | Abrir a porta                                |
| R172   | 1              | 6                       | 1                               | Elevador já está a caminho do andar desejado |
| R173   | 1              | 6                       | 2                               | Descer para 1o andar depois                  |
| R174   | 1              | 6                       | 3                               | Descer para 1o andar depois                  |
| R175   | 1              | 6                       | 4                               | Descer para 1o andar depois                  |
| R176   | 1              | 6                       | 5                               | Descer para 1o andar depois                  |
| R177   | 2              | 6                       | 1                               | Subir para 2o andar depois                   |
| R178   | 2              | 6                       | 2                               | Elevador já está a caminho do andar desejado |
| R179   | 2              | 6                       | 3                               | Descer para 2o andar depois                  |
| R180   | 2              | 6                       | 4                               | Descer para 2o andar depois                  |
| R181   | 2              | 6                       | 6                               | Descer para 2o andar depois                  |
| R182   | 3              | 6                       | 1                               | Subir para 3o andar depois                   |
| R183   | 3              | 6                       | 2                               | Subir para 3o andar depois                   |
| R184   | 3              | 6                       | 3                               | Elevador já está a caminho do andar desejado |
| R185   | 3              | 6                       | 5                               | Descer para 3o andar depois                  |
| R186   | 3              | 6                       | 6                               | Descer para 3o andar depois                  |
| R187   | 4              | 6                       | 1                               | Subir para 4o andar depois                   |
| R188   | 4              | 6                       | 2                               | Subir para 4o andar depois                   |
| R189   | 4              | 6                       | 3                               | Subir para 4o andar depois                   |
| R190   | 4              | 6                       | 4                               | Elevador já está a caminho do andar desejado |
| R191   | 4              | 6                       | 6                               | Descer para 4o andar depois                  |
| R192   | 5              | 6                       | 1                               | Subir para 5o andar depois                   |
| R193   | 5              | 6                       | 2                               | Subir para 5o andar depois                   |
| R194   | 5              | 6                       | 3                               | Subir para 5o andar depois                   |
| R195   | 5              | 6                       | 4                               | Subir para 5o andar depois                   |
| R196   | 5              | 6                       | 5                               | Elevador já está a caminho do andar desejado |
