Algoritmos de Curvas e Recortes Gráficos

Este repositório reúne implementações práticas de algoritmos clássicos de Computação Gráfica, com foco na geração de curvas e recorte de primitivas geométricas, desenvolvidas em Python utilizando a biblioteca Pygame.

O objetivo principal é estudar, comparar e visualizar o funcionamento desses algoritmos, destacando suas diferenças conceituais, desempenho e resultados visuais.

📌 Algoritmos Implementados
🔹 Curvas de Bézier

Foram implementadas duas abordagens distintas para geração de curvas de Bézier:

1. Método Paramétrico (Forma Polinomial)

Baseado na formulação matemática das curvas de Bézier.

Utiliza coeficientes binomiais (polinômios de Bernstein).

A curva é obtida avaliando o parâmetro t ∈ [0, 1] em passos regulares.

📎 Características:

Implementação direta e simples.

Custo computacional proporcional ao número de pontos amostrados.

Fácil controle da suavidade via número de passos.

2. Algoritmo de De Casteljau (Divisão Recursiva)

Baseado em interpolações lineares sucessivas entre os pontos de controle.

Utiliza subdivisão recursiva até que os segmentos sejam suficientemente pequenos.

📎 Características:

Mais estável numericamente.

A densidade de pontos se adapta à curvatura.

Muito utilizado em sistemas gráficos reais.

🔹 Algoritmos de Recorte
Sutherland–Hodgman (Recorte de Polígonos)

Realiza o recorte de um polígono contra uma janela convexa.

O polígono é processado aresta por aresta da janela.

São tratados os quatro casos clássicos:

Dentro → Dentro

Fora → Dentro

Dentro → Fora

Fora → Fora

📎 Particularidades da implementação:

Teste de ponto interno feito via produto vetorial.

Cálculo de interseções inspirado no Cohen–Sutherland.

Desenho das arestas feito com o algoritmo de Bresenham.

🔹 Algoritmo de Bresenham (Linhas)

Utilizado para rasterizar linhas no plano cartesiano.

Trabalha apenas com operações inteiras.

Integrado ao algoritmo de recorte para visualização precisa.

🖥️ Tecnologias Utilizadas

Python 3

Pygame

Matemática computacional aplicada à Computação Gráfica

▶️ Como Executar

Instale o Pygame:

pip install pygame


Execute qualquer arquivo Python do repositório:

python nome_do_arquivo.py


Uma janela gráfica será aberta exibindo:

Pontos de controle

Curvas geradas

Polígonos originais e recortados

📊 Comparações Realizadas
Aspecto	Paramétrico	De Casteljau
Forma de cálculo	Avaliação direta	Subdivisão recursiva
Estabilidade numérica	Média	Alta
Controle da suavidade	Passos fixos	Tolerância
Uso prático	Didático	Profissional
🎓 Finalidade Acadêmica

Este projeto foi desenvolvido com fins educacionais, visando:

Compreender algoritmos fundamentais de CG;

Visualizar o comportamento geométrico das curvas;

Comparar abordagens matemáticas e computacionais;

Consolidar conceitos de rasterização e recorte.
