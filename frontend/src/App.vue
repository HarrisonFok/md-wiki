<template>
  <div id="app">
    <table class="table">
      <thead>
        <th>Name</th>
        <th>Content</th>
      </thead>
      <tbody>
        <!-- @dblclick="$data.student = student" -->
        <tr v-for="article in articles" :key="article.id">
          <td>{{ article.name }}</td>
          <td>{{ article.content }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      articles: []
    }
  },
  async created() {
    let res = await fetch("http://localhost:8000/articles/")
    this.articles = await res.json()
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
