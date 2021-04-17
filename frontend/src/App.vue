<template>
  <div id="app">
    <form @submit.prevent="createArticle">
      <div class="form-group row">
        <div class="row">
          <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="article.name">
          <input type="text" class="form-control col-3 mx-2" placeholder="Content" v-model="article.content">
          <div class="btn btn-success" @click="createArticle()">Submit</div>
        </div>
      </div>
    </form>
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
      article: {
        'name': '',
        'content': ''
      },
      articles: []
    }
  },
  async created() {
    let res = await fetch("http://localhost:8000/articles/")
    this.articles = await res.json()
  },
  methods: {
    async createArticle() {
      let res = await fetch("http://localhost:8000/articles/", {
        method: 'post',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.article)
      })
      this.articles.push(await res.json())
    }
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
