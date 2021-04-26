# AFD Animator

## Sobre o projeto

    O objetivo do projeto é simular um AFD e AFN. O simulador lê as especificações de um AFD/AFN a partir de um arquivo de entrada do tipo .txt e simula o comportamento passo-a-passo do AFD/AFN sobre uma determinada palavra.

    Logo, a partir de uma especificação de um AF dada por um arquivo de entrada, tem-se como saída uma animação da simulação do comportamento do AF sobre determinada palavra.

## Tecnologias utilizadas

    - Sistema Operacional: Windows
    - Linguaguem: Python

## Implementação

    Utilizou-se o pacote Graphviz para Python, para facilitar a criação e renderização dos grafos na linguagem DOT. Para instalar, utiliza-se a linha de comando abaixo no prompt: 

            $ pip install graphviz

## Execução

    A ferramenta funciona por meio de linha de comando e deve aceitar um arquivo como parâmetro. Logo, ao executar o programa pela linha de comando, é necessário passar o caminho do arquivo de entrada como parâmentro. Por exemplo:

            $ python AFDanimator.py C:\Users\Usuario\Desktop\AFD.txt

    Caso a imagem esteja no mesmo diretório do arquivo .py, basta passar o nome do .txt como parâmetro.

    Ao terminar a execução. Caso seja realizada com sucesso, a palavra a ser consumida pelo autômato será mostrada no prompt, as imagens geradas a cada passo (consumo de um simbolo da palavra) e o gif com a animação da palavra sendo consumida será armazenada em uma pasta de nome "output". As imagens terão nome 'grafo0.gv.png', 'grafo1.gv.png', 'grafo2.gv.png' até 'grafoN.gv.png' onde N é o tamanho da palavra. O gif gerado terá nome 'animacao.gif'.

    A cada simbolo, os estados correntes serão pintados de cinza. 

    Ao final da palavra, os estados correntes serão pintados das seguintes cores:

			- Verde: caso a palavra for aceita pelo autômato.
			- Vermelho: caso a palavra não for aceita pelo automâto.

## Exemplos

    No diretório do projeto, há dois arquivos de texto que contêm a configuração de dois AFs (um AFN e um AFD). Há também, duas pastas referentes a sáida obtida para os dois exemplos.

## Observações importantes

    É necessário manter a pasta output limpa, pois o código reunirá todas as imagens contidas nela para gerar o gif, caso tenha alguma imagem que não foi gerada pela execução isso poderá gerar uma animação erradao.
    
