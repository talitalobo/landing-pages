#!/bin/bash
# Script para medir atraso de um ponto A a dois pontos B e C

ping -c 100 www.google.com > experimento01C.txt


# Ponto A para o ponto C (ponto A dentro da rede da Ufcg e ponto C fora)
echo "----  Experimentos da maquina A com a máquina C  ----"

ping -c 100 www.google.com > C/experimento10C.txt


echo "--- FINAL DO EXPERIMENTO ---"

