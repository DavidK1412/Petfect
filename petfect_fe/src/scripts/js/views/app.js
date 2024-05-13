import {jwtDecode} from "jwt-decode";

export default {
    name: 'App',
    data: function() {
        return {
            isAuthenticated: false
        }
    },
    methods: {
        logOut:function()  {
            sessionStorage.clear();
            this.$router.push({
                name: 'LandingPage'
            })
        },
        loadView: function(){
            const accessToken = sessionStorage.getItem('access');
            if(accessToken){
                const decodedToken = jwtDecode(accessToken);
                const view = decodedToken.role === 'ROLE_ADMIN' ? 'AdminView' : 'UserView';
                this.isAuthenticated = true;
                this.$router.push({
                    name: this.isAuthenticated ? view : 'LandingPage'
                });
            } else {
                this.loadLandingPage();
            }
        },
        loadLandingPage: function() {
            this.isAuthenticated = false;

            this.$router.push({
                name: 'LandingPage'
            })
        },
        register: function (){
            this.$router.push({
                name: 'Register'
            })
        }
    },
    created: function() {
        const accessToken = sessionStorage.getItem('access');
        if(accessToken){
            const decodedToken = jwtDecode(accessToken);
            const view = decodedToken.role === 'ROLE_ADMIN' ? 'AdminView' : 'UserView';
            this.isAuthenticated = true;
            this.$router.push({
                name: this.isAuthenticated ? view : 'LandingPage'
            });
        } else {
            this.isAuthenticated = false;
            this.$router.push({
                name: 'LandingPage'
            });
        }
    }
}