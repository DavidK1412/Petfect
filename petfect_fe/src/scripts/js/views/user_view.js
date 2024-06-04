import SidebarMenu from "@/components/Sidebar.vue";
import PetsAdmin from "@/components/PetsAdmin.vue";
import EmployeesAdmin from "@/scripts/js/components/employees_admin";
import ClientsAdmin from "@/scripts/js/components/clients_admin";
import UsersAdmin from "@/scripts/js/components/users_admin";

export default {
    name: 'UserView',
    components: {UsersAdmin, ClientsAdmin, EmployeesAdmin, SidebarMenu, PetsAdmin },
    data() {
        return {
            selected: 'pets',
            compKey: 0
        }
    },
    methods: {
        changeComponent(component) {
            this.selected = component;
            this.compKey += 1;
        },
        reloadComponent() {
            this.compKey += 1;
        }
    }
}