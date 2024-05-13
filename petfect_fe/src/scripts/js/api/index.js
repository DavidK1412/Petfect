import axios from 'axios';
const baseApiURL = process.env.VUE_APP_API_URL;

export const axiosInstance = axios.create({
   baseURL: baseApiURL,
   timeout: 10000,
});

export { ENDPOINTS } from './endpoints';
export { postData, getData, putData, deleteData, patchData } from './methods';