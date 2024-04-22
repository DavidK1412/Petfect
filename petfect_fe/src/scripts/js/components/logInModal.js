import { ref } from "vue";
import {VueRecaptcha} from "vue-recaptcha";

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