#!/bin/bash
# Script para medir atraso de um ponto A a dois pontos B e C

# Ponto A para o ponto B (ambos dentro da rede da Ufcg)
echo "----  Experimentos da maquina A com a máquina B  ----"


ping -c 100 spearman > B/experimento10B.txt

echo "--- FINAL DO EXPERIMENTO ---"






# for C in computers; do
#   ping -q -c 1 $C && ssh $C 'check something'
# done
