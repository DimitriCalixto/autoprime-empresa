# Criando uma estrutura de dados
num_samples = 120

# Inserindo variáveis independentes
categorias = ["Sedan", "SUV", "Hatchback", "Esportivo"]
categoria = np.random.choice(categorias, num_samples)  # Categorias dos veículos
preco_medio = {
    "Sedan": 40000,
    "SUV": 60000,
    "Hatchback": 30000,
    "Esportivo": 80000
}
preco = [preco_medio[cat] + np.random.uniform(-5000, 5000) for cat in categoria]
promocao = np.random.choice([0, 1], num_samples)


vendas = [
    600 - 0.01 * p + 120 * promo + (50 if cat in ["SUV", "Esportivo"] else 20) +
    np.random.normal(0, 25)
    for p, promo, cat in zip(preco, promocao, categoria)
]

# Estrutura os dados em um DataFrame
dados_projeto = pd.DataFrame({
    "Categoria": categoria,
    "Preco": preco,
    "Promocao": promocao,
    "Vendas": vendas
})

dados_projeto.head()  # Exibindo os primeiros dados