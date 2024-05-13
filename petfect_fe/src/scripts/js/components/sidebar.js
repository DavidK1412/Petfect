import { ref } from 'vue';

export default {
    name: 'SidebarMenu',
    data () {
        return {
            is_expanded: ref(localStorage.getItem("is_expanded") === "true"),
            loaded: false,
            user
        }
    }
}