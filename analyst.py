Envios_sem_botao = int(input("Envios sem botão: "))
Envios_com_botao = int(input("Envios com botão: "))
Envios_confirmados = int(input("Envios confirmados: "))

Total = Envios_com_botao + Envios_sem_botao

Resultado = (100 * Envios_confirmados) / Total

print(f"{Resultado}% dos envios obtiveram a confirmação de {Total} envios.")
