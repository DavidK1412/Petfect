import { ref } from "vue";
import { VueRecaptcha } from "vue-recaptcha";
import { axiosInstance, postData, ENDPOINTS } from "@/scripts/js/api";

const captcha = ref(false);
const error = ref(null);


export default {
    name: 'LogInPopUp',
    components: {
        VueRecaptcha,
    },
    data() {
        return {
            captchaKey: process.env.VUE_APP_RECAPTCHA_KEY,
            email: "",
            password: "",
        }
    },
    methods: {
        closePopUp(){
            this.$emit("close");
        },
        async logIn() {
            if (!this.email || !this.password || !captcha.value) {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Por favor, rellena todos los campos y el captcha',
                });
                return;
            }
            const data = {
                email: this.email,
                password: this.password
            }

            postData(
                axiosInstance,
                ENDPOINTS.auth.login,
                data,
                {},
            ).then((response) => {
                if (response.status === 200) {
                    this.$swal.fire({
                        icon: 'success',
                        title: '¡Bienvenido!',
                        text: 'Has iniciado sesión correctamente',
                    });
                    sessionStorage.setItem('access', response.data.access);
                    sessionStorage.setItem('refresh', response.data.refresh);
                    this.$emit('loadView');
                } else {
                    this.$swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: 'Usuario o contraseña incorrectos',
                    });
                }
            })
        },
    },
    setup() {
        const handleSuccess = () => {
            captcha.value = true;
            error.value = null;
        }

        const onExpired = () => {
            captcha.value = false;
        }

        const handleError = () => {
            captcha.value = false;
            error.value = "Hay un error con el captcha";
        }

        return {
            handleSuccess,
            handleError,
            onExpired,
            captcha,
            error
        }
    }
}