import { es } from '@formkit/i18n';
import { createMultiStepPlugin } from "@formkit/addons";
import { genesisIcons } from '@formkit/icons';
import '@formkit/themes'
import '@formkit/addons/css/multistep';

const config = {
    locales: {
        es
    },
    locale: 'es',
    plugins: [
        createMultiStepPlugin()
    ],
    theme: 'genesis',
    icons: {
        ...genesisIcons
    }
}

export default config;