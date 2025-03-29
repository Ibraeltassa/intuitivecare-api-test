<template>
  <div class="container">
    <h1>Buscar Operadoras</h1>
    <input v-model="termoBusca" @keyup.enter="buscar" placeholder="Digite um termo de busca..." />
    <button @click="buscar">Buscar</button>

    <div v-if="resultados.length">
      <h2>Resultados:</h2>
      <ul>
        <li v-for="(operadora, index) in resultados" :key="index">
          <strong>{{ operadora['Razao Social'] || operadora['razao_social'] }}</strong><br />
          CNPJ: {{ operadora['CNPJ'] || operadora['cnpj'] }}<br />
          Registro ANS: {{ operadora['Registro ANS'] || operadora['registro_ans'] }}
        </li>
      </ul>
    </div>

    <div v-else-if="buscou">
      <p>Nenhum resultado encontrado.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termoBusca: '',
      resultados: [],
      buscou: false
    };
  },
  methods: {
    async buscar() {
      if (!this.termoBusca.trim()) return;

      try {
        const response = await fetch(`http://localhost:5000/buscar?q=${this.termoBusca}`);
        const data = await response.json();
        this.resultados = data;
        this.buscou = true;
      } catch (error) {
        console.error('Erro ao buscar:', error);
      }
    }
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 40px auto;
  font-family: Arial, sans-serif;
}
input {
  padding: 10px;
  width: 80%;
  margin-right: 10px;
}
button {
  padding: 10px 20px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin-bottom: 20px;
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
}
</style>
