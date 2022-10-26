import { api } from '@/api';
import { useAuthStore } from '@/stores';

function authHeader() {
    // return auth header with jwt if user is logged in and request is to the api url
    const { user } = useAuthStore();
    const isLoggedIn = user.access_token;
    if (isLoggedIn) {
      return { 'Authorization': `Bearer ${user.access_token}` };
    }
    return {};
  }

async function handleResponse(response) {
    const resp = await response;

    console.log(resp);
    if(resp.statusText != "OK"){
        const error = (resp.data && resp.data.message) || resp.status;
        console.log(error);
        return Promise.reject(error);
    }
    return resp.data;
}

async function handleResponse2(response) {
    const resp = await response;

    console.log(resp);
    if(resp.statusText != "OK"){
        const error = (resp.data && resp.data.message) || resp.status;
        console.log(error);
        return Promise.reject(error);
    }
    return resp.data.all_users;
}

async function handleResponseGetAdmin(response) {
    const resp = await response;

    console.log(resp);
    if(resp.statusText != "OK"){
        const error = (resp.data && resp.data.message) || resp.status;
        console.log(error);
        return Promise.reject(error);
    }
    return resp.data;
}

async function postRequest(){
    return async (url, body) => {
        console.log(`func ${url} ${body}`);
        return await api.post(url, new URLSearchParams(body)).then(handleResponse);
    }
}

async function getRequest(){
    return async (url) => {
        const yourConfig = authHeader();
        console.log(`func ${url}`);
        console.log(yourConfig);
        return await api.get(url, {headers: yourConfig}).then(handleResponse2);
    }
}

async function getAdmin(){
    return async (url) => {
        const config = authHeader();
        console.log(config);
        return await api.get(url, {headers: config}).then(handleResponseGetAdmin)
    }
}

export const reqWrapper = {
    post: await postRequest(),
    get: await getRequest(),
    getAdmin: await getAdmin()
};