import axios from './http'

const cases = {
    getList(params){
        return axios.get('/testCase/list',params)
    },
    createCaseByText(params){
        return axios.post('/testCase/text', params)
    },
    createCaseByFile(params){
        return axios('/testCase/file',{
            method:'post',
            data:params,
            headers:{'Content-type':'multipart/form-data'}
        })
    },
    editCase(params){
        return axios.put('/testCase/',params)
    },
    deleteCase(params){
        return axios.delete('/testCase/'+params.caseId, params)
    },
    creatTask(params){
        return axios.post('/task',params)
    }
}

export default cases