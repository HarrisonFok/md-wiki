<template>
  <div>
    <div v-if="this.error == null">
        <router-link :to="'/edit/' + article.name">
            <div class="btn btn-outline-info btn-sm mx-1">Edit</div>
        </router-link>
        <h1>{{ this.article.name }}</h1>
        <p>{{ this.article.content }}</p>
    </div>
    <div v-else>
        <h3>
            No article with this exact name found. Use Edit button in the header to add it.
        </h3>
    </div>
  </div>
</template>

<script>
export default {
    name: 'Article',
    data() {
        return {
            article: {},
            error: null
        }
    },
    async created() {
        let name = this.$route.params.name
        let res = await fetch(`http://localhost:8000/articles/${name}`)
        console.log(res)
        let content = await res.json()
        let checkError = {"detail": "Not Found"}
        if (!res.ok) {
            this.error = checkError
        } else {
            this.article = { name, content }
        }
    }
}
</script>

<style>

</style>