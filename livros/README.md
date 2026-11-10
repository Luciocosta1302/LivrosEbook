# livros/

Um diretório por romance, nomeado com um slug curto em minúsculas (ex.: `noite-de-sao-joao`).

```
livros/<slug>/
  biblia.md             Memória oficial do livro (de templates/biblia.md)
  pistas.md             Mapa de pistas e reviravoltas (de templates/pistas.md)
  conceitos.md          Os três conceitos apresentados na Etapa 1 e qual foi escolhido
  arquitetura.md        Sinopse, linha do tempo, arcos, estrutura de capítulos (Etapa 2)
  personagens/
    <nome>.md           Uma ficha por protagonista e por secundário relevante (de templates/personagem.md)
  capitulos/
    01-<titulo>.md      Um arquivo por capítulo, com o cabeçalho de planejamento em comentário
    02-<titulo>.md
```

O livro ativo é o indicado em `livros/ATIVO` (arquivo de texto com o slug). Os comandos `/capitulo`, `/revisar`, `/biblia` e `/dna` trabalham sobre ele. Se o arquivo não existir e houver só um livro, ele é o ativo.
