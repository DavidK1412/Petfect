import { FormKit } from "@formkit/vue";
import { axiosInstance, postData, patchData, ENDPOINTS } from "@/scripts/js/api";

export default {
    name: 'Register',
    components: { FormKit },
    data() {
        return {
            clientSignUp: {
                name: '',
                email: '',
                password: '',
                phone: '',
                address: '',
                role: 2
            },
            validatePass: '',
            verificationCode: {
                code: ''
            }
        }
    },
    methods: {
        async createClient (handlers){
            postData(
                axiosInstance,
                ENDPOINTS.auth.register,
                this.clientSignUp,
                {}
            ).then((response) => {
                if (response.status === 201) {
                    this.$swal.fire({
                        icon: 'info',
                        title: 'Por favor, revisa tu e-mail',
                        text: 'Hemos enviado un correo de verificación a tu email',
                    });
                }
                handlers.incrementStep(1)()
            }).catch((error) => {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'No se ha podido registrar el usuario',
                });
            });
        },
        async verifyEmail(handlers) {
            const customEndpoint = ENDPOINTS.auth.activate.replace('email', this.clientSignUp.email);
            patchData(
                axiosInstance,
                customEndpoint,
                this.verificationCode,
                {}
            ).then((response) => {
                if (response.status === 200) {
                    this.$swal.fire({
                        icon: 'success',
                        title: '¡Bienvenido!',
                        text: 'Tu cuenta ha sido activada. Vuelve a iniciar sesión',
                    });
                    this.$emit('loadLandingPage');
                }
            }).catch((error) => {
                this.$swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'El código de verificación es incorrecto',
                });
            });
        }
    }
}