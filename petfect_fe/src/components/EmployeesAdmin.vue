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
              <p style="font-size: 2rem"><strong>Nombre:</strong> {{ this.employeeProto.name }}</p>
              <p style="font-size: 2rem"><strong>Correo:</strong> {{ this.employeeProto.email }}</p>
              <p style="font-size: 2rem"><strong>Teléfono:</strong> {{ this.employeeProto.phone }}</p>
            </div>
            <div class="col-6">
              <p style="font-size: 2rem"><strong>Especialidades:</strong></p>
              <ul>
                <li style="font-size: 2rem" v-for="speciality in this.employeeProto.speciality">{{ speciality.name }}</li>
              </ul>
            </div>
          </div>

        </div>
        <div class="modal-footer">
          <button type="button" @click="getEmployees()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Editar empleado</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <FormKit type="multi-step" tab-style="progress" :hide-progress-labels="true" :allow-incomplete="false">
            <FormKit type="step" name="stepOne">
              <FormKit v-model="this.employeeProto.name"  type="text" label="Nombre" validation="required" />
              <FormKit v-model="this.employeeProto.email" type="email" label="Email" validation="required|email" />
              <FormKit v-model="this.employeeProto.phone" type="text" label="Teléfono" validation="required" />
              <!--<FormKit v-model="this.employeeProto.url_image" type="text" label="URL Imagen"/>-->
            </FormKit>
            <FormKit type="step" name="stepTwo">
              <FormKit type="checkbox"
                       v-model="this.employeeProto.specialities"
                       label="Especialidades del empleado"
                       :options="this.specialities"
                       help="Seleccione la(s) especialidad(es) del empleado"
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
          <button type="button" @click="getEmployees()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="updateEmployee()" class="btn btn-success" data-bs-dismiss="modal" v-if="ready">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>
  <!-- Modal -->
  <div class="modal fade" id="createModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="exampleModalLabel">Crear empleado</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <FormKit type="multi-step" tab-style="progress" :hide-progress-labels="true" :allow-incomplete="false">
            <FormKit type="step" name="stepOne">
              <FormKit v-model="this.employeeProto.name"  type="text" label="Nombre" validation="required" />
              <FormKit v-model="this.employeeProto.email" type="email" label="Email" validation="required|email" />
              <FormKit v-model="this.employeeProto.phone" type="text" label="Teléfono" validation="required" />
              <!--<FormKit v-model="this.employeeProto.url_image" type="text" label="URL Imagen"/>-->
            </FormKit>
            <FormKit type="step" name="stepTwo">
              <FormKit type="checkbox"
                       v-model="this.employeeProto.specialities"
                       label="Especialidades del empleado"
                       :options="this.specialities"
                       help="Seleccione la(s) especialidad(es) del empleado"
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
          <button type="button" @click="getEmployees()" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
          <button type="button" @click="saveEmployee()" class="btn btn-success" data-bs-dismiss="modal" v-if="ready">Guardar cambios</button>
        </div>
      </div>
    </div>
  </div>


  <div id="main">
    <div class="top-elements">
      <h1 class="text-center">Gestión de empleados</h1>
      <button  class="btn" data-bs-toggle="modal" data-bs-target="#createModal">Agregar</button>
    </div>
    <div class="table-responsive">
      <table id="dtab" class="table table-striped">
        <thead>
          <tr>
            <th>#</th>
            <th>Nombre</th>
            <th>Correo</th>
            <th>Télefono</th>
            <th>URL Imagen</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(employee, index) in employees" :key="employee.id">
            <td>{{ index + 1 }}</td>
            <td>{{ employee?.name }}</td>
            <td>{{ employee?.email }}</td>
            <td>{{ employee?.phone }}</td>
            <td>{{ employee?.image_url }}</td>
            <td>
              <button data-bs-toggle="modal" data-bs-target="#editModal" class="btn btn-primary" @click="getDetailedEmployee(employee)">Editar</button>
              <button class="btn btn-danger" @click="deleteEmployee(employee)">Eliminar</button>
              <button data-bs-toggle="modal" data-bs-target="#detailModal" class="btn btn-info" @click="getDetailedEmployee(employee)">Ver</button>
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

.formkit-tabs{
  width: 100% !important;
}

.modal-body > p {
  font-size: 1.5rem !important;
}
</style>

<script src="../scripts/js/components/employees_admin.js"></script>