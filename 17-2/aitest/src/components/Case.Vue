<template>
    <div>
        <template>
            <v-tabs :value="0" background-color="primary">
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">任务管理</v-tab>
            </v-tabs>
        </template>
        <v-dialog v-model = "addDialog" max-width = "500px">
            <v-card>
                <v-card-title>
                    添加测试用例
                </v-card-title>
                <v-card-test>
                    <v-container>
                        <v-test-field label="用例名称"></v-test-field>
                        <v-select :items="selectItems" label="用例类型" outlined></v-select>
                        <v-textarea label="用例数据"></v-textarea>
                    </v-container>
                </v-card-test> 
                <v-card-action>
                    <v-btn color="primary">确定</v-btn>
                    <v-btn color="primary" text>取消</v-btn>

                </v-card-action>
            </v-card>
        </v-dialog>
        
        <v-btn color="primary" class="btn">添加用例</v-btn>
        <v-btn color="success" class="btn">生成任务</v-btn>
        <template>
            <v-data-table
                v-model="selected"
                :headers="headers"
                :items="desserts"
                item-key="name"
                show-select
                class="elevation-1"
            >
                
            </v-data-table>
        </template>


    </div>
</template>

<script>
export default {
    data () {
        return {
            addDialog:flase,
            selectItems:["文本","文件"]
            selected:[],
            headers:[
                {
                    text:'id',
                    value:''
                },
                {
                    text:'用例名称',
                    value:''
                },
                {
                    text:'用例数据',
                    value:''
                },
                {
                    text:'操作',
                    value:''
                }
            ],
            desserts:[]
        }
    },
    methods: {
        
    }
}
</script>

<style scoped>
.btn{
    margin: 10px;
}

</style>

