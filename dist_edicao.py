# ED(S, T, i, j): int
# // S: String inicial, T: String final, i: [1..m], j:[1..n]
# // retorna o número mínimo de edições quando comparando
# // S[i] com T[j]. m é o tamanho de S, n o tamanho de T
# //
# Caso Base:
# Quando ficamos sem caracteres para comparer em S ou em T. Se em ambas, o
# resultado é 0. Se uma das duas, retorna o restante dos caracteres da que não
# está vazia;
# Casos Recursivos
# Se S[i] == T[i], chame recursivamente ED(S, T, i-1, j-1) (foi match, não
# precisa fazer nada nesta posição, o custo é zero.
# Se não, três chamadas recursivas são necessárias:
# • Substituição: ED(S, T, i-1, j-1) + 1
# • Inserção: ED(S, T, i, j-1) + 1
# • Remoção: ED(S, T, i-1, j) + 1
# • Retorne a que resultar em menor custo

global iteracoes 
iteracoes = 0

def ED(S: str, T: str, i: int, j: int) -> int:
    global iteracoes
    iteracoes += 1
    # Caso base: se S está vazia, precisa inserir todos os j caracteres de T
    if i == 0:
        return j
    # Caso base: se T está vazia, precisa remover todos os i caracteres de S
    if j == 0:
        return i

    # Se os caracteres são iguais, não há custo, segue comparando anteriores
    if S[i - 1] == T[j - 1]:
        return ED(S, T, i - 1, j - 1)

    # Se diferentes, considera os 3 casos: substituição, inserção, remoção
    substituicao = ED(S, T, i - 1, j - 1) + 1
    insercao = ED(S, T, i, j - 1) + 1
    remocao = ED(S, T, i - 1, j) + 1

    return min(substituicao, insercao, remocao)


s1 = "Casablanca"
t1 = "Portentoso"

s2 = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to simplify the build processes in the Jakarta Turbine project. There were several projects, each with their own Ant build files, that were all slightly different. JARs were checked into CVS. We wanted a standard way to build the projects, a clear definition of what the project consisted of, an easy way to publish project information and a way to share JARs across several projects. The result is a tool that can now be used for building and managing any Java-based project. We hope that we have created something that will make the day-to-day work of Java developers easier and generally help with the comprehension of any Java-based project."

t2 = "This post is not about deep learning. But it could be might as well. This is the power of kernels. They are universally applicable in any machine learning algorithm. Why you might ask? I am going to try to answer this question in this article. Go to the profile of Marin Vlastelica Pogančić Marin Vlastelica Pogančić Jun"

print(ED(s1, t1, len(s1), len(t1)))  # Saída esperada: 10
print(iteracoes)  # Saída esperada: 10

iteracoes = 0
print(ED(s2, t2, len(s2), len(t2)))  # Saída esperada: ??
print(iteracoes)