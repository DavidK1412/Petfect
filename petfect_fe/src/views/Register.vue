<script src="@/scripts/js/views/register.js"></script>

<template>
  <div class="background">
      <div class="register">
          <div class="register-inner">
              <div class="register-close" @click="this.$emit('loadLandingPage')">
                  &times;
              </div>
            <div class="legends">
              <h1 class="">¡Hola!, sé parte de nuestra familia</h1>
              <p> Por favor, rellena los datos para registrarte <a @click="this.$emit('loadLandingPage')">¿Ya tienes cuenta?</a></p>
            </div>
            <div class="register-form">
              <FormKit type="multi-step" :allow-incomplete="false">
                <FormKit type="step" name="datosPeronales">
                  <FormKit
                      prefix-icon="avatarMan"
                      type="text" label="Nombre"
                      validation="required"
                      v-model="this.clientSignUp.name"
                  />
                  <FormKit
                      prefix-icon="telephone"
                      type="text"
                      label="Telefono"
                      validation="required"
                      v-model="this.clientSignUp.phone"
                  />
                  <FormKit
                      prefix-icon="button"
                      type="text" label="Dirección"
                      validation="required"
                      v-model="this.clientSignUp.address"
                  />
                  <template #stepNext="{ handlers, node }">
                    <FormKit
                        type="button"
                        @click="handlers.incrementStep(1)()"
                        label="Siguiente"
                        data-next="true"
                    />
                  </template>
                </FormKit>
                <FormKit type="step" name="datosCuenta">
                  <FormKit type="email"
                           label="Correo"
                           prefix-icon="email"
                           validation="required|email"
                           v-model="this.clientSignUp.email"
                  />
                  <FormKit
                      prefix-icon="password"
                      type="password"
                      label="Contraseña"
                      validation="required"
                      v-model="this.clientSignUp.password"
                  />
                  <FormKit
                      prefix-icon="password"
                      type="password"
                      label="Confirmar contraseña"
                      validation="required"
                      v-model="this.validatePass"
                  />
                  <template #stepNext="{ handlers, node }">
                    <FormKit
                        type="button"
                        @click="this.createClient(handlers)"
                        label="Siguiente"
                        data-next="true"
                    />
                  </template>
                </FormKit>
                <FormKit type="step" name="verificacion">
                  <FormKit
                      prefix-icon="link"
                      type="text"
                      label="Ingresa el código de verificación"
                      validation="required"
                      v-model="this.verificationCode.code"
                  />
                  <template #stepNext="{ handlers, node }">
                    <FormKit
                        type="button"
                        @click="this.verifyEmail(handlers)"
                        label="Verificar"
                        data-next="true"
                    />
                  </template>
                </FormKit>
              </FormKit>
            </div>
          </div>

      </div>
  </div>
</template>

<style scoped>
@import "../styles/css/views/register.css";

</style>