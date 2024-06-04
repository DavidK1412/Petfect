<template>
  <div class="home">
    <SidebarMenu
        class="sidebar"
        v-on:setPets="changeComponent('pets')"
    >
    </SidebarMenu>
    <div class="content">
      <PetsAdmin v-if="this.selected==='pets' " :key="compKey" v-on:reloadComponent="reloadComponent()"></PetsAdmin>
    </div>
  </div>
</template>

<script src="@/scripts/js/views/user_view.js"></script>

<style scoped>
@import "@/styles/css/views/generic_view.css";
</style>