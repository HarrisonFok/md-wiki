<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <div class="row">
          <input type="text" class="form-control col-2 mx-2" placeholder="Name" v-model="article.name">
          <input type="text" class="form-control col-2 mx-2" placeholder="Content" v-model="article.content">
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
        <tr v-for="article in articles" :key="article.id" @dblclick="$data.article = article">
          <td>{{ article.name }}</td>
          <td>{{ article.content }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteArticle(article)">x</button>
          </td>
          <td>
            <div class="btn btn-outline-info btn-sm mx-1" @click="viewArticle(article)">View</div>
          </td>
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
      article: {},
      articles: []
    }
  },
  async created() {
    await this.getArticles()
  },
  methods: {
    async getArticles() {
      let res = await fetch("http://localhost:8000/articles/")
      this.articles = await res.json()
    },
    async createArticle() {
      await this.getArticles()
      await fetch("http://localhost:8000/articles/", {
        method: 'post',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.article)
      })
      await this.getArticles()
    },
    async deleteArticle(article) {
      await this.getArticles()
      await fetch(`http://localhost:8000/articles/${article.id}/`, {
        method: 'delete',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.article)
      })
      await this.getArticles()
    },
    async viewArticle(article) {
      this.$router.push({ path: `${article.name}`, name: "Single", params: { article: article }})
    },
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
