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



.dt-paging {
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  margin-top: 1rem !important;
}

.dt-paging > button {
  font-size: 1.2rem !important;
  background-color: #8f42db !important;
  color: white !important;
  border: 1px solid #8f42db !important;
  margin: 0 0.5rem !important;
  width: 3.5rem !important;
  height: 3.5rem !important;
  border-radius: 50% !important;
}

#main {
  /*Center items*/
  font-size: 1.8rem;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
}

#main h1 {
  font-size: 2.5rem;
  margin-top: 2rem;
}

#main .table-responsive {
  width: 100%;
  margin-top: 2rem;
}

.top-elements{
  display: flex;
  width: 95%;
  margin-top: 2rem;
}

.top-elements button {
  background-color: #8f42db;
  color: white;
  border: 1px solid #8f42db;
  width: 10rem;
  height: 3rem;
  margin-left: 5rem;
  font-size: 1.5rem;
}

.top-elements button:hover {
  background-color: #6f32b0;
  border: 1px solid #6f32b0;
}

</style>
