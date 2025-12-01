import pandas as pd
import numpy as np

def criar_csv_historico(file_name='vagas_historico.csv', n_samples=200):
    """Gera um dataset de histórico de vagas simulado e salva como CSV."""
    np.random.seed(42)
    
    # 1. Cria as features
    df = pd.DataFrame({
        'Exp_Anos': np.random.randint(0, 15, n_samples),
        'Ingles_Avancado': np.random.randint(0, 2, n_samples),
        'Conhece_Python': np.random.randint(0, 2, n_samples),
        'Tem_Cloud': np.random.randint(0, 2, n_samples),
    })

    # 2. Cria a regra de resultado (Target)
    # Lógica: É APTO se (Exp >= 5 E Python) OU (Exp >= 8 E Cloud) OU (Inglês E Python)
    df['Resultado'] = np.where(
        ((df['Exp_Anos'] >= 5) & (df['Conhece_Python'] == 1)) |
        ((df['Exp_Anos'] >= 8) & (df['Tem_Cloud'] == 1)) |
        ((df['Ingles_Avancado'] == 1) & (df['Conhece_Python'] == 1)),
        'APTO',
        'NAO_APTO'
    )
    
    # Adiciona um pouco de aleatoriedade no resultado final para simular "ruído original"
    # O seu código já injeta mais ruído (FP) depois, mas isso torna o dataset inicial mais real.
    for i in df.index:
        if np.random.rand() < 0.05: # 5% de chance de inverter o resultado
            df.loc[i, 'Resultado'] = 'APTO' if df.loc[i, 'Resultado'] == 'NAO_APTO' else 'NAO_APTO'

    # 3. Salva o arquivo CSV
    df.to_csv(file_name, index=False)
    print(f"✅ Arquivo '{file_name}' gerado com sucesso!")
    print(f"Total de amostras salvas: {len(df)}")
    print("\nRodando o CÓDIGO FINAL agora, ele usará este arquivo.")

# Executa a função para criar o arquivo
criar_csv_historico()