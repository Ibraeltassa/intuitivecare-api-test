from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Caminho para o arquivo CSV
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'Relatorio_cadop.csv')

# Carrega os dados uma única vez ao iniciar o servidor
df_operadoras = pd.read_csv(DATA_PATH, sep='\t', dtype=str).fillna('')

# Converte todos os valores para minúsculo para facilitar a busca
df_operadoras = df_operadoras.applymap(lambda x: x.lower())

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('q', '').strip().lower()

    if not termo:
        return jsonify({"erro": "Parâmetro de busca 'q' é obrigatório."}), 400

    # Busca textual em todas as colunas (registro relevante = contém termo em qualquer lugar)
    resultados = df_operadoras[df_operadoras.apply(lambda row: termo in ' '.join(row.values), axis=1)]

    return jsonify(resultados.head(10).to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
