# Work_Roleta
 
## Roteiro
Salve salve

Antes de mais nada, o trabalho pode ser encontrado no github: https://github.com/oziieljuniior/Work_Roleta

Qualquer atualização prévia, ou ajuste no código, deve ser comunicado diretamento no grupo de whatsapp.

Na versão de lançamento - 28/02/2023. O diretório do trabalho consiste em 12 arquivos na sua aba inicia. São eles:

1) Data1/
2) Data2/
3) data_teste/
4) pictures/
5) python_project/
6) search/
7) gitattributes
8) gitignore
9) python-version
10) LICENSE
11) README.md
12) requerimentos.txt

Cada arquivo tem sua funcionalidade e pode ser alterado futuramento, de acordo com o decorrer do trabalho. Segue uma explicação breve sobre:

1) Data1/

	Este arquivo foi elaborado inicialmente como data_teste, contudo, ao realizar a atualização dos códigos, o seu nome foi mudado para data1. E ele existe porque é o primeiro conjunto de imagens coletado do site de aposta. Além disso, ele pode servir para treinamento e estudo de casos futuros.

2) Data2/

	De maneira análoga ao Data1/, o arquivo foi utilizado como data_teste e em comparação ao primeiro arquivo, o Data2/ vem com algumas atualizações dentro do seu diretório que deve ser utilizado em todas as coletas futuras. Sua estrutura interna foi dividida em:
	
	1) Numero_Tratado/
	2) Numeros/
	3) Numeros_Gerais/
	
	Esses três arquivos tem a sua funcionalidade explicada a partir do código elaborado no trabalho. E eles consistem em, 1) tratamento das imagens coletadas, 2) imagens coletadas e 3) verificação das imagens coletadas. 

3) data_teste/

	Este arquivo é utilizado para coleta mútua dos números sorteados na roleta, seu desenvolvimento tem a mesma estrutua do arquivo Data2/ e é nele que os códigos restantes vão estar se baseando em eventuais sinais de sequência de números.

4) pictures/

	No decorrer do trabalho são realzidas algumas amostras de fotos do seu desenvolvimento, assim, nesse arquivo ficam localizados todos os ensaios, alertas, avisos, caracteristicas, visualização de padrões e outros. 
5) python_project/

	Arquivo principal do projeto, sua estrutura interna é dividida em:

	1) Reconhecimento/
	2) att.mp3
	3) class_mouse_position.py
	4) fire_0_0.py
	5) fire_0_1.py
	6) get_colors.py
	7) hour_mouse.py
	
	Os códigos do 3) ~ 7) são utilizados de acordo com a proposta do trabalho. E os arquivos 1) e 2) são para trabalho de reconhecimento de caracteres em imagens e música de alerta respectivamente. Em seguida, estarei detalhando como utilizar esses códigos para trabalho de coleta e análise dos números.
	
6) search/
	
	Esse arquivo é suporte do arquivo do python_project e nele estão salvos imagens do arquivo fire_0_0.py. Estas, organizam e estruturam o código como um todo.
	
7) gitattributes

	Arquivo suporte para upload do projeto direto do pc.
	
8) gitignore

	Arquivo suporte para upload do projeto direto do pc.
	
9) python-version

	arquivo que identifica a versão do python utilizada para desenvolvimento do trabalho
	
10) LICENSE

	copyright do projeto
	
11) README.md

	Arquivo onde podemos estruturar o relatório
	
12) requerimentos.txt

	Arquivo das bibliotecas utilizadas no projeto
	
- Explicação dos códigos

	Observe que a ideia do projeto consistia em, implementar um código onde ele identificaria os números sorteados no jogo e a partir de um padrão de repetição de coluna, enviar um sinal ao usuário. Esse padrão de ajuste deve ser configurado pelo usuário. E se possível, implementar um código que realize o carregamento da aba do jogo no navegador.
	
	Dessa maneira, para a implementação desse projeto como um todo, o seu desenvolvimento foi
1) Utilizar um código onde ele realiza a captura dos números sorteados
2) Utilizar um código onde ele realiza a conversão do número sorteado e avise o usuário
3) Utilizar um código que realiza o carregamento da aba do jogo no navegador

	Assim, os arquivos principais podem ser identificados como

1. fire_0_0.py
2. fire_0_1.py
3. hour_mouse.py

	E os arquivos secundários são
	
	1) att.mp3
	2) class_mouse_position.py
	3) get_colors.py
	
	Então, para a utilização dos códigos, você pode realizar a seguinte estrutura:
	
	1) Ao realizar o inicio da coleta, verificar se as posições estão e cores estão sendo identificadas com o código get_colors.py. Caso seja necessário um ajuste, utilize o arquivo class_mouse_position.py para capturar a posição do mouse na tela.
	2) Em seguida, verifique se os cliques em tela do arquivo hour_mouse.py estão funcionando, coso seja necessário um ajuste, utilize o aquivo class_mouse_position.py para capturar a posição do mouse na tela.
	3) Verifique se a pasta data_teste/Numeros/ está vazia, caso seja necessário ajuste a pasta de acordo com a sua necessidade. Mas atenção, essa pasta deve estar vazia para cada reinicio do fire_0_1.py
	4) Configurações iniciais ajustadas, você pode executar os três arquivos principais. Atenção para a ordem, caso queira realizar uma coleta fiel aos números sorteados. Isto é, execute o código fire_0_1.py antes do código fire_0_0.py. Não esqueça de executar o código hour_mouse.py para a movimentação do mouse na tela do jogo.
	
- Conclusões

	Para uma coleta fiel dos dados e conversão, é necessário realizar um treinamento com um banco de imagens grande, ou seja, precisamos de pelo menos 1 ou 2 dias de coleta dos números. Além disso, como estamos tentando automatizar esse processo, pode ser que o código de conversão não tenha uma acurácia fiel aos números coletados, por isso o arquivo reconhecimento foi criado e ele deve ser utilizado em projetos futuros.
	
	Ademais, qualquer atualização e ajuste deve ser comunicado previamente nos altos. Também, algumas reuniões devem ser realizadas para explicação do projeto como um todo.
	
	
