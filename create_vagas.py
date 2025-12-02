import pandas as pd
import numpy as np

def criar_csv_historico(file_name='vagas_historico.csv', n_samples=200):
    """Gera um dataset de histórico de vagas simulado e salva como CSV sem 'Exp_Anos'."""
    np.random.seed(42)
    
    # 1. Cria as features (APENAS as 3 solicitadas)
    df = pd.DataFrame({
        'Ingles_Avancado': np.random.randint(0, 2, n_samples),
        'Conhece_Python': np.random.randint(0, 2, n_samples),
        'Tem_Cloud': np.random.randint(0, 2, n_samples),
    })

    # 2. Cria a regra de resultado (Target) - NOVA LÓGICA SEM EXP_ANOS
    # Lógica: É APTO se (Inglês E Python) OU (Cloud E Python) OU (Inglês E Cloud)
    df['Resultado'] = np.where(
        ((df['Ingles_Avancado'] == 1) & (df['Conhece_Python'] == 1)) |
        ((df['Tem_Cloud'] == 1) & (df['Conhece_Python'] == 1)) |
        ((df['Ingles_Avancado'] == 1) & (df['Tem_Cloud'] == 1)),
        'APTO',
        'NAO_APTO'
    )
    
    # Adiciona um pouco de aleatoriedade no resultado final para simular "ruído original"
    for i in df.index:
        if np.random.rand() < 0.05: # 5% de chance de inverter o resultado
            df.loc[i, 'Resultado'] = 'APTO' if df.loc[i, 'Resultado'] == 'NAO_APTO' else 'NAO_APTO'

    # 3. Salva o arquivo CSV
    df.to_csv(file_name, index=False)
    
    print(f"✅ Arquivo '{file_name}' gerado com sucesso!")
    print(f"Total de amostras salvas: {len(df)}")
    print("Colunas no CSV: ['Ingles_Avancado', 'Conhece_Python', 'Tem_Cloud', 'Resultado']")
    print("\nRodando o CÓDIGO FINAL agora, ele usará este arquivo.")

# Executa a função para criar o arquivo
criar_csv_historico()