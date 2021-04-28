<template>
  <div>
    <h1>{{article.name}}</h1>
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <div class="row">
          <input type="text" class="form-control col-2 mx-2" placeholder="Content" v-model="article.content">
          <div class="btn btn-success" @click="editArticle()">Save</div>
          <div class="btn btn-danger" @click="cancelEdit()">Cancel</div>
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