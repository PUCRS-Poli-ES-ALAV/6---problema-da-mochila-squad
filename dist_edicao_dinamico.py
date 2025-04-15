def dist_ed_prog_dina(A: str, B: str) -> int:
    m = len(A)
    n = len(B)
    matriz = [[0] * (n + 1) for _ in range(m + 1)]
    iteracoes = 0

    # Inicialização das bordas
    for i in range(1, m + 1):
        matriz[i][0] = i  # Remoção
    for j in range(1, n + 1):
        matriz[0][j] = j  # Inserção

    # Preenchimento da matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iteracoes += 1
            custo_extra = 0 if A[i - 1] == B[j - 1] else 1
            matriz[i][j] = min(
                matriz[i - 1][j] + 1,         # Remoção
                matriz[i][j - 1] + 1,         # Inserção
                matriz[i - 1][j - 1] + custo_extra  # Substituição ou Match
            )

    print(f"Número de iterações: {iteracoes}")
    return matriz[m][n]

def main():
    s1 = "Casablanca"
    t1 = "Portentoso"

    s2 = "Maven, a Yiddish word meaning accumulator of knowledge, began as an attempt to simplify the build processes in the Jakarta Turbine project. There were several projects, each with their own Ant build files, that were all slightly different. JARs were checked into CVS. We wanted a standard way to build the projects, a clear definition of what the project consisted of, an easy way to publish project information and a way to share JARs across several projects. The result is a tool that can now be used for building and managing any Java-based project. We hope that we have created something that will make the day-to-day work of Java developers easier and generally help  with the comprehension of any Java-based project."
    t2 = "This post is not about deep learning. But it could be might as well. This is the power of kernels. They are universally applicable in any machine learning algorithm. Why you might ask? I am going to try to answer this question in this article. Go to the profile of Marin Vlastelica Pogančić Marin Vlastelica Pogančić Jun"
    print(dist_ed_prog_dina(s1, t1))  # Saída esperada: 10
    print(dist_ed_prog_dina(s2, t2))
    # Saída esperada: ??

main()