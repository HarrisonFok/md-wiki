<template>
    <div>
        <!-- {{$route.params.article}} -->
        <div class="btn btn-outline-info btn-sm mx-1" @click="editArticle(article)">Edit</div>
        {{this.$route.params.article.name}}
        {{this.$route.params.article.content}}
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
            this.$router.push({ name: "Edit", params: { article: article}})
        }
    },
    created() {
        console.log(this.$route.params)
        // this.article = this.$route.params
        // console.log(this.article)
    }
}
</script>
