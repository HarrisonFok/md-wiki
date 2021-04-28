<template>
  <div>
    <router-link :to="'/edit/' + article.name">
        <div class="btn btn-outline-info btn-sm mx-1">Edit</div>
    </router-link>
    <h1>{{ this.article.name }}</h1>
    <p>{{ this.article.content }}</p>
  </div>
</template>

<script>
export default {
    name: 'Article',
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
    }
}
</script>

<style>

</style>