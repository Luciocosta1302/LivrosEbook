---
name: capitulo
description: Escreve o próximo capítulo do livro ativo (ou o capítulo indicado), com planejamento, revisão interna pelo checklist e atualização da bíblia e do mapa de pistas no mesmo turno.
---

Você é o agente de `agente/PROMPT.md`. Argumento opcional: número do capítulo ou instruções do usuário para este capítulo.

## Antes de escrever

1. Leia `livros/ATIVO`, depois `biblia.md`, `pistas.md`, `arquitetura.md` e as fichas de quem aparece no capítulo. Leia também o capítulo anterior inteiro.
2. Determine o número do capítulo: o próximo na estrutura, salvo indicação do usuário.
3. Preencha mentalmente o cabeçalho de `templates/capitulo.md`: função principal, o que muda, eixo dominante do DNA, camadas A/B/C, pista a plantar ou pagar, cena íntima (ou não) e sua motivação, e a alternativa menos previsível para a cena principal.
4. Se o mapa prevê uma pista para este capítulo, planeje a cena de modo que a pista seja útil na própria cena e tenha leitura inocente mais provável (`agente/FORESHADOWING.md`).

## Escrita (Etapa 3)

- Cenas dramatizadas, não resumos. Diálogo com subtexto. Voz distinta por personagem.
- Continuidade estrita com a cronologia e com "quem sabe o quê".
- Respeite o DNA: um eixo domina, outro acompanha.
- Extensão coerente com o planejado na arquitetura.

## Revisão (Etapa 4)

Aplique `agente/REVISAO.md` por inteiro. Reescreva o que falhar. Só então entregue.

## Entrega

1. Salve em `livros/<slug>/capitulos/NN-<titulo-curto>.md` com o cabeçalho de planejamento preenchido em comentário, incluindo "função cumprida" e observações da revisão.
2. Atualize `biblia.md`: cronologia, estado da relação, quem sabe o quê, fatos novos, objetos, lugares, conflitos em aberto, detalhes que precisam voltar, status na estrutura de capítulos.
3. Atualize `pistas.md`: pista plantada (com o trecho exato) ou paga.
4. Responda ao usuário em poucas linhas: o que acontece, o que mudou na relação, pista plantada ou paga, pendência para o próximo capítulo. Depois, o texto do capítulo.
