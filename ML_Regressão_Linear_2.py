# Convertido em categorias para valores numéricos
dados_projeto['Categoria_Num'] = dados_projeto['Categoria'].map({
    "Sedan": 1, "SUV": 2, "Hatchback": 3, "Esportivo": 4
})

# Dividido os dados em treino e teste
X = dados_projeto[['Preco', 'Promocao', 'Categoria_Num']]
y = dados_projeto['Vendas']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinado o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Previsões
y_pred = model.predict(X_test)

# Avaliação do modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Coeficientes e desempenho
resultados_finais = {
    "Coeficientes": model.coef_,
    "Intercepto": model.intercept_,
    "Erro Quadrático Médio (MSE)": mse,
    "R²": r2
}

resultados_finais