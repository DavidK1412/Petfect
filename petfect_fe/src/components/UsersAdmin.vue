<template>
  <!-- Modal -->
  <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title" style="font-size: 3rem !important;" id="exampleModalLabel">Detalle usuario</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.clientProto?.name }}</p>
              <p style="font-size: 2rem"><strong>Correo:</strong> {{ this.clientProto?.user?.email }}</p>
              <p style="font-size: 2rem"><strong>Rol:</strong> {{ this.clientProto?.user?.role?.name }}</p>
            </div>
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Verificado:</strong> {{ this.clientProto?.user?.email_verified ? 'Sí' : 'No' }}</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getClients()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Gestión de Usuarios</h1>
      <button  class="btn" @click="this.print()" >Descargar esta página</button>
    </div>
    <div class="table-responsive">
      <table id="dtab" class="table table-striped">
        <thead>
        <tr>
          <th>#</th>
          <th>Nombre</th>
          <th>Correo</th>
          <th>Rol</th>
          <th>Verificado</th>
          <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(client, index) in clients" :key="client.id">
          <td>{{ index + 1 }}</td>
          <td>{{ client?.name }}</td>
          <td>{{ client?.user?.email }}</td>
          <td>{{ client?.user?.role?.name }}</td>
          <td>{{ client?.user?.email_verified ? 'Sí' : 'No' }}</td>
          <td>
            <button class="btn btn-primary"
                    @click="changeUserRole(client?.user?.role?.id === 1 ? 2 : 1, client)">
              {{
                client?.user?.role?.id === 1 ? 'Cliente' : 'Admin'
              }}
            </button>
            <button class="btn btn-danger" @click="deleteClient(client)">Eliminar</button>
            <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedClient(client)">Ver</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div id="printable" style="width: 80%">
      <!-- Texto centrado diciendo catalogo de combos -->
      <h1 class="text-center">Usuarios</h1>
      <!-- Tabla de usuarios, nombre, correo, rol y verificado -->
      <div class="catalogo" v-for="client in clients">
        <!-- Left side -->
        <div class="left">
          <h2>{{ client.name }}</h2>
          <p> - {{ client.user.email }}</p>
          <p>Rol: <strong>{{ client.user.role.name }}</strong></p>
          <p>Verificado: <strong>{{ client.user.email_verified ? 'Sí' : 'No' }}</strong></p>
        </div>
      </div>

    </div>
  </div>
</template>

<style>
@media print {
  body {
    visibility: hidden;
  }
  .table-responsive {
    visibility: visible;
    position: absolute;
    left: 0;
    top: 0;
  }
}
</style>

<script src="@/scripts/js/components/users_admin.js"></script>