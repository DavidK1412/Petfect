<template>
  <aside :class="`${ is_expanded ? 'is-expanded' : ''}`">
    <div class="logo">
      <img src="@/assets/footer_logo.svg" alt="">
    </div>

    <div class="menu-toggle-wrap">
      <button class="menu-toggle" @click="ToggleMenu">
        <span class="material-icons">keyboard_double_arrow_right</span>
      </button>
    </div>
    <h3 class="text-center">Bienvenido: {{  }}</h3>
    <div class="menu">

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

</style>