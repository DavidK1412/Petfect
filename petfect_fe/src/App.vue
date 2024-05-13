<template>
  <router-view
      v-on:loadLandingPage="loadLandingPage"
      v-on:loadView="loadView"
      v-on:logOut="logOut"
      v-on:register="register"
  />
</template>

<script src="@/scripts/js/views/app.js"></script>

<style>
</style>
