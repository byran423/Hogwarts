<template>
    <div>
        <template>
            <v-tabs :value="0" background-color="primary">
                <v-tab @click="$router.push({name:'Case'})">用例管理</v-tab>
                <v-tab @click="$router.push({name:'Task'})">任务管理</v-tab>
                <v-tab @click="$router.push({name:'Jenkins'})">Jenkins管理</v-tab>
                <v-tab @click="$router.push({name:'Report'})">报告管理</v-tab>
            </v-tabs>
        </template>


        <v-dialog v-model = "addDialog" max-width = "500px">
            <v-card>
                <v-card-title>
                    添加测试用例
                </v-card-title>
                <v-card-text>
                    <v-container>
                        <v-text-field label="用例名称" v-model="addItem.name"></v-text-field>
                        <v-select :items="selectItem" label="用例类型" v-model="addItem.type" outlined></v-select>
                        <v-textarea label="用例数据" v-model="addItem.data"></v-textarea>
                        <v-text-field label="备注" v-model="addItem.remark"></v-text-field>

                    </v-container>
                </v-card-text> 
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" class="btn" @click="addCase()">确定</v-btn>
                    <v-btn color="primary" text class="btn" @click="addDialog=false">取消</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        
        
        <v-btn color="primary" class="btn" @click="addDialog = true">添加用例</v-btn>
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
            <template v-slot:[`item.operate`] = "{ item }">
            <v-btn color="primary" text small @click="modifyCase(item)">编辑</v-btn>
            <v-btn color="error" text small @click="deleteCase(item)">删除</v-btn>
            </template>


            </v-data-table>
        </template>
    </div>
</template>

<script>
export default {
    data () {
        return {
            addDialog:false,
            selectItem:['文本','文件'],
            addItem:{
                name:'',
                type:'',
                data:'',
                remark:''
            },
            selected:[],
            headers:[
                {
                    text:'id',
                    value:'id'
                },
                {
                    text:'用例名称',
                    value:'caseName'
                },
                {
                    text:'用例数据',
                    value:'caseData'
                },
                {
                    text:'操作',
                    value:'operate'
                }
            ],
            desserts:[]
        }
    },
    created () {
        let post_data = {
            pageNum:1,
            pageSize:10
        }
        this.$api.cases.getList(post_data).then(res => {
            console.log(res)
            this.desserts = res.data.data.data
        })
    },
    methods: {
        addCase(){
            console.log(this.addItem)
            let post_data = {
                caseData:this.addItem.data,
                caseName:this.addItem.name,
                remark:this.addItem.remark
            }
            this.$api.cases.createCaseByText(post_data).then(res => {
                console.log(res)
                this.addDialog = false
            })
        }
    }
}
</script>

<style scoped>
.btn{
    margin: 10px;
}

</style>

