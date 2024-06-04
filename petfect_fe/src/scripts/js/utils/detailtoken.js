import { axiosInstance, getData , ENDPOINTS } from "@/scripts/js/api";
import { jwtDecode } from "jwt-decode";

export const getClientDetail = async () => {
    const token = sessionStorage.getItem('access');
    if (!token) {
        return null;
    }
    const decoded = jwtDecode(token);
    const userId = decoded.client_id;
    const endpoint = ENDPOINTS.clients.detail.replace('id', userId);
    const response = await getData(
        axiosInstance,
        endpoint,
        {
            Authorization: `Bearer ${token}`
        }
    )
    if (response.status === 200) {
        response.data.role = decoded.role;
        return response.data;
    }
}

export const getClientId = async () => {
    const token = sessionStorage.getItem('access');
    if (!token) {
        return null;
    }
    const decoded = jwtDecode(token);
    return decoded.client_id;
}