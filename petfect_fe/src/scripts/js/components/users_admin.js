import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";


export default {
    name: 'UsersAdmin',
    components: {
        FormKit
    },
    data() {
        return {
            clients : [],
            clientProto: {
                name: '',
                email: '',
                phone: '',
                address: ''
            },
            ready: false
        }
    },
    methods: {
        async getClients() {
            const response = await getData(axiosInstance, ENDPOINTS.clients.list, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.clients = response.data;
            }
        },
        loadTable() {
            this.$nextTick(() => {
                // destroy actual table object if exists
                if (this.table) {
                    this.table.destroy();
                }
                if (document.querySelector("#dtab")) {
                    this.table = new DataTable("#dtab");
                }
            })
        },
        async getDetailedClient(client) {
            const url = ENDPOINTS.clients.detail.replace('id', client.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.clientProto = response.data;
            }
        },
        async deleteClient(client) {
            const url = ENDPOINTS.clients.delete.replace('id', client.id);
            const response = await axiosInstance.delete(url, {headers: {Authorization: `Bearer ${sessionStorage.getItem('access')}`}});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado eliminado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async changeUserRole(role_id, client) {
            const url = ENDPOINTS.users.edit.replace('id', client?.user?.email);
            const response = await axiosInstance.patch(url, {role: role_id}, {headers: {Authorization: `Bearer ${sessionStorage.getItem('access')}`}})
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Rol de empleado actualizado correctamente',
                });
            }
            this.$emit('reloadComponent');
        }
    },
    async mounted() {
        await this.getClients();
        this.loadTable()
    }
}