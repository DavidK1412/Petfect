<script src="@/scripts/js/components/sidebar.js"></script>

<template>
  <aside :class="`${ is_expanded ? 'is-expanded' : ''}`">
    <div class="logo">
      <img src="@/assets/footer_logo.svg" alt="">
    </div>

    <div class="menu-toggle-wrap">
      <i class="menu-toggle" @click="ToggleMenu">
        <span class="material-icons">keyboard_double_arrow_right</span>
      </i>
    </div>
    <div class="menu">
      <h3 class="text-center">Bienvenido: {{ this.user.name }}</h3>
      <div v-if="!this.isAdmin && this.loaded">
        <div class="button" @click="this.$emit('setPets')">
          <span class="material-icons">pets</span>
          <span class="text">Mis mascotas</span>
        </div>
      </div>
      <div v-if="this.isAdmin && this.loaded">
        <div class="button" @click="this.$emit('setEmployees')">
          <span class="material-icons">group</span>
          <span class="text">Gestión empleados</span>
        </div>
        <div class="button" @click="this.$emit('setClients')">
          <span class="material-icons">diversity_1</span>
          <span class="text">Gestión Clientes</span>
        </div>
        <div class="button" @click="this.$emit('setUsers')">
          <span class="material-icons">account_circle</span>
          <span class="text">Gestión Usuarios</span>
        </div>
        <div class="button" @click="this.$emit('setServices')">
          <span class="material-icons">content_cut</span>
          <span class="text">Servicios</span>
        </div>
        <div class="button" @click="this.$emit('setCombos')">
          <span class="material-icons">inventory_2</span>
          <span class="text">Combos</span>
        </div>
      </div>
    </div>
    <div class="flex"></div>

    <div class="menu">
      <div v-on:click="logOut" class="button">
        <span class="material-icons">logout</span>
        <span class="text">Cerrar sesión</span>
      </div>
    </div>
  </aside>
</template>

<style scoped>
@import "@/styles/css/components/Sidebar/sidebar.css";
</style>