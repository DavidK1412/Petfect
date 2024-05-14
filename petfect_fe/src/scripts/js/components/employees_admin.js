import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";


export default {
    name: 'EmployeesAdmin',
    components: {
        FormKit
    },
    data() {
        return {
            table: null,
            employees : [],
            specialities: [],
            employeeProto: {
                name: '',
                email: '',
                phone: '',
                specialities: [],
                url_image: null,
            },
            ready: false
        }
    },
    methods: {
        async getEmployees() {
            const response = await getData(axiosInstance, ENDPOINTS.employees.list, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.employees = response.data;
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
        },
        verifyData() {
            if (this.employeeProto.name === '' || this.employeeProto.email === '' || this.employeeProto.phone === '' || this.employeeProto.specialities.length === 0) {
                this.ready = false;
            }
            this.employeeProto.specialities = this.employeeProto.specialities.map(speciality => {
                return {
                    id: speciality
                }
            });
            this.ready = true
            this.$swal.fire({
                icon: 'success',
                title: '¡Listo!',
                text: 'Los datos son correctos. Por favor, presiona el botón de guardar',
            });
        },
        async saveEmployee() {
            if (!this.ready) {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Por favor, verifica los datos antes de guardar',
                });
                return;
            }
            const response = await postData(axiosInstance, ENDPOINTS.employees.create, this.employeeProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 201) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado creado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async getDetailedEmployee(employee) {
            const url = ENDPOINTS.employees.getDetail.replace('id', employee.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.employeeProto = response.data;
            }
        },
        async updateEmployee() {
            const url = ENDPOINTS.employees.edit.replace('id', this.employeeProto.id);
            const response = await patchData(axiosInstance, url, this.employeeProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Empleado actualizado correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async deleteEmployee(employee) {
            const url = ENDPOINTS.employees.delete.replace('id', employee.id);
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
        await this.getEmployees();
        await this.getSpecialities();
        this.loadTable()
    }
}