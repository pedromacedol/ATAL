# Análise e Técnicas de Algoritmos

A Disciplina tem como objetivo demonstrar técnicas de análise de algoritmos, com ênfase em paradigmas, estruturas de dados e nos algoritmos relacionados. Buscando entender a complexidade, aplicar as técnicas de construção e classificar nos conjuntos P e NP os algoritmos.
___

### **Pseudocódigo**

O pseudocódigo descreve as etapas de um código utilizando uma linguagem natural, como o português. Portanto, ao invés de comandos próprios da linguagem deve ser utilizados verbos de ação para indicar o que está acontecendo a cada etapa.

  Um exemplo de pseudocódigo utilizado para verificar a idade da pessoa:


  ```
  algoritmo “validarEntrada”
    declare anoNascimento, anoAtual, idade numerico
    declare nome literal

    escreva “Digite o ano de nascimento:”
    leia anoNascimento
    escreva “Digite o ano atual:”
    leia anoAtual
    idade <- (anoAtual - anoNascimento)
    escreva “Sua idade é:”,idade

    se idade >= 18 entao
      leia nome

    escreva nome,”sua entrada foi permitida.”
  fim_algoritmo
  ```
 
 ___

 ### **Corretude de Algoritmos**
  A corretude de um algoritmo verifica se um algoritmo está correto, utilizando os parâmetros de entrada e saída. Portanto, as entradas são estabelecidas e após a execução do código é verificado se a saída está de acordo como o valor passado e as operações realizadas nele. 

![image](https://user-images.githubusercontent.com/36522521/222968398-fa8e893e-f7b7-4079-a9a5-3768905a3148.png)


No exemplo acima, podemos afirma que o algoritmo está correto para o valor 0 na entrada, pois o x = 0 + 1 = 1 e a saída foi o valor 1. Nesse caso é possível visualizar e verificar rapidamente, porém imagina um algoritmo com dezenas de entradas e saídas, para isso que utilizamos a corretude. 
  
  
3 formas de realizar:
  - Prova por indução
  - Invariante de Laço
  - Teste de algoritmos recursivos
  
 
 
#### Prova por indução

Na prova por indução é utilizada para provar a verdade de um número infinito de proposições. Sendo possível provar os seguintes objetos discretos:
  - Inequações
  - Complexidade de algoritmos
  - Teoremas sobre grafos e árvores

  
  
 
