export const ENDPOINTS = {
    auth: {
        login: 'auth/login/',
        activate: 'users/email/activate/',
        createWithOutEmployee: 'users/',
        register: 'clients/'
    },
    clients: {
        detail: 'clients/id/',
        list: 'clients/',
        edit: 'clients/id/',
        delete: 'clients/id/',
    },
    users: {
        list: 'users/',
        edit: 'users/id/',
    },
    employees: {
        getSpecialities: 'employees/speciality/',
        list: 'employees/',
        create: 'employees/',
        getDetail: 'employees/id/',
        edit: 'employees/id/',
        delete: 'employees/id/',
    },
    pets: {
        list: 'clients_pets/detail/id/',
        create: 'clients_pets/',
        detail: 'clients_pets/id/',
        edit: 'clients_pets/id/',
        delete: 'clients_pets/id/',
    },
    services: {
        list: 'services/',
        create: 'services/',
        detail: 'services/id/',
        edit: 'services/id/',
        delete: 'services/id/',
    },
    combos: {
        list: 'combos/',
        create: 'combos/',
        detail: 'combos/id/',
        edit: 'combos/id/',
        delete: 'combos/id/',
    },
}