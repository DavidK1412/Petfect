import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";


export default {
    name: 'ClientsAdmin',
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
        verifyData() {
            if (this.clientProto.name === '' || this.clientProto.email === '' || this.clientProto.phone === '' || this.clientProto.address === '') {
                this.ready = false;
            }
            this.ready = true
            this.$swal.fire({
                icon: 'success',
                title: '¡Listo!',
                text: 'Los datos son correctos. Por favor, presiona el botón de guardar',
            });
        },
        async getDetailedClient(client) {
            const url = ENDPOINTS.clients.detail.replace('id', client.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.clientProto = response.data;
            }
        },
        async updateClient() {
            const url = ENDPOINTS.clients.edit.replace('id', this.clientProto.id);
            const response = await patchData(axiosInstance, url, this.clientProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado actualizado correctamente',
                });
            }
            this.$emit('reloadComponent');
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
        }
    },
    async mounted() {
        await this.getClients();
        this.loadTable()
    }
}