---
name: dna
description: Mostra ou altera o DNA literário (romance, suspense, humor, sensualidade) do livro ativo, explicando o que cada mudança altera na escrita dos próximos capítulos.
---

Você é o agente de `agente/PROMPT.md`. Leia `agente/DNA.md`, `livros/ATIVO` e a `biblia.md` do livro.

Sem argumento: mostre o DNA atual do livro no formato de `agente/DNA.md` e, em duas ou três frases, como ele está se refletindo nos capítulos escritos.

Com argumento (ex.: "suspense 70", "sensualidade 2", "mais humor"): 
1. Traduza o pedido em novos valores.
2. Explique, com base nas tabelas de `agente/DNA.md`, o que muda concretamente na escrita a partir do próximo capítulo.
3. Se a mudança afeta a arquitetura (ex.: suspense sobe muito e a estrutura só tinha uma reviravolta), proponha os ajustes em `arquitetura.md` e `pistas.md` e peça confirmação antes de aplicá-los.
4. Registre o novo DNA na bíblia com a data e o capítulo a partir do qual vale.

Não altere capítulos já escritos.
