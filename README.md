# LivrosEbook — Agente Literário

Um escritor de ficção configurado como parceiro de criação: romancista brasileiro contemporâneo, editor, roteirista e arquiteto de histórias.

A proposta é combinar a **química romântica, os diálogos inteligentes e a tensão amorosa** (estudadas em Ali Hazelwood) com a **arquitetura de mistérios, reviravoltas e personagens psicologicamente complexos** (estudada em Raphael Montes), sem copiar nenhum dos dois. O resultado deve ter identidade própria: romances viciantes, emocionantes, sensuais e imprevisíveis, que pareçam vividos, não fabricados.

## Estrutura do repositório

```
agente/
  PROMPT.md            Prompt mestre do agente (identidade, regras, método de trabalho)
  DNA.md               DNA literário: os quatro eixos ajustáveis e o que cada valor muda na escrita
  FORESHADOWING.md     Protocolo de pista dupla (o diferencial da casa)
  REVISAO.md           Checklist de revisão aplicado a todo capítulo antes de ser entregue
templates/
  biblia.md            Bíblia do livro (memória literária)
  personagem.md        Ficha psicológica de protagonista
  pistas.md            Mapa de pistas, leituras inocentes e revelações
  capitulo.md          Cabeçalho de planejamento de capítulo
livros/
  <slug-do-livro>/     Um diretório por romance (ver livros/README.md)
.claude/
  agents/romancista.md Subagente para uso dentro do Claude Code
  skills/              Comandos: /novo-livro, /capitulo, /revisar, /biblia, /dna, /tendencias
CLAUDE.md              Instruções que ativam o agente ao abrir este repositório no Claude Code
```

## Como usar

### No Claude Code

Abra este repositório. O `CLAUDE.md` carrega o agente automaticamente.

| Comando | O que faz |
|---|---|
| `/novo-livro` | Conversa inicial e, depois, três conceitos originais (Etapa 1) seguidos da arquitetura (Etapa 2) |
| `/capitulo` | Escreve o próximo capítulo do livro ativo, com revisão interna, e atualiza a bíblia |
| `/revisar` | Passa o checklist de revisão em um capítulo existente e reescreve os trechos fracos |
| `/biblia` | Mostra ou atualiza a bíblia do livro (fatos, cronologia, pistas, pendências) |
| `/dna` | Mostra ou altera o DNA literário do livro ativo |
| `/tendencias` | Pesquisa o mercado editorial atual (só com acesso à internet; nunca inventa dados) |

### Em qualquer outro chat

Copie o conteúdo de `agente/PROMPT.md` como instrução de sistema e, se quiser ajustar o equilíbrio da obra, inclua também `agente/DNA.md` com os valores escolhidos.

## DNA literário padrão

| Eixo | Valor inicial |
|---|---|
| Romance e conexão emocional | 90% |
| Suspense e reviravoltas | 55% |
| Humor e diálogos divertidos | 65% |
| Intensidade das cenas sensuais | 4 de 5 |

Esses valores não são fórmula matemática. São orientações para que o romance seja o coração da obra e o suspense funcione como segunda força narrativa. Cada livro pode ter o seu próprio DNA, registrado na bíblia.

## Princípios inegociáveis

- Originalidade, profundidade e naturalidade nunca são sacrificadas por previsibilidade.
- Nada de escrita genérica de IA: a beleza vem da precisão, não do excesso de adjetivos.
- Toda reviravolta é preparada com pistas legítimas. O leitor deve pensar "como não percebi?", nunca "de onde saiu isso?".
- Somente personagens adultos, relações consensuais, e cenas íntimas sempre ligadas à evolução emocional.
- Nenhum dado editorial é inventado.
