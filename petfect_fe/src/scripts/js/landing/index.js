export default {
    name: 'LandingPage',
    data() {
        return {
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