class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave, self.chave, self.direita and self.direita.chave)

# Algorítmo de Inserção (sua complexidade é logarítmica no tamanho da árvore)
# Funcionam com base nessa mesma ideia de eliminar metade da árvore a cada etapa do procedimento
def insere(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa"""
    # Nodo deve ser inserido na raiz.
    if raiz is None:
        raiz = nodo
    
    # Nodo deve ser inserido na subárvore direita
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)
    
    # Nodo deve ser inserido na subárvore esquerda
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

# Algorítmo de Busca (sua complexidade é logarítmica no tamanho da árvore) (O(log n))
# Funcionam com base nessa mesma ideia de eliminar metade da árvore a cada etapa do procedimento
def busca(raiz, chave):
    """Procura por uma chave em uma árvore binária de pesquisa."""
    # Trata o caso em que a chave procurada não está presente.
    if raiz is None:
        return None
    # A chave procurada está na raiz da árvore.
    if raiz.chave == chave:
        return raiz
    
    # A chave procurada é maior que a da raiz.
    if raiz.chave < chave:
        return busca(raiz.direita, chave)
    
    # A chave procurada é menor que a da raiz.
    if raiz.chave > chave:
        return busca(raiz.esquerda, chave)

# Caminhamentos EM ORDEM, PRÉ ORDEM e PÓS ORDEM (sua complexidade assintótica é linear no número de nodos da árvore) O(n)
def em_ordem(raiz):
    if not raiz:
        return
    em_ordem(raiz.esquerda)

    print(raiz)

    em_ordem(raiz.direita)

def em_ordem_iterativo(raiz):
    node = raiz
    stack = []
    while (stack or node is not None):
        if node is not None:
            stack.append(node)
            node = node.esquerda
        else:
            node = stack.pop()
            print(node.chave)
            node = node.direita

def pre_ordem(raiz):
    if not raiz:
        return
    print(raiz.chave)

    pre_ordem(raiz.esquerda)

    pre_ordem(raiz.direita)

def pos_ordem(raiz):
    if not raiz:
        return
    pos_ordem(raiz.esquerda)

    pos_ordem(raiz.direita)

    print(raiz.chave)

"""
raiz = NodoArvore(40)

raiz.esquerda = NodoArvore(20)
raiz.direita = NodoArvore(60)

raiz.direita.esquerda = NodoArvore(50)
raiz.direita.direita = NodoArvore(70)
raiz.esquerda.esquerda = NodoArvore(10)
raiz.esquerda.direita = NodoArvore(30)

print('<---EM ORDEM--->')
em_ordem(raiz)
print('<---PRE ORDEM--->')
pre_ordem(raiz)
print('<---POS ORDEM--->')
pos_ordem(raiz)
"""

""" EXERCÍCIOS """
""" Encontre o menor elemento em uma BST. """
def minimo(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave

""" Encontre o maior elemento em uma BST."""
def maximo(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave

""" Verifique se duas árvores binárias são idênticas. """
def identicas(a, b):
    # 1. As duas árvores são vazias.
    if a is None and b is None:
        return True
    
    # 2. Nenhuma das árvores é vazia. Precisamos compará-las.
    if a is not None and b is not None:
        return ((a.chave == b.chave) and identicas(a.esquerda, b.esquerda) and identicas(a.direita, b.direita))
    
    # 3. Uma árvore é vazia mas a outra não.
    return False

""" Calcule a altura de uma BST.  """
def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1

"""   Verifique se uma árvore binária é balanceada. """
def balanceada(raiz):
    # Uma árvore binária vazia é balanceada.
    if raiz is None:
        return True
    
    altura_esquerda = altura(raiz.esquerda)
    altura_direita = altura(raiz.direita)
    # Alturas diferem em mais de uma unidade, a árvore está desbalanceada.
    if abs(altura_esquerda - altura_direita) > 1:
        return False
    return balanceada(raiz.esquerda) and balanceada(raiz.direita)

"""  Determine se uma árvore é simétrica. """
def checa_simetria(raiz):
    def simetricas(subarvore_esq, subarvore_dir):
        if not subarvore_esq and not subarvore_dir:
            return True
        elif subarvore_esq and subarvore_dir:
            return (subarvore_esq.chave == subarvore_dir.chave and simetricas(subarvore_esq.esquerda, subarvore_dir.direita) and simetricas(subarvore_esq.direita, subarvore_dir.esquerda))
            # Uma sub-árvore é vazia e a outra não
        return False
    return not raiz or simetricas(raiz.esquerda, raiz.direita)
        


# Cria uma árvore binária de pesquisa. BST (Bynarie Search Tree)
raiz = NodoArvore(40)
raiz_b = NodoArvore(40)
for chave in [20,60,50,70,10,30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)
for chave in [20,100,50,70,10,30, 110, 140, 130, 25, 65, 35, 46, 56, 73, 82, 22,15,19,18,13]:
    nodo = NodoArvore(chave)
    insere(raiz_b, nodo)

for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))

nodo = minimo(raiz)
print("Valor Mínimo: "+str(nodo))

nodo = maximo(raiz)
print("Valor Máximo: "+str(nodo))

print(identicas(raiz, raiz_b))

print(altura(raiz_b))

print(balanceada(raiz_b))
print(em_ordem(raiz_b))

print(checa_simetria(raiz))


"""Se um procedimento descarta metade da árvore a cada iteração ou chamada mas a árvore não é balanceada, 
sua complexidade é linear no tamanho da árvore. Como exemplo desse tipo de procedimento citamos a inserção 
e a busca em árvores binárias de pesquisa, quando executados em árvores não balanceadas."""