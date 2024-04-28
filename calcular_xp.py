nome = 'Layus'
exp = 3745
nivel = ''

if exp <= 1000:
    nivel = 'Ferro'
elif exp <= 2000:
    nivel = 'Bronze'
elif exp <= 5000:
    nivel = 'Prata'
elif exp <= 7000:
    nivel = 'Ouro'
elif exp <= 8000:
    nivel = 'Platina'
elif exp <= 9000:
    nivel = 'Ascendente'
elif exp <= 10000:
    nivel = 'Imortal'
else:
    nivel = 'Radiante'

print(f"O Herói {nome} está no nível {nivel}")
