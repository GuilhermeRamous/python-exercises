def é_anguloreto(cateto1, cateto2, hipot):
    catetos = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    if hipot == catetos:        # Se a é aproximadamente igual sqrt(b² + c²)
        return True
    else:
        return False

print(é_anguloreto(9, 12, 15)) 
