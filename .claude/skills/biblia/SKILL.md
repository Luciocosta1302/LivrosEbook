---
name: biblia
description: Mostra um resumo da bíblia do livro ativo (estado da relação, cronologia, pistas, pendências) ou registra um fato, decisão ou mudança justificada que o usuário informar.
---

Você é o agente de `agente/PROMPT.md`. Leia `livros/ATIVO` e a `biblia.md` e o `pistas.md` do livro.

Sem argumento: apresente um resumo em poucas linhas por seção: onde a história está (último capítulo, data na cronologia), estado atual da relação, verdade escondida e quantas pistas estão plantadas/pagas, conflitos em aberto, detalhes que precisam voltar, próximos capítulos previstos.

Com argumento: interprete como uma informação a registrar (fato novo, decisão sobre um personagem, mudança de rumo, correção). Atualize a seção correta da bíblia, das fichas ou do mapa de pistas. Se a informação contradiz algo já escrito nos capítulos, avise o usuário, proponha a justificativa narrativa e registre em "Mudanças justificadas" após a confirmação.

Nunca altere um capítulo já escrito a partir deste comando; para isso, use `/revisar`.
