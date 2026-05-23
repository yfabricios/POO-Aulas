## 1. Requisitos Funcionais (RF)
- **RF01 - Login de Alunos**: O sistema deve permitir que os Alunos façam login utilizando a mesma matrícula e senha do sistema acadêmico da escola.
- **RF02 - Submeter Proposta**: O sistema deve permitir que um aluno possa submeter a proposta de um projeto informando título, área de conhecimento e um resumo.
- **RF03 - Busca para Convidar Colegas**: O sistema deve permitir que o aluno possa convidar outros colegas para sua equipe, buscando pelo nome ou matrícula.
- **RF04 - Inscrições Encerradas Automaticamente**: O sistema deve encerrar todas as inscrições de projetos exatamente 15 dias antes da data do evento.
- **RF05 - Verificação se está em Equipe**: O sistema deve verificar se o aluno já está em uma equipe.
- **RF06 - Permissão de Projetos**: O sistema não deve permitir que um aluno seja convidado para outra equipe caso já participe de uma.
- **RF07 - Visualização de Orientadores**: O sistema deve permitir que Professores Orientadores acessem o sistema para visualizar os projetos submetidos na sua área de conhecimento.
- **RF08 - E-mail do Motivo da Recusa**: O sistema deve enviar um e-mail aos alunos da equipe informando o motivo caso o projeto seja recusado.
- **RF09 - Atribuição de Nota do Avaliador**: O sistema deve permitir que o avaliador acesse o projeto pelo sistema e atribua notas de 0 a 10 para três critérios: Inovação, Execução Técnica e Apresentação.
- **RF10 - Salvamento Offline**: O sistema deve ser capaz de salvar as notas offline no navegador do avaliador e sincronizar com o servidor assim que a conexão voltar.
- **RF11 - Painel para a Coordenação**: O sistema deve fornecer um painel para a Coordenação realizar o encerramento oficial das avaliações do evento.
- **RF12 - Média Aritmética**: O sistema deve calcular a média aritmética das notas de cada equipe e gerar o ranking geral por área de conhecimento após o fechamento das avaliações.
- **RF13 - Ranking Geral em PDF**: O sistema deve permitir a exportação desse resultado em formato PDF para a cerimônia de premiação.

## 2. Requisitos Não Funcionais (RNF)
- **RNF01 - Interoperabilidade**: O sistema deve integrar-se ao sistema acadêmico da escola por meio de uma API para realizar a validação de login (matrícula e senha).
- **RNF02 - Responsividade**: Obrigatoriamente as telas do sistema devem se adaptar perfeitamente a dispositivos móveis como tablets e celulares (design responsivo).
- **RNF03 - Tolerância de Falhas**: O sistema deve ser capaz de operar em modo offline no navegador do avaliador para armazenar localmente os dados das avaliações em caso de queda de rede.

## 3. Regras de Negócio (RN)
- **RN01 - Mínimo e Máximo de Aluno**: Cada equipe pode ter no máximo 4 alunos e no mínimo 2.
- **RN02 - Projetos por Ano**: Um aluno só pode participar de um único projeto por ano.
- **RN03 - Bloqueio de Convites**: O sistema deve impedir que um aluno receba ou aceite convites caso ele já pertença a uma equipe ativa.
- **RN04 - Prazo de Inscrição**: O bloqueio automático de submissões de projetos deve ocorrer exatamente 15 dias antes da data estipulada para o evento.

- **RN05 - Projeto Recusado**: Os Professores Orientadores precisam avaliar a proposta e decidir se a aprovam ou recusam[cite: 25]. [cite_start]Caso o projeto seja recusado, o professor deve obrigatoriamente preencher um campo de justificativa.
- **RN06 - Escala de Pontuação**: As notas atribuídas pelos avaliadores devem limitar-se estritamente ao intervalo de 0 a 10 para cada um dos seguintes critérios: Inovação, Execução Técnica e Apresentação.