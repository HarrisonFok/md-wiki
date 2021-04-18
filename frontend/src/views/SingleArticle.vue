<template>
    <div>
        <div class="btn btn-outline-info btn-sm mx-1" @click="editArticle($route.params.article)">Edit</div>
        <p>{{this.$route.params.article.name}}</p>
        <p>{{this.$route.params.article.content}}</p>
    </div>
</template>

<script>
export default {
    methods: {
        editArticle(article) {
            console.log(article)
            this.$router.push({ name: "Edit", params: { article: this.$route.params.article}})
        }
    }
}
</script>
