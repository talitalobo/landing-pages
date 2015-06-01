# Tutorial GGplot2
================================================================



**GGplot2** � um pacote de visualiza��o de dados que pode ser utilizado junto � ferramenta R, neste tutorial mostraremos um pouco sobre a instala��o e exemplos utilizando esta biblioteca.

Esta biblioteca � um conjunto de componentes independentes que podem ser utilizados de diferentes maneiras, construindo gr�ficos de maneira incremental. 

"A general scheme for data visualization which breaks up graphs into semantic components such as scales and layers. Ggplot2 can serve as a replacement for the base graphics in R and contains a number of defaults for web and print display of common scales".


## Instala��o e Carregamento do pacote

A instala��o e utiliza��o da biblioteca no RStudio � feita da seguinte maneira, respectivamente (retire a #):


```r
#install.packages("ggplot2")

#library(ggplot2)
```


## Exemplo 1 - Criando o primeiro plot

Utilizaremos uma base de dados padr�o do R, iris - para mais informa��es: help(iris).


```r
# Carrega a base de dados em mt
iris <- iris

# Breve sum�rio sobre os dados
summary(iris)
```

```
##   Sepal.Length    Sepal.Width     Petal.Length    Petal.Width          Species  
##  Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100   setosa    :50  
##  1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300   versicolor:50  
##  Median :5.800   Median :3.000   Median :4.350   Median :1.300   virginica :50  
##  Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199                  
##  3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800                  
##  Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500
```


Diferente de outras bibliotecas GGplot2 n�o � verborr�gico e a gera��o dos gr�ficos utiliza o conceito de camadas. Podemos guardar gr�ficos em vari�veis, adicionar outras camadas e, finalmente, plotar o gr�fico. Ent�o, simplesmente temos:


```r
# ggplot(data=iris ...) - Inicia o objeto ggplot e define a base de dados a ser usada naquele plot
# ggplot(data=iris, aes(x=Sepal.Length, y=Petal.Length, shape = Species)) - aes (Aesthetics) descreve como as vari�veis dos dados s�o mapeadas para elementos visuais. 
# Neste caso o eixo x representar� o Tamanho da S�pala (Sepal.Length), o eixo y o Tamanho da P�tala (Petal.Length) e a forma do ponto (shape) depender� da Esp�cie (Specie) da flor.

a <- ggplot(data=iris, aes(x=Sepal.Length, y=Petal.Length, shape = Species)) 

# geom_point(...) espeficica o tipo de gr�fico que estamos construindo, neste caso um gr�fico de pontos ou gr�fico de dispers�o - scatterplot. Utilizando o operador '+' pode-se contruir o gr�fico incrementalmente adicionando camadas ao objeto ggplot criado acima. 

a <- a + geom_point(size=4)

# Plot do gr�fico
a
```

![plot of chunk unnamed-chunk-3](figure/unnamed-chunk-3-1.png) 

Como incremento do gr�fico podemos tamb�m definir labels para os eixos, cores, titulo, dentre outras propriedades. 


```r
# ggplot(data=iris, aes(x=Sepal.Length, y=Petal.Length, shape = Species)) + geom_point(size=4, aes(colour=Species)) + xlab("Tamanho da S�pala") + ylab("Tamanho da P�tala") + ggtitle("�ris")

# ou 

ggplot(data=iris, aes(x=Sepal.Length, y=Petal.Length, shape = Species, col = Species)) + geom_point(size=4, aes(colour=Species)) + xlab("Tamanho da S�pala") + ylab("Tamanho da P�tala") + ggtitle("�ris")
```

![plot of chunk unnamed-chunk-4](figure/unnamed-chunk-4-1.png) 


xlab ylab ggtitle
bar chart
line chart  
stacked bar chart
histogram


Referencias:
* http://ggplot2.org/
* http://docs.ggplot2.org/current/ggplot.html
* http://docs.ggplot2.org/current/index.html
* http://en.wikipedia.org/wiki/Ggplot2
* Manual completo - http://cran.r-project.org/web/packages/ggplot2/ggplot2.pdf
* http://docs.ggplot2.org/0.9.3/aes.html
* **http://stackoverflow.com/questions/11657380/is-there-a-table-or-catalog-of-aesthetics-for-ggplot2**
* http://www.ling.upenn.edu/~joseff/avml2012/#Section_1.1
* http://blog.echen.me/2012/01/17/quick-introduction-to-ggplot2/
* 
