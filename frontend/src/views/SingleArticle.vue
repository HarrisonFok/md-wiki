<template>
    <div>
        <!-- {{$route.params.article}} -->
        <div class="btn btn-outline-info btn-sm mx-1" @click="editArticle(article)">Edit</div>
        <p>{{this.$route.params.article.name}}</p>
        <p>{{this.$route.params.article.content}}</p>
        <!-- {{$route.params.article}} -->
    </div>
</template>

<script>
export default {
    data() {
        return {
            article: {}
        }
    },
    methods: {
        editArticle(article) {
            // console.log(this.$route.params.article.name)
            console.log(this.article)
            // path: `/edit/${this.$route.params.article.name}`
            this.$router.push({ name: "Edit", params: { article: article}})
        }
    }
}
</script>
