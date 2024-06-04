<template>
  <!-- Modal -->
  <div class="modal fade" id="detailModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title" style="font-size: 3rem !important;" id="exampleModalLabel">Detalle Combo</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.comboProto.name }}</p>
              <p style="font-size: 2rem"><strong>Descripción:</strong> {{ this.comboProto.description }}</p>
              <p style="font-size: 2rem"><strong>Valor:</strong> $ {{ this.comboProto.price }}</p>
            </div>
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Servicios:</strong></p>
              <ul>
                <li style="font-size: 2rem" v-for="service in this.comboProto.services">{{ service.name }}</li>
              </ul>
            </div>
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Especialidades:</strong></p>
              <ul>
                <li style="font-size: 2rem" v-for="service in this.comboProto.services">{{ service.required_speciality?.name }}</li>
              </ul>
            </div>
          </div>

        </div>
        <div class="modal-footer">
          <button type="button" @click="getCombos()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Editar combo</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <FormKit type="multi-step" tab-style="progress" :hide-progress-labels="true" :allow-incomplete="false">
            <FormKit type="step" name="stepOne">
              <FormKit v-model="this.comboProto.name"  type="text" label="Nombre" validation="required" />
              <FormKit v-model="this.comboProto.description" type="text" label="Descripción" validation="required" />
              <FormKit v-model="this.comboProto.price" type="number" label="Precio" validation="required" />
            </FormKit>
            <FormKit type="step" name="stepTwo">
              <FormKit type="checkbox"
                       v-model="this.comboProto.services"
                       label="Servicios del combo"
                       :options="this.services"
                       help="Seleccione los servicios del combo"
              />
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
          <button type="button" @click="getCombos()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="updateCombo()" class="btn btn-success" data-bs-dismiss="modal" v-if="ready">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="createModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Crear combo</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <FormKit type="multi-step" tab-style="progress" :hide-progress-labels="true" :allow-incomplete="false">
            <FormKit type="step" name="stepOne">
              <FormKit v-model="this.comboProto.name"  type="text" label="Nombre" validation="required" />
              <FormKit v-model="this.comboProto.description" type="text" label="Descripción" validation="required" />
              <FormKit v-model="this.comboProto.price" type="number" label="Precio" validation="required" />
              <!--<FormKit v-model="this.employeeProto.url_image" type="text" label="URL Imagen"/>-->
            </FormKit>
            <FormKit type="step" name="stepTwo">
              <FormKit type="checkbox"
                       v-model="this.comboProto.services"
                       label="Servicios del combo"
                       :options="this.services"
                       help="Seleccione los servicios del combo"
              />
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
          <button type="button" @click="getCombos()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="saveCombo()" class="btn btn-success" data-bs-dismiss="modal" v-if="ready">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>


  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Gestión de combos</h1>
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
          <th>Acciones</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(combo, index) in combos" :key="combo.id">
          <td>{{ index + 1 }}</td>
          <td>{{ combo?.name }}</td>
          <td>{{ combo?.description }}</td>
          <td>$ {{ combo?.price }}</td>
          <td>
            <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-primary" @click="getDetailedCombo(combo)">Editar</button>
            <button class="btn btn-danger" @click="deleteCombo(combo)">Eliminar</button>
            <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedCombo(combo)">Ver</button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    <div id="printable" style="width: 80%">
      <!-- Texto centrado diciendo catalogo de combos -->
      <h1 class="text-center">Catálogo de combos</h1>
      <!-- Tabla de precios -->
      <div class="catalogo" v-for="combo in combos">
        <!-- Left side -->
        <div class="left">
          <h2>{{ combo.name }}</h2>
          <p> - {{ combo.description }}</p>
          <p>Precio: <strong>$ {{ combo.price }}</strong></p>
        </div>
        <!-- Right side -->
        <div class="right">
          <h3>Servicios: </h3>
          <ul>
            <li v-for="service in combo.services"> - {{ service.name }}</li>
          </ul>
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

<script src="../scripts/js/components/combos_admin.js"></script>