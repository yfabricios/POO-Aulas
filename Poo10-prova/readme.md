<!-- 
MODELS

1- "atendimento, cliente, profissional, servico" tem a mesma estrura e serve para deixar os "get, set, to_json e from_json" (elementos da vida real).

2- "atendimentosao, clientedao, profissionaldao, servicodao, horariodao" criam o arquivo json e fazem o json "inserir, atualizar, etc." e verifica ele (seria como um banco de dados).

3- "horario" como o horario tem que ser feito em conjuntos com os outros precisa conter "servico, cliente, etc."

---------------------------------

TEMPLATES

"manteratendimentoui, manterclienteui, etc." É aqui aonde a interface vai interagir, os botoes, escritas e etc.

---------------------------------

SERVICE.py = ele conecta as UI's com o DAO. Basicamento como a pessoa digita algo ele tranfere para o dao como confirmar

INDEX.py = é o arquivo que escolhe o arquivo que vai aparecer na tela, basicamente serve como controlator.

-->