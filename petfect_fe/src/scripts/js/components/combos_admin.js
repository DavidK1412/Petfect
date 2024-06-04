import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";


export default {
    name: 'CombosAdmin',
    components: {
        FormKit
    },
    data() {
        return {
            table: null,
            combos : [],
            services: [],
            comboProto: {
                name: '',
                description: '',
                price: 0,
                services: [],
            },
            ready: false
        }
    },
    methods: {
        async getCombos() {
            const response = await getData(axiosInstance, ENDPOINTS.combos.list, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.combos = response.data;
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
        async getServices() {
            const response = await getData(axiosInstance, ENDPOINTS.services.list, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.services = response.data.map(service => {
                    return { value: service.id, label: service.name }
                });
            }
        },
        verifyData() {
            console.log(this.comboProto)
            if (this.comboProto.name === '' || this.comboProto.description === '' || this.comboProto.price === 0 || this.comboProto.services.length === 0) {
                this.ready = false;
            }
            this.comboProto.services = this.comboProto.services.map(service => {
                return {
                    id: service
                }
            });
            console.log(this.comboProto)
            this.ready = true
            this.$swal.fire({
                icon: 'success',
                title: '¡Listo!',
                text: 'Los datos son correctos. Por favor, presiona el botón de guardar',
            });
        },
        async saveCombo() {
            if (!this.ready) {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Por favor, verifica los datos antes de guardar',
                });
                return;
            }
            const response = await postData(axiosInstance, ENDPOINTS.combos.create, this.comboProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 201) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado creado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async getDetailedCombo(combo) {
            const url = ENDPOINTS.combos.detail.replace('id', combo.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.comboProto = response.data;
            }
        },
        async updateCombo() {
            const url = ENDPOINTS.combos.edit.replace('id', this.comboProto.id);
            const response = await patchData(axiosInstance, url, this.comboProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado actualizado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async deleteCombo(combo) {
            const url = ENDPOINTS.combos.delete.replace('id', combo.id);
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
        download(){
            window.print();
        }
    },
    async mounted() {
        await this.getCombos();
        await this.getServices();
        this.loadTable()
    }
}