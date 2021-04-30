<template>
  <v-card
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <div v-if="this.error == null">
        <v-card-actions>
            <router-link :to="'/edit/' + article.name">
                <v-btn
                    color="deep-purple lighten-2"
                    text
                >
                    Edit
                </v-btn>
            </router-link>
        </v-card-actions>

        <v-card-title><strong>Name: </strong>{{ this.article.name}}</v-card-title>
        <v-divider class="mx-4"></v-divider>
        <v-card-text><strong>Content: </strong>{{ this.article.content }}</v-card-text>
    </div>
    <div v-else>
        <h3>
            No article with this exact name found. Use Edit button in the header to add it.
        </h3>
    </div>
  </v-card>
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