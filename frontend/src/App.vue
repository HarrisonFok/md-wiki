<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <div class="row">
          <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="article.name">
          <input type="text" class="form-control col-3 mx-2" placeholder="Content" v-model="article.content">
          <div class="btn btn-success" @click="submitForm()">Submit</div>
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
    submitForm() {
      console.log(this.article)
      if (this.article.id === undefined) {
        this.createArticle()
      } else {
        this.editArticle()
      }
    },
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
    async editArticle() {
      await this.getArticles()
      await fetch(`http://localhost:8000/articles/${this.article.id}/`, {
        method: 'put',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.article)
      })
      await this.getArticles()
      this.article = {}
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
