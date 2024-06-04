import {axiosInstance, getData, postData, ENDPOINTS, patchData} from "@/scripts/js/api";
import DataTable from 'datatables.net-dt';
import { FormKit } from "@formkit/vue";
import { getClientId } from "@/scripts/js/utils/detailtoken";

export default {
    name: 'PetsAdmin',
    components: {
        FormKit
    },
    data() {
        return {
            table: null,
            pets : [],
            petDetail: {
                sizes: {
                    "Grande": 1,
                    "Pequeño": 2,
                    "Mediano": 3
                },
                types: {
                    "Perro": 1,
                    "Gato": 2,
                    "Otros": 3
                }
            },
            petProto: {
                name: '',
                size: null,
                type: null,
                url_image: null,
            },
            ready: false
        }
    },
    methods: {
        async getPets() {
            const clientId = await getClientId();
            const url = ENDPOINTS.pets.list.replace('id', clientId);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 200) {
                this.pets = response.data;
                console.log(this.pets);
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
        async savePet() {
            const response = await postData(axiosInstance, ENDPOINTS.pets.create, this.petProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`})
            if (response.status === 201) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Masdcota creada correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async getDetailedPet(pet) {
            const url = ENDPOINTS.pets.detail.replace('id', pet.id);
            const response = await getData(axiosInstance, url, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.petProto = response.data;
            }
        },
        async updatePet() {
            const url = ENDPOINTS.pets.edit.replace('id', this.petProto.id);
            console.log(this.petProto);
            const response = await patchData(axiosInstance, url, this.petProto, {Authorization: `Bearer ${sessionStorage.getItem('access')}`});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Mascota actualizada correctamente',
                });
            }
            this.$emit('reloadComponent');
        },
        async deletePet(pet) {
            const url = ENDPOINTS.pets.delete.replace('id', pet.id);
            const response = await axiosInstance.delete(url, {headers: {Authorization: `Bearer ${sessionStorage.getItem('access')}`}});
            if (response.status === 200) {
                this.$swal.fire({
                    icon: 'success',
                    title: '¡Listo!',
                    text: 'Mascota eliminado correctamente',
                });
            }
            this.$emit('reloadComponent');
        }
    },
    async mounted() {
        await this.getPets();
        this.loadTable()
    }
}