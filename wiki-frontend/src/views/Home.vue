<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <v-row>
          <v-col cols="12" sm="6" md="4" style="margin-left: 30px">
            <v-text-field v-model="article.name" label="Name"></v-text-field>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-text-field v-model="article.content" label="Content"></v-text-field>
          </v-col>
        </v-row>
      </div>
      <v-btn @click="createArticle()">Submit</v-btn>
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
            <!-- <div class="btn btn-outline-info btn-sm mx-1">View</div> -->
            <v-btn>View</v-btn>
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

<style scoped>
    .centered-input {
      text-align: center
    }
</style>