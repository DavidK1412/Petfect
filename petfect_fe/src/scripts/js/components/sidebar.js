import { ref } from 'vue';
import { getClientDetail } from "@/scripts/js/utils/detailtoken";

export default {
    name: 'SidebarMenu',
    data () {
        return {
            is_expanded: ref(localStorage.getItem("is_expanded") === "true"),
            isAdmin: false,
            loaded: false,
            user: {
                name: 'cargando...',
            }
        }
    },
    methods: {
        ToggleMenu: function () {
            this.is_expanded = !this.is_expanded;
            localStorage.setItem("is_expanded", this.is_expanded);
        },
        logOut: function () {
            sessionStorage.clear("token");
            localStorage.setItem("is_expanded", true);
            this.$router.push({ name: 'LandingPage' });
        },
        getUser: async function () {
            await new Promise( resolve => setTimeout(resolve, 2000));
            this.user = await getClientDetail();
            if (this.user.role === 'ROLE_ADMIN'){
                this.isAdmin = true;
            }
            this.loaded = true;
        }
    },
    async created() {
        await this.getUser();
    }
}