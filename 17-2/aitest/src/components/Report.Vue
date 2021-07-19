<template>
    <div>
        <template>
            <v-tabs :value="3" background-color="primary">
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">任务管理</v-tab>
            </v-tabs>
        </template> 
        report
    </div>
</template>

<script>
export default {
    data () {
        return {
            
        }
    },
    methods: {
        
    }
}
</script>

<style scoped>

</style>