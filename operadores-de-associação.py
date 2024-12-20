curso = "curso de python"
frutas = ["maça", "uva", "melão", "manga", "limão"]
saques = [1500, 100]

print ("python" in curso)
print ("pera" not in frutas)
print (200 in saques)
print ("melão" and "uva" in frutas)
print ("manga" and "mamão" in frutas)
print ("melão" in frutas or "uva" in frutas)
print ("manga" in frutas or "mamão" in frutas)
print (100 and 1500 in saques)
print (100 in saques or 1500 in saques)
print (200 and 100 in saques)
print (400 in saques or 1500 in saques)

#a sentença de "or" fica maior, pois ele retorna no primeiro valor verdadeiro e não avalia a expressão como um todo.