<template>
  <!-- Modal -->
  <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title" style="font-size: 3rem !important;" id="exampleModalLabel">Detalle empleado</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.clientProto.name }}</p>
              <p style="font-size: 2rem"><strong>Correo:</strong> {{ this.clientProto.email }}</p>
              <p style="font-size: 2rem"><strong>Teléfono:</strong> {{ this.clientProto.phone }}</p>
            </div>
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Dirección:</strong> {{ this.clientProto.address }}</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getClients()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Editar cliente</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <FormKit type="multi-step" tab-style="progress" :hide-progress-labels="true" :allow-incomplete="false">
            <FormKit type="step" name="stepOne">
              <FormKit v-model="this.clientProto.name"  type="text" label="Nombre" validation="required" />
              <FormKit v-model="this.clientProto.email" type="email" label="Email" validation="required|email" />
              <FormKit v-model="this.clientProto.phone" type="text" label="Teléfono" validation="required" />
              <!--<FormKit v-model="this.employeeProto.url_image" type="text" label="URL Imagen"/>-->
            </FormKit>
            <FormKit type="step" name="stepTwo">
              <FormKit v-model="this.clientProto.address" type="text" label="Dirección" validation="required" />
              <template #stepNext="{ handlers, node }">
                <FormKit
                    type="button"
                    @click="this.verifyData()"
                    label="Validar"
                />
              </template>
            </FormKit>
          </FormKit>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getClients()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="updateClient()" class="btn btn-success" data-bs-dismiss="modal" v-if="ready">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>
  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Gestión de clientes</h1>
    </div>
    <div class="table-responsive">
      <table id="dtab" class="table table-striped">
        <thead>
        <tr>
          <th>#</th>
          <th>Nombre</th>
          <th>Correo</th>
          <th>Télefono</th>
          <th>Dirección</th>
          <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(client, index) in clients" :key="client.id">
          <td>{{ index + 1 }}</td>
          <td>{{ client?.name }}</td>
          <td>{{ client?.email }}</td>
          <td>{{ client?.phone }}</td>
          <td>{{ client?.address }}</td>
          <td>
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-primary" @click="getDetailedClient(client)">Editar</button>
            <button class="btn btn-danger" @click="deleteClient(client)">Eliminar</button>
            <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedClient(client)">Ver</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script src="@/scripts/js/components/clients_admin.js"></script>