<template>
  <!-- Modal -->
  <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title" style="font-size: 3rem !important;" id="exampleModalLabel">Detalle servicio</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.serviceProto.name }}</p>
              <p style="font-size: 2rem"><strong>Descripción:</strong> {{ this.serviceProto.description }}</p>
              <p style="font-size: 2rem"><strong>Precio:</strong> ${{ this.serviceProto.price }}</p>
              <p style="font-size: 2rem"><strong>Especialidad:</strong> {{ this.serviceProto.required_speciality?.name }}</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getServices()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Editar Servicio</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <!-- Form with camps to edit the pet (Name: text , size: checkbox, type: checkbox), no VueForm -->
          <div class="form-group">
            <label for="name">Nombre</label>
            <input type="text" class="form-control" id="name" v-model="this.serviceProto.name">
            <label for="description">Descripción</label>
            <input type="text" class="form-control" id="description" v-model="this.serviceProto.description">
            <label for="price">Precio</label>
            <input type="number" class="form-control" id="price" v-model="this.serviceProto.price">
            <label for="required_speciality">Especialidad</label>
            <select class="form-select" id="required_speciality" v-model="this.serviceProto.required_speciality">
              <option v-for="speciality in this.specialities" :value="speciality?.value">{{ speciality?.label }}</option>
            </select>
          </div>
          <div class="modal-footer">
            <button type="button" @click="getServices()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            <button type="button" @click="updateService()" class="btn btn-success" data-bs-dismiss="modal">Guardar cambios</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="createModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Crear Servicio</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label for="name">Nombre</label>
            <input type="text" class="form-control" id="name" v-model="this.serviceProto.name">
            <label for="description">Descripción</label>
            <input type="text" class="form-control" id="description" v-model="this.serviceProto.description">
            <label for="price">Precio</label>
            <input type="number" class="form-control" id="price" v-model="this.serviceProto.price">
            <label for="required_speciality">Especialidad</label>
            <select class="form-select" id="required_speciality" v-model="this.serviceProto.required_speciality">
              <option v-for="speciality in this.specialities" :value="speciality?.value">{{ speciality?.label }}</option>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getServices()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="saveService()" class="btn btn-success" data-bs-dismiss="modal">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>


  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Gestión de servicios</h1>
      <button  class="btn" data-bs-toggle="modal" data-bs-target="#createModal">Agregar</button>
      <button  class="btn" @click="this.download()">Catalogo</button>
    </div>
    <div class="table-responsive">
      <table id="dtab" class="table table-striped">
        <thead>
        <tr>
          <th>#</th>
          <th>Nombre</th>
          <th>Descripción</th>
          <th>Precio</th>
          <th>Especialidad</th>
          <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(service, index) in services" :key="service.id">
          <td>{{ index + 1 }}</td>
          <td>{{ service?.name }}</td>
          <td>{{ service?.description }}</td>
          <td>$ {{ service?.price }}</td>
          <td>{{ service?.required_speciality?.name }}</td>
          <td>
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-primary" @click="getDetailedService(service)">Editar</button>
            <button class="btn btn-danger" @click="deleteService(service)">Eliminar</button>
            <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedService(service)">Ver</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div id="printable" style="width: 80%">
      <!-- Texto centrado diciendo catalogo de combos -->
      <h1 class="text-center">Catálogo de servicios</h1>
      <!-- Tabla de precios -->
      <div class="catalogo" v-for="service in services">
        <!-- Left side -->
        <div class="left">
          <h2>{{ service.name }}</h2>
          <p> - {{ service.description }}</p>
          <p>Precio: <strong>$ {{ service.price }}</strong></p>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.catalogo {
  display: flex;
  justify-content: space-between;
  margin: 1rem;
  padding: 1rem;
  border: 1px solid black;
  width: 80%;
}

@media screen {
  #printable {
    display: none;
  }
}

@media print {
  body * {
    visibility: hidden;
    overflow: hidden;
  }
  #printable,
  #printable *
  {
    display: block;
    visibility: visible;

  }
  #printable {
    position: absolute;
    left: 0;
    top: 0;
  }
}
.btn {
  font-size: 1.5rem !important;
  margin: 0 0.3rem !important;
}

.modal-title{
  font-size: 1.8rem !important;
}

.formkit-tabs{
  width: 100% !important;
}

.modal-body > p {
  font-size: 1.5rem !important;
}
</style>
<script src="../scripts/js/components/services_admin.js"></script>
