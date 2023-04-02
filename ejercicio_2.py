horas = 4.833 * 40
pago_seguridad = 0.085
salario = (horas*4) - pago_seguridad
valor_seguridad = pago_seguridad % salario

print(int(salario), valor_seguridad)