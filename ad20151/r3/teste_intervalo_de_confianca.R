require("Rmisc")
require("asbio")

prop.acertos.media <- function(populacao, n.Amostras, tamAmostra){
  
  amostras <- data.frame(upper = numeric(nAmostras), mean = numeric(nAmostras), lower = numeric(nAmostras))

  for(i in 1:nAmostras){
    amostra <- sample(populacao, tamAmostra)
    amostras[i,] <- CI(amostra)
  }
  
  pop.media <- mean(populacao)
  amostras$cont.pop.media <- (amostras$upper >= pop.media & amostras$lower <= pop.media)
  
  return(prop.table(table(amostras$cont.pop.media)))
}


prop.acertos.mediana <- function(populacao, n.Amostras, tamAmostra){
  
  amostras <- data.frame(median = numeric(nAmostras), lower = numeric(nAmostras), upper = numeric(nAmostras))
  
  for(i in 1:nAmostras){
    amostra <- sample(populacao, tamAmostra)
    amostras[i,] <- ci.median(amostra)$ci
  }
  
  pop.mediana <- median(populacao)
  amostras$cont.pop.mediana <- (amostras$upper >= pop.mediana & amostras$lower <= pop.mediana)
  
  return(prop.table(table(amostras$cont.pop.mediana)))
}

nAmostras <- 500
nObservacoes <- 25

#para populacao normal
populacao.norm <- rnorm(100)
prop.acertos.media(populacao.norm, nAmostras, nObservacoes)
prop.acertos.mediana(populacao.norm, nAmostras, nObservacoes)

#para populacao normal com outliers
outliers <- c(30,20,10)
populacao.norm.out <- c(populacao.norm, outliers)
prop.acertos.media(populacao.norm.out, nAmostras, nObservacoes)
prop.acertos.mediana(populacao.norm.out, nAmostras, nObservacoes)
