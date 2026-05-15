#Tarefa 2.1, Definição da Arquitetura

Escolhi a arquitetura em camadas pois separa o sistema em responsabilidades bem definidaas, o que é perfeito pra um desenvolvimento web; e assim, facilitando manuteranção, segurança e escalonamento

                ┌─────────────────┐
                │     Usuários    │
                │ Aluno/Professor │
                │     Gestor      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │    Frontend     │
                │      Web        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   API Backend   │
                └────────┬────────┘
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
┌─────────────┐ ┌────────────────┐ ┌──────────────┐
│ Autenticação│ │ Controle da IA │ │ Relatórios   │
└──────┬──────┘ └────────┬───────┘ └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                ┌─────────────────┐
                │ Banco de Dados  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Serviço de IA   │
                └─────────────────┘

Explicação desses relacionamentos:

Usuários → *acessam* → Frontend  
Frontend → *envia requisições para* → API Backend  
API Backend → *gerencia* → Serviço de Autenticação  
API Backend → *controla* → Serviço de Gerenciamento de Turmas  
API Backend → *coordena* → Serviço de Chat Educacional  
API Backend → *gera dados para* → Serviço de Relatórios  
API Backend → *envia conteúdos para validação* → Serviço de Controle da IA  
Serviço de Controle da IA → *filtra informações antes de enviar para* → Serviço de IA  
Todos os serviços → *armazenam e recuperam dados de* → Banco de Dados

Limitação: 
A principal limitação dessa arquitetura é o sobrecarregamento do backend. 

Reflexão final:
Essa padrão arquitetural é mais fácil de desenvolver no começo, mas se for MUITO pra frente, pode virar um grande problema. Achei isso paia. Provavelmente não usaria num projeto real. 

#Tarefa 2.1

1 - Factory Method - Criacional - Com o objetivo de centralizar a criação de diferentes usuários
Usado em user.py -> UserFactory -> create_user()

          User
            ▲
 ┌──────────┼──────────┐
 │          │          │
Teacher   Student   Manager
            ▲
            │
       UserFactory

2 - Strategy - Comportamental - Permitir diferentes estratéias de resposta de IA
Usado em ai_service.py -> ResponseStrategy 
                          NormalResponse
                          SimplifiedResponse

        ResponseStrategy
               ▲
       ┌───────┴────────┐
       │                │
NormalResponse   SimplifiedResponse
       ▲
       │
    AIService

Um problema futuro é ter vários tipos de usuários. Hoje temos 3: Professor, aluno e gestor. Isso pode escalonar muito na função create_user. Já a função estrategy é bom num projeto menor porque aumenta flexiblidade, mas com o escalonamente do projeto aumenta ainda mais a complexidade. 

#Tarefa 2.3

Foram utilizados testes unitários com unittest, testando funções isoladas do sistema, como criação de usuários e gerenciamento de materiais. Essa estratégia é adequada pra protótipos simples, podendo testar coisa por coisas. Não foi testand interface gráfica, integração com IA ou banco de dados. 

Acho que a parte mais difícil de testar seria a parte da interação com a IA, porque depende muito das pessoas que vão usar ess serviço. Pode ser qualquer tipo de pessoa. 