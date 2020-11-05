 
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

r"""
 Counts words in UTF8 encoded, '\n' delimited text received from the network every second.
 Usage: network_wordcount.py <hostname> <port>
   <hostname> and <port> describe the TCP server that Spark Streaming would connect to receive data.
 To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
"""
from __future__ import print_function

import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Modo de uso: wordCount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)
        

#Primeiro, importamos StreamingContext, que é o principal ponto de entrada para todas as #funcionalidades de streaming. Criamos um StreamingContext local com dois threads de execução e #intervalo de lote de 1 segundo.
        
    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc, 1)


#Usando este contexto, podemos criar um DStream que representa streaming de dados de uma fonte TCP, #especificado como nome do host (por exemplo, localhost) e porta (por exemplo, 9999).

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))
    

#Essas linhas DStream representam o fluxo de dados que será recebido do servidor de dados. Cada #registro neste DStream é uma linha de texto. Em seguida, queremos dividir as linhas por espaço em #palavras.    

#flatMap é uma operação DStream de um para muitos que cria um novo DStream gerando vários novos #registros de cada registro no DStream de origem. Nesse caso, cada linha será dividida em várias #palavras e o fluxo de palavras é representado como as palavras DStream. Em seguida, queremos #contar essas palavras.

#As palavras DStream são posteriormente mapeadas (transformação um-para-um) para um DStream de #(palavra, 1) pares, que é então reduzido para obter a frequência das palavras em cada lote de #dados. Por fim, wordCounts.pprint () imprimirá algumas das contagens geradas a cada segundo.

#Observe que, quando essas linhas são executadas, o Spark Streaming apenas configura o cálculo que #executará quando for iniciado, e nenhum processamento real foi iniciado ainda. Para iniciar o #processamento após todas as transformações terem sido configuradas, finalmente chamamos
        
    counts = lines.flatMap(lambda line: line.split(" "))\
                  .map(lambda word: (word, 1))\
                  .reduceByKey(lambda a, b: a+b)
    
    #Imprimri resultado na tela              
    counts.pprint()


    ssc.start()
    ssc.awaitTermination()
