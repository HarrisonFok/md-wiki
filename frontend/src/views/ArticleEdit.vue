<template>
    <div>
        <h1>{{$route.params.article.name}}</h1>
        {{$route.params.article.content}}
        <div class="form-group row">
            <div class="row">
            <input type="text" class="form-control col-2 mx-2" placeholder="Name" v-model="article.name">
            <input type="text" class="form-control col-2 mx-2" placeholder="Content" v-model="article.content">
            <div class="btn btn-success" @click="submitForm()">Submit</div>
            </div>
        </div>
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
        submitForm() {
            console.log(this.article)
            this.editArticle(this.$route.params.article)
        },
        async editArticle() {
            console.log(this.$route.params.article.id)
            await fetch(`http://localhost:8000/articles/${this.$route.params.article.id}/`, {
                method: 'put',
                headers: {
                "Content-Type": "application/json"
                },
                body: JSON.stringify(this.article)
            })
            this.article = {}
        },
    }
}
</script>
