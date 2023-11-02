hora, minutos, segundos = map(int, input().split(':'))

conversao_hora_seg = hora * 3600
conversao_minutos_seg = minutos * 60
conversao_segundos = segundos * 1 

soma_dos_segundos = conversao_hora_seg + conversao_minutos_seg + conversao_segundos
print(f'La se foram {soma_dos_segundos} segundos que nao voltam mais...')