<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

// import { useAlertStore } from '@/stores';
import { useUsersStore, useAlertStore } from '@/stores';

import { router } from '@/router';

const schema = Yup.object().shape({
  // firstName: Yup.string()
  //   .required('First Name is required'),
  // lastName: Yup.string()
  //   .required('Last Name is required'),
  username: Yup.string()
    .required('Username is required'),
  password: Yup.string()
    .required('Password is required')
    .min(6, 'Password must be at least 6 characters'),
});

async function onSubmit(values) {
  const usersStore = useUsersStore();
  const alertStore = useAlertStore();
  try {
    // await api.post('/users/register', new URLSearchParams(values));
    // console.log(values);
    console.log(values);
    await usersStore.register(values);
    console.log(usersStore.$state);
    await router.push('/account/login');
    alertStore.success('Registration successful');
  } catch (error) {
    alertStore.error(error);
  }
}
</script>

  <template>
    <div class="column is-offset-one-fifth is-three-fifths">
      <div class="card">
        <div class="card-header is-justify-content-center py-4">
          <p class="title is-4">Регистрация</p>
        </div>
        <div class="card-body">
            <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                <!-- <div class="column mx-3 form-group">
                    <label class="label">Имя</label>
                    <Field name="firstName" type="text" class="form-control input is-4" :class="{ 'is-danger': errors.firstName }" />
                    <div class="help is-danger">{{ errors.firstName }}</div>
                </div>
                <div class="column mx-3 form-group">
                    <label class="label">Фамилия</label>
                    <Field name="lastName" type="text" class="form-control input is-4" :class="{ 'is-danger': errors.lastName }" />
                    <div class="help is-danger">{{ errors.lastName }}</div>
                </div> -->
                <div class="column mx-3 form-group">
                    <label class="label">Имя пользователя</label>
                    <Field name="username" type="text" class="form-control input is-4" :class="{ 'is-danger': errors.username }" />
                    <div class="help is-danger">{{ errors.username }}</div>
                </div>
                <div class="column mx-3 form-group">
                    <label class="label">Пароль</label>
                    <Field name="password" type="password" class="form-control input is-4" :class="{ 'is-danger': errors.password }" />
                    <div class="help is-danger">{{ errors.password }}</div>
                </div>
                <!-- <div class="columns is-justify-content-center">
                    <div class="column control is-one-fifth">
                      <button type="submit" class="button is-link" :disabled="isSubmitting">
                          <span v-show="isSubmitting" class="is-loading"></span>
                          Регистрация
                      </button>
                    </div>
                    <div class="column control is-one-fifth">
                      <router-link to="login" class="button is-link is-light ">Отмена</router-link>
                    </div>
                </div> -->
                <div class="field is-grouped is-justify-content-center pb-4">
                  <p class="control">
                    <button type="submit" class="button is-link" :disabled="isSubmitting">
                      <span v-show="isSubmitting" class="is-loading"></span>
                      Регистрация
                    </button>
                  </p>
                  <p class="control is-one-fifth">
                      <router-link to="login" class="button is-link is-light ">Отмена</router-link>
                  </p>
                </div>

            </Form>
        </div>
      </div>
    </div>
  </template>
