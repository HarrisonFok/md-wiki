<template>
    <div>
        {{$route.params.article}}
    </div>
</template>

<script>
export default {
    data() {
        return {
            article: {}
        }
    },
}
</script>
