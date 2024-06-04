<template>
  <!-- Modal -->
  <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title" style="font-size: 3rem !important;" id="exampleModalLabel">Detalle mascota</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.petProto.name }}</p>
              <p style="font-size: 2rem"><strong>Tamaño:</strong> {{ this.petProto.pet_size }}</p>
              <p style="font-size: 2rem"><strong>Tipo:</strong> {{ this.petProto.pet_type }}</p>
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getPets()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Editar Mascota</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <!-- Form with camps to edit the pet (Name: text , size: checkbox, type: checkbox), no VueForm -->
          <div class="form-group">
            <label for="name">Nombre</label>
            <input type="text" class="form-control" id="name" v-model="this.petProto.name">
            <label for="size">Tamaño</label>
            <select class="form-select" id="size" v-model="this.petProto.size">
              <option value="2">Pequeño</option>
              <option value="3">Mediano</option>
              <option value="1">Grande</option>
            </select>
            <label for="type">Tipo</label>
            <select class="form-select" id="type" v-model="this.petProto.type">
              <option value="1">Perro</option>
              <option value="2">Gato</option>
              <option value="3">Otro</option>
            </select>
          </div>
        <div class="modal-footer">
          <button type="button" @click="getPets()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="updatePet()" class="btn btn-success" data-bs-dismiss="modal">Guardar cambios</button>
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
          <h1 class="modal-title fs-5" id="exampleModalLabel">Crear Mascota</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-group">
            <label for="name">Nombre</label>
            <input type="text" class="form-control" id="name" v-model="this.petProto.name">
            <label for="size">Tamaño</label>
            <select class="form-select" id="size" v-model="this.petProto.size">
              <option value="2">Pequeño</option>
              <option value="3">Mediano</option>
              <option value="1">Grande</option>
            </select>
            <label for="type">Tipo</label>
            <select class="form-select" id="type" v-model="this.petProto.type">
              <option value="1">Perro</option>
              <option value="2">Gato</option>
              <option value="3">Otro</option>
            </select>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" @click="getPets()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="savePet()" class="btn btn-success" data-bs-dismiss="modal">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>


  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Mis Mascotas</h1>
      <button  class="btn" data-bs-toggle="modal" data-bs-target="#createModal">Agregar</button>
    </div>
    <div class="table-responsive">
      <table id="dtab" class="table table-striped">
        <thead>
        <tr>
          <th>#</th>
          <th>Nombre</th>
          <th>Tamaño</th>
          <th>Tipo</th>
          <th>URL Imagen</th>
          <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(pet, index) in pets" :key="pet.id">
          <td>{{ index + 1 }}</td>
          <td>{{ pet?.name }}</td>
          <td>{{ pet?.pet_size }}</td>
          <td>{{ pet?.pet_type }}</td>
          <td>{{ pet?.url_image }}</td>
          <td>
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-primary" @click="getDetailedPet(pet)">Editar</button>
            <button class="btn btn-danger" @click="deletePet(pet)">Eliminar</button>
            <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedPet(pet)">Ver</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<style>

.btn {
  font-size: 1.5rem !important;
  margin: 0 0.3rem !important;
}

.modal-title{
  font-size: 1.8rem !important;
}


.modal-body > p {
  font-size: 1.5rem !important;
}
</style>
<script src="../scripts/js/components/pets_admin.js"></script>