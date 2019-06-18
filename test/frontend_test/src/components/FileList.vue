<template>
    <div>
        <ul v-for="(file, i) in files" :key="i" class="list-unstyled">
            <li @click="download(file.filename)">
                {{file.filenames}}
            </li>
        </ul>
    </div>
</template>


<script>
export default {
    name :"FileList",
    props :["files"],
    methods: {
        download(filename){
            this.$emit("down-file", filename)
        },
        delFile(file){
            this.$emit("del-file", filename)
        }
    },
}
</script>