
def letra_repetida(palabra):
  orden = []
  letra = {}
  for c in palabra:
    if c in letra:
      letra[c] += 1
    else:
      letra[c] = 1 
      orden.append(c)
  for c in orden:
    if letra[c] == 1:
      return c
  return None


if __name__ == "__main__":
    
    print(letra_repetida('Y E E T'))
    print(letra_repetida('califragislisticoespialidoso'))
    print(letra_repetida('esternoclediomastoideo'))