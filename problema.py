fn_antigo = 1 # f1
fn_novo = 1   # f2
ln_antigo = 1 # l1
ln_novo = 3   # l2
iguais = "1" + " " # lista de termos que aparecem na duas sequencias, já coloquei o um pq adianta o processo


for i in range(1000): # Isso representa uma repetição de 1000 vezes. Tudo o que está dentro disso vai repetir 1000 vezes
    fn_novo = fn_novo + fn_antigo # aqui obtemos um novo valor
    fn_antigo = fn_novo - fn_antigo # aqui conservamos o valor anterior

    ln_novo = ln_novo + ln_antigo # aqui obtemos um novo valor
    ln_antigo = ln_novo - ln_antigo # aqui conservamos o valor anterior

    if ln_novo == fn_novo: # se ln_novo for igual a  fn_novo, será colocado este valor na lista
        iguais = iguais + str(ln_novo) + " " # aqui é adicionado o novo valor caso a condição anterior for verdadeira

print(iguais) # aqui é mostrado na tela o valores que aparecem na duas listas

   
