import LogInPopUp from "@/components/LogInPopUp.vue";

export default {
    name: 'LandingPage',
    components: {
        LogInPopUp
    },
    data() {
        return {
            popUp: false,
            currentTestimonial: 0,
            indicators: [],
            mobileMenu: null,
            nav: null,
        }
    },
    mounted() {
        this.indicators = Array.from(this.$refs.indicators.children);
        this.mobileMenu = this.$refs.mobileMenu;
        this.nav = this.$refs.nav;
    },
    methods: {
        togglePopUp() {
            this.popUp = !this.popUp;
        },
        changeSlide(index) {
            this.indicators[this.currentTestimonial].classList.remove("active");
            this.$refs.slider.style.marginLeft = `-${index * 100}%`;
            this.indicators[index].classList.add("active");
            this.currentTestimonial = index;
        },
        toggleMenu() {
            this.nav.classList.toggle("active");
            const active = this.nav.classList.contains("active");
            this.mobileMenu.setAttribute("aria-expanded", active);
            this.mobileMenu.setAttribute("aria-label", active ? "Cerrar menu" : "Abrir menu");
        },
    }
}