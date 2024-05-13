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
        <div class="button">
          <span class="material-icons">pets</span>
          <span class="text">Mis mascotas</span>
        </div>
      </div>
      <div v-if="this.isAdmin && this.loaded">
        <div class="button">
          <span class="material-icons">group</span>
          <span class="text">Gestión empleados</span>
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