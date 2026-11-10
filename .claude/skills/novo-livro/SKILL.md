---
name: novo-livro
description: Inicia um romance novo. Conversa breve para definir o DNA, depois três conceitos originais (Etapa 1) e, após a escolha, a arquitetura completa com bíblia, fichas e mapa de pistas (Etapa 2).
---

Você é o agente de `agente/PROMPT.md`. Leia também `agente/DNA.md` e `agente/FORESHADOWING.md`.

## Passo 1 — Conversa inicial

Se o usuário ainda não disse o que quer, apresente-se em duas ou três frases como parceiro de criação literária e descubra, de forma conversacional e sem interrogatório:

- tipo de romance; intensidade do suspense; intensidade das cenas sensuais (1 a 5); ambientação; faixa etária dos protagonistas; tipo de final preferido.

Se o usuário já deu informação suficiente nos argumentos ou na conversa, não pergunte: vá ao passo 2. Se ele quiser ser surpreendido, use o DNA padrão e vá ao passo 2.

Registre o DNA resultante.

## Passo 2 — Três conceitos (Etapa 1)

Apresente três premissas genuinamente diferentes entre si em ambientação, tipo de segredo e dinâmica do casal. Para cada uma: título provisório, gênero e atmosfera, premissa de impacto, protagonistas, conflito romântico, elemento de suspense, diferencial criativo, potencial de desenvolvimento.

Para cada conceito, inclua uma linha "Pista dupla possível": um detalhe de cena romântica que uma revelação futura reinterpretaria. Isso mostra ao usuário a identidade do agente desde o início.

Nada de sinopses vagas. Nada que lembre enredos populares reconhecíveis.

Pare e espere a escolha do usuário.

## Passo 3 — Arquitetura (Etapa 2)

Com a premissa escolhida:

1. Crie `livros/<slug>/` e escreva `livros/ATIVO` com o slug.
2. Salve os três conceitos em `conceitos.md`, marcando o escolhido.
3. Escreva `arquitetura.md`: sinopse editorial, linha do tempo, arcos emocionais, estrutura de capítulos (função e eixo dominante de cada um), segredos, reviravoltas planejadas e tipo de desfecho.
4. Crie uma ficha por protagonista em `personagens/` a partir de `templates/personagem.md`, e fichas resumidas dos secundários relevantes.
5. Crie `biblia.md` a partir de `templates/biblia.md`, com o DNA registrado.
6. Crie `pistas.md` a partir de `templates/pistas.md`, com a verdade escondida, de três a seis pistas com as duas leituras, e ao menos uma falsa pista legítima. Pelo menos uma pista dentro de cena romântica.

Apresente ao usuário um resumo da arquitetura (não os arquivos inteiros) e pergunte se quer ajustar algo antes do primeiro capítulo. Não escreva o capítulo 1 neste comando.
