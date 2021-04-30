<template>
  <div>
    <h1 style="margin-left: 20px">{{article.name}}</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <div class="row">
          <!-- <input type="text" class="form-control col-2 mx-2" placeholder="Content" v-model="article.content"> -->
          <v-col cols="12" sm="6" md="4" style="margin-left: 30px">
            <v-text-field v-model="article.content"></v-text-field>
          </v-col>
          <v-btn @click="editArticle()">Save</v-btn>
          <v-btn @click="cancelEdit()">Cancel</v-btn>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
    name: 'Edit',
    data() {
        return {
            article: {}
        }
    },
    async created() {
        let name = this.$route.params.name
        let res = await fetch(`http://localhost:8000/articles/${name}`)
        let content = await res.json()
        this.article = { name, content}
        console.log(this.article)
    },
    methods: {
        goHome() {
            this.$router.push("/")
        },
        async editArticle() {
            const { name, content } = this.article
            if (!name || !content) return
            await fetch(`http://127.0.0.1:8000/articles/${this.article.name}`, {
                method: "put",
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify({name, content})
            })
            this.goHome()
        },
        async cancelEdit() {
            this.goHome()
        }
    }

}
</script>

<style>

</style>