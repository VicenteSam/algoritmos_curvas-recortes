Algoritmos de Curvas e Recortes Gráficos
---------------------------------------------

Implementação de algoritmos clássicos de Computação Gráfica para geração de curvas e recorte geométrico, desenvolvidos em Python com Pygame, com foco didático, visualização e comparação de resultados.

📌 Objetivos do Projeto

Implementar algoritmos fundamentais de Computação Gráfica;

Visualizar o funcionamento matemático e geométrico das técnicas;

Comparar diferentes abordagens para geração de curvas;

Integrar algoritmos de rasterização e recorte;

Consolidar conceitos teóricos por meio de implementação prática.

---------------------------------------------

🧮 Algoritmos Implementados
1. Curvas de Bézier
1.1 Método Paramétrico (Polinômios de Bernstein)

A curva é gerada pela avaliação direta da equação paramétrica da curva de Bézier:

O parâmetro t varia no intervalo [0, 1];

Para cada valor de t, calcula-se um ponto da curva;

Utiliza coeficientes binomiais (comb).

Características:

Implementação simples e direta;

Suavidade controlada pelo número de passos;

Custo computacional proporcional à quantidade de amostras.

---------------------------------------------

1.2 Algoritmo de De Casteljau

Baseado em interpolações lineares sucessivas entre os pontos de controle:

O algoritmo subdivide a curva recursivamente;

A subdivisão continua até atingir uma tolerância mínima;

A curva é aproximada por segmentos de reta.

Características:

Alta estabilidade numérica;

Melhor adaptação à curvatura local;

Amplamente utilizado em sistemas gráficos reais.

---------------------------------------------

2. Algoritmos de Recorte
2.1 Sutherland–Hodgman (Recorte de Polígonos)

Algoritmo utilizado para recortar um polígono contra uma janela convexa:

O polígono é processado contra cada aresta da janela;

São analisados quatro casos clássicos:

Dentro → Dentro

Fora → Dentro

Dentro → Fora

Fora → Fora

Detalhes da implementação:

Teste de ponto interno usando produto vetorial;

Cálculo de interseções inspirado no algoritmo de Cohen–Sutherland;

Integração com o algoritmo de Bresenham para visualização.

---------------------------------------------

3. Rasterização de Linhas
3.1 Algoritmo de Bresenham

Utilizado para desenhar linhas no plano cartesiano:

Trabalha apenas com operações inteiras;

Alta eficiência computacional;

Base para visualização dos polígonos e curvas.

📊 Comparação entre Métodos de Curvas
| Critério              | Paramétrico      | De Casteljau         |
| --------------------- | ---------------- | -------------------- |
| Tipo de cálculo       | Avaliação direta | Subdivisão recursiva |
| Estabilidade numérica | Média            | Alta                 |
| Controle da suavidade | Número de passos | Tolerância           |
| Uso prático           | Educacional      | Profissional         |


🖥️ Tecnologias Utilizadas

Python 3

Pygame

Matemática computacional aplicada à Computação Gráfica

▶️ Como Executar

Instale o Pygame:

pip install pygame


Execute qualquer script do repositório:

python nome_do_arquivo.py


Uma janela gráfica será aberta exibindo:

Pontos de controle;

Curvas geradas;

Polígonos originais e recortados.
