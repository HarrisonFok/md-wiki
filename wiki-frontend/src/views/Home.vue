<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <div class="row">
          <v-text-field v-model="article.name"></v-text-field>
          <v-text-field v-model="article.content"></v-text-field>
          <!-- <div class="btn btn-success" @click="createArticle()">Submit</div> -->
          <v-btn @click="createArticle()">Submit</v-btn>
        </div>
      </div>
    </form>
    <table class="table">
      <thead>
        <th>Name</th>
        <th>Content</th>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.id" @dblclick="$data.article = article">
          <td>{{ article.name }}</td>
          <td>{{ article.content }}</td>
          <router-link :to="'/' + article.name">
            <div class="btn btn-outline-info btn-sm mx-1">View</div>
          </router-link>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      article: {},
      articles: [],
    }
  },
  async created() {
    await this.getArticles()
  },
  methods: {
    async getArticles() {
      let res = await fetch("http://127.0.0.1:8000/articles/")
      this.articles = await res.json()
    },
    async createArticle() {
      await this.getArticles()
      const { name, content } = this.article
      if (!name || !content) return
      await fetch(`http://127.0.0.1:8000/articles/${this.article.name}`, {
        method: "put",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({name, content})
      })
      await this.getArticles()
      this.article = {}
    }
  }
}
</script>
