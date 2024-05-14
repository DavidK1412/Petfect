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
    },
    employees: {
        getSpecialities: 'employees/speciality/',
        list: 'employees/',
        create: 'employees/',
        getDetail: 'employees/id/',
        edit: 'employees/id/',
        delete: 'employees/id/',
    }
}