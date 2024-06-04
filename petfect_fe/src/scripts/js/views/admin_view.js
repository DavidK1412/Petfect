import SidebarMenu from "@/components/Sidebar.vue";
import EmployeesAdmin from "@/components/EmployeesAdmin.vue";
import ClientsAdmin from "@/components/ClientsAdmin.vue";
import UsersAdmin from "@/components/UsersAdmin.vue";
import ServicesAdmin from "@/components/ServicesAdmin.vue";
import CombosAdmin from "@/components/CombosAdmin.vue";

export default {
    name: 'AdminView',
    components: {
        EmployeesAdmin,
        SidebarMenu,
        ClientsAdmin,
        UsersAdmin,
        ServicesAdmin,
        CombosAdmin
    },
    data() {
        return {
            selected: 'employees',
            compKey: 0
        }
    },
    methods: {
        changeComponent(component) {
            this.selected = component;
            console.log(this.selected)
            this.compKey += 1;
        },
        reloadComponent() {
            this.compKey += 1;
        }
    }
}