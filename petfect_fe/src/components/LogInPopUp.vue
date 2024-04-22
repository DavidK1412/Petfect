<script src="../scripts/js/components/logInModal.js">
</script>

<template>
  <div class="pop-up">
    <div class="pop-up-inner">
      <div class="pop-up-close" @click="closePopUp()">
        &times;
      </div>
      <div class="legends">
        <h1 class="">¡Bienvenido de nuevo!</h1>
        <p> Por favor, rellena los datos para iniciar sesión <a>¿Aún no tienes cuenta?</a></p>
      </div>
      <label for="email">Correo</label>
      <input type="email" name="email"  placeholder="Correo">
      <label for="password">Contraseña</label>
      <input type="password" name="password"  placeholder="Contraseña">
      <span class="error" v-if="error !== null"> {{ this.error }}</span>
      <button class="btn-primary">Iniciar sesión</button>
      <a class="special-link">¿Olvidaste tu contraseña?</a>
      <div id="recaptchaInput">
        <VueRecaptcha
            :sitekey=this.captchaKey
            :load-recaptcha-script='true'
            @verify='handleSuccess'
            @error='handleError'
            @expired='onExpired'
        ></VueRecaptcha>
      </div>
    </div>
  </div>
</template>

<style src="@/styles/css/components/PopUp/styles.css" scoped>
</style>