export const postData = async (axiosInstance, endpoint, data, headers) => {
    try {
        console.log(axiosInstance)
        return await axiosInstance.post(endpoint, data, { headers });
    } catch (error) {
        return error.response;
    }
}

export const getData = async (axiosInstance, endpoint, headers) => {
    try {
        return await axiosInstance.get(endpoint, { headers });
    } catch (error) {
        return error.response;
    }
}

export const putData = async (axiosInstance, endpoint, data, headers) => {
    try {
        return await axiosInstance.put(endpoint, data, { headers });
    } catch (error) {
        return error.response;
    }
}

export const deleteData = async (axiosInstance, endpoint, headers) => {
    try {
        return await axiosInstance.delete(endpoint, { headers });
    } catch (error) {
        return error.response;
    }
}

export const patchData = async (axiosInstance, endpoint, data, headers) => {
    try {
        return await axiosInstance.patch(endpoint, data, { headers });
    } catch (error) {
        return error.response;
    }
}