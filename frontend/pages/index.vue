<template>
  <div class="container">
    <h1>Reverse String</h1>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="input-string">Input String:</label>
        <input id="input-string" type="text" v-model="inputString" />
      </div>
      <div class="form-group">
        <button class="btn btn-primary" type="submit">Reverse</button>
      </div>
    </form>
    <div v-if="outputString" class="output">
      <h2>Output:</h2>
      <p>{{ outputString }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputString: "",
      outputString: "",
    };
  },
  methods: {
    async handleSubmit() {
      const response = await fetch("http://127.0.0.1:8000/reverse", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          input_string: this.inputString,
        }),
      });
      const data = await response.json();
      console.log(data);
      this.outputString = data;
    },
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 1rem;
}
.form-group {
  margin-bottom: 1rem;
}
.btn {
  padding: 0.5rem 1rem;
  border-radius: 4px;
  border: none;
  background-color: #007bff;
  color: #fff;
}
.btn:hover {
  background-color: #0069d9;
}
.output {
  margin-top: 2rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
</style>
