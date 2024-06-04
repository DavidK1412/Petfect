<script src="@/scripts/js/views/admin_view.js"></script>
<template>
    <div class="home">
        <SidebarMenu
            class="sidebar"
            v-on:setEmployees="changeComponent('employees')"
            v-on:setClients="changeComponent('clients')"
            v-on:setUsers="changeComponent('users')"
            v-on:setServices="changeComponent('services')"
            v-on:setCombos="changeComponent('combos')"
        >
        </SidebarMenu>
        <div class="content">
          <EmployeesAdmin v-if="this.selected==='employees' " :key="compKey" v-on:reloadComponent="reloadComponent()"></EmployeesAdmin>
          <ClientsAdmin v-if="this.selected==='clients' " :key="compKey" v-on:reloadComponent="reloadComponent()"></ClientsAdmin>
          <UsersAdmin v-if="this.selected==='users' " :key="compKey" v-on:reloadComponent="reloadComponent()"></UsersAdmin>
          <ServicesAdmin v-if="this.selected==='services' " :key="compKey" v-on:reloadComponent="reloadComponent()"></ServicesAdmin>
          <CombosAdmin v-if="this.selected==='combos' " :key="compKey" v-on:reloadComponent="reloadComponent()"></CombosAdmin>
        </div>
    </div>
</template>
<style scoped>
@import "@/styles/css/views/generic_view.css";
</style>