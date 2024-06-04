import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";

export default {
    name: 'ServicesAdmin',
    components: {
        FormKit
    },
    data() {
        return {
            table: null,
            services : [],
            specialities: [],
            serviceProto: {
                name: '',
                description: '',
                price: 0,
                required_speciality: null,
            },
            ready: false
        }
    },
    methods: {
        async getServices() {
            const response = await getData(axiosInstance, ENDPOINTS.services.list, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            console.log(response)
            if (response.status === 200) {
                this.services = response.data;
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
        async getSpecialities() {
            const response = await getData(axiosInstance, ENDPOINTS.employees.getSpecialities, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.specialities = response.data.map(speciality => {
                    return { value: speciality.id, label: speciality.name }
                });
            }
            console.log(this.specialities)
        },
        async saveService() {
            const response = await postData(axiosInstance, ENDPOINTS.services.create, this.serviceProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status !== 201) {
                this.$swal.fire({
                    icon: 'error',
                    title: '¡Error!',
                    text: 'Hubo un error al crear el servicio',
                });
                return;
            }
            this.$swal.fire({
                icon: 'success',
                title: '¡Listo!',
                text: 'Empleado creado correctamente',
            });
            this.$emit('reloadComponent');
        },
        async getDetailedService(service) {
            const url = ENDPOINTS.services.detail.replace('id', service.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.serviceProto = response.data;
            }
        },
        async updateService() {
            const url = ENDPOINTS.services.edit.replace('id', this.serviceProto.id);
            const response = await patchData(axiosInstance, url, this.serviceProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado actualizado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async deleteService(service) {
            const url = ENDPOINTS.services.delete.replace('id', service.id);
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
        await this.getServices();
        await this.getSpecialities();
        this.loadTable()
    }
}