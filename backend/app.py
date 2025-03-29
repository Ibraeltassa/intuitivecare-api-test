from flask import Flask, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Carrega os dados ao iniciar o app
DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'Relatorio_cadop.csv')
df_operadoras = pd.read_csv(DATA_PATH, sep='\t')

@app.route('/buscar', methods=['GET'])
def buscar_operadoras():
    termo = request.args.get('q', '').lower()
    if not termo:
        return jsonify([])

    resultados = df_operadoras[df_operadoras.apply(lambda row: termo in str(row).lower(), axis=1)]
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
