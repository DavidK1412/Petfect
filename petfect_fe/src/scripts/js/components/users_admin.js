import { DataTable } from "datatables.net-vue3";
import { axiosInstance, getData , ENDPOINTS } from "@/scripts/js/api";

export default {
    name: 'UsersAdmin',
    components: {
        DataTable
    },
    data() {
        return {
            users : []
        }
    },
    methods: {
        getUsers() {
            getData(
                axiosInstance,
                ENDPOINTS.users.list,
                {
                    Authorization: `Bearer ${sessionStorage.getItem('access')}`
                }
            ).then(response => {
                if (response.status === 200) {
                    this.users = response.data;
                }
            })
        },
        loadTable() {

        }
    }
}